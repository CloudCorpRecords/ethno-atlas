# Ethno-Atlas — Pitch Deck (10 slides)

Slide count: 10

## Slide 1 — Title

Ethno-Atlas: a research catalogue for ethnopharmacology and health.
A searchable, sourced catalogue of plants with documented traditional uses — for researchers, not a medical advice tool.
Built Nov 2, 2026, inside EthnoHack's Nov 2–8 window.

## Slide 2 — Problem

Traditional plant knowledge is scattered across herbals, papers, and folk traditions, and is often retold online without sources or with inflated health claims. Researchers need a small, honest starting point with sources attached.

## Slide 3 — Approach

Build a catalogue, not a clinic: one JSON dataset, a standard-library Python search library and CLI, and a dependency-free static web UI. Every entry carries scientific name, common names, regions, traditional use, plant part, preparation as traditionally documented, compound class, and source-type notes.

## Slide 4 — Dataset

24 entries, 13 region labels, 16 compound classes. Examples: Curcuma longa (turmeric, curcuminoids, South Asia), Zingiber officinale (ginger, gingerols), Cinchona officinalis (quinoline alkaloids, South America), Artemisia annua (sesquiterpene lactones, East Asia). Validation enforces all fields and rejects banned efficacy phrasing.

## Slide 5 — Demo

CLI: `python3 cli.py validate` → "OK: 24 entries valid, no banned efficacy phrasing found". `search --name turmeric` → 1 result. `search --use digestive` → 8 results. `search --compound flavonoids` → 4 results. `search --region "South Asia"` → 8 results. Web UI filters the same dataset and shows entry detail on click. Tests: 14 passed.

## Slide 6 — Research value

Reusable JSON for researchers; combined filters (region + compound class, name + use keyword) for quick hypothesis scouting; source-type notes that point back to ethnobotanical literature and traditional knowledge instead of presenting folklore as fact.

## Slide 7 — Limitations / Disclaimer

Research / educational use only. Not medical advice. Traditional use is not proven efficacy. No dosages for treatment, no clinical trial results claimed. 24 entries is a starting catalogue, not a world survey; compound classes are class-level, not measured composition; regional labels are broad and traditional.

## Slide 8 — AI disclosure

Build Disclosure: AI-built. This project was built by AI agents (Tree / Muse fleet) directed by Rene Turcios (CloudCorpRecords). Rene set the problem and acceptance review; agents designed, coded, tested, and documented the project. It was originally built during the EthnoHack event window in November 2026 and is published as a standalone open-source project. AI tools used are credited in the Built With list. Open source under MIT.

## Slide 9 — Next steps

Add source-level citations per entry, grow the catalogue with contributor review, add export formats for researchers, and publish the repo and demo for community correction — keeping the no-efficacy-claims check on every contribution.

## Slide 10 — Thank you

Thank you. Ethno-Atlas: documented traditional uses, sourced and searchable, with the claims kept honest. Questions welcome — research use only, not medical advice.
