# Damjan Popič — osebna spletna stran / personal website

**Live:** https://damjan-popic.github.io/digital-linguistics-playbook/damjan/

Self-contained Slovenian/English website. It shares the existing Playbook's hosting,
not its navigation or visual design. No existing Playbook page is replaced.

## Najhitrejše urejanje / the quickest way to edit

1. On any published page, click **Uredi to stran / Edit this page** near the bottom.
2. Sign into GitHub as the repository owner. Edit the text in the Markdown file.
3. Click **Commit changes** and commit to `main` (or merge your proposed change).
4. The existing **Publish MkDocs site** workflow rebuilds both sites and publishes them.
   A failed check stops publication; the last successful site remains live.

No local installation is needed for everyday editing. The public Edit link does
not give visitors write access: GitHub still enforces repository permissions.

## Kje je kaj / content map

| Page | Slovenian source | English source |
| --- | --- | --- |
| Home | `content/sl/index.md` | `content/en/index.md` |
| Bio | `content/sl/o-meni.md` | `content/en/about.md` |
| Research | `content/sl/raziskovanje.md` | `content/en/research.md` |
| Projects | `content/sl/projekti.md` | `content/en/projects.md` |
| Teaching | `content/sl/poucevanje/index.md` | `content/en/teaching/index.md` |
| AGRFT | `content/sl/poucevanje/agrft.md` | `content/en/teaching/agrft.md` |
| Digital Linguistics | `content/sl/poucevanje/digitalno-jezikoslovje.md` | `content/en/teaching/digital-linguistics.md` |
| Students | `content/sl/za-studente.md` | `content/en/students.md` |
| Contact | `content/sl/kontakt.md` | `content/en/contact.md` |

The small block between the first two `---` lines sets the page title,
description and section. Keep `key` unchanged: it pairs the translations.
Write normal text below the second `---` line. Use `##` for headings, because
`title` already supplies the page's main heading. Slovenian and English are
edited separately; nothing is silently machine-translated.

Example content:

```markdown
## 1. srečanje — Uvod

Kratek opis srečanja in navodila.

[Predstavitev](/assets/files/agrft-uvod.pdf)
```

## Dodajanje gradiv / adding materials

In GitHub, use **Add file → Upload files** in `personal-site/assets/files/`.
Create that folder on the first upload. Link to a file as shown above; the builder
adjusts `/assets/` links for the site's actual location. Filenames without spaces
are easiest. Only upload material that may be shared publicly. Upload the file
before adding its link, or commit both changes together: missing files fail validation.

Never upload grades, student lists, submitted assignments, passwords, access keys,
private correspondence or readings you are not permitted to distribute.

## Dodajanje strani / adding a page

Copy a nearby Markdown file in each language. Give both copies the same new
`key`, but their own translated title and text. Link to them from the relevant
teaching or project page using ordinary relative Markdown links, such as
`[New course](new-course.md)`. Both language versions are required. The language
switcher then finds the matching page automatically. To add a top-level menu
item, also add its key and translated label in both language sections of `site.yml`.

## Local preview

Python 3.10 or newer:

```bash
python -m venv .venv
# Linux/macOS/WSL:
source .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1
python -m pip install -r personal-site/requirements.txt
python personal-site/build.py
python -m http.server 8000 --directory personal-site/_site
```

Open http://localhost:8000/ . After editing, run the build command again and
refresh the browser. The default `_site` output is ignored by Git.

Tests:

```bash
python -m unittest discover -s personal-site -p 'test_*.py'
```

The builder checks paired translations, headings, internal links, downloadable
files and anchor targets before replacing its own generated output. It refuses
to overwrite a non-generated directory and never clears the parent Playbook site.

## Hosting and moving later

The initial deployment is an isolated `/damjan/` directory of the existing
`digital-linguistics-playbook` Pages site. A root-level account site would require
a separate `damjan-popic.github.io` repository and Pages setup. Those administration
actions were not available through the connection used to create this version.

This folder is portable: the content and templates have no dependency on the
Playbook. A new repository can run `pip install -r personal-site/requirements.txt`
and `python personal-site/build.py --output site --site-url https://damjan-popic.github.io/`,
then publish `site/` through GitHub Pages. Update `url`, `repository`, `branch` and
`source_path` in `site.yml` to keep canonical URLs and editing links correct.
Do not change the shared Playbook's domain merely to move this personal site.

## Technical notes

Ordinary Markdown + one Python builder + a shared Jinja template and CSS.
The existing host already uses Python; this keeps the initial site lighter than
adding a second document-publishing toolchain. There is no CMS, database,
JavaScript dependency, analytics, external font request or login requirement for readers.
Light/dark appearance follows the reader's device. Public content is rendered as
static HTML with paired language links, canonical URLs and its own sitemap.

Institutional references are listed in `SOURCES.md`. Course details not confirmed
for publication were deliberately left out. Check and polish both languages before
using these draft descriptions as formal course regulations or a definitive CV.
