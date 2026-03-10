#!/usr/bin/env python3
"""Build a cap-table dilution report from CSV/TSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


COLUMNS = ["股东", "当前股数", "新增股数"]


def detect_delimiter(sample: str) -> str:
    return "\t" if "\t" in sample else ","


def to_float(value: str) -> float:
    return float((value or "0").strip() or "0")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a cap-table dilution report from CSV/TSV.")
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

    total_before = sum(to_float(row.get("当前股数", "")) for row in rows)
    total_new = sum(to_float(row.get("新增股数", "")) for row in rows)
    total_after = total_before + total_new

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("# 股权稀释测算表\n\n")
        handle.write(f"- 投前总股数: {total_before:.2f}\n")
        handle.write(f"- 新增股数: {total_new:.2f}\n")
        handle.write(f"- 投后总股数: {total_after:.2f}\n\n")
        handle.write("| 股东 | 当前股数 | 新增股数 | 投前持股比例 | 投后持股比例 |\n")
        handle.write("| --- | --- | --- | --- | --- |\n")
        for row in rows:
            current = to_float(row.get("当前股数", ""))
            issued = to_float(row.get("新增股数", ""))
            before_pct = current / total_before if total_before else 0
            after_pct = (current + issued) / total_after if total_after else 0
            handle.write(
                f"| {row.get('股东', '').strip()} | {current:.2f} | {issued:.2f} | {before_pct:.4%} | {after_pct:.4%} |\n"
            )

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
