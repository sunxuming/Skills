#!/usr/bin/env python3
"""Screen text files for obvious publication-risk categories."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


TEXT_EXTENSIONS = {".md", ".markdown", ".txt", ".docx"}
PATTERNS = {
    "minor-sexual-content": [
        re.compile(r"(未成年|儿童|小学生|中学生|少女|男童).{0,20}(性|色情|性交|性行为|猥亵)", re.IGNORECASE),
    ],
    "sexual-coercion-or-abuse": [
        re.compile(r"(强奸|迷奸|下药|性侵|猥亵|胁迫发生关系)", re.IGNORECASE),
    ],
    "hate-or-dehumanization": [
        re.compile(r"(种族清洗|灭绝.*民族|劣等民族|仇恨.*群体|清除.*群体)", re.IGNORECASE),
    ],
    "violent-or-illicit-instructions": [
        re.compile(r"(制毒|制爆|炸药配方|枪支改造|投毒|伪造公章|骗贷|盗刷|社工库)", re.IGNORECASE),
    ],
    "self-harm-encouragement": [
        re.compile(r"(去自杀|教你自残|鼓励自杀|一起自杀)", re.IGNORECASE),
    ],
    "extremist-praise": [
        re.compile(r"(加入极端组织|宣扬恐怖主义|赞美恐袭|效忠恐怖组织)", re.IGNORECASE),
    ],
}


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        with archive.open("word/document.xml") as handle:
            data = handle.read().decode("utf-8", errors="ignore")
    return re.sub(r"<[^>]+>", " ", data)


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return extract_docx_text(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def iter_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Screen text for obvious compliance risks.")
    parser.add_argument("path", help="File or directory to scan.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 2 if any category is flagged.",
    )
    args = parser.parse_args()

    root = Path(args.path)
    files = iter_files(root)
    if not files:
        print("No supported files found.")
        return 1

    flagged = []
    for path in files:
        text = read_text(path)
        for category, patterns in PATTERNS.items():
            matches = []
            for pattern in patterns:
                for match in pattern.finditer(text):
                    snippet = text[max(0, match.start() - 24): match.end() + 24]
                    snippet = re.sub(r"\s+", " ", snippet)
                    matches.append(snippet[:160])
            if matches:
                flagged.append((path, category, matches[:3]))

    if not flagged:
        print("No obvious risk categories detected.")
        return 0

    print("Compliance review required:")
    for path, category, snippets in flagged:
        print(f"- {path} [{category}]")
        for snippet in snippets:
            print(f"  snippet: {snippet}")
    return 2 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
