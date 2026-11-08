"""Tests for Ethno-Atlas. Standard library unittest only."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ethno_atlas import (  # noqa: E402
    REQUIRED_FIELDS,
    check_no_efficacy_claims,
    load_catalog,
    search,
    validate_catalog,
)


class TestDatasetSchema(unittest.TestCase):
    def setUp(self):
        self.entries = load_catalog()

    def test_at_least_20_entries(self):
        self.assertGreaterEqual(len(self.entries), 20)

    def test_every_entry_has_all_required_fields(self):
        for e in self.entries:
            for field in REQUIRED_FIELDS:
                self.assertIn(field, e, f"{e.get('scientific_name')}: missing {field}")
                self.assertTrue(e[field], f"{e.get('scientific_name')}: empty {field}")

    def test_validate_catalog_passes(self):
        self.assertEqual(validate_catalog(self.entries), [])

    def test_validate_detects_missing_field(self):
        bad = copy.deepcopy(self.entries)
        del bad[0]["compound_class"]
        errors = validate_catalog(bad)
        self.assertTrue(any("compound_class" in err for err in errors))

    def test_dataset_file_is_valid_json(self):
        path = Path(__file__).resolve().parents[1] / "data" / "plants.json"
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 20)


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.entries = load_catalog()

    def test_search_by_name_common(self):
        results = search(self.entries, name="turmeric")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["scientific_name"], "Curcuma longa")

    def test_search_by_name_scientific(self):
        results = search(self.entries, name="Zingiber officinale")
        self.assertEqual(len(results), 1)

    def test_search_by_region(self):
        results = search(self.entries, region="South Asia")
        names = {e["scientific_name"] for e in results}
        self.assertIn("Curcuma longa", names)
        self.assertIn("Zingiber officinale", names)
        self.assertGreaterEqual(len(results), 5)

    def test_search_by_use_keyword(self):
        results = search(self.entries, use="digestive")
        self.assertGreaterEqual(len(results), 3)
        for e in results:
            self.assertIn("digestive", e["traditional_use"].lower())

    def test_filter_by_compound_class(self):
        results = search(self.entries, compound="flavonoids")
        self.assertGreaterEqual(len(results), 3)
        for e in results:
            self.assertIn("flavonoid", e["compound_class"].lower())

    def test_combined_filters(self):
        results = search(self.entries, region="South Asia", compound="flavonoids")
        self.assertGreaterEqual(len(results), 1)

    def test_no_match_returns_empty(self):
        self.assertEqual(search(self.entries, name="nonexistentplantxyz"), [])


class TestNoEfficacyClaims(unittest.TestCase):
    def setUp(self):
        self.entries = load_catalog()

    def test_no_banned_efficacy_phrasing(self):
        self.assertEqual(check_no_efficacy_claims(self.entries), [])

    def test_checker_catches_banned_word(self):
        bad = copy.deepcopy(self.entries)
        bad[0]["traditional_use"] = "This plant cures everything."
        violations = check_no_efficacy_claims(bad)
        self.assertTrue(violations)
        self.assertEqual(violations[0][0], "Curcuma longa")


if __name__ == "__main__":
    unittest.main()
