#!/usr/bin/env python3
"""Lightweight validation for project pages."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "docs" / "projects"
REQUIRED_HEADINGS = [
    "## What this project does",
    "## Use this when",
    "## What to inspect in the code",
    "## Relevant playbook workflows",
    "## Limits and cautions",
]


def main() -> int:
    failures: list[str] = []
    files = sorted(p for p in PROJECTS.glob("*.md") if p.name != "index.md")
    if not files:
        failures.append("No project pages found under docs/projects/.")

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if "[:octicons-mark-github-16: Open the repository]" not in text:
            failures.append(f"{rel}: missing GitHub repository link")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                failures.append(f"{rel}: missing heading '{heading}'")

    if failures:
        print("Project check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"OK: checked {len(files)} project pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
