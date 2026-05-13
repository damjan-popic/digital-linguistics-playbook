---
title: "TextHarvester"
description: "A small Python tool for harvesting readable web text into corpus-ready files."
tags: [projects, corpus, scraping, web, python]
---

# TextHarvester

<div class="answer-meta" markdown>
<span>corpus building</span>
<span>Python</span>
<span>web text</span>
</div>

## What this project does

TextHarvester collects readable text from web pages. For each URL, it downloads the HTML, removes obvious boilerplate, detects language, wraps the result in a minimal corpus-like structure, and saves one text file per URL.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/text_harvester)

## Use this when

- you need a small web corpus for teaching, exploration, or a pilot study;
- you want a transparent introduction to content extraction heuristics;
- you need users to inspect how scraping, cleaning, language detection, and export are connected;
- you want a lightweight alternative to a large crawler.

## What to inspect in the code

- `textharvester.py` — the main script and importable functions.
- `harvest()` — the function that returns the extracted result.
- `save_result_as_txt()` — the export step.
- HTML-cleaning and content-selection functions — useful for showing how boilerplate removal is only an informed guess.
- Language-detection logic — useful for multilingual-page diagnostics.

## Minimal run path

```bash
pip install requests beautifulsoup4 lxml langdetect
python textharvester.py https://example.org/article
```

Expected output:

```text
harvested_texts/example_org_article.txt
```

The file contains a minimal `<corpus><text ...>` wrapper with URL, title, download time, primary language, language distribution, and extracted paragraphs.

## Relevant playbook workflows

- [How do I scrape a single-topic website into a mini corpus?](../scenarios/corpora/scrape-a-single-topic-website-into-a-mini-corpus.md)
- [How do I filter a corpus by language with fastText?](../scenarios/corpora/filter-a-corpus-by-language-with-fasttext.md)
- [How do I package a corpus with FAIR metadata?](../scenarios/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I write a README for a humanities dataset?](../scenarios/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to harvest three pages from the same website. They should compare the extracted text with the original pages and mark:

- what was kept correctly;
- what boilerplate remained;
- what useful content was removed;
- whether language detection matches the main article text.

## Limits and cautions

- Content extraction is heuristic. It will fail on some layouts.
- Scraping should respect terms of use, access limits, robots policies, and copyright.
- A small script is not a preservation system. Keep source URLs, timestamps, and notes about collection scope.
- Do not treat harvested text as neutral: menus, captions, comments, ads, and related links can slip into the corpus.
