# Essential Eight Mapping Workspace

This workspace collects Essential Eight (E8) material, curated notes, evidence, mappings, and automation so contributors can ingest uploads quickly and keep a defensible trail for auditors. Use this README as the front door for contributors, reviewers, and assessors.

## Directory map (authoritative)

| Path | Purpose | Key maintainers | Typical contents |
| --- | --- | --- | --- |
| `Uploads/` | Raw, unmodified source files (PDF, DOCX, XLSX, CSV, JSON) received from customers, vendors, or auditors. | Intake owner; evidence librarian | Originals, import logs, checksum reports, intake notes |
| `Notes/` | Curated Markdown integrations that summarize uploads, capture key findings, and map to the Essential Eight. | Control owners; analysts | Summaries with provenance links, extraction notes, mapping snippets |
| `Mappings/` | Canonical mapping sets from the Essential Eight to other frameworks (NIST CSF, ISO 27001, CIS, PCI-DSS). | Governance; compliance | Crosswalk tables, gap overlays, scoping guidance |
| `Checklists/` | Operator-friendly checklists for readiness reviews, uplift campaigns, and evidence capture. | Operations; projects | Activity lists, acceptance criteria, roll-forward guidance |
| `Policies/` | Policy and standard templates aligned to the Essential Eight controls and maturity levels. | GRC; architecture | Policy statements, control objectives, decision records |
| `References/` | External citations, articles, and authoritative sources that underpin the mappings. | Librarian; research | Citation index, URLs, publication metadata |
| `Evidence/YYYY-MM-DD/` | Dated evidence packs (immutable snapshots) with manifests tying files to scope periods. | Evidence librarian | Evidence files, signed PDFs, screenshots, log exports, `manifest.md` |
| `Gaps-and-Actions.md` | Master register for identified gaps, remediation steps, and ownership. | Program manager | Gap table, action traceability, closure evidence |
| `Tools/` | Helper scripts and templates that standardize manifests, hashes, and upload hygiene. | Automation | Python/PowerShell scripts, schema examples |

### Quick-start workflows

1. **Direct upload with traceability** (Option 1 baseline)
   - Drop files in `Uploads/` with no content changes.
   - Record intake details in `Uploads/manifest-template.md` and add SHA256 hashes if available.
   - If an upload belongs to a dated evidence pack, place a copy in `Evidence/YYYY-MM-DD/` and list it in that manifest.
2. **Curated Markdown integration** (Option 2)
   - Create a new note in `Notes/` using the template in `Notes/README.md`.
   - Extract key controls, findings, and mappings; cite the source upload.
   - Reference any remediation in `Gaps-and-Actions.md`.
3. **Structured library by artifact type** (Option 3)
   - Place mappings, checklists, policies, and reference indexes in their dedicated folders.
   - Ensure each artifact has an “owner”, “last reviewed”, and “applicability” section.
4. **Gap analysis & alignment set** (Option 4)
   - Use `Gaps-and-Actions.md` to log current state, desired state, owners, due dates, and evidence pointers.
   - Include links back to notes, mappings, or evidence packs that justify the gap or validate the fix.
5. **Versioned evidence packs** (Option 5)
   - Create dated folders under `Evidence/` (e.g., `Evidence/2025-03-31/`).
   - Populate the local `manifest.md` with files and scope periods; store source files locally to keep the pack immutable.
   - Cross-reference the manifest from actions that rely on that evidence snapshot.

## Contribution checklist

- [ ] Add new uploads to `Uploads/` and log them in `Uploads/manifest-template.md`.
- [ ] Generate or update notes under `Notes/` for each significant upload.
- [ ] Extend mappings in `Mappings/Essential8-Control-Matrix.md` when new frameworks or systems are in play.
- [ ] Refresh operational checklists in `Checklists/Implementation-Checklist.md` during each sprint.
- [ ] Align policies in `Policies/Policy-Template.md` with any design or architecture shifts.
- [ ] Add citations to `References/Source-Index.md` for any external content referenced.
- [ ] Update `Gaps-and-Actions.md` whenever gaps are discovered or closed.
- [ ] Add or refresh dated evidence packs to reflect the latest validated configuration.

## Intake and triage

1. **Receive artifact** → Verify filename, source, and checksum (if provided).
2. **Store original** → Save to `Uploads/` without modification.
3. **Classify** → Tag as policy, checklist, mapping, evidence, or reference.
4. **Decide destination** → If immutable evidence, copy into a dated `Evidence/` pack; otherwise link only from the manifest.
5. **Document** → Create or update the corresponding note, checklist, or mapping entry.
6. **Traceability** → Ensure `Gaps-and-Actions.md` references the evidence backing each closure.

## Naming conventions

| Artifact type | Pattern | Example |
| --- | --- | --- |
| Uploads | `<YYYY-MM-DD>-<source>-<topic>.<ext>` | `2025-02-01-vendorA-app-whitelist.xlsx` |
| Notes | `<topic>-note.md` | `macro-controls-note.md` |
| Evidence pack folder | `Evidence/<YYYY-MM-DD>/` | `Evidence/2025-03-31/` |
| Mappings | `<framework>-mapping.md` | `nist-csf-mapping.md` |
| Checklists | `<area>-checklist.md` | `workstation-hardening-checklist.md` |
| Policies | `<domain>-policy.md` | `application-control-policy.md` |
| References | `<source>-reference.md` | `asd-guidance-reference.md` |

