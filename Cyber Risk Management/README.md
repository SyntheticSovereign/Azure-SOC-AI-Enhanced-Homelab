# Cyber Risk Management Repository

This folder provides reusable templates, checklists, and guides for creating cyber risk management documentation such as asset catalogs, risk assessments, and control mappings. The goal is to help teams rapidly stand up a consistent evidence package aligned to ISO 27005, COBIT 2019, NIST CSF, and related frameworks.

## Folder structure

- `templates/` — CSV templates for asset inventories, risk registers, and control mapping matrices.
- `guides/` — How-to playbooks, scoring references, and workflow guidance for building assessments.
- `checklists/` — Repeatable task lists for project kickoff, workshops, and reporting cycles.
- `profiles/` — Example company profiles and scenario write-ups to illustrate how to populate the templates.

## How to use

1. Copy the templates into your working directory.
2. Tailor the columns to match your governance language and tooling (e.g., GRC platforms, spreadsheets, or data catalogs).
3. Fill in asset and risk data collaboratively with stakeholders from security, IT, privacy, and business units.
4. Use the control mapping template to document how each risk is mitigated and which framework requirements are met.
5. Leverage the guides to facilitate workshops, run tabletop exercises, and report findings.

## Recommended workflow

1. **Scope** — Define objectives, risk appetite, and applicable frameworks.
2. **Inventory** — Capture business services, supporting assets, data classifications, and owners.
3. **Assess** — Identify threats, vulnerabilities, and existing controls. Score likelihood and impact using the scoring reference.
4. **Prioritize** — Use risk ratings and business criticality to create a remediation backlog.
5. **Treat** — Map controls, assign owners, and track due dates. Align with COBIT governance and ISO risk treatment plans.
6. **Report** — Produce board-ready summaries, executive heat maps, and control coverage views.
7. **Improve** — Schedule quarterly reviews, tabletop exercises, and continuous control monitoring.

## Key templates

- `templates/asset_inventory_template.csv` — Asset register with business context and confidentiality/integrity/availability (CIA) ratings.
- `templates/risk_register_template.csv` — Risk statements, scenarios, scoring, and treatment plans.
- `templates/control_mapping_template.csv` — Crosswalk between risks, controls, and frameworks (ISO 27001 Annex A, NIST CSF, COBIT objectives).

## Notes

- CSV templates are intentionally verbose so you can prune columns that are not relevant to your organization.
- Sample rows illustrate recommended phrasing for risk statements, threats, and mitigations.
- Scoring values are ordinal (1–5) but can be adapted to quantitative models if desired.
