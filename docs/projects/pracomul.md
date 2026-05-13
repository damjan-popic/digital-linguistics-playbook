---
title: "Pracomul-SLC Analyzer"
description: "A dialogue-corpus pipeline that exports tidy token, turn, speaker, and aggregate tables."
tags: [projects, dialogue-corpus, lexical-diversity, tidy-data, Spanish]
---

# Pracomul-SLC Analyzer

<div class="answer-meta" markdown>
<span>dialogue corpus</span>
<span>tidy data</span>
<span>lexical diversity</span>
</div>

## What this project does

Pracomul-SLC Analyzer turns a Pracomul SLC-style dialogue-corpus export into tidy data frames and precomputed aggregate tables. It recognizes speaker turns, normalizes transcription artefacts, attaches speaker metadata, computes lexical-diversity and sentence-level diagnostics, and exports CSV outputs.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/pracomul)

## Use this when

- you have dialogue data with speaker turns and metadata;
- you need to transform a plain-text corpus export into analysis-ready tables;
- you want users to compare token-level, turn-level, speaker-level, and aggregate data;
- you need a concrete example of lexical-diversity measures in a pipeline.

## What to inspect in the code

- `analyze_slc.py` — the main self-contained pipeline.
- `analysis.ipynb` and related notebooks — exploratory analysis.
- `slc_column_dictionary.xlsx` — column documentation.
- `results/` — generated output tables, if present.
- `data/` — source material; check rights before reuse.

## Minimal run path

```bash
conda create -n slc python=3.10 spacy lexicalrichness pandas tqdm -c conda-forge
conda activate slc
python -m spacy download es_core_news_md
python analyze_slc.py data/corpus.txt results
```

Expected outputs include token tables, turn tables, speaker-centered tables, aggregate summaries, and lexical-diversity measures.

## Relevant playbook workflows

- [How do I turn messy humanities notes into a reusable dataset?](../scenarios/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md)
- [How do I visualise a frequency list with Voyant?](../scenarios/visualization/visualise-a-frequency-list-with-voyant.md)
- [How do I make an interactive term-frequency dashboard?](../scenarios/visualization/make-an-interactive-term-frequency-dashboard.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to draw the data model: corpus → document → speaker → turn → token → aggregate. Then have them decide which research questions require each level.

## Limits and cautions

- Dialogue transcription conventions shape the output.
- Sentence boundaries in conversational data are approximate.
- Lexical-diversity metrics are sensitive to text length and preprocessing.
- Original transcripts may have non-commercial or restricted-use licensing.
