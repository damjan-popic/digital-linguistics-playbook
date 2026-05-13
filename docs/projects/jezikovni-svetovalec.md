---
title: "Jezikovni svetovalec"
description: "A source-grounded Slovenian language-advisor architecture with a persistent LLM-maintained wiki."
tags: [projects, language-advisor, RAG, wiki, Slovene]
---

# Jezikovni svetovalec

<div class="answer-meta" markdown>
<span>language advisor</span>
<span>source-grounded answers</span>
<span>rights caution</span>
</div>

## What this project does

Jezikovni svetovalec is an architecture for answering Slovenian language questions from a local source corpus and maintaining a persistent LLM-supported wiki. It combines raw source layers, extracted corpus pages, a searchable index, context-building tools, agent instructions, and a durable Markdown wiki.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/jezikovni-svetovalec)

## Use this when

- you want to design a source-grounded language-advice system;
- you need a model for separating raw sources, extracted source text, and generated wiki summaries;
- you want to teach why answers should cite the source layer;
- you need an example of a persistent knowledge base maintained alongside LLM workflows.

## What to inspect in the code

- `data/raw/` — raw source PDFs, if present locally and lawfully available.
- `data/corpus/` — extracted page-level and combined Markdown.
- `data/index/search.sqlite` — full-text index.
- `tools/search.py` — source search.
- `tools/context.py` — context-pack building.
- `tools/wiki_search.py` and `tools/wiki_lint.py` — persistent wiki maintenance.
- `wiki/` — durable Markdown pages, log, and index.
- `AGENTS.md`, `.agents/`, `.github/`, `CLAUDE.md` — agent instructions.

## Minimal run path

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
python tools/search.py "vejica pred ki"
python tools/context.py "Ali se Novo mesto piše z veliko začetnico?"
python tools/wiki_search.py "naselbinska imena"
python tools/wiki_lint.py
```

## Relevant playbook workflows

- [How do I audit AI output against source documents?](../scenarios/ai/audit-ai-output-against-source-documents.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)
- [How do I decide whether a digitised source should be public?](../scenarios/ethics/decide-whether-a-digitised-source-should-be-public.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)

## Practice use

Ask users to design a source-grounded answer protocol. For one language question, they should specify: source priority, citation format, source-vs-summary separation, update log entry, and what should happen when sources disagree.

## Limits and cautions

- The repository README explicitly treats source PDFs and extracted text as restricted course material unless redistribution rights are clear.
- This project should be used publicly as an architecture pattern unless the source corpus has been legally cleared.
- Source-grounded answers still require verification, especially for normative language questions.
- Generated wiki summaries should never replace source citations.
