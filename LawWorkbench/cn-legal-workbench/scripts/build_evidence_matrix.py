#!/usr/bin/env python3
"""Convert CSV or TSV rows into a Markdown evidence matrix."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


EXPECTED_COLUMNS = [
    "序号",
    "证据名称",
    "形成时间",
    "证明目的",
    "证明对象",
    "来源",
    "备注",
]


def detect_delimiter(sample: str) -> str:
    if "\t" in sample:
        return "\t"
    return ","


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Markdown evidence matrix from CSV/TSV.")
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
        handle.write("| " + " | ".join(EXPECTED_COLUMNS) + " |\n")
        handle.write("| " + " | ".join(["---"] * len(EXPECTED_COLUMNS)) + " |\n")
        for row in rows:
            values = [row.get(column, "").strip() for column in EXPECTED_COLUMNS]
            handle.write("| " + " | ".join(values) + " |\n")

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
