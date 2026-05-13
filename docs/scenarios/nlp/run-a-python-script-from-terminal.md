---
title: "How do I run a Python script from the terminal?"
description: "A small workflow for writing and running a first Python script inside a project folder."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, terminal, scripts, beginner]
---

# How do I run a Python script from the terminal?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Many reproducible NLP workflows are scripts, not notebook screenshots. A script is a `.py` file that can be run again with the same input and settings.

!!! quote "One-sentence version"
    Put code in `scripts/`, run it from the project root, and keep input and output paths predictable.

## You need

- Python 3.12.
- An activated virtual environment.
- A text editor such as VS Code.
- A project folder.

## Tools

- Terminal or PowerShell.
- A code editor.
- `python script.py`: the basic command for running a script.

## Workflow

1. Create a basic project structure.

```text
nlp-first-steps/
├── data/
├── output/
└── scripts/
```

2. Create a file:

```text
scripts/hello.py
```

3. Add this code:

```python
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

message = "Hello from a reproducible Python script."
print(message)

(output_dir / "hello.txt").write_text(message + "\n", encoding="utf-8")
```

4. From the project root, run:

```bash
python scripts/hello.py
```

5. Check the output folder.

```text
output/hello.txt
```

## Output

A working script and a small output file created by the script.

## Check yourself

- Did you run the script from the project root?
- Did the script create `output/hello.txt`?
- Can you delete the output file and recreate it by running the script again?

## Common traps

- Running the script from the wrong folder and breaking relative paths.
- Saving the file as `hello.py.txt` by accident.
- Editing one copy of a script and running another.
- Writing output manually instead of letting the script produce it.

## Practice task

Modify the script so that it writes your name, the date, and the Python version into `output/run-info.txt`.

## Useful extension

Add this to the script to record the Python version:

```python
import sys
print(sys.version)
```
