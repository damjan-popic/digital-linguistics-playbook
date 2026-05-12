# Contribute

Contributions should be small, useful, and easy to test.

## Add an answer

Use the helper script:

```bash
python scripts/new_answer.py "How do I clean OCR text for corpus analysis?" --category corpora --difficulty beginner --tags OCR,corpus,cleaning
```

Then edit the generated file.

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
- Could a tired student follow it on a Thursday afternoon?

If the answer to the last one is no, simplify.
