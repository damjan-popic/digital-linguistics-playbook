---
title: "Digital Linguist Kickstart"
description: "A minimal starter repository for a first reproducible script and sanity-check workflow."
tags: [projects, starter, python, reproducibility]
---

# Digital Linguist Kickstart

<div class="answer-meta" markdown>
<span>starter repo</span>
<span>Python</span>
<span>sanity check</span>
</div>

## What this project does

Digital Linguist Kickstart is a very small starter repository. At the time this catalogue was prepared, the public repository contained a `sanity_check.py` file and minimal structure, but no full README.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/digital_linguist_kickstart)

## Use this when

- you want a tiny first-code example rather than a full pipeline;
- you want users to practice adding a README, requirements, input/output notes, and tests;
- you need a deliberately small repo for teaching Git basics.

## What to inspect in the code

- `sanity_check.py` — the starter script.
- `.gitignore` — what local files are excluded.

## Suggested improvement path

Turn this into a complete minimal project by adding:

- `README.md` with purpose, input, command, output, and checks;
- `requirements.txt` or `pyproject.toml` if dependencies exist;
- `data/sample/` with tiny legal sample data;
- `tests/` with one smoke test;
- `.github/workflows/` with a basic CI check.

## Relevant playbook workflows

- [How do I standardise project file names?](../scenarios/automation/standardise-project-file-names.md)
- [How do I automate a linguistic workflow with a Makefile?](../scenarios/automation/automate-a-linguistic-workflow-with-a-makefile.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to turn the repository into a minimal reproducible project. They should write the README first, then make the code match the README.

## Limits and cautions

- This is not yet a full case study.
- A minimal script becomes reusable only when inputs, outputs, assumptions, and checks are documented.
- Sparse repositories are good teaching material precisely because the missing pieces are visible.
