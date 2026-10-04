#!/usr/bin/env python3
"""Check legacy personal-page redirects without building the personal website."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import os
from pathlib import Path
import time
from urllib.request import Request, urlopen
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://damjan-popic.github.io/digital-linguistics-playbook/"


class RefreshCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_refresh = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.has_refresh = True


def read_live(route: str) -> bytes:
    suffix = "?migration=" + os.environ.get("GITHUB_SHA", "manual")
    request = Request(BASE + route + suffix, headers={"Cache-Control": "no-cache", "User-Agent": "personal-site-migration-check"})
    with urlopen(request, timeout=20) as response:
        if response.status != 200 or urlsplit(response.url).path != urlsplit(BASE + route).path:
            raise ValueError(f"Unexpected status or destination for {route}")
        return response.read()


def retry(operation):
    for attempt in range(6):
        try:
            return operation()
        except (OSError, ValueError) as error:
            if attempt == 5:
                raise
            print(f"Retry {attempt + 1}/5: {error}", flush=True)
            time.sleep(5)


def main(site_dir: Path | None, live: bool):
    files = sorted((ROOT / "docs" / "damjan").rglob("index.html"))
    if len(files) != 19:
        raise ValueError(f"Expected 19 legacy redirects, found {len(files)}")

    def check(path):
        relative = path.relative_to(ROOT / "docs")
        expected = path.read_bytes()
        if site_dir is not None and (site_dir / relative).read_bytes() != expected:
            raise ValueError(f"Redirect missing or changed in the built site: {relative}")
        if live:
            route = relative.as_posix().removesuffix("index.html")
            def compare():
                if read_live(route) != expected:
                    raise ValueError(f"Published redirect does not match: {route}")
            retry(compare)
        print(f"PASS {'public' if live else 'built'} redirect: {relative}", flush=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(check, files))
    if live:
        root = retry(lambda: read_live(""))
        parser = RefreshCheck()
        parser.feed(root.decode("utf-8"))
        if parser.has_refresh or b"Digital Linguistics Playbook" not in root:
            raise ValueError("The Playbook homepage was replaced or redirected")
        print("PASS public Playbook homepage remains a separate site.", flush=True)
    print("Verified all 19 legacy redirects.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path)
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    if args.site_dir is None and not args.live:
        parser.error("Specify --site-dir or --live")
    main(args.site_dir, args.live)
