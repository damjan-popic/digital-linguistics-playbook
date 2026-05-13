---
title: "How do I export CLASSLA results to CSV?"
description: "A workflow for turning CLASSLA annotation into a table that can be inspected, filtered, and reused."
category: "NLP"
difficulty: "intermediate"
time: "45–75 min"
tags: [CLASSLA, CSV, pandas, annotation, Slovene]
---

# How do I export CLASSLA results to CSV?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>intermediate</span>
<span>45–75 min</span>
</div>

## What you are trying to do

NLP results are easier to inspect and teach when they are in a table. This workflow processes multiple `.txt` files with CLASSLA and exports one CSV file with document ID, sentence ID, token ID, token, lemma, and POS tag.

!!! quote "One-sentence version"
    Keep document provenance in the output table, otherwise annotation becomes detached from the source.

## You need

- Python 3.12.
- CLASSLA installed and tested.
- `pandas` installed.
- A folder of plain-text files.

## Tools

- CLASSLA for annotation.
- pandas for table export.
- CSV for review in spreadsheet tools.

## Workflow

1. Install pandas if needed.

```bash
python -m pip install pandas
```

2. Put input files here:

```text
data/raw/texts/
```

3. Create `scripts/classla_folder_to_csv.py`.

```python
from pathlib import Path
import pandas as pd
import classla

input_dir = Path("data/raw/texts")
output_path = Path("output/classla-tokens.csv")
output_path.parent.mkdir(exist_ok=True)

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
rows = []

for txt_path in sorted(input_dir.glob("*.txt")):
    doc_id = txt_path.stem
    text = txt_path.read_text(encoding="utf-8")
    doc = nlp(text)

    for sent_id, sentence in enumerate(doc.sentences, start=1):
        for word in sentence.words:
            rows.append(dict(
                doc_id=doc_id,
                source_file=txt_path.name,
                sent_id=sent_id,
                word_id=word.id,
                text=word.text,
                lemma=word.lemma,
                upos=word.upos,
            ))

df = pd.DataFrame(rows)
df.to_csv(output_path, index=False)
print(f"Wrote {len(df)} tokens to {output_path}")
```

4. Run the script.

```bash
python scripts/classla_folder_to_csv.py
```

5. Open `output/classla-tokens.csv` and inspect the first rows.

## Output

A CSV file where each row is one annotated token.

## Check yourself

- Does every row have a `doc_id` and `source_file`?
- Is the number of tokens plausible for the input texts?
- Are there empty lemmas or unexpected tags?
- Can you filter by `upos` in a spreadsheet?

## Common traps

- Losing document identity by exporting only token and lemma.
- Mixing texts from different languages without a language column.
- Treating token-level output as if it were already analysis.
- Opening CSV in a spreadsheet and accidentally changing encoding or separators.

## Practice task

Process three short Slovene texts and create a frequency table of the 20 most frequent lemmas. Inspect whether function words dominate the list.

## Useful extension

Add columns for metadata by joining this token table with a separate `metadata.csv` file using `doc_id`.
