#!/usr/bin/env python3
"""Allocate inflows across waterfall priorities from CSV/TSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


COLUMNS = ["顺位", "项目", "应付金额"]


def detect_delimiter(sample: str) -> str:
    return "\t" if "\t" in sample else ","


def to_float(value: str) -> float:
    return float((value or "0").strip() or "0")


def main() -> int:
    parser = argparse.ArgumentParser(description="Allocate cashflow by waterfall priority.")
    parser.add_argument("input", help="CSV or TSV input file.")
    parser.add_argument("output", help="Markdown output file.")
    parser.add_argument("--inflow", type=float, required=True, help="Total cash inflow to allocate.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    sample = input_path.read_text(encoding="utf-8", errors="ignore")
    delimiter = detect_delimiter(sample)

    with input_path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        rows = list(reader)

    rows.sort(key=lambda row: int((row.get("顺位", "0") or "0").strip() or "0"))
    remaining = args.inflow

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("# Cash Flow Waterfall 分配表\n\n")
        handle.write(f"- 可分配现金流: {args.inflow:.2f}\n\n")
        handle.write("| 顺位 | 项目 | 应付金额 | 实付金额 | 缺口 |\n")
        handle.write("| --- | --- | --- | --- | --- |\n")
        for row in rows:
            due = to_float(row.get("应付金额", ""))
            paid = min(remaining, due)
            gap = due - paid
            remaining -= paid
            handle.write(
                f"| {row.get('顺位', '').strip()} | {row.get('项目', '').strip()} | {due:.2f} | {paid:.2f} | {gap:.2f} |\n"
            )
        handle.write(f"\n- 分配后剩余现金流: {remaining:.2f}\n")

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
