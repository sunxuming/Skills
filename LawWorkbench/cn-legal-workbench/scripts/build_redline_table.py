#!/usr/bin/env python3
"""Build a Markdown contract comparison table from CSV/TSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


COLUMNS = [
    "条款位置",
    "原文要点",
    "修改后要点",
    "修改类型",
    "修改理由",
    "风险防控价值",
]


def detect_delimiter(sample: str) -> str:
    return "\t" if "\t" in sample else ","


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a redline explanation table from CSV/TSV.")
    parser.add_argument("input", help="CSV or TSV source file.")
    parser.add_argument("output", help="Target Markdown file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    sample = input_path.read_text(encoding="utf-8", errors="ignore")
    delimiter = detect_delimiter(sample)

    with input_path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = list(reader)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("| " + " | ".join(COLUMNS) + " |\n")
        handle.write("| " + " | ".join(["---"] * len(COLUMNS)) + " |\n")
        for row in rows:
            values = [row.get(column, "").strip() for column in COLUMNS]
            handle.write("| " + " | ".join(values) + " |\n")

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
