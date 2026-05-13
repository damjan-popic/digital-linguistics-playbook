---
title: "How do I structure a small Python NLP project?"
description: "A simple folder structure for beginner NLP projects that keeps input, scripts, and output separate."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, project structure, reproducibility, NLP]
---

# How do I structure a small Python NLP project?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Small projects become confusing very quickly if data, scripts, outputs, notes, screenshots, and virtual environments all live in the same folder. This structure gives students a clean default.

!!! quote "One-sentence version"
    Separate raw data, scripts, outputs, documentation, and environment files from the beginning.

## You need

- A project folder.
- Python 3.12.
- A virtual environment.
- A text editor.

## Tools

- Folders and clear file names.
- `README.md` for human documentation.
- `requirements.txt` for package documentation.
- `.gitignore` for files that should not be committed.

## Workflow

1. Create this structure:

```text
my-nlp-project/
├── data/
│   ├── raw/
│   └── processed/
├── output/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

2. Put original files in `data/raw/`.
3. Put cleaned or transformed files in `data/processed/`.
4. Put Python scripts in `scripts/`.
5. Put generated tables, charts, and reports in `output/`.
6. Document the project in `README.md`.
7. Add this to `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
.DS_Store
```

8. Add package names to `requirements.txt`.

Example:

```text
pandas
classla
matplotlib
```

## Output

A project folder that can be understood, shared, reviewed, and rerun.

## Check yourself

- Can another person find the raw data without asking you?
- Can another person find the script that produced a result?
- Are generated files separate from original files?
- Is `.venv/` excluded from Git?

## Common traps

- Editing raw data directly without preserving the original.
- Saving scripts as `final_final_really_final.py`.
- Putting output files into the same folder as input files.
- Forgetting to document how the results were produced.

## Practice task

Create this folder structure for a small corpus of three texts. Add a README that explains what the data is and which script should be run first.

## Useful extension

Add a simple `Makefile` later, once the workflow has more than one repeated command.
