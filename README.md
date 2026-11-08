# Ethno-Atlas

A searchable, sourced catalogue of plants with documented traditional uses, designed for researchers.

## Disclaimer — research / educational use only. Not medical advice.

Entries describe traditional and documented uses as recorded in ethnobotanical literature and traditional knowledge. They are **not proven efficacy claims, not treatment recommendations, and not a substitute for qualified professional advice**. Consult qualified professionals for health decisions. No dosages for treatment are given, and no clinical trial results are claimed.

## Problem

Traditional plant knowledge is scattered across herbals, ethnobotanical papers, and folk traditions, and is often retold online without sources or with inflated health claims. Researchers need a small, honest starting catalogue: what plant, where it is traditionally documented, what part was used, how it was traditionally prepared, what compound class is widely documented for it, and what kind of source the note comes from — with traditional-use wording kept distinct from proven efficacy.

## What it does

- A curated dataset of 24 plants in `data/plants.json`.
- Search and filter by plant name (scientific or common), region, traditional-use keyword, and compound class.
- JSON output for research reuse.
- Validation: every entry must have all required fields, and a banned-phrasing check rejects efficacy wording presented as fact.
- A dependency-free static web UI (`web/index.html`) that loads the JSON dataset and lets a user search, filter, and view an entry in detail.

## How to run it

Requirements: Python 3 only (standard library). No third-party packages.

```bash
# From this project folder:
python3 cli.py validate
python3 cli.py list
python3 cli.py search --name turmeric
python3 cli.py search --region "South Asia"
python3 cli.py search --use digestive
python3 cli.py search --compound flavonoids
python3 cli.py search --region "South Asia" --json
python3 cli.py show "Curcuma longa"
```

Run the tests:

```bash
python3 -m unittest discover -s tests -v
```

Web UI: `fetch()` cannot reliably load a JSON file over `file://` in most browsers, so serve the project folder over HTTP:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/web/index.html
```

The UI reads `../data/plants.json`, so keep the `web/` and `data/` folders in their relative positions.

## Tech stack

- Python 3 standard library only for the data, library (`ethno_atlas.py`), CLI (`cli.py`), and tests (`tests/`, stdlib `unittest`).
- Dependency-free static web UI: one HTML page plus vanilla JavaScript reading a JSON dataset. No build step, no framework.
- Dataset: plain JSON, so it can be reused without this code.

## Dataset provenance note

This is a curated traditional-use catalogue, not a clinical database. Entries summarise widely documented traditional uses and compound classes at catalogue level (for example, curcuminoids for turmeric, gingerols for ginger, quinoline alkaloids for cinchona bark) with source-type notes such as "ethnobotanical literature" or "traditional knowledge" and the tradition where applicable. It does not reproduce clinical trial data, does not assign dosages for treatment, and does not present traditional use as proven efficacy. Corrections and source-level citations are welcome as contributions.

## Limitations

- 24 entries only — a starting catalogue, not a survey of world ethnobotany.
- Compound class is given at class level only, not as a measured composition.
- Traditional-use notes are summaries, not quotations from primary sources; researchers should follow the source-type notes to primary literature before citing any entry.
- Regional labels are broad and traditional, not botanical distribution maps.

## Build Disclosure: AI-built. This project was built by AI agents (Tree / Muse fleet) directed by Rene Turcios (CloudCorpRecords). Rene set the problem and acceptance review; agents designed, coded, tested, and documented the project. It was originally built during the EthnoHack event window in November 2026 and is published here as a standalone open-source project. AI tools used are credited in the Built With list. Open source under MIT.

## Built With

- Python 3 (standard library)
- HTML / JavaScript (no dependencies)
- AI tools: Tree / Muse fleet (see Build Disclosure above)

## License

MIT — see `LICENSE`.
