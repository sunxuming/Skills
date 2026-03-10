#!/usr/bin/env python3
"""Scan extracted long-text materials for hidden risk markers."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = {
    "霸王条款/单方优势": [r"单方有权", r"最终解释权", r"甲方有权单方"],
    "对赌/估值调整": [r"对赌", r"估值调整", r"补偿义务", r"回购义务"],
    "监管红线": [r"不得", r"禁止", r"行政处罚", r"整改", r"合规要求"],
    "退出/终止风险": [r"单方解除", r"自动终止", r"终止条件", r"提前到期"],
    "赔偿与责任上限": [r"责任上限", r"赔偿上限", r"不承担责任", r"免责"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan extracted dossier text for risk markers.")
    parser.add_argument("path", help="Path to a .txt or .md file.")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8", errors="ignore")
    hits = 0
    for label, patterns in PATTERNS.items():
        matches = []
        for pattern in patterns:
            for match in re.finditer(pattern, text):
                snippet = text[max(0, match.start() - 30):match.end() + 30]
                matches.append(re.sub(r"\s+", " ", snippet))
        if matches:
            hits += 1
            print(f"[{label}]")
            for snippet in matches[:5]:
                print(f"- {snippet}")
    if hits == 0:
        print("No configured risk markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
