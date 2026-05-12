#!/usr/bin/env python3
"""Lightweight validation for playbook answer pages.

This intentionally uses only the Python standard library, so it can run in GitHub Actions
without extra packages.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "docs" / "scenarios"

REQUIRED_META = ["title", "description", "category", "difficulty", "time", "tags"]
REQUIRED_HEADINGS = [
    "## What you are trying to do",
    "## You need",
    "## Tools",
    "## Workflow",
    "## Output",
    "## Check yourself",
    "## Common traps",
    "## Classroom version",
]


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta


def main() -> int:
    failures: list[str] = []
    files = sorted(p for p in SCENARIOS.rglob("*.md") if p.name != "index.md")
    if not files:
        failures.append("No answer pages found under docs/scenarios/.")

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        meta = read_frontmatter(text)
        for key in REQUIRED_META:
            if key not in meta or not meta[key]:
                failures.append(f"{rel}: missing frontmatter key '{key}'")
        title = meta.get("title", "")
        if title and not re.search(r"How do I .+\?\"?$", title):
            failures.append(f"{rel}: title should be phrased as 'How do I ...?'")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                failures.append(f"{rel}: missing heading '{heading}'")

    if failures:
        print("Answer check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"OK: checked {len(files)} answer pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
