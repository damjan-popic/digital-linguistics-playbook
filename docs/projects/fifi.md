---
title: "FiFi"
description: "A crawler and corpus builder for preparing institutional website content for retrieval and chatbot use."
tags: [projects, crawler, chatbot, RAG, institutional-websites]
---

# FiFi

<div class="answer-meta" markdown>
<span>crawler</span>
<span>RAG</span>
<span>institutional website</span>
</div>

## What this project does

FiFi crawls an institutional website and builds a corpus suitable for retrieval and chatbot preparation. It outputs page/file records, text chunks, downloaded files, optional HTML snapshots, and a crawl manifest with provenance metadata.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/fifi)

## Use this when

- you need to prepare website content for a source-grounded assistant;
- you want to teach crawling, chunking, and metadata as separate steps;
- you need a clear example of `documents.jsonl` plus `chunks.jsonl`;
- you want to explain why retrieval needs navigation metadata, not only text.

## What to inspect in the code

- `fifi/crawler.py` — crawl logic and corpus generation.
- `scripts/crawl_ff.py` — CLI entry point.
- `data/` — local crawl outputs, intentionally kept out of Git.
- `documents.jsonl` output — source records.
- `chunks.jsonl` output — retrieval-ready chunks.
- `manifest.json` output — crawl summary.

## Minimal run path

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

python scripts/crawl_ff.py \
  --output-dir data/ff-main \
  --max-html-pages 1500 \
  --max-files 600
```

## Relevant playbook workflows

- [How do I scrape a single-topic website into a mini corpus?](../scenarios/corpora/scrape-a-single-topic-website-into-a-mini-corpus.md)
- [How do I audit AI output against source documents?](../scenarios/ai/audit-ai-output-against-source-documents.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to design a crawl manifest before crawling. They should specify scope, excluded hosts, file types, chunk size, metadata fields, and the policy for pages that require login or contain personal data.

## Limits and cautions

- Institutional websites may contain personal data, outdated content, private systems, or login-protected areas.
- Chunks should keep enough metadata to cite and navigate back to the source.
- Crawl outputs should be reviewed before being embedded, indexed, or published.
- A chatbot corpus is only as good as its source scope, freshness, and retrieval metadata.
