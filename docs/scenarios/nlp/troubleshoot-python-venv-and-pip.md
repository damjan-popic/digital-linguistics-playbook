---
title: "How do I troubleshoot Python venv and pip problems?"
description: "A practical checklist for diagnosing the most common beginner Python environment problems."
category: "NLP"
difficulty: "beginner"
time: "15–45 min"
tags: [Python, venv, pip, troubleshooting, beginner]
---

# How do I troubleshoot Python venv and pip problems?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–45 min</span>
</div>

## What you are trying to do

Most beginner Python problems are not deep programming problems. They are environment problems: wrong Python, inactive virtual environment, wrong `pip`, wrong folder, or missing package.

!!! quote "One-sentence version"
    Before debugging code, check Python version, environment activation, current folder, and package location.

## You need

- A terminal.
- A project folder.
- Python 3.12.
- The ability to copy the exact error message.

## Tools

- `python --version`: checks the active Python.
- `python -m pip --version`: checks which pip belongs to the active Python.
- `pwd` or `cd`: checks the current folder.
- `dir` or `ls`: lists files in the current folder.

## Workflow

1. Check Python version.

```bash
python --version
```

Expected:

```text
Python 3.12.x
```

2. Check whether the environment is active.

Look for `(.venv)` in your terminal prompt. Then run:

```bash
python -m pip --version
```

The path should contain `.venv`.

3. Check your current folder.

On Windows:

```cmd
cd
```

On macOS or Linux:

```bash
pwd
```

4. Check whether the script exists where you think it exists.

On Windows:

```cmd
dir scripts
```

On macOS or Linux:

```bash
ls scripts
```

5. If a package is missing, install it inside the active environment.

```bash
python -m pip install package-name
```

6. If the environment is hopelessly confused, recreate it.

```bash
# deactivate first if needed
deactivate

# remove the old environment manually or with your file manager
# then create a new one with Python 3.12
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Output

A clearer diagnosis: wrong Python, inactive environment, missing package, wrong folder, or real code error.

## Check yourself

- Does `python --version` show 3.12?
- Does `python -m pip --version` point inside `.venv`?
- Are you running the command from the project root?
- Did you copy the full error message, not just the final line?

## Common traps

- Searching the internet for the last error line while ignoring the earlier, more useful part of the traceback.
- Installing a package with one Python and running code with another.
- Creating several `.venv` folders and activating the wrong one.
- Assuming the problem is CLASSLA when the actual problem is the environment.

## Practice task

Intentionally deactivate your environment and try to import `pandas`. Then activate the environment and try again. Explain the difference.

## Useful extension

Create a diagnostic script called `scripts/check_environment.py`:

```python
import sys
from pathlib import Path

print("Python:", sys.version)
print("Executable:", sys.executable)
print("Current folder:", Path.cwd())
```
