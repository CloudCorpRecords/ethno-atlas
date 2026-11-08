"""Command-line interface for Ethno-Atlas.

Examples:
  python3 cli.py list
  python3 cli.py search --name turmeric
  python3 cli.py search --region "South Asia"
  python3 cli.py search --use digestive
  python3 cli.py search --compound flavonoids
  python3 cli.py search --name ginger --json
  python3 cli.py validate
  python3 cli.py show "Curcuma longa"
"""
import argparse
import json
import sys

from ethno_atlas import (
    check_no_efficacy_claims,
    load_catalog,
    search,
    validate_catalog,
)


def _print_entry(e):
    print(f"{e['scientific_name']} ({', '.join(e['common_names'])})")
    print(f"  Regions: {', '.join(e['regions'])}")
    print(f"  Traditional use: {e['traditional_use']}")
    print(f"  Plant part: {e['plant_part']}")
    print(f"  Preparation (as traditionally documented): {e['preparation']}")
    print(f"  Compound class: {e['compound_class']}")
    print(f"  Sources: {e['source_notes']}")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ethno-atlas")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list all entries")
    sp = sub.add_parser("search", help="search / filter entries")
    sp.add_argument("--name")
    sp.add_argument("--region")
    sp.add_argument("--use")
    sp.add_argument("--compound")
    sp.add_argument("--json", action="store_true")
    sub.add_parser("validate", help="validate dataset schema and claims check")
    show = sub.add_parser("show", help="show one entry by scientific name")
    show.add_argument("name")

    args = parser.parse_args(argv)
    entries = load_catalog()

    if args.command == "list":
        for e in entries:
            _print_entry(e)
            print()
        print(f"{len(entries)} entries")
        return 0

    if args.command == "search":
        results = search(entries, name=args.name, region=args.region,
                         use=args.use, compound=args.compound)
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            for e in results:
                _print_entry(e)
                print()
            print(f"{len(results)} result(s)")
        return 0

    if args.command == "validate":
        errors = validate_catalog(entries)
        violations = check_no_efficacy_claims(entries)
        if errors:
            print("Validation errors:")
            for err in errors:
                print(f"  - {err}")
        if violations:
            print("Efficacy-claim violations:")
            for name, field, pat in violations:
                print(f"  - {name} [{field}] matched {pat}")
        if not errors and not violations:
            print(f"OK: {len(entries)} entries valid, no banned efficacy phrasing found")
            return 0
        return 1

    if args.command == "show":
        results = search(entries, name=args.name)
        exact = [e for e in results if e["scientific_name"].lower() == args.name.lower()]
        chosen = exact or results
        if not chosen:
            print(f"No entry found for: {args.name}", file=sys.stderr)
            return 1
        _print_entry(chosen[0])
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
