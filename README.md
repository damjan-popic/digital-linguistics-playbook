# Digital Linguistics Playbook

A living, classroom-built FAQ for digital linguistics and digital humanities.

The project collects short, practical answers to questions like:

- How do I turn an Excel glossary into TBX?
- How do I OCR a batch of scanned PDFs?
- How do I map places mentioned in a text?
- How do I audit an AI-generated summary against a source?

The site is built with **MkDocs Material** and designed for GitHub Pages. Students can contribute one small answer at a time, which keeps the project delightfully alive instead of becoming yet another noble-but-dead course repository.

## What changed in this revamp

- Reworked the site into a question-first FAQ/playbook.
- Added a clean MkDocs Material setup with search, tags, cards, dark mode, and polished CSS.
- Removed generated/local clutter from the source repo: `site/` and `venv/` now belong in `.gitignore`.
- Added GitHub Pages deployment workflow.
- Added contribution docs, answer template, style guide, rubric, classroom sprint formats, and a large question bank.
- Expanded the original 38 scenarios into polished, consistent how-to pages and added broader digital-humanities starters.
- Added scripts for creating and checking answer pages.

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

1. Push this repo to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions**.
4. Push to `main`; the workflow in `.github/workflows/pages.yml` builds and publishes the site.

## Contribution rhythm for classes

A good cycle is:

1. Students claim a question from the question bank.
2. They draft one answer with a tiny reproducible workflow.
3. Another group tests it.
4. The authors revise using the rubric.
5. The class merges the answer and celebrates the tiny public good they just created.

Small, tested, honest answers beat giant heroic tutorials every time.
