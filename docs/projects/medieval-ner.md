---
title: "Medieval NER"
description: "A hybrid and supervised workflow for person extraction in medieval notarial material."
tags: [projects, NER, historical-texts, annotation, medieval]
---

# Medieval NER

<div class="answer-meta" markdown>
<span>historical NLP</span>
<span>NER</span>
<span>annotation schema</span>
</div>

## What this project does

Medieval NER is a blueprint for extracting person mentions from medieval notarial material. It combines a hybrid extractor baseline with a planned supervised fine-tuning workflow, using explicit `PER` span annotation as the safest first target.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/medieval-ner)

## Use this when

- you need a concrete historical-NLP case study;
- you want to teach why domain-specific NER cannot simply be delegated to an off-the-shelf model;
- you need an example of starting with a small label set before expanding an annotation schema;
- you want to compare rule-based extraction, model-based extraction, and hybrid post-processing.

## What to inspect in the code

- `process_ner.py` — hybrid inference pipeline.
- `Rules.md` — extraction expectations.
- `annotation_guidelines.md` — annotation guidance.
- `train_ner.py` — fine-tuning entry point.
- `evaluate_ner.py` — evaluation on token labels and entity spans.
- `prepare_training_data.py` — conversion from character-span annotations to token labels.
- `data/annotation_schema.md` — annotation standard.

## Minimal run path

For a pilot workflow:

```bash
.venv/bin/python prepare_training_data.py \
  --input data/annotations/example_annotations.jsonl \
  --output data/processed/example_tokenized.jsonl

.venv/bin/python train_ner.py \
  --train data/splits/train.jsonl \
  --dev data/splits/dev.jsonl \
  --output-dir models/medieval-ner-per

.venv/bin/python evaluate_ner.py \
  --model models/medieval-ner-per \
  --test data/splits/test.jsonl
```

## Relevant playbook workflows

- [How do I extract named entities with spaCy?](../scenarios/nlp/extract-named-entities-with-spacy.md)
- [How do I audit AI output against source documents?](../scenarios/ai/audit-ai-output-against-source-documents.md)
- [How do I make a tiny digital edition of a historical text?](../scenarios/editions/make-a-tiny-digital-edition-of-a-historical-text.md)
- [How do I visualise uncertainty in humanities data?](../scenarios/visualization/visualise-uncertainty-in-humanities-data.md)

## Practice use

Give users five short medieval-style passages and ask them to annotate only explicit person spans using `B-PER` and `I-PER`. Then compare disagreements: title boundary, patronymic boundary, place-origin phrase, saint reference, and repeated mention.

## Limits and cautions

- The first useful label set is deliberately narrow.
- Historical spelling, formulaic phrases, and abbreviated references can break generic NER.
- Fine-tuning requires consistent annotation more than a large but noisy dataset.
- Exact-span evaluation is more meaningful here than loose token-level success.
