---
title: "How do I annotate a small text with CLASSLA?"
description: "A first reusable CLASSLA workflow for tokenizing, lemmatizing, and POS-tagging one plain-text file."
category: "NLP"
difficulty: "beginner"
time: "30–60 min"
tags: [CLASSLA, Slovene, tokenization, lemmatization, POS tagging]
---

# How do I annotate a small text with CLASSLA?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You have a short Slovene text and want to produce linguistic annotation: tokens, lemmas, and part-of-speech tags. Start with one file before trying a whole corpus.

!!! quote "One-sentence version"
    Process one plain-text file, export the annotation, inspect it manually, and only then scale up.

## You need

- Python 3.12.
- CLASSLA installed and tested.
- The Slovene CLASSLA model downloaded.
- One UTF-8 plain-text file.

## Tools

- CLASSLA for tokenization, lemmatization, and POS tagging.
- `pathlib` for input and output paths.
- Plain text as the safest first input format.

## Workflow

1. Create `data/raw/sample-sl.txt`.

```text
Digitalna humanistika povezuje jezik, podatke in interpretacijo.
Majhni preizkusi preprečijo velike napake.
```

2. Create `scripts/annotate_classla_txt.py`.

```python
from pathlib import Path
import classla

input_path = Path("data/raw/sample-sl.txt")
output_path = Path("output/sample-sl.tsv")
output_path.parent.mkdir(exist_ok=True)

text = input_path.read_text(encoding="utf-8")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp(text)

rows = ["sent_id\tword_id\ttext\tlemma\tupos"]

for sent_id, sentence in enumerate(doc.sentences, start=1):
    for word in sentence.words:
        rows.append(
            f"{sent_id}\t{word.id}\t{word.text}\t{word.lemma}\t{word.upos}"
        )

output_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Wrote {output_path}")
```

3. Run the script.

```bash
python scripts/annotate_classla_txt.py
```

4. Open `output/sample-sl.tsv`.
5. Check whether tokenization, lemmas, and tags look plausible.

## Output

A TSV file with sentence ID, word ID, token text, lemma, and UPOS tag.

## Check yourself

- Are sentence boundaries correct?
- Are Slovene characters preserved?
- Do common nouns and verbs have plausible lemmas?
- Did punctuation become separate tokens?

## Common traps

- Feeding PDF or Word files directly into the NLP pipeline instead of extracting clean text first.
- Assuming the first output is automatically correct.
- Forgetting that token IDs may become more complex if multi-word tokens are present.
- Processing too much text before inspecting a small sample.

## Practice task

Annotate a 5–10 sentence Slovene text. Select 20 random tokens and manually check whether their lemmas look correct.

## Useful extension

Add document metadata columns such as `doc_id`, `title`, and `source_file` before combining many annotated files.
