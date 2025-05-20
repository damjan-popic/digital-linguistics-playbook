---
title:  Bulk download PDFs OCR
---

**When to use** Harvest scanned PDFs to text.

**Input** CSV of PDF URLs

**Tools** [wget](https://www.gnu.org/software/wget/), [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), [pdfimages](https://poppler.freedesktop.org), [pdftoppm](https://poppler.freedesktop.org)

**Steps** `wget -i links.csv -P pdfs` ▸ OCR images

**Output** ./ocr_text/*.txt

!!! tip "Pro tip"
    Use `--psm 6` for columns.

---
