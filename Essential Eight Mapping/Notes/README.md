# Notes Workflow (Curated Markdown Integration)

Use this directory to capture concise, citeable summaries of uploaded artifacts while keeping originals intact in `../Uploads/`. Notes are the bridge between raw evidence and the mapping/checklist/policy library.

## When to create a note

- A new upload arrives (audit evidence, vendor advisory, config export, policy draft).
- An existing artifact changes and the evidence pack needs version alignment.
- You need to extract specific control coverage for gap closure or audit response.

## Required metadata per note

| Field | Description | Example |
| --- | --- | --- |
| Title | Clear, human-readable summary of the artifact. | “Intune Application Control Baseline – Feb 2025” |
| Source | Origin of the artifact (vendor, internal team, auditor). | “Security Engineering; exported from Intune” |
| Date received | YYYY-MM-DD intake date. | 2025-02-01 |
| Related uploads | Relative links to `../Uploads/<file>` or evidence pack paths. | `../Uploads/2025-02-01-intune-applocker.xlsx` |
| Scope | Systems, business units, or environments covered. | “Windows workstations; APAC; production only” |
| Controls covered | Essential Eight strategies and maturity levels addressed. | “AC (M2), UAH (M2), MFA (M1)” |
| Analyst | Person creating the note. | “Analyst: J. Smith” |
| Evidence pointers | Specific lines, screenshots, or exports referenced. | “Manifest line 12; screenshot ‘Figure 2’” |
| Actions | Any follow-ups referenced in `../Gaps-and-Actions.md`. | “Action GAP-017: Harden jump hosts” |

## Note templates

### Standard extraction note

```markdown
# <Artifact title>

- **Source**: <author or organization>
- **Date received**: <YYYY-MM-DD>
- **Related uploads**: [../Uploads/<filename>](../Uploads/<filename>)
- **Scope**: <systems/controls covered>
- **Controls covered**: <E8 strategies + maturity levels>
- **Analyst**: <Name>

## Summary
- <bullet summarizing control alignment>
- <bullet summarizing evidence or observations>
- <bullet summarizing risks or exceptions>

## Detailed mapping
| Control/Practice | Evidence reference | Status | Notes |
| --- | --- | --- | --- |
| <Strategy/ID> | <manifest line / file section> | <Aligned/Partial/GAP> | <rationale>
| <Strategy/ID> | <manifest line / file section> | <Aligned/Partial/GAP> | <rationale>

## Action references
- [ ] <Action item> — owner, due date (tracked in ../Gaps-and-Actions.md)
- [ ] <Action item> — owner, due date (tracked in ../Gaps-and-Actions.md)

## Evidence snippets
- <Screenshot or log line> — <explain relevance>
- <Configuration export> — <explain relevance>

## Reviewer checklist
- [ ] Metadata completed
- [ ] Links resolve to files or manifest entries
- [ ] Controls mapped to `Mappings/Essential8-Control-Matrix.md`
- [ ] Actions added or updated in `../Gaps-and-Actions.md`
- [ ] Note saved with consistent naming (`<topic>-note.md`)
```

### Rapid triage note (for same-day audits)

```markdown
# <Artifact title> (Rapid)

- **Source**: <source>
- **Date received**: <YYYY-MM-DD>
- **Related uploads**: <link>
- **Scope**: <scope>
- **Analyst**: <name>

## Key facts
- <fact 1>
- <fact 2>
- <fact 3>

## Controls confirmed
- <E8 strategy + maturity>

## Gaps observed
- <gap>

## Immediate evidence
- <screenshot/log/export>

## Next actions (24–48h)
- [ ] <Action/owner/due>
```

### Comparative note (multiple artifacts)

Use this when combining multiple uploads into a single narrative (e.g., Intune + SCCM baselines).

