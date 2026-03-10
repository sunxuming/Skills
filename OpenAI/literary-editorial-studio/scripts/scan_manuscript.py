#!/usr/bin/env python3
"""Scan Markdown or plain-text manuscripts for structural issues."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".markdown", ".txt"}
CHAPTER_PATTERN = re.compile(
    r"^(?:#+\s+)?(?:(?:chapter|part|volume)\s+(\d+)|\u7b2c([0-9\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u3007\u96f6]+)[\u7ae0\u8282\u5377\u56de])",
    re.IGNORECASE,
)


def iter_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def extract_heading_issues(text: str) -> list[str]:
    issues: list[str] = []
    previous_level = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("#"):
            continue
        level = len(line) - len(line.lstrip("#"))
        if previous_level and level > previous_level + 1:
            issues.append(f"line {lineno}: heading jumps from H{previous_level} to H{level}")
        previous_level = level
    return issues


def extract_chapter_markers(text: str) -> list[str]:
    markers: list[str] = []
    for line in text.splitlines():
        match = CHAPTER_PATTERN.match(line.strip())
        if match:
            markers.append(line.strip())
    return markers


def scan_path(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    issues = [f"{path}: {issue}" for issue in extract_heading_issues(text)]

    markers = extract_chapter_markers(text)
    counts = Counter(markers)
    for marker, count in counts.items():
        if count > 1:
            issues.append(f"{path}: duplicate chapter marker `{marker}` appears {count} times")

    if not markers:
        issues.append(f"{path}: no chapter or part markers found")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan manuscript structure.")
    parser.add_argument("path", help="File or directory to scan.")
    args = parser.parse_args()

    root = Path(args.path)
    files = iter_files(root)
    if not files:
        print("No .md or .txt files found.")
        return 1

    all_issues: list[str] = []
    for path in files:
        all_issues.extend(scan_path(path))

    if all_issues:
        print("Structural review:")
        for issue in all_issues:
            print(f"- {issue}")
    else:
        print("No structural issues detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
