# Digital Linguistics Playbook  

> **Legend**  
> **When to use** ▸ **Input** ▸ **Tools** ▸ **Steps** ▸ **Output** ▸ **Pro tips**  
---
## 1 Import terminology Excel → TBX
**When to use** Generate standards‑compliant TBX from a spreadsheet.
**Input** `glossary.xlsx` (columns: ID, EN, ES, Definition)
**Tools** [Glossary Converter](https://www.glossaryconverter.com)
**Steps** 1 Drag file onto app ▸ 2 Map columns ▸ 3 Select “TBX‑Basic”
**Output** `glossary.tbx`
**Pro tips** Tick “Generate term IDs” if the sheet lacks them.

---
## 2 Bulk‑clean glossary in Excel (Power Query)
**When to use** Remove duplicates, trim spaces, unify casing.
**Input** `glossary.xlsx`
**Tools** [Excel Power Query](https://support.microsoft.com/excel)
**Steps** Data › Get & Transform ▸ “Trim/Clean” ▸ “Remove duplicates”
**Output** Clean sheet ready for TBX
**Pro tips** Record steps so you can refresh with new data.

---
## 3 Validate TBX with TBXChecker
**When to use** Catch malformed XML before publishing.
**Input** `*.tbx`
**Tools** [TBXChecker](https://github.com/LTAC-Global/tbxchecker)
**Steps** Open file ▸ Click “Validate”
**Output** Log of errors/warnings
**Pro tips** Fix critical errors first.

---
## 4 Convert TBX → SDL MultiTerm
**When to use** Share a termbase with Trados users.
**Input** `glossary.tbx`
**Tools** [SDL MultiTerm Convert](https://docs.rws.com/889668/520853)
**Steps** Launch wizard ▸ “TBX‑BASIC” ▸ Finish
**Output** `glossary.sdltb`
**Pro tips** Stick to UTF‑8 to avoid diacritics issues.

---
## 5 Version‑control termbase with Git
**When to use** Track edits & collaborate asynchronously.
**Input** `*.tbx`
**Tools** [Git](https://git-scm.com), [Git LFS](https://git-lfs.github.com)
**Steps** `git lfs track "*.tbx"` ▸ commit ▸ push
**Output** History with diffs
**Pro tips** Use `git diff --color-words` for readable changes.

---
## 6 Import termbase into memoQ
**When to use** Enable term recognition in translation grid.
**Input** `*.tbx` or `*.csv`
**Tools** [memoQ](https://www.memoq.com)
**Steps** Resources ▸ Termbases ▸ Import ▸ Map languages
**Output** Active termbase
**Pro tips** Set deprecated terms to “Forbidden”.

---
## 7 Forbidden term QA in CAT tool
**When to use** Enforce branding or regulatory compliance.
**Input** Translation project
**Tools** [memoQ QA](https://help.memoq.com), [Trados QA Checker](https://docs.rws.com)
**Steps** Add term list ▸ Run QA
**Output** Violation report
**Pro tips** Mark as *Critical* to block delivery.

---
## 8 Batch convert subtitle formats (Subtitle Edit)
**When to use** Need SRT, VTT, ASS in one go.
**Input** Master `*.srt`
**Tools** [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit)
**Steps** Select files ▸ Choose target formats ▸ Run
**Output** Multiple subtitle files
**Pro tips** Enable “Maintain time‑codes”.

---
## 9 Auto‑timestamp video with Whisper
**When to use** Generate Spanish subs from scratch.
**Input** `video.mp4`
**Tools** [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit), [Whisper](https://github.com/openai/whisper)
**Steps** Load video ▸ Choose model ▸ Generate
**Output** Timed Spanish SRT
**Pro tips** GPU speeds up ~70 %.

---
## 10 Translate subtitles via DeepL + MKVToolNix
**When to use** Quick bilingual subtitles.
**Input** `es.srt`
**Tools** [DeepL plugin](https://github.com/Barefist/SubtitlesTranslator), [MKVToolNix](https://mkvtoolnix.download)
**Steps** Auto‑translate ▸ Save `en.srt` ▸ `mkvmerge ...`
**Output** MKV with selectable subs
**Pro tips** Use `--language 0:spa`.

---
## 11 Standardise project file naming
**When to use** Ensure reproducible pipelines.
**Input** Mixed files
**Tools** [Bulk Rename Utility](https://www.bulkrenameutility.co.uk)
**Steps** Regex: `{code}_{lang}_{ver}.ext`
**Output** Consistent names
**Pro tips** Describe pattern in README.

---
## 12 Align bilingual docs with LF Aligner
**When to use** Create TM from document pairs.
**Input** `doc_en.txt` + `doc_es.txt`
**Tools** [LF Aligner](https://sourceforge.net/projects/aligner)
**Steps** Choose files ▸ Language pair ▸ Align
**Output** `aligned.tmx`
**Pro tips** Enable Google MT hints.

---
## 13 Build TM with OmegaT
**When to use** Free, cross‑platform TM creation.
**Input** Folders `source/` + `target/`
**Tools** [OmegaT](https://omegat.org)
**Steps** New project ▸ Add files ▸ Align
**Output** `project_save.tmx`
**Pro tips** Split large TMs by domain.

---
## 14 Extract term candidates with AntConc
**When to use** Seed a new termbase.
**Input** Corpus TXT
**Tools** [AntConc](https://www.laurenceanthony.net/software/antconc)
**Steps** Set min freq 5 ▸ Export bigrams
**Output** `terms.csv`
**Pro tips** Filter stop‑words first.

---
## 15 Generate terminology with Termostat
**When to use** Contrastive term extraction.
**Input** Specialised vs. general corpus
**Tools** [Termostat](https://termostat.tsr.cesnet.cz)
**Steps** Upload corpora ▸ Compute key terms
**Output** Ranked list
**Pro tips** Log‑likelihood is robust.

---
## 16 Custom stop‑word list for spaCy
**When to use** Improve NLP preprocessing.
**Input** Corpus
**Tools** [spaCy](https://spacy.io)
**Steps** Build frequency list ▸ Manual prune ▸ `update(set)`
**Output** `stopwords.json`
**Pro tips** Maintain per‑domain lists.

---
## 17 Annotate corpus with UDPipe
**When to use** Add POS, lemma, dependency parse.
**Input** TXT
**Tools** [UDPipe](https://ufal.mff.cuni.cz/udpipe)
**Steps** `udpipe --tokenize --tag --parse model.udpipe text.txt > out.conllu`
**Output** `out.conllu`
**Pro tips** Chunk large files to avoid OOM.

---
## 18 Query corpus with CQPweb
**When to use** Advanced pattern queries.
**Input** Vertical file
**Tools** [CQPweb](https://cwb.sourceforge.io/cqpweb.php)
**Steps** Upload ▸ Build indexes ▸ Run CQP
**Output** KWIC + frequency tables
**Pro tips** Save query favorites.

---
## 19 Visualise frequency list with Voyant
**When to use** Quickly show word clouds.
**Input** Corpus
**Tools** [Voyant Tools](https://voyant-tools.org)
**Steps** Upload ▸ “Cirrus”
**Output** Interactive visual
**Pro tips** Export SVG.

---
## 20 Cross‑lingual embeddings with fastText
**When to use** Compare semantic similarity across languages.
**Input** Sentence lists
**Tools** [fastText](https://fasttext.cc)
**Steps** `fasttext print-word-vectors ...`
**Output** `vecs.tsv`
**Pro tips** Use PCA for plotting.

---
## 21 Scrape single-topic website
**When to use** Build niche corpus fast.
**Input** Seed URLs in `seeds.txt`
**Tools** [requests](https://docs.python-requests.org), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [readability-lxml](https://github.com/buriy/python-readability)
**Steps** `python scrape.py --seeds seeds.txt --depth 1`
**Output** Folder of clean TXT
**Pro tips** Respect robots.txt; sleep between hits.

---
## 22 Bulk download PDFs & OCR
**When to use** Harvest scanned PDFs to text.
**Input** CSV of PDF URLs
**Tools** [wget](https://www.gnu.org/software/wget/), [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), [pdfimages](https://poppler.freedesktop.org), [pdftoppm](https://poppler.freedesktop.org)
**Steps** `wget -i links.csv -P pdfs` ▸ OCR images
**Output** ./ocr_text/*.txt
**Pro tips** Use `--psm 6` for columns.

---
## 23 Filter Common Crawl with CC‑Net
**When to use** Create large clean monolingual corpus.
**Input** Common Crawl dump list
**Tools** [CC‑Net](https://github.com/facebookresearch/cc_net), [fastText](https://fasttext.cc)
**Steps** `cc_net download ...` ▸ `cc_net clean ...`
**Output** Deduplicated JSONL
**Pro tips** Raise min_len for quality.

---
## 24 Deduplicate with MinHash
**When to use** Remove near‑duplicate sentences.
**Input** TXT corpus folder
**Tools** [datasketch](https://ekzhu.github.io/datasketch/)
**Steps** MinHash 128‑bit ▸ LSH 0.9
**Output** clean.txt + log
**Pro tips** Lower‑case tokens first.

---
## 25 Language‑ID filter with fastText
**When to use** Strip noise languages.
**Input** Raw TXT
**Tools** [fastText](https://fasttext.cc)
**Steps** `fasttext predict-prob ...`
**Output** English‑only corpus
**Pro tips** Parallelise with GNU Parallel.

---
## 26 Collocation graph AntConc → Cytoscape
**When to use** Visualise lexical networks.
**Input** Plain‑text corpus
**Tools** [AntConc](https://www.laurenceanthony.net/software/antconc), [Cytoscape](https://cytoscape.org)
**Steps** AntConc Collocates ▸ Export CSV ▸ Cytoscape import
**Output** Interactive graph
**Pro tips** Filter MI<3 edges.

---
## 27 Dispersion plot in LancsBox
**When to use** Show keyword distribution.
**Input** TXT file(s)
**Tools** [LancsBox](https://corpora.lancs.ac.uk/lancsbox)
**Steps** Load corpus ▸ Search ▸ Plot
**Output** PNG/SVG plot
**Pro tips** Normalise by section length.

---
## 28 Entity extraction with spaCy
**When to use** Generate terminology seeds.
**Input** TXT files
**Tools** [spaCy](https://spacy.io), [pandas](https://pandas.pydata.org)
**Steps** Run NER ▸ Save to CSV
**Output** entities.csv
**Pro tips** Filter by POS pattern.

---
## 29 Sentence‑align EuroParl with hunalign
**When to use** Build parallel MT data.
**Input** EuroParl XML pair
**Tools** [hunalign](https://github.com/danielvarga/hunalign), [EuroParl](https://www.statmt.org/europarl/)
**Steps** Strip XML ▸ `hunalign ...`
**Output** aligned.txt
**Pro tips** Use dictionary for recall.

---
## 30 Harvest bilingual subtitles via OpenSubtitles
**When to use** Obtain colloquial parallel lines.
**Input** Movie IDs
**Tools** [OpenSubtitles API](https://opensubtitles.stoplight.io/), [pysrt](https://github.com/byroot/pysrt)
**Steps** Download subs ▸ Align timelines
**Output** subtitles.jsonl
**Pro tips** Filter CPS >20.

---
## 31 Back‑translate with OPUS‑MT
**When to use** Augment low‑resource side.
**Input** Monolingual tgt text
**Tools** [Marian](https://marian-nmt.github.io), [OPUS‑MT](https://huggingface.co/Helsinki-NLP)
**Steps** `marian-decoder ...`
**Output** synthetic_src.txt
**Pro tips** Tag lines __BT__.

---
## 32 Evaluate MT with COMET‑22
**When to use** Human‑oriented SOTA metric.
**Input** src,mt,ref
**Tools** [COMET](https://github.com/Unbabel/COMET)
**Steps** `comet evaluate ...`
**Output** comet_scores.csv
**Pro tips** Bootstrap 95 % CI.

---
## 33 Speaker diarisation with Pyannote
**When to use** Segment audio by speaker.
**Input** audio.wav
**Tools** [pyannote.audio](https://github.com/pyannote/pyannote-audio)
**Steps** Run pipeline ▸ Export RTTM
**Output** RTTM + JSON
**Pro tips** Fine‑tune on meetings.

---
## 34 Auto subtitle + burn‑in with FFmpeg
**When to use** Create bilingual hard‑sub video.
**Input** video.mp4
**Tools** [Whisper](https://github.com/openai/whisper), [FFmpeg](https://ffmpeg.org)
**Steps** Whisper ▸ Translate ▸ `ffmpeg ... subtitles=`
**Output** out.mp4
**Pro tips** Use `-crf 23` to compress.

---
## 35 Interactive term‑frequency dashboard
**When to use** Stakeholder‑friendly live filtering.
**Input** term_count.csv
**Tools** [Observable Plot](https://observablehq.com/plot)
**Steps** Upload CSV ▸ Plot.barY
**Output** Web dashboard
**Pro tips** Cache dataset in gist.

---
## 36 Sentence similarity heat‑map
**When to use** Track topic drift over series.
**Input** Sentences list
**Tools** [sentence-transformers](https://www.sbert.net), [Matplotlib](https://matplotlib.org)
**Steps** Encode ▸ Cos matrix ▸ imshow
**Output** heatmap.png
**Pro tips** Cluster reorder for clarity.

---
## 37 Package corpus with FAIR metadata
**When to use** Publish corpus for reuse & citation.
**Input** clean/*.txt
**Tools** [jsonschema](https://json-schema.org), [Zenodo](https://zenodo.org)
**Steps** Compute stats ▸ metadata.json ▸ zip
**Output** mycorpus.zip
**Pro tips** Add SHA‑256 checksums.

---
## 38 Automate pipeline with Makefile
**When to use** One‑command reproducible build.
**Input** Raw data + Makefile
**Tools** [GNU Make](https://www.gnu.org/software/make)
**Steps** Define targets clean/align/evaluate
**Output** report.txt
**Pro tips** Use .PHONY; SHELL=/bin/bash.
