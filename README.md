# Digital Linguistics Playbook

An open reference for practical workflows in digital linguistics, language technology, corpus work, translation, archives, publishing, and digital humanities.

The project collects concise answers to questions such as:

- How do I turn an Excel glossary into TBX?
- How do I OCR a batch of scanned PDFs?
- How do I map places mentioned in a text?
- How do I audit an AI-generated summary against source documents?

The site is built with **MkDocs Material** and is designed for deployment with **GitHub Pages**.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Then open the local address shown in the terminal.

## Build the site

```bash
python scripts/check_answers.py
mkdocs build --strict
```

## Create a new answer page

```bash
python scripts/new_answer.py "How do I clean OCR text for corpus analysis?" --category corpora --difficulty beginner --tags OCR,corpus,cleaning
```

Then edit the generated Markdown file and run:

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
