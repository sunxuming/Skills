#!/usr/bin/env python3
"""Convert CSV/TSV red flags into a Markdown diligence report."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


COLUMNS = [
    "编号",
    "风险事实",
    "影响范围",
    "风险等级",
    "交易影响",
    "整改建议",
    "估值/担保建议",
    "是否终止",
]


def detect_delimiter(sample: str) -> str:
    return "\t" if "\t" in sample else ","


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a red-flag diligence report from CSV/TSV.")
    parser.add_argument("input", help="CSV or TSV input file.")
    parser.add_argument("output", help="Markdown output file.")
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
        handle.write("# Red Flag Report\n\n")
        handle.write("| " + " | ".join(COLUMNS) + " |\n")
        handle.write("| " + " | ".join(["---"] * len(COLUMNS)) + " |\n")
        for row in rows:
            values = [row.get(column, "").strip() for column in COLUMNS]
            handle.write("| " + " | ".join(values) + " |\n")

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
