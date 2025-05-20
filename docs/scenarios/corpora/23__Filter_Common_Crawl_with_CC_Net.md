---
title: _Filter_Common_Crawl_with_CC_Net
---

**When to use** Create large clean monolingual corpus.
**Input** Common Crawl dump list
**Tools** [CC‑Net](https://github.com/facebookresearch/cc_net), [fastText](https://fasttext.cc)
**Steps** `cc_net download ...` ▸ `cc_net clean ...`
**Output** Deduplicated JSONL
**Pro tips** Raise min_len for quality.

---
