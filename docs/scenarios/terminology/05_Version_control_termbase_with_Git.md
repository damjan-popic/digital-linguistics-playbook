---
title: Controlling versions of a termbase with Git
category: Terminology
tags: [git, TBX, intermediate]
---

**When to use** Track edits & collaborate asynchronously.

**Input** `*.tbx`

**Tools** [Git](https://git-scm.com), [Git LFS](https://git-lfs.github.com)

**Steps** `git lfs track "*.tbx"` ▸ commit ▸ push

**Output** History with diffs

!!! tip "Pro tip"
    Use `git diff --color-words` for readable changes.

---
