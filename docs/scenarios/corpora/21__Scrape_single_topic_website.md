---
title: _Scrape_single_topic_website
---

**When to use** Build niche corpus fast.
**Input** Seed URLs in `seeds.txt`
**Tools** [requests](https://docs.python-requests.org), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [readability-lxml](https://github.com/buriy/python-readability)
**Steps** `python scrape.py --seeds seeds.txt --depth 1`
**Output** Folder of clean TXT
**Pro tips** Respect robots.txt; sleep between hits.

---
