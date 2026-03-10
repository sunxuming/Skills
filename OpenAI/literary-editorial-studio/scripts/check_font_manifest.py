#!/usr/bin/env python3
"""Check a font plan against a small low-risk registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_registry() -> dict:
    registry_path = Path(__file__).resolve().parent.parent / "assets" / "font-registry.json"
    return json.loads(registry_path.read_text(encoding="utf-8"))


def load_manifest(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    fonts = data.get("fonts")
    if not isinstance(fonts, list):
        raise ValueError("Manifest must contain a `fonts` list.")
    return fonts


def normalize_name(name: str) -> str:
    return " ".join(name.lower().split())


def main() -> int:
    parser = argparse.ArgumentParser(description="Review a font plan.")
    parser.add_argument(
        "--manifest",
        help="Path to a JSON manifest with a top-level `fonts` list.",
    )
    parser.add_argument(
        "--font",
        action="append",
        default=[],
        help="Font name to review. Can be repeated.",
    )
    args = parser.parse_args()

    registry = load_registry()
    entries = registry["fonts"]
    index = {}
    for item in entries:
        for alias in item["aliases"]:
            index[normalize_name(alias)] = item

    requested = []
    if args.manifest:
        requested.extend(load_manifest(Path(args.manifest)))
    requested.extend({"name": font} for font in args.font)

    if not requested:
        parser.error("Provide --manifest or at least one --font.")

    unknown = 0
    for request in requested:
        name = request["name"]
        item = index.get(normalize_name(name))
        if not item:
            unknown += 1
            print(f"- {name}: manual-review-required (not in bundled registry)")
            continue
        print(f"- {name}: low-risk-example")
        print(f"  license: {item['license']}")
        print(f"  source: {item['source']}")
        print("  note: re-check current license text before commercial release or redistribution")

    return 1 if unknown else 0


if __name__ == "__main__":
    raise SystemExit(main())
