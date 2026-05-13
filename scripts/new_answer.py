#!/usr/bin/env python3
'''Create a new Digital Linguistics Playbook answer page.'''
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "scenarios"
REQUIRED_CATEGORIES = {
    "terminology", "cat-tools", "subtitling", "automation", "nlp", "corpora",
    "pdf", "visualization", "mt-eval", "audio", "publishing", "data-wrangling",
    "editions", "mapping", "ai", "ethics"
}


def slugify(text: str) -> str:
    text = text.lower().replace("how do i", "")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"(^-|-$)", "", text) or "new-answer"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new answer page.")
    parser.add_argument("title", help="Question-style title, ideally starting with 'How do I ...?'")
    parser.add_argument("--category", required=True, help="Category slug, e.g. corpora, mapping, ai")
    parser.add_argument("--difficulty", default="beginner", choices=["beginner", "intermediate", "advanced"])
    parser.add_argument("--time", default="30–60 min")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    category = args.category.strip().lower()
    if category not in REQUIRED_CATEGORIES:
        allowed = ", ".join(sorted(REQUIRED_CATEGORIES))
        raise SystemExit(f"Unknown category '{category}'. Allowed: {allowed}")

    title = args.title.strip()
    if not title.lower().startswith("how do i"):
        title = "How do I " + title[0].lower() + title[1:]
    if not title.endswith("?"):
        title += "?"

    slug = slugify(title)
    path = DOCS / category / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    if not tags:
        tags = [category, args.difficulty]

    tag_text = ", ".join(tags)
    path.write_text(f'''---
title: "{title}"
description: "Draft answer. Replace this with a one-sentence summary."
category: "{category}"
difficulty: "{args.difficulty}"
time: "{args.time}"
tags: [{tag_text}]
---

# {title}

<div class="answer-meta" markdown>
<span>{category}</span>
<span>{args.difficulty}</span>
<span>{args.time}</span>
</div>

## What you are trying to do

Explain the practical situation.

## You need

- Input file, source, or dataset
- Tool access
- Decision criteria

## Tools

- [Tool name](https://example.org)

## Workflow

1. Start with a tiny sample.
2. Do the smallest useful step.
3. Check the output.
4. Scale only after the sample works.

## Output

Name the expected output.

## Check yourself

- How do you know the workflow worked?
- What should be inspected manually?
- What would count as failure?

## Common traps

- Trap one.
- Trap two.

## Practice task

Describe a short exercise or test case that lets readers try or extend the workflow.
''', encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
