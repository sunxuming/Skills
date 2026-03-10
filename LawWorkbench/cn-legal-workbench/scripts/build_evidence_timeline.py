#!/usr/bin/env python3
"""Build a chronology and catalog from OCR-extracted evidence rows."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED = [
    "时间",
    "来源",
    "主体",
    "关键内容",
    "证明目的",
    "备注",
]


def detect_delimiter(sample: str) -> str:
    return "\t" if "\t" in sample else ","


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an evidence timeline from CSV/TSV.")
    parser.add_argument("input", help="CSV or TSV input.")
    parser.add_argument("output", help="Markdown output.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    sample = input_path.read_text(encoding="utf-8", errors="ignore")
    delimiter = detect_delimiter(sample)

    with input_path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = list(reader)

    rows.sort(key=lambda row: row.get("时间", ""))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("# 证据时间轴\n\n")
        for row in rows:
            handle.write(f"- {row.get('时间', '').strip()} | {row.get('主体', '').strip()} | {row.get('关键内容', '').strip()}\n")
        handle.write("\n# 证据目录\n\n")
        handle.write("| " + " | ".join(REQUIRED) + " |\n")
        handle.write("| " + " | ".join(["---"] * len(REQUIRED)) + " |\n")
        for row in rows:
            values = [row.get(column, "").strip() for column in REQUIRED]
            handle.write("| " + " | ".join(values) + " |\n")

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
