---
title:  Filter Common Crawl with CC Net
---

**When to use** Create large clean monolingual corpus.

**Input** Common Crawl dump list

**Tools** [CC‑Net](https://github.com/facebookresearch/cc_net), [fastText](https://fasttext.cc)

**Steps** `cc_net download ...` ▸ `cc_net clean ...`

**Output** Deduplicated JSONL

!!! tip "Pro tip"
    Raise min_len for quality.

---
