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

Use [Code examples](projects/index.md) when you want to inspect a real repository related to a workflow. Code-example pages point to the relevant code files, expected outputs, reuse limits, and linked playbook questions.

## Improve the playbook

Every page can be refined. Useful contributions include clearer steps, better examples, screenshots, alternative tools, updated links, accessibility notes, project links, and more precise warnings about failure modes.

## Local commands

```bash
pip install -r requirements.txt
mkdocs serve
python scripts/check_answers.py
mkdocs build --strict
```

## If you are starting with Python

Start with the small NLP path:

1. [Install Python 3.12 for NLP work](scenarios/nlp/install-python-312-for-nlp.md)
2. [Create a Python 3.12 virtual environment](scenarios/nlp/create-a-python-312-virtual-environment.md)
3. [Install Python packages with pip](scenarios/nlp/install-python-packages-with-pip.md)
4. [Run a Python script from the terminal](scenarios/nlp/run-a-python-script-from-terminal.md)
5. [Read and write text files in Python](scenarios/nlp/read-and-write-text-files-in-python.md)
6. [Read and write CSV files with pandas](scenarios/nlp/read-and-write-csv-files-with-pandas.md)
7. [Structure a small Python NLP project](scenarios/nlp/structure-a-small-python-nlp-project.md)
8. [Troubleshoot Python venv and pip problems](scenarios/nlp/troubleshoot-python-venv-and-pip.md)
9. [Use the Python/NLP starter project](scenarios/nlp/use-the-python-nlp-starter-project.md)
10. [Install and test CLASSLA with Python 3.12](scenarios/nlp/install-and-test-classla.md)
11. [Annotate a small text with CLASSLA](scenarios/nlp/annotate-a-small-text-with-classla.md)
12. [Export CLASSLA results to CSV](scenarios/nlp/export-classla-results-to-csv.md)

Use Python 3.12 for these workflows. Do not jump to a newer Python version unless the project documentation says it is supported.

