---
title: "How do I read and write text files in Python?"
description: "A first text-processing workflow using plain-text files, pathlib, and UTF-8 encoding."
category: "NLP"
difficulty: "beginner"
time: "20–40 min"
tags: [Python, text files, UTF-8, pathlib, beginner]
---

# How do I read and write text files in Python?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

Before NLP becomes models and annotation, it is mostly reading files, cleaning strings, and saving results. This workflow shows the smallest useful text-processing script.

!!! quote "One-sentence version"
    Read text as UTF-8, transform it in a visible way, and write a new file without destroying the original.

## You need

- Python 3.12.
- A project folder with `data/`, `output/`, and `scripts/`.
- One plain-text file saved as UTF-8.

## Tools

- `pathlib`: a built-in Python library for file paths.
- `.read_text()` and `.write_text()`: simple methods for reading and writing text.
- UTF-8 encoding: the default choice for multilingual text work.

## Workflow

1. Create this file:

```text
data/sample.txt
```

2. Add a few lines of text.

```text
Digital humanities starts with small, inspectable steps.
Python can read this file.
Python can also write a changed version.
```

3. Create this script:

```text
scripts/clean_text.py
```

4. Add this code:

```python
from pathlib import Path

input_path = Path("data/sample.txt")
output_path = Path("output/sample-cleaned.txt")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")

# A tiny visible transformation.
cleaned = text.lower().strip()

output_path.write_text(cleaned + "\n", encoding="utf-8")
print(f"Wrote {output_path}")
```

5. Run the script.

```bash
python scripts/clean_text.py
```

6. Open `output/sample-cleaned.txt` and compare it with the original.

## Output

A new cleaned text file. The original file remains unchanged.

## Check yourself

- Does the script preserve the original input file?
- Does the output file use UTF-8 and display characters correctly?
- Can you explain what `.lower()` and `.strip()` changed?

## Common traps

- Overwriting the original file before checking the result.
- Forgetting `encoding="utf-8"` and getting broken characters.
- Thinking that lowercasing is always safe. It may destroy useful information in names and abbreviations.
- Doing too many cleaning steps at once, then not knowing which step caused an error.

## Practice task

Create a script that reads `data/sample.txt`, counts the number of characters and lines, and writes the results to `output/text-report.txt`.

## Useful extension

Try adding one cleaning step at a time and saving each version separately:

```text
sample-cleaned-01-lowercase.txt
sample-cleaned-02-no-extra-spaces.txt
```