```markdown
# <Comparative topic>

- **Artifacts compared**: [../Uploads/<file1>](../Uploads/<file1>), [../Uploads/<file2>](../Uploads/<file2>)
- **Reason**: <why the comparison is needed>
- **Analyst**: <name>

## Comparison summary
| Topic | Artifact A | Artifact B | Alignment | Notes |
| --- | --- | --- | --- | --- |
| Patching scope | <text> | <text> | <Aligned/Differ> | <rationale> |
| Control coverage | <text> | <text> | <Aligned/Differ> | <rationale> |
| Evidence quality | <text> | <text> | <Aligned/Differ> | <rationale> |

## Actions
- [ ] <Action> — link to GAP ID
- [ ] <Action> — link to GAP ID
```

## Publishing workflow

1. Create the note using the appropriate template.
2. Validate links to uploads and manifests.
3. Map each claim to `Mappings/Essential8-Control-Matrix.md` references.
4. Add new gaps or update statuses in `../Gaps-and-Actions.md`.
5. Commit the note and update the index below.

## Index of curated notes

- *(Add new notes here with one-line descriptors and owners)*
- Example entry: `intune-applocker-note.md` — Controls AC-01/AC-05/AC-10 (M2) — Owner: Endpoint Engineering — Last reviewed: 2025-02-01

## Style guardrails

- Write in short bullets; avoid marketing language.
- Prefer control IDs (AC-##, PA-##, etc.) instead of paragraphs when possible.
- Always include the evidence pointer (manifest line or file path).
- If an artifact is superseded, mark the note header with `Status: Superseded by <link>`.
- If redactions were applied, mention scope and reason in the summary.

## Quality checklist for reviewers

- [ ] Metadata complete and accurate.
- [ ] Control IDs align to `Mappings/Essential8-Control-Matrix.md`.
- [ ] Evidence links resolve and are in dated packs when required.
- [ ] Actions added/updated in `../Gaps-and-Actions.md`.
- [ ] No sensitive credentials or secrets captured in notes.

## Suggested tags for discovery

- `AC`, `PA`, `MO`, `UAH`, `RAP`, `PO`, `MFA`, `RB`
- `M0`, `M1`, `M2`, `M3`
- `windows`, `macos`, `linux`, `saas`, `cloud`, `on-prem`, `hybrid`
- `evidence`, `gap`, `policy-draft`, `audit-response`, `rapid`

## Frequently referenced uploads (examples)

| Upload | Purpose | Notes |
| --- | --- | --- |
| `2025-02-01-intune-applocker.xlsx` | AppLocker policy export | Use for AC-01 to AC-10 evidence; cite line numbers |
| `2025-02-05-wsus-ring-plan.docx` | Patch ring design | Supports PA-05 and PO-04 | 
| `2025-02-10-macro-policy.pdf` | Macro control policy | Use for MO-01 to MO-06 evidence |
| `2025-02-12-pam-config.json` | PAM platform config export | Supports RAP-03, RAP-04, RAP-06 |
| `2025-02-15-backup-restore-test.md` | Restore exercise | Evidence for RB-05 and RB-06 |

## Troubleshooting link hygiene

- If VS Code or Markdown preview breaks relative links, prefix with `./` (e.g., `./../Uploads/<file>`).
- For paths containing spaces, wrap the link in angle brackets: `[link](<../Uploads/file name.pdf>)`.
- When linking to a specific manifest row, add the row label: `Evidence/2025-03-31/manifest.md#rb-05`.

## Lifecycle management

- Replace outdated notes instead of editing historical evidence packs; keep a pointer to the superseded note for traceability.
- Use git history for diffable changes; avoid force pushes.
- Add `Last reviewed: YYYY-MM-DD` at the end of each note to track freshness.

## Ready-made snippets

- **Exception language**: “This control is partially met due to <reason>. A compensating control is in place: <control>. Target closure: <date>.”
- **Risk statement**: “If <condition> persists, <impact> may occur, resulting in <consequence>. Probability: <High/Med/Low>.”
- **Evidence pointer**: “See `Evidence/<date>/manifest.md`, entry `<ID>`, for screenshot and config export.”

## Contact

- **Primary**: Control owner for the relevant strategy.
- **Secondary**: Evidence Librarian for link hygiene and manifest alignment.
