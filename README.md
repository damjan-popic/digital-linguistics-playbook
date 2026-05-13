# Digital Linguistics Playbook

An open reference for practical workflows in digital linguistics, language technology, corpus work, translation, archives, publishing, and digital humanities.

The project collects concise answers to practical questions and links selected workflows to real code repositories. Example questions include:

- How do I turn an Excel glossary into TBX?
- How do I OCR a batch of scanned PDFs?
- How do I map places mentioned in a text?
- How do I audit an AI-generated summary against source documents?

The site is built with **MkDocs Material** and is designed for deployment with **GitHub Pages**. The Python/NLP teaching path standardizes on **Python 3.12** to avoid package-compatibility surprises.

## Local setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate      # Windows: py -3.12 -m venv .venv, then .venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

Then open the local address shown in the terminal.

## Build the site

```bash
python scripts/check_answers.py
mkdocs build --strict
```

## Python/NLP starter project

The repository includes a runnable beginner project at `examples/python-nlp-first-steps/`. It contains sample text files, CSV data, Python scripts, and a small `requirements.txt` for the Python 3.12, pandas, and CLASSLA workflows.

## Project and code catalogue

The public site includes a **Projects and code** section. Each project page links a repository to relevant playbook workflows and identifies what to inspect, how to run a minimal example, what outputs to expect, and which data or rights cautions apply.

## Create a new answer page

```bash
python scripts/new_answer.py "How do I clean OCR text for corpus analysis?" --category corpora --difficulty beginner --tags OCR,corpus,cleaning
```

Then edit the generated Markdown file. For a detailed copy-paste structure, see `docs/contribute/topic-template.md`. Run:

```bash
python scripts/check_answers.py
mkdocs build --strict
```

## Recommended GitHub Pages setup

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Push to `main`; the workflow in `.github/workflows/pages.yml` builds and publishes the site.

## Contribution model

Each contribution should answer one practical question, provide a reproducible workflow, name the expected output, and include checks for common failure modes. Small, tested, well-documented procedures are more useful than broad unverified tutorials.

Teaching materials and workshop prompts are kept outside the published documentation tree in `teaching/`.
