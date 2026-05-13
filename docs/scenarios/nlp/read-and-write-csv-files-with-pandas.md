---
title: "How do I read and write CSV files with pandas?"
description: "A beginner workflow for loading tabular humanities data, inspecting it, and saving a cleaned CSV file."
category: "NLP"
difficulty: "beginner"
time: "30–45 min"
tags: [Python, pandas, CSV, data, beginner]
---

# How do I read and write CSV files with pandas?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–45 min</span>
</div>

## What you are trying to do

Many NLP and digital humanities projects start with a CSV file: document metadata, annotation labels, OCR corrections, keyword lists, or entity tables. This workflow shows how to read, inspect, lightly clean, and save CSV data.

!!! quote "One-sentence version"
    Load the CSV, inspect the columns, change one thing, and export a new file rather than silently overwriting the original.

## You need

- Python 3.12.
- An activated virtual environment.
- `pandas` installed.
- A small CSV file.

## Tools

- [pandas](https://pandas.pydata.org/): a Python library for tables.
- CSV: a simple table format that can be opened in spreadsheet tools and processed by scripts.

## Workflow

1. Install pandas if needed.

```bash
python -m pip install pandas
```

2. Create `data/documents.csv`.

```csv
id,title,year,text
1,First text,2024,"This is a short text."
2,Second text,2025,"This is another short text."
3,Messy text,,"This row has a missing year."
```

3. Create `scripts/read_csv.py`.

```python
from pathlib import Path
import pandas as pd

input_path = Path("data/documents.csv")
output_path = Path("output/documents-cleaned.csv")
output_path.parent.mkdir(exist_ok=True)

df = pd.read_csv(input_path)

print("Columns:", list(df.columns))
print("Rows:", len(df))
print(df.head())

# Add a simple derived column.
df["text_length"] = df["text"].str.len()

# Keep the original file untouched.
df.to_csv(output_path, index=False)
print(f"Wrote {output_path}")
```

4. Run the script.

```bash
python scripts/read_csv.py
```

5. Open `output/documents-cleaned.csv`.

## Output

A cleaned or enriched CSV file with an added `text_length` column.

## Check yourself

- Are all expected columns present?
- Did the number of rows stay the same?
- Are missing values visible rather than hidden?
- Can the output CSV be opened in a spreadsheet editor?

## Common traps

- Forgetting `index=False` and adding a useless extra column.
- Letting a spreadsheet silently change dates, IDs, or leading zeros.
- Treating a missing value as if it were a real value.
- Mixing separators such as commas, semicolons, and tabs without checking.

## Practice task

Add a column called `has_year` that is `True` when the year is present and `False` when it is missing. Export the result.

## Useful extension

For larger projects, create a `metadata_report.md` file that lists columns, missing values, and suspicious rows.
