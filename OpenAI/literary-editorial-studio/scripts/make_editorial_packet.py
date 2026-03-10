#!/usr/bin/env python3
"""Scaffold reusable editorial packet files."""

from __future__ import annotations

import argparse
from pathlib import Path


PRESETS = {
    "project-frame": """# Project Frame
- Working title: {title}
- Project type:
- Intended readership:
- Scope:
- Current stage:
- Core promise:
- Non-negotiable constraints:
""",
    "story-bible": """# Story Bible
- Working title: {title}
- Premise:
- Point of view plan:
- World or setting rules:
- Core cast:
- Major conflicts:
- Continuity anchors:
- Terminology to preserve:
- Long-range payoff seeds:
""",
    "continuation-brief": """# Continuation Brief
- Working title: {title}
- Current manuscript boundary:
- Last confirmed chapter or section:
- Active conflicts:
- Current timeline:
- Current location:
- Current knowledge state:
- Required callbacks:
- Immediate next-step target:
""",
    "developmental-memo": """# Developmental Edit Memo
- Working title: {title}
- Scope:
- Main problem:
- Secondary problem:
- Structural risk:
- Continuity-sensitive areas:

## Recommended actions
- Action 1:
- Action 2:
- Action 3:

## What to preserve
- Voice:
- Canon:
- Intended reader effect:
""",
    "review-packet": """# Review Packet
- Working title: {title}
- Purpose:
- Scope:
- Canon cutoff:
- Included chapters or sections:
- Open questions:
- Required decisions:
""",
    "docx-handoff": """# DOCX Handoff Plan
- Working title: {title}
- Deliverable type:
- Heading hierarchy:
- Page numbering logic:
- Header/footer logic:
- Typography plan:
- Comments or tracked changes to preserve:
- Export target:
""",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a starter editorial packet.")
    parser.add_argument("preset", choices=sorted(PRESETS.keys()))
    parser.add_argument("output", help="Target file path to create.")
    parser.add_argument("--title", default="Untitled Project", help="Working title.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    output_path = Path(args.output)
    if output_path.exists() and not args.force:
        parser.error(f"{output_path} already exists. Use --force to overwrite.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    body = PRESETS[args.preset].format(title=args.title.strip() or "Untitled Project")
    output_path.write_text(body, encoding="utf-8")
    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
