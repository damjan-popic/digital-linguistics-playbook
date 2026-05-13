---
title: "Digital Linguistics Playbook"
description: "The MkDocs Material reference site that hosts these workflows and project pages."
tags: [projects, MkDocs, GitHub-Pages, documentation]
---

# Digital Linguistics Playbook

<div class="answer-meta" markdown>
<span>documentation site</span>
<span>MkDocs</span>
<span>GitHub Pages</span>
</div>

## What this project does

Digital Linguistics Playbook is the public reference site that hosts practical workflows and worked code examples for digital linguistics and digital humanities. It is built with MkDocs Material and deployed through GitHub Pages.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/digital-linguistics-playbook)

## Use this when

- you need a model for a Markdown-first reference site;
- you want users to publish small, tested how-to pages;
- you need GitHub Pages deployment without a custom backend;
- you want a long-term home for reusable workflows and project documentation.

## What to inspect in the code

- `docs/scenarios/` — workflow pages.
- `docs/projects/` — worked code examples.
- `docs/contribute/` — templates and contribution guidelines.
- `mkdocs.yml` — site configuration and navigation.
- `.github/workflows/pages.yml` — GitHub Pages deployment.
- `scripts/new_answer.py` — scaffolds new workflow pages.
- `scripts/check_answers.py` — validates required answer-page structure.

## Minimal run path

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Build and validate:

```bash
python scripts/check_answers.py
mkdocs build --strict
```

## Relevant playbook workflows

- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I automate a linguistic workflow with a Makefile?](../scenarios/automation/automate-a-linguistic-workflow-with-a-makefile.md)

## Practice use

Ask users to add one new workflow page using the topic template. Another user must then test the instructions before the page is merged.

## Limits and cautions

- Navigation is configured manually in `mkdocs.yml`.
- Published pages should be production-facing; teaching-only prompts can live outside `docs/`.
- The site should link to code rather than duplicating entire scripts.
