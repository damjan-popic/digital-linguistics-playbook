---
title: "Projects and code"
description: "Worked examples that connect playbook workflows to public repositories."
tags: [projects, code, repositories, examples]
---

# Projects and code

The playbook workflows are paired with real repositories wherever possible. These project pages do not replace the original READMEs; they explain **why the code matters**, **which files to inspect**, **what the outputs look like**, and **which playbook workflows the project supports**.

Use this section when you want to move from a general workflow to production-facing code.

## How to use a project page

1. Read the project page first, not only the GitHub README.
2. Check the **What to inspect** section before opening random files.
3. Run the smallest safe example before touching real data.
4. Read the **Limits and cautions** section before reusing data, models, crawlers, or source texts.
5. Link back to the relevant playbook workflow when writing documentation or teaching materials.

!!! warning "Code is usually safer than data"
    Public code can often be reused, adapted, and cited. Public data is different. Corpora, interview transcripts, institutional documents, cultural heritage material, PDFs, student writing, and scraped website content may carry copyright, privacy, consent, or community-access restrictions. When in doubt, publish the workflow and a small legal sample, not the full source material.

## Catalogue

<div class="grid cards" markdown>

-   **TextHarvester**  
    Harvest readable web text into corpus-ready files.  
    [:octicons-arrow-right-24: View project](text-harvester.md)

-   **Corpus Augmenter**  
    Convert and enrich TEI, VRT, and CoNLL-U corpora with CLASSLA.  
    [:octicons-arrow-right-24: View project](corpus-augmenter.md)

-   **Wikivir**  
    Build and analyse a large Slovene Wikisource corpus.  
    [:octicons-arrow-right-24: View project](wikivir.md)

-   **Šolar lexical analysis**  
    Reannotate Šolar safely and run lexical/syntactic analysis.  
    [:octicons-arrow-right-24: View project](korpus-solar-analysis.md)

-   **Pracomul-SLC Analyzer**  
    Turn dialogue-corpus exports into tidy tables and aggregate measures.  
    [:octicons-arrow-right-24: View project](pracomul.md)

-   **Medieval NER**  
    Design and evaluate NER for medieval notarial material.  
    [:octicons-arrow-right-24: View project](medieval-ner.md)

-   **Ladakh Relations**  
    Publish a static knowledge graph, map, and corpus index.  
    [:octicons-arrow-right-24: View project](ladakh-relations.md)

-   **FiFi**  
    Crawl an institutional website into documents and retrieval chunks.  
    [:octicons-arrow-right-24: View project](fifi.md)

-   **Jezikovni svetovalec**  
    Build a source-grounded language-advisor architecture.  
    [:octicons-arrow-right-24: View project](jezikovni-svetovalec.md)

-   **Vejice Word Add-in**  
    Review Slovenian comma placement inside Microsoft Word.  
    [:octicons-arrow-right-24: View project](vejice-add-in.md)

-   **createAI**  
    Analyse user/AI interview transcript sections.  
    [:octicons-arrow-right-24: View project](createai.md)

-   **Digital Linguist Kickstart**  
    Minimal starter repository for a first sanity-check script.  
    [:octicons-arrow-right-24: View project](digital-linguist-kickstart.md)

-   **Digital Linguistics Playbook**  
    The MkDocs site that hosts this reference.  
    [:octicons-arrow-right-24: View project](digital-linguistics-playbook.md)

</div>

## Reuse checklist

Before featuring or reusing a repository publicly, check:

- the README explains the purpose and the minimal command;
- dependencies are listed in `requirements.txt`, `pyproject.toml`, `package.json`, or similar;
- sample data is legal to publish;
- large/generated data is not accidentally committed;
- private credentials, tokens, PDFs, transcripts, or local paths are not exposed;
- expected outputs are named;
- failure modes are documented;
- license and citation expectations are clear.
