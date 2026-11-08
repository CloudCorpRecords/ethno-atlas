# Ethno-Atlas — Demo (real CLI output, Nov 2, 2026)

Disclaimer: research / educational use only. Not medical advice. Outputs below are verbatim from the commands shown, run in this project folder.

## 1. Validate

Command: `python3 cli.py validate`

```
OK: 24 entries valid, no banned efficacy phrasing found
```

## 2. Search by name

Command: `python3 cli.py search --name turmeric`

```
Curcuma longa (Turmeric)
  Regions: South Asia, Southeast Asia
  Traditional use: Documented in ethnobotanical literature as traditionally used in culinary practice and folk practice associated with digestive comfort and joint comfort in traditional systems.
  Plant part: Rhizome
  Preparation (as traditionally documented): Rhizome dried and ground into powder for culinary use, as traditionally documented.
  Compound class: Curcuminoids
  Sources: Ethnobotanical literature; traditional knowledge (Ayurvedic tradition)

1 result(s)
```

## 3. Filter by region

Command: `python3 cli.py search --region "South Asia"` — 8 results: Curcuma longa, Zingiber officinale, Camellia sinensis, Ocimum tenuiflorum, Withania somnifera, Centella asiatica, Piper nigrum, Cinnamomum verum.

## 4. Search by traditional-use keyword

Command: `python3 cli.py search --use digestive` — 8 result(s):

- Curcuma longa, Zingiber officinale, Camellia sinensis, Matricaria chamomilla, Mentha piperita, Glycyrrhiza glabra, Piper nigrum, Cinnamomum verum

## 5. Filter by compound class

Command: `python3 cli.py search --compound flavonoids` — 4 result(s):

- Matricaria chamomilla, Ocimum tenuiflorum, Theobroma cacao, Sambucus nigra

## 6. Tests

Command: `python3 -m unittest discover -s tests -v`

```
Ran 14 tests in 0.024s

OK
```

## 7. Web UI

Serve with `python3 -m http.server 8000` and open `http://localhost:8000/web/index.html`. The page loads `data/plants.json`, offers name / region / compound-class / use-keyword filters, and shows an entry detail panel on click. (No screenshot or video is claimed here; see the project report for the video status.)
