# Start here

The Playbook is organized around a simple format: **one question, one workflow, one verifiable output**.

## Find a workflow

Use the navigation, tags, or search to find a page that matches your task. The best match is usually a concrete question, such as:

- How do I OCR a batch of scanned PDFs?
- How do I map places mentioned in a text?
- How do I turn messy notes into a reusable dataset?
- How do I audit an AI-generated summary against source documents?

## Read before running

Before following a workflow, check:

- what input data or source material is required;
- which tools or accounts are needed;
- what output the workflow should produce;
- which checks are recommended before trusting the result;
- whether there are rights, privacy, licensing, or provenance issues.

## Work small first

Run every workflow on a tiny sample before scaling up. A five-line test file, one scanned page, or one short text can reveal problems before they become expensive.

## Move from workflow to code

Use [Projects and code](projects/index.md) when you want to inspect a real repository related to a workflow. Project pages point to the relevant code files, expected outputs, reuse limits, and linked playbook questions.

## Improve the playbook

Every page can be refined. Useful contributions include clearer steps, better examples, screenshots, alternative tools, updated links, accessibility notes, project links, and more precise warnings about failure modes.

## Local commands

```bash
pip install -r requirements.txt
mkdocs serve
python scripts/check_answers.py
mkdocs build --strict
```
