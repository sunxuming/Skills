---
name: literary-editorial-studio
description: End-to-end studio for novels, literary fiction, serialized fiction, and other long-form editorial writing projects. Use when Codex needs to handle more than one adjacent stage in the same request, such as project framing, canon or continuity control, developmental editing, line editing, manuscript normalization, editorial packet assembly, typography planning, Word-ready delivery, or publication-safety screening.
---

# Literary Editorial Studio

## Operating model

Treat long-form writing as one production pipeline. Classify the deliverable first, rebuild the active document state, choose one primary lane, and keep adjacent editing, formatting, and compliance work inside this skill so the user does not need to chain multiple related skills.

## Scope and hard boundaries

- Use this skill for lawful editorial, manuscript, and delivery work on original or authorized text.
- Do not generate illegal content, exploitation content, hateful abuse, fraud or forgery assistance, violent wrongdoing instructions, extremist praise, or content that violates basic human dignity.
- Do not write sexual content involving minors, non-consensual sexual abuse, or content that meaningfully facilitates abuse.
- Do not imitate a living author's distinctive voice or reproduce copyrighted passages beyond short user-supplied excerpts needed for analysis.
- Do not claim a font is commercially safe unless its current license text and redistribution terms have been checked. Use `low-risk` language, not guarantees.

## Single-skill rule

- Stay in this skill when the request spans two or more neighboring stages: planning, editing, formatting, packaging, or delivery.
- Do not split the work into specialist skills unless the task is purely one narrow mode or the user explicitly wants a specialist-only pass.
- Load only the reference or script that matches the active lane.

## Workflow

### 1. Frame the deliverable

- Identify whether the user needs a story bible, continuation brief, developmental edit, line edit, manuscript cleanup, review packet, release bundle, or `.docx` handoff.
- Identify whether the material is idea-stage, in-progress draft, late-stage edit, or final delivery.
- If the input is fragmented, infer the smallest useful output and list missing high-risk inputs.

### 2. Rebuild the live document state

- Extract title, scope, current chapter or section boundary, point of view, timeline anchors, terminology, style constraints, formatting state, and unresolved editorial issues.
- Separate confirmed facts, draft inconsistencies, and your own assumptions.
- Preserve canon terms, chronology, and scene outcomes unless the user explicitly allows structural change.

### 3. Choose the primary lane

- Architecture lane: premise, bible, chapter map, continuity ledger, escalation plan.
- Development lane: diagnose pacing, clarity, stakes, argument flow, thematic drift, or structural weakness before rewriting.
- Prose lane: line edit, dialogue cleanup, action clarity, compression, expansion, or voice alignment on existing text.
- Manuscript lane: normalize headings, chapter files, synopses, glossaries, review packets, and release bundles.
- Delivery lane: prepare Word-ready structure, numbering, typography plan, and export-minded handoff.
- Compliance lane: screen the draft, package, and font plan for obvious publication-risk issues before release.

### 4. Produce one package that moves the project forward

- Return the smallest complete package that resolves the current bottleneck.
- For broad requests, include the next usable artifact instead of stopping at abstract advice.
- When useful, include a short `Next Stage` note so the same skill can continue without reclassification.

### 5. Run publication-safety checks

- Check for continuity breaks, heading and numbering drift, unstable terminology, and formatting regressions.
- Check for content that appears to violate law, platform safety expectations, basic public ethics, or human dignity.
- Check that any proposed font plan uses only fonts whose current license and redistribution status are documented and re-verified.
- When risk exists, explain the issue, refuse the unsafe part, and offer a safer alternative path.

## Output packages

- Project pack: premise, canon pack, chapter map, continuity ledger, and next-step plan.
- Revision pack: editorial diagnosis, revised text, and continuity-risk notes.
- Manuscript pack: normalized file structure, chapter naming scheme, synopsis, cast sheet, glossary, or review packet.
- Delivery pack: Word style map, heading logic, numbering plan, typography note, and final handoff checklist.
- Compliance pack: flagged passages, risk categories, manual-review notes, and safer rewrite guidance.

## Internal references

- Read [references/editorial-templates.md](references/editorial-templates.md) for reusable briefs, memos, and project templates.
- Read [references/manuscript-presets.md](references/manuscript-presets.md) for file layouts, review packets, release bundles, and `.docx` handoff structure.
- Read [references/compliance-guardrails.md](references/compliance-guardrails.md) for refusal boundaries, risky-content categories, and safe fallback behavior.
- Read [references/font-policy.md](references/font-policy.md) for low-risk font selection, redistribution warnings, and manifest-review rules.
- Read [references/pipeline-checklists.md](references/pipeline-checklists.md) for fast routing and QA.

## Bundled scripts

- Run [scripts/make_editorial_packet.py](scripts/make_editorial_packet.py) to scaffold a standard editorial packet or manuscript support document.
- Run [scripts/scan_manuscript.py](scripts/scan_manuscript.py) to inspect Markdown or plain-text manuscripts for heading, numbering, and naming issues.
- Run [scripts/check_text_compliance.py](scripts/check_text_compliance.py) to screen `.md`, `.txt`, or `.docx` drafts for obvious publication-risk categories.
- Run [scripts/check_font_manifest.py](scripts/check_font_manifest.py) to review a planned font set against the bundled low-risk registry.

## Practical rules

- Prefer original prose and abstract style targets over author mimicry.
- Prefer semantic structure over visual hacks.
- Prefer short, explicit risk notes over false certainty.
- Preserve comments, review intent, and user-supplied canon when editing.
- Treat all compliance and font checks as screening support, not final legal advice.
