---
title: "How do I install Python packages with pip?"
description: "A safe workflow for installing packages inside a virtual environment and recording them in requirements.txt."
category: "NLP"
difficulty: "beginner"
time: "15–30 min"
tags: [Python, pip, packages, requirements, beginner]
---

# How do I install Python packages with pip?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–30 min</span>
</div>

## What you are trying to do

Python packages add extra functionality. For NLP work, you may need packages such as `pandas`, `classla`, `spacy`, or `matplotlib`. Install them inside an activated virtual environment, not globally.

!!! quote "One-sentence version"
    Activate `.venv`, install with `python -m pip install ...`, then record the package list in `requirements.txt`.

## You need

- An activated Python 3.12 virtual environment.
- Internet access.
- A terminal.
- A clear idea of which package you need.

## Tools

- `python -m pip`: the safest way to call pip from the active Python environment.
- `requirements.txt`: a portable list of project dependencies.
- [PyPI](https://pypi.org/): the main package index for Python packages.

## Workflow

1. Activate your virtual environment.

2. Install one small package first.

```bash
python -m pip install pandas
```

3. Test whether the package imports.

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

4. Save the installed packages.

```bash
python -m pip freeze > requirements.txt
```

5. Later, another user can recreate the environment with:

```bash
python -m pip install -r requirements.txt
```

6. For teaching examples, prefer a small hand-written `requirements.txt` instead of a huge frozen file.

Example:

```text
pandas
classla
matplotlib
```

## Output

An installed package and a `requirements.txt` file that documents what the project needs.

## Check yourself

- Did you activate `.venv` before installing?
- Does `python -m pip --version` point inside `.venv`?
- Can you import the installed package with `python -c "import package_name"`?

## Common traps

- Running `pip install` with the wrong Python environment.
- Installing packages globally and then not knowing why another project broke.
- Sharing code without `requirements.txt`.
- Freezing hundreds of packages when the project only needs three.

## Practice task

Create a virtual environment, install `pandas`, test the import, and create a `requirements.txt` file. Then open the file and inspect what it contains.

## Useful extension

Add a short installation section to your project README:

```markdown
## Install

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
