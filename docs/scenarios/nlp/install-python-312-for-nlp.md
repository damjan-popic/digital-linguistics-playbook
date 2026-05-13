---
title: "How do I install Python 3.12 for NLP work?"
description: "A small, safe setup guide for installing Python 3.12 as the standard version for beginner NLP workflows."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, Python 3.12, setup, NLP, beginner]
---

# How do I install Python 3.12 for NLP work?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

You want a stable Python setup for small NLP exercises. Use **Python 3.12** for this playbook path. Do not use Python 3.13 or higher unless your teacher explicitly asks you to, because some NLP packages may lag behind the newest Python release.

!!! quote "One-sentence version"
    Install Python 3.12, check that the terminal can find it, and only then create project-specific virtual environments.

## You need

- A terminal: Terminal, PowerShell, Windows Terminal, macOS Terminal, or a Linux shell.
- Permission to install software on your computer.
- Python **3.12.x**.
- A project folder where you can safely experiment.

## Tools

- [Python](https://www.python.org/): the programming language used in the workflows.
- `python --version` or `python3.12 --version`: a command that checks which Python version you are running.
- `py -3.12`: the Windows Python launcher command, useful when several Python versions are installed.

## Workflow

1. Install Python 3.12 from the official Python website or your system package manager.
2. Open a new terminal after installation.
3. Check the version.

On Windows, try:

```powershell
py -3.12 --version
```

On macOS or Linux, try:

```bash
python3.12 --version
```

4. Confirm that the result starts with `Python 3.12`.
5. Create a project folder.

```bash
mkdir nlp-first-steps
cd nlp-first-steps
```

6. Do not install NLP packages globally. Use a virtual environment in the next step.

## Output

A working Python 3.12 installation and a clean project folder ready for a virtual environment.

## Check yourself

- Does `py -3.12 --version` or `python3.12 --version` show Python 3.12?
- Are you inside a project folder, not your Downloads folder or desktop chaos zone?
- Can you explain which command starts Python 3.12 on your machine?

## Common traps

- Installing the newest Python version and then discovering that an NLP package does not support it yet.
- Installing packages globally instead of inside a virtual environment.
- Having several Python versions installed and not knowing which one the terminal is using.
- Copying commands for Linux into Windows PowerShell without adapting them.

## Practice task

Create a folder called `nlp-first-steps`, open a terminal inside it, and write down the exact command that shows Python 3.12 on your machine.

## Useful extension

Add a `README.md` file to the folder and record your Python version there:

```markdown
# NLP first steps

Python version used: 3.12.x
```
