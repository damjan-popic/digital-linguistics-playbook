---
title: "Ladakh Relations"
description: "A static-site and local-pipeline repository for graphs, maps, corpus indexing, and relation discovery."
tags: [projects, knowledge-graph, map, cultural-heritage, static-site]
---

# Ladakh Relations

<div class="answer-meta" markdown>
<span>knowledge graph</span>
<span>map</span>
<span>static publishing</span>
</div>

## What this project does

Ladakh Relations is a static-site and local-pipeline repository for an interactive research graph. It supports graph nodes and edges, a map view, geocoding review, a corpus index, cleaning and annotation workflows, candidate relation discovery, and GitHub Pages deployment without a backend.

[:octicons-mark-github-16: Open the repository](https://github.com/damjan-popic/ladakh-relations)

## Use this when

- you want a production-facing example of a static DH interface;
- you need to connect people, places, documents, meetings, and relation candidates;
- you want to teach graph data alongside maps and source text;
- you want a no-backend publication model for a cultural-heritage project.

## What to inspect in the code

- `schema/` — data model and structural expectations.
- `data/` — generated graph and map data.
- `corpus/` — normalized source/transcription index.
- `scripts/` — cleaning, indexing, candidate-link, and review workflows.
- `index.html`, `app.js`, `style.css` — static front-end.
- `.github/workflows/` — deployment workflow.

## Minimal run path

```bash
python scripts/serve_local.py
```

Then open the local site shown by the script, usually `http://localhost:8000`.

## Relevant playbook workflows

- [How do I build a simple cultural heritage map?](../scenarios/mapping/build-a-simple-cultural-heritage-map.md)
- [How do I map places mentioned in a text?](../scenarios/mapping/map-places-mentioned-in-a-text.md)
- [How do I turn messy humanities notes into a reusable dataset?](../scenarios/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md)
- [How do I decide whether a digitised source should be public?](../scenarios/ethics/decide-whether-a-digitised-source-should-be-public.md)

## Practice use

Ask users to add three candidate entities and two relations to a tiny graph file. They should then decide which relations are confirmed, inferred, uncertain, or rejected, and document why.

## Limits and cautions

- Relation candidates are not confirmed evidence.
- Cultural heritage data may require access controls, community review, or contextual framing.
- Geocoding should be reviewed manually.
- Static-site publication is convenient, but public visibility is a rights and ethics decision.
