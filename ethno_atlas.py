"""Ethno-Atlas: a searchable, sourced catalogue of plants with documented
traditional uses, for researchers. Research/educational use only.
Not medical advice.

Standard library only.
"""
import json
import re
from pathlib import Path

REQUIRED_FIELDS = [
    "scientific_name",
    "common_names",
    "regions",
    "traditional_use",
    "plant_part",
    "preparation",
    "compound_class",
    "source_notes",
]

# Banned efficacy phrasing: words that would present a traditional use as a
# proven fact. Traditional-use wording is checked separately by validation.
BANNED_PATTERNS = [
    r"\bcures\b",
    r"\bcure\b",
    r"\btreats\b",
    r"\bproven to\b",
    r"\bclinically proven\b",
    r"\bguaranteed to\b",
    r"\bheals\b",
]

DEFAULT_DATA = Path(__file__).resolve().parent / "data" / "plants.json"


def load_catalog(path=None):
    path = Path(path) if path else DEFAULT_DATA
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("dataset must be a JSON list of entries")
    return data


def _contains(text):
    return text.lower() if isinstance(text, str) else ""


def validate_catalog(entries):
    """Return a list of error strings; empty list means valid."""
    errors = []
    seen = set()
    for i, e in enumerate(entries):
        label = e.get("scientific_name", f"entry {i}") if isinstance(e, dict) else f"entry {i}"
        if not isinstance(e, dict):
            errors.append(f"entry {i}: not an object")
            continue
        for field in REQUIRED_FIELDS:
            if field not in e or e[field] in (None, "", [], {}):
                errors.append(f"{label}: missing or empty field '{field}'")
        if e.get("scientific_name") in seen:
            errors.append(f"{label}: duplicate scientific_name")
        seen.add(e.get("scientific_name"))
        if not isinstance(e.get("common_names"), list) or not e.get("common_names"):
            errors.append(f"{label}: common_names must be a non-empty list")
        if not isinstance(e.get("regions"), list) or not e.get("regions"):
            errors.append(f"{label}: regions must be a non-empty list")
        # No dosage numbers for treatment: reject dosage-like patterns in
        # preparation/traditional_use (e.g. "take 500 mg daily").
        for field in ("preparation", "traditional_use"):
            text = e.get(field, "")
            if re.search(r"\b\d+\s*(mg|g|ml|grams?|milligrams?)\b.*\b(daily|per day|three times)", text, re.I):
                errors.append(f"{label}: {field} looks like a dosage instruction")
    return errors


def check_no_efficacy_claims(entries):
    """Return a list of (scientific_name, field, matched_pattern) violations."""
    violations = []
    fields = ["traditional_use", "preparation", "source_notes"]
    for e in entries:
        for field in fields:
            text = _contains(e.get(field, ""))
            for pat in BANNED_PATTERNS:
                if re.search(pat, text):
                    violations.append((e.get("scientific_name"), field, pat))
    return violations


def search(entries, name=None, region=None, use=None, compound=None):
    results = entries
    if name:
        q = name.lower()
        results = [e for e in results
                   if q in e["scientific_name"].lower()
                   or any(q in c.lower() for c in e["common_names"])]
    if region:
        q = region.lower()
        results = [e for e in results
                   if any(q in r.lower() for r in e["regions"])]
    if use:
        q = use.lower()
        results = [e for e in results if q in e["traditional_use"].lower()]
    if compound:
        q = compound.lower()
        results = [e for e in results if q in e["compound_class"].lower()]
    return results
