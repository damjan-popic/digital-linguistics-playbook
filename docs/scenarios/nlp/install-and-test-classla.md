---
title: "How do I install and test CLASSLA with Python 3.12?"
description: "A cautious beginner workflow for installing CLASSLA in a Python 3.12 virtual environment and testing it on one sentence."
category: "NLP"
difficulty: "beginner"
time: "30–60 min"
tags: [Python, CLASSLA, Slovene, NLP, installation]
---

# How do I install and test CLASSLA with Python 3.12?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

CLASSLA is a Python toolkit for linguistic annotation of South Slavic languages, including Slovene. This workflow installs it in a clean **Python 3.12** virtual environment and tests one sentence before doing anything ambitious.

!!! quote "One-sentence version"
    Use Python 3.12, install CLASSLA inside `.venv`, download the model, and test one sentence before processing a corpus.

## You need

- Python 3.12, not higher.
- An activated virtual environment.
- Internet access for installing packages and downloading models.
- Enough disk space for language models.
- Patience with first-time model downloads.

## Tools

- [CLASSLA](https://github.com/clarinsi/classla): linguistic annotation toolkit.
- `pip`: Python package installer.
- Python scripts for repeatable annotation.

## Workflow

1. Create and activate a Python 3.12 virtual environment.

On Windows:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

2. Upgrade packaging tools.

```bash
python -m pip install --upgrade pip setuptools wheel
```

3. Install CLASSLA.

```bash
python -m pip install classla
```

4. Download the Slovene model.

```bash
python -c "import classla; classla.download('sl')"
```

5. Create `scripts/test_classla.py`.

```python
import classla

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp("To je kratek preizkus slovenskega jezikovnega označevanja.")

for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.upos, sep="\t")
```

6. Run the script.

```bash
python scripts/test_classla.py
```

## Output

A terminal output with token, lemma, and UPOS tag for each word in the test sentence.

## Check yourself

- Does `python --version` show Python 3.12 inside the environment?
- Did CLASSLA download the Slovene model successfully?
- Does the test script print one token per line?
- Are Slovene characters displayed correctly?

## Common traps

- Using Python 3.13 or higher and hitting package compatibility problems.
- Forgetting to activate the virtual environment before installing CLASSLA.
- Downloading a model once and assuming it is included in Git. Models are local resources, not source code.
- Starting with a large corpus before testing one sentence.

## Practice task

Change the test sentence, rerun the script, and identify the lemma and POS tag of three Slovene words.

## Useful extension

After the test works, save the package list:

```bash
python -m pip freeze > requirements.txt
```
