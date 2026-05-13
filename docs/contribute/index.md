# Contribute

Contributions should be small, useful, and easy to test.

## Add an answer

Use the [topic template](topic-template.md) for a complete Markdown structure, or generate a starter page with the helper script:

```bash
python scripts/new_answer.py "How do I clean OCR text for corpus analysis?" --category corpora --difficulty beginner --tags OCR,corpus,cleaning
```

Then edit the generated file. If the page is meant to point readers to real code, add a **Worked example** section and link to the relevant page in [Projects and code](../projects/index.md).

## Add a project page

Use the [project page template](project-template.md) when documenting a repository as a worked code example. Project pages should explain what the repository does, what to inspect, how to run the smallest safe version, what outputs to expect, and what data or rights limitations apply.

## Check before opening a pull request

```bash
python scripts/check_answers.py
mkdocs build --strict
```

## What maintainers should ask

- Does this answer one practical question?
- Is the workflow tested on a tiny example?
- Are failure modes named honestly?
- Are rights, privacy, and source provenance addressed where needed?
- Could a tired reader follow it without extra explanation?

If the answer to the last one is no, simplify.
