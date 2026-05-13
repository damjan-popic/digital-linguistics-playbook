---
title: "Corpus Augmenter"
description: "A CLASSLA-based pipeline for converting and enriching TEI, VRT, and CoNLL-U corpora."
tags: [projects, CLASSLA, CoNLL-U, TEI, annotation]
---

# Corpus Augmenter

<div class="answer-meta" markdown>
<span>NLP</span>
<span>CLASSLA</span>
<span>CoNLL-U</span>
</div>

## What this project does

Corpus Augmenter is a Slovene corpus-processing pipeline built around CLASSLA. It converts TEI or VRT/Vert inputs into CoNLL-U-like structures, fills missing annotation layers, combines files, and preserves existing annotation where possible.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/corpus_augmenter)

## Use this when

- you have TEI, VRT, or partial CoNLL-U and need a more complete linguistic annotation layer;
- you need to preserve manual annotations while filling missing fields;
- you want to teach the difference between conversion, annotation, augmentation, and validation;
- you need users to see why metadata comments matter in CoNLL-U workflows.

## What to inspect in the code

- `tei2conllu.py` — TEI-to-CoNLL-U conversion.
- `vert2conllu.py` — VRT/Vert conversion.
- `xml2conllu.py` — XML conversion support.
- `run_classla.py` — the main annotation/augmentation driver.
- `run_classla_shards.py` — batch or shard-oriented processing.
- `file_compare.py` — useful for inspecting before/after differences.

## Minimal run path

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install classla rich
python -c "import classla; classla.download('sl')"
```

Typical augmentation pattern:

```bash
python run_classla.py \
  --mode augment \
  --lang sl \
  --in out_conllu_from_tei \
  --out out_augmented \
  --stats out_stats
```

## Relevant playbook workflows

- [How do I annotate a corpus with UDPipe?](../scenarios/nlp/annotate-a-corpus-with-udpipe.md)
- [How do I extract named entities with spaCy?](../scenarios/nlp/extract-named-entities-with-spacy.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I automate a linguistic workflow with a Makefile?](../scenarios/automation/automate-a-linguistic-workflow-with-a-makefile.md)

## Practice use

Give users a tiny TEI or CoNLL-U sample with missing layers. Ask them to predict which fields should remain unchanged and which fields should be filled by CLASSLA. Then run the augmentation and compare.

## Limits and cautions

- CLASSLA model output is annotation, not truth. Manual checks remain necessary.
- GPU support speeds up large corpora, but CPU runs may be slow.
- Conversion scripts must be checked against the actual source schema.
- Idempotence matters: re-running should not silently overwrite trusted annotations.