## Change control and review cadence

- **Weekly**: Intake review to triage new uploads and ensure notes exist.
- **Bi-weekly**: Checklist and mapping updates synchronized with sprint reviews.
- **Monthly**: Policy and reference review for currency against vendor releases and ASD updates.
- **Quarterly**: Evidence pack creation with immutable snapshots and manifest sign-off by control owners.
- **Event-driven**: Immediate update when security incidents or audit findings impact Essential Eight coverage.

## Evidence quality gates

- Every manifest entry must capture **scope period**, **owner**, **system**, **control coverage**, and **applicability notes**.
- Screenshots require timestamps and hostnames; logs require log source, filter criteria, and export time.
- Scripts or configuration exports should include version numbers and commands used to generate them.
- For notes, include **source link**, **extraction date**, **analyst**, and **controls impacted**.
- For mappings, cite the authoritative source (e.g., ASD, NIST, ISO) and the rationale for alignment.

## Minimum viable kit for a new assessment

- `Uploads/manifest-template.md` populated with incoming artifacts and hashes.
- `Notes/<artifact>-note.md` capturing the core control coverage for each upload.
- `Mappings/Essential8-Control-Matrix.md` tailored to the assessed environment (cloud/on-prem/hybrid).
- `Checklists/Implementation-Checklist.md` scheduled across teams with owners and due dates.
- `Policies/Policy-Template.md` issued with decision records and exceptions.
- `Evidence/<date>/manifest.md` created for the assessment period.
- `Gaps-and-Actions.md` baselined with open items and validation steps.

## Crosswalk highlights

- Each Essential Eight strategy is mapped to:
  - ASD maturity levels (M0–M3)
  - NIST CSF categories (ID, PR, DE, RS, RC)
  - ISO 27001 Annex A controls
  - CIS v8 safeguards
  - PCI-DSS 4.0 requirements (where applicable)
- Detailed mapping tables live in `Mappings/Essential8-Control-Matrix.md` and should be updated as frameworks evolve.

## Roles and responsibilities

- **Evidence Librarian**: Maintains `Uploads/`, validates hashes, curates manifests, and owns dated evidence packs.
- **Control Owner**: Updates notes, checklists, and gap statuses for their assigned strategy.
- **GRC Lead**: Approves mappings, policies, and alignment decisions; tracks deviations.
- **Automation Engineer**: Maintains `Tools/` and scripts that keep manifests and hashes consistent.
- **Auditor/Reviewer**: Consumes manifests, notes, and mappings; verifies that gaps are closed with evidence.

## Automation stubs (Tools/)

- `manifest_builder.py`: Generates manifest tables from YAML input and injects SHA256 hashes for uploads.
- `checksum-report.md`: Placeholder for future automation output summarizing checksum validation runs.
- `manifest.schema.yaml`: Optional schema describing fields required in manifests (scope period, owner, system, control, evidence path).

## How to request updates

- File an issue describing the artifact type, target folder, scope period, and urgency.
- Include whether you need curated notes, mappings, or gap updates.
- Assign a control owner and due date; ensure reviewers are tagged for policy or mapping changes.

## Escalation path

- If evidence is missing or stale, escalate to the Evidence Librarian and Program Manager.
- If mappings conflict with authoritative guidance, escalate to the GRC Lead.
- If tooling breaks or hashes mismatch, escalate to the Automation Engineer.

## Audit-ready checklist

- [ ] Every evidence pack has a signed `manifest.md` with scope period and owner.
- [ ] Notes link to the exact upload used for extraction.
- [ ] Gap closures reference evidence with timestamps and hostnames where applicable.
- [ ] Policies and checklists reflect the current version of the environment (cloud providers, EDR, SIEM, patch tooling).
- [ ] Mappings cite authoritative sources and document assumptions or scoping exclusions.

## Extending this workspace

- Add additional frameworks (e.g., SOC 2, HIPAA, GDPR) to the mapping matrix when relevant.
- Capture system-specific runbooks (e.g., “macOS hardening for M365 tenants”) under `Checklists/`.
- Store architecture diagrams supporting Essential Eight coverage under `References/` with revision history.
- Add data classifications or tenant identifiers when evidence spans multiple environments.

## Onboarding recipe for new analysts

1. Read this README and the mapping matrix in `Mappings/Essential8-Control-Matrix.md`.
2. Review the latest evidence pack manifest to understand baseline coverage.
3. Walk through open items in `Gaps-and-Actions.md` and align with your control ownership.
4. Shadow a curated note creation using an existing upload.
5. Run automation scripts in `Tools/` to validate manifests and hashes.

## FAQs

**Q: Where do I put screenshots from a tool that also exports CSV?**
- Store both in the dated `Evidence/` folder; cite both in the manifest with the same scope period.

**Q: How do I show maturity progression between packs?**
- Use the “Evidence quality gates” and “Change control” sections to note deltas; add a row in `Gaps-and-Actions.md` describing uplift.

**Q: Can I link to cloud storage instead of storing files?**
- Prefer local copies for immutability. If impossible, include signed URLs with expiry dates and validation notes.

## Last reviewed

- Repository structure last expanded: 2025-01-01.
- Update this field whenever the workspace structure changes.
