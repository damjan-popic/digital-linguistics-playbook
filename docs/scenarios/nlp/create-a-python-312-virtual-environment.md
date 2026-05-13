---
title: "How do I create a Python 3.12 virtual environment?"
description: "A beginner-friendly workflow for creating and activating a project-specific Python virtual environment."
category: "NLP"
difficulty: "beginner"
time: "15–30 min"
tags: [Python, venv, virtual environment, setup, beginner]
---

# How do I create a Python 3.12 virtual environment?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>15–30 min</span>
</div>

## What you are trying to do

A virtual environment is a small isolated Python space for one project. It keeps package installs separate, so one project does not break another. For this playbook, create environments with **Python 3.12**.

!!! quote "One-sentence version"
    One project gets one virtual environment; activate it before installing packages or running scripts.

## You need

- Python 3.12 installed.
- A terminal.
- A project folder.
- Basic comfort with copying commands carefully.

## Tools

- `venv`: Python's built-in virtual environment tool.
- `pip`: the package installer used inside the environment.
- `requirements.txt`: a simple text file listing the packages a project needs.

## Workflow

1. Enter your project folder.

```bash
cd nlp-first-steps
```

2. Create the environment.

On Windows:

```powershell
py -3.12 -m venv .venv
```

On macOS or Linux:

```bash
python3.12 -m venv .venv
```

3. Activate it.

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

4. Check that the environment is active.

```bash
python --version
python -m pip --version
```

5. Upgrade packaging tools inside the environment.

```bash
python -m pip install --upgrade pip setuptools wheel
```

6. When you are finished, deactivate the environment.

```bash
deactivate
```

## Output

A `.venv/` folder inside your project and an activated environment where `python --version` reports Python 3.12.

## Check yourself

- Does your terminal prompt show something like `(.venv)`?
- Does `python --version` show Python 3.12 after activation?
- Does `python -m pip --version` point to the `.venv` folder?

## Common traps

- Creating the environment with the wrong Python version.
- Forgetting to activate the environment before installing packages.
- Deleting or moving the `.venv` folder and then wondering why commands stopped working.
- Committing `.venv/` to Git. Add it to `.gitignore` instead.

## Practice task

Create a virtual environment in a new folder, activate it, run `python --version`, then deactivate it. Write down the four commands you used.

## Useful extension

Create a `.gitignore` file and add:

```text
.venv/
__pycache__/
*.pyc
```
