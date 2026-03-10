# PRC Legal Workbench

One OpenAI Codex skill for partner-level PRC legal drafting, contract review, dispute work, diligence, data-asset compliance, Word redlining, OCR evidence handling, PDF parsing, Excel legal calculations, and public-source compliance research.

This repository is intentionally packaged as a single public OpenAI skill so users do not need to chain multiple adjacent legal skills for normal Chinese legal-document workflows.

## Important identification

This repository is an `OpenAI Codex skill` package.

- It is meant to be installed into a Codex skills directory and invoked as `$cn-legal-workbench`.
- It is not a standalone desktop app, SaaS product, law firm, filing platform, or official legal-information system.
- The root deliverable in this repository is the `cn-legal-workbench/` skill folder, not an executable program.

## What it is

`cn-legal-workbench` is a self-contained OpenAI Codex skill for:

- contract drafting, review, and strategic redlining
- litigation and arbitration documents
- evidence catalogs, chronologies, and hearing-prep materials
- due diligence and red-flag reporting
- data-asset capitalization, compliance, and ABS structure review
- family-wealth risk-isolation structuring
- Word-ready redline and clean-version delivery planning
- OCR evidence organization and PDF dossier scanning
- Excel-based legal calculations and transaction modeling
- OSINT-style public-source compliance monitoring

## What it is not

This repository does not provide:

- legal authority to practice law
- fake-law, fake-case, or fake-evidence generation
- forgery, false litigation, regulatory evasion, debt evasion, or coercive abuse workflows
- unauthorized data scraping guidance beyond lawful and documented public-source review
- client-specific legal advice files or confidential matter files
- government endorsement, court endorsement, or any claim of official status
- guaranteed legal outcomes

## Why this repository exists

Many PRC legal workflows break across too many neighboring steps: facts, redlines, pleadings, evidence tables, long-document review, spreadsheets, and source verification. This skill keeps those connected stages under one operational surface:

- one entry point
- one output discipline
- one set of references
- one set of local helper scripts
- one place to document lawful-use boundaries

## Repository structure

```text
.
|-- cn-legal-workbench/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   |-- references/
|   `-- scripts/
|-- .gitignore
|-- LICENSE
|-- README.md
`-- SECURITY.md
```

## Included helper scripts

- `make_legal_packet.py`
  Creates starter working papers for contracts, disputes, diligence, data-asset matters, legal-tech tasks, and family-wealth projects.
- `scan_contract_elements.py`
  Screens a contract for missing essential clause families.
- `build_evidence_matrix.py`
  Converts CSV or TSV rows into a lawyer-ready evidence matrix.
- `build_red_flag_report.py`
  Converts diligence red flags into a structured Markdown report.
- `build_redline_table.py`
  Turns change notes into a contract comparison explanation table.
- `build_evidence_timeline.py`
  Builds a chronology and evidence catalog from OCR-extracted rows.
- `compute_legal_amounts.py`
  Calculates overdue amounts, LPR-based interest, and labor-compensation figures.
- `build_cap_table.py`
  Builds an equity dilution report from structured share rows.
- `build_cashflow_waterfall.py`
  Allocates inflows across a transaction or ABS waterfall.
- `scan_dossier_terms.py`
  Scans long extracted text for hidden risk markers.
- `make_osint_report.py`
  Scaffolds a public-source compliance and monitoring report.

## Quick start

### 1. Install the OpenAI skill

Copy the `cn-legal-workbench` folder into your Codex skills directory:

- Windows: `%USERPROFILE%\\.codex\\skills\\`
- macOS/Linux: `~/.codex/skills/`

Then restart Codex.

### 2. Use it in OpenAI Codex

Example prompts:

- `Use $cn-legal-workbench to review this PRC contract, redline it at Level 2, and produce a clean version plus issue table.`
- `Use $cn-legal-workbench to draft a PRC complaint, evidence matrix, and case strategy memo from these materials.`
- `Use $cn-legal-workbench to analyze these screenshots and PDFs, build an evidence timeline, and flag authenticity risks.`
- `Use $cn-legal-workbench to review this data-asset project for capitalization conditions, source legality, and ABS structure risk.`

### 3. Run local helper scripts

Examples:

```bash
python cn-legal-workbench/scripts/make_legal_packet.py contract output/contract-packet.md --title "Demo Matter"
python cn-legal-workbench/scripts/scan_contract_elements.py path/to/contract.txt
python cn-legal-workbench/scripts/build_evidence_matrix.py path/to/evidence.csv
python cn-legal-workbench/scripts/compute_legal_amounts.py overdue --principal 100000 --days 90 --annual-rate 0.1
```

## Public-release stance

This repository is for lawful legal-document operations, internal work-product preparation, structured review, and source-based compliance support inside an OpenAI Codex skill workflow.

It is not a substitute for bar admission, filing rights, court acceptance, regulatory approval, or matter-specific human sign-off. It should not be used to fabricate materials, misrepresent legal authority, or conceal unlawful conduct.

## Safety and responsible-use stance

This skill is designed to:

- require fact clarification before formal output when key facts are missing
- anchor legal conclusions to current authoritative sources
- reject fabricated law, fabricated evidence, and clearly unlawful misuse
- preserve source-accounting expectations for OCR, PDF, OSINT, and diligence workflows

For repository-level reporting and maintenance expectations, see [SECURITY.md](SECURITY.md).

## Release checklist

Before publishing or updating this repository:

1. Run the Codex skill validator against `cn-legal-workbench/`.
2. Run `py_compile` or sample executions for the bundled scripts.
3. Confirm the repo contains no client files, no court filings from real matters, no confidential screenshots, and no third-party proprietary databases.
4. Re-check the authority references and public-source descriptions in the skill if the legal baseline changes.
5. Confirm the public docs still describe the actual lawful-use and anti-abuse boundaries.

## License

Released under the MIT License. See [LICENSE](LICENSE).
