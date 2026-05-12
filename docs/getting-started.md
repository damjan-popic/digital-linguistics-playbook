# Start here

The Playbook is built around a simple format: **one question, one answer, one testable workflow**.

## For students

1. Pick a question from the [question bank](classroom/question-bank.md).
2. Draft the answer using the [answer template](contribute/answer-template.md).
3. Test the workflow on a tiny example.
4. Add checks, traps, and an honest note about limits.
5. Ask another group to test it.

## For teachers

Use the repo as a repeatable class project. Each semester can add a new layer:

- one cohort adds beginner answers;
- another tests and revises them;
- another adds screenshots or datasets;
- another localises examples for Slovene or other languages.

This makes the repository a never-ending story in the good way, not the “abandoned wiki from 2017” way.

## For maintainers

Keep the bar low enough for students to contribute, but high enough that pages are useful:

- every page must answer a practical question;
- every page must include checks and common traps;
- every tool-heavy page should state what was actually tested;
- every data page should mention provenance, rights, and uncertainty.

## Local commands

```bash
pip install -r requirements.txt
mkdocs serve
python scripts/check_answers.py
mkdocs build --strict
```
