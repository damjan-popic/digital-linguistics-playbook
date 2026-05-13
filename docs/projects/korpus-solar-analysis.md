---
title: "Šolar lexical analysis pipeline"
description: "A project-specific pipeline for safe CLASSLA reannotation and lexical/syntactic analysis of Šolar data."
tags: [projects, Šolar, CLASSLA, lexical-diversity, corpus-analysis]
---

# Šolar lexical analysis pipeline

<div class="answer-meta" markdown>
<span>corpus analysis</span>
<span>reannotation</span>
<span>reports</span>
</div>

## What this project does

The Šolar lexical analysis pipeline reannotates Šolar CoNLL-U data with CLASSLA while preserving source IDs, sentence boundaries, token IDs, token forms, and metadata links. It then runs lexical, syntactic, collocation, statistical, plotting, and reporting workflows.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/korpus-solar-analysis)

## Use this when

- you need a model example of ID-safe reannotation;
- you want to compare original and regenerated annotation layers;
- you need a corpus-analysis pipeline that produces tables, plots, and Markdown reports;
- you want users to understand why metadata linkage can break during NLP processing.

## What to inspect in the code

- `scripts/run_solar_pipeline.py` — full workflow runner.
- `scripts/solar_reannotate.py` — ID-safe CLASSLA reannotation.
- `scripts/check_solar_conllu.py` — sanity checks for CoNLL-U and metadata.
- `scripts/solar_analysis.py` — quantitative analysis.
- `scripts/build_report.py` — Markdown report generation.
- `scripts/prepare_mwe_review.py` — manual-review sheet for MWE candidates.
- `configs/` — one-command pipeline configuration.

## Minimal run path

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_solar_pipeline.py \
  --models-dir ~/classla_resources_shared \
  --download-models
```

The original corpus file must be placed where the README expects it. Do not assume the raw corpus is included.

## Relevant playbook workflows

- [How do I annotate a corpus with UDPipe?](../scenarios/nlp/annotate-a-corpus-with-udpipe.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I build a collocation graph from AntConc to Cytoscape?](../scenarios/visualization/build-a-collocation-graph-from-antconc-to-cytoscape.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Show users two CoNLL-U snippets: one with preserved `sent_id` values and one with generated replacement IDs. Ask them to explain which one can still be joined to metadata and why.

## Limits and cautions

- The pipeline is intentionally specific to Šolar metadata and research questions.
- Some outputs are exploratory, especially MWE/collocation candidates.
- Contact-zone or regional labels should be treated as coarse triage, not as standalone dialectological conclusions.
- Reannotation changes the linguistic layer; it should be documented as a new version, not silently merged with the original.
