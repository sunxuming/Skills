# Literary Editorial Studio

One Codex skill for long-form writing, editorial revision, manuscript formatting, Word-ready delivery planning, and release-safety screening.

This repository is meant for lawful editorial work on original or authorized text. It is intentionally packaged as a single public skill so users do not need to chain multiple adjacent skills for normal fiction or literary editing workflows.

## What it is

`literary-editorial-studio` is a self-contained skill for:

- project framing and continuity control
- developmental editing
- line editing and prose cleanup
- manuscript normalization
- review packet and release bundle assembly
- Word-ready delivery planning
- publication-safety screening
- low-risk font-plan review

## What it is not

This repository does not provide:

- illegal-content generation workflows
- exploitative, hateful, extremist, fraudulent, or violent wrongdoing assistance
- sexual content involving minors
- coercive sexual abuse content
- living-author imitation workflows
- copyrighted sample chapters or text corpora
- third-party font binaries
- legal guarantees or compliance guarantees

## Why this repository exists

Many writing workflows sit in the gap between planning, revision, formatting, and release. This skill keeps those neighboring steps inside one operational surface:

- one entry point
- one set of templates
- one set of local helper scripts
- one place to document safety and licensing boundaries

## Repository structure

```text
.
|-- literary-editorial-studio/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   |-- references/
|   |-- scripts/
|   `-- assets/
|-- LICENSE
|-- README.md
`-- SECURITY.md
```

## Included helper scripts

- `make_editorial_packet.py`
  Creates starter files for project frames, review packets, continuation briefs, and `.docx` handoff notes.
- `scan_manuscript.py`
  Scans Markdown or plain-text manuscripts for basic heading and chapter-marker issues.
- `check_text_compliance.py`
  Screens `.md`, `.txt`, and `.docx` files for obvious publication-risk categories that require manual review.
- `check_font_manifest.py`
  Reviews a font manifest against the bundled low-risk example registry.

## Quick start

### 1. Install the skill

Copy the `literary-editorial-studio` folder into your Codex skills directory:

- Windows: `%USERPROFILE%\\.codex\\skills\\`
- macOS/Linux: `~/.codex/skills/`

Then restart Codex.

### 2. Use it in Codex

Example prompts:

- `Use $literary-editorial-studio to clean up this manuscript, build a review packet, and prepare a Word handoff plan.`
- `Use $literary-editorial-studio to review this novel chapter for continuity, line editing, and release-risk issues.`
- `Use $literary-editorial-studio to create a project frame, continuation brief, and formatting plan for this long-form draft.`

### 3. Run local helper scripts

Examples:

```bash
python literary-editorial-studio/scripts/make_editorial_packet.py review-packet output/review-packet.md --title "Demo Project"
python literary-editorial-studio/scripts/scan_manuscript.py path/to/manuscript
python literary-editorial-studio/scripts/check_text_compliance.py path/to/draft.docx
python literary-editorial-studio/scripts/check_font_manifest.py --manifest literary-editorial-studio/assets/font-manifest.example.json
```

## Font and licensing stance

This repository does not bundle font files.

It includes a small registry of low-risk example fonts whose official upstream projects publish permissive licenses. The registry currently references:

- Noto CJK: [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk)
- Source Han Sans: [adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans)
- Source Han Serif: [adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif)
- LXGW WenKai: [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai)

Before redistribution, embedding, packaging, or commercial release, re-check the current license text at the official source. Treat the registry as a screening aid, not a warranty.

## Safety and responsible-use stance

This skill is built for lawful editorial assistance on original or authorized text.

- It refuses clearly unsafe or illegal content categories.
- It is designed to flag obvious publication risks instead of pretending certainty.
- It is not a substitute for legal review, publishing counsel, platform review, or font-license review.

For repository-level reporting and maintenance expectations, see [SECURITY.md](SECURITY.md).

## Release checklist

Before publishing or updating this repository:

1. Run the Codex skill validator against `literary-editorial-studio/`.
2. Run the bundled scripts on a small sample file.
3. Re-check upstream font license pages referenced in `assets/font-registry.json`.
4. Confirm the repo contains no private manuscripts, no copyrighted sample chapters, and no third-party font binaries.
5. Confirm the public docs still describe the actual safety and scope boundaries.

## License

Released under the MIT License. See [LICENSE](LICENSE).
