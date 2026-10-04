#!/usr/bin/env python3
"""Build the bilingual site from Markdown; only its own output directory is replaced."""
from __future__ import annotations
import argparse
import html
import json
import os
import posixpath
import re
import shutil
import tempfile
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
MARKER = ".damjan-site"


def read_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"{path}: expected YAML metadata between --- lines")
    header, body = text[4:].split("\n---\n", 1)
    meta = yaml.safe_load(header)
    if not isinstance(meta, dict):
        raise ValueError(f"{path}: metadata must be a mapping")
    for key in ("key", "title", "description", "kicker"):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            raise ValueError(f"{path}: missing text field {key}")
    rel = path.relative_to(CONTENT)
    route = rel.with_suffix("").as_posix()
    route = route[:-5] if route.endswith("/index") else route + "/"
    return dict(meta, lang=rel.parts[0], route=route, source=rel.as_posix(), body=body)


def relative_url(target: str, current: str) -> str:
    result = posixpath.relpath(target.rstrip("/") or ".", current.rstrip("/") or ".")
    return result + "/" if target.endswith("/") or not target else result


def slug(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", folded).strip("-") or "section"


def render_markdown(page: dict, by_source: dict) -> tuple[str, list]:
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    tokens = md.parse(page["body"])
    toc, seen = [], {}
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            if token.tag == "h1":
                raise ValueError(f'{page["source"]}: use ## headings; title already supplies H1')
            children = tokens[i + 1].children or []
            title = "".join(t.content for t in children if t.type in ("text", "code_inline"))
            base = slug(title)
            seen[base] = seen.get(base, 0) + 1
            anchor = base if seen[base] == 1 else f"{base}-{seen[base]}"
            token.attrSet("id", anchor)
            if token.tag == "h2":
                toc.append(dict(id=anchor, title=title))

    def rewrite(token):
        attr = "href" if token.type == "link_open" else "src" if token.type == "image" else None
        if attr:
            value = token.attrGet(attr) or ""
            parts = urlsplit(value)
            if not parts.scheme and not parts.netloc and parts.path:
                if parts.path.endswith(".md"):
                    source = posixpath.normpath(posixpath.join(posixpath.dirname(page["source"]), unquote(parts.path)))
                    if source not in by_source:
                        raise ValueError(f'{page["source"]}: missing Markdown target {value}')
                    target = relative_url(by_source[source]["route"], page["route"])
                    token.attrSet(attr, urlunsplit(("", "", target, parts.query, parts.fragment)))
                elif parts.path.startswith("/assets/"):
                    target = relative_url(parts.path.lstrip("/"), page["route"])
                    token.attrSet(attr, urlunsplit(("", "", target, parts.query, parts.fragment)))
        for child in token.children or []:
            rewrite(child)
    for token in tokens:
        rewrite(token)
    return md.renderer.render(tokens, md.options, {}), toc


class HTMLAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.h1, self.lang = [], set(), 0, None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise ValueError(f'Duplicate HTML id: {attrs["id"]}')
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def validate(output: Path) -> tuple[int, int]:
    pages = {}
    for path in output.rglob("*.html"):
        audit = HTMLAudit()
        audit.feed(path.read_text(encoding="utf-8"))
        if audit.h1 != 1 or audit.lang not in ("sl", "en"):
            raise ValueError(f"{path}: expected one H1 and a valid page language")
        pages[path.resolve()] = audit
    checks = 0
    for path, audit in pages.items():
        for value in audit.links:
            parts = urlsplit(value)
            if parts.scheme or parts.netloc:
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_relative_to(output.resolve()):
                raise ValueError(f"{path}: link escapes the personal site: {value}")
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                raise ValueError(f"{path}: broken local link: {value}")
            if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f"{path}: missing anchor: {value}")
            checks += 1
    return len(pages), checks


def build(output: Path, site_url: str | None = None) -> tuple[int, int]:
    output = output.resolve()
    if ROOT.is_relative_to(output) or any(output.is_relative_to(ROOT / folder) for folder in ("content", "assets", "templates")):
        raise ValueError("Refusing to overwrite source files or an ancestor directory")
    if output.exists() and any(output.iterdir()) and not (output / MARKER).is_file():
        raise ValueError(f"Refusing to replace non-generated directory: {output}")
    site = yaml.safe_load((ROOT / "site.yml").read_text(encoding="utf-8"))
    site["url"] = (site_url or site["url"]).rstrip("/") + "/"
    if urlsplit(site["url"]).scheme not in ("http", "https"):
        raise ValueError("Site URL must start with http:// or https://")
    page_list = [read_page(p) for p in sorted(CONTENT.rglob("*.md"))]
    pages, by_source = {}, {}
    for page in page_list:
        identifier = (page["lang"], page["key"])
        if page["lang"] not in site["languages"] or identifier in pages:
            raise ValueError(f'Invalid language or duplicate key: {page["source"]}')
        pages[identifier] = page
        by_source[page["source"]] = page
    for page in page_list:
        for language in site["languages"]:
            if (language, page["key"]) not in pages:
                raise ValueError(f'Missing {language} translation for {page["key"]}')
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]), undefined=StrictUndefined)
    template = env.get_template("page.html")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".damjan-build-", dir=output.parent) as work:
        staging = Path(work) / "site"
        staging.mkdir()
        shutil.copytree(ROOT / "assets", staging / "assets")
        # The site root is a Slovenian home-page alias; its canonical points to /sl/.
        render_pages = page_list + [dict(pages[("sl", "home")], route="")]
        for page in render_pages:
            body, toc = render_markdown(page, by_source)
            translations = {language: pages[(language, page["key"])] for language in site["languages"]}
            canonical = site["url"] + translations[page["lang"]]["route"]
            rendered = template.render(
                site=site, page=page, pages=pages, ui=site["languages"][page["lang"]], body=body, toc=toc,
                translations=translations, canonical=canonical,
                relative=lambda route: relative_url(route, page["route"]),
                link=lambda key: relative_url(pages[(page["lang"], key)]["route"], page["route"]),
                asset=lambda name: relative_url("assets/" + name, page["route"]),
                edit_url=f'{site["repository"]}/edit/{site["branch"]}/{site["source_path"]}/{quote(page["source"], safe="/")}',
            )
            destination = staging / page["route"] / "index.html"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered + "\n", encoding="utf-8")
        urls = "".join(f'<url><loc>{html.escape(site["url"] + page["route"])}</loc></url>\n' for page in page_list)
        (staging / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n', encoding="utf-8")
        (staging / MARKER).write_text("Generated personal site; safe to rebuild.\n", encoding="utf-8")
        (staging / "build.json").write_text(json.dumps({"site": site["name"], "languages": list(site["languages"]), "content_pages": len(page_list), "source_commit": os.environ.get("GITHUB_SHA", "local")}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result = validate(staging)
        if output.exists():
            shutil.rmtree(output)
        shutil.move(str(staging), str(output))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--site-url", help="Override the public URL when moving to a new host")
    args = parser.parse_args()
    try:
        count, checks = build(args.output, args.site_url)
        print(f"Built {count} HTML pages; passed {checks} local-link checks: {args.output}")
    except (ValueError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
