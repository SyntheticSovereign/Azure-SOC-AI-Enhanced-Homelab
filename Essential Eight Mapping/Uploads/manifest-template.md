# Uploads Intake Manifest Template

Use this template when ingesting raw files into `Uploads/` or preparing them for dated evidence packs. Keep originals unchanged; record hashes and provenance.

## Intake log

| ID | Filename | Source | Date received | Hash (SHA256) | Size | Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UP-001 | <file> | <vendor/team> | <YYYY-MM-DD> | <hash> | <size> | <owner> | <context> |
| UP-002 | <file> | <vendor/team> | <YYYY-MM-DD> | <hash> | <size> | <owner> | <context> |

_Add rows per file. Use IDs consistently in notes and manifests._

## Provenance checklist

- [ ] Filename follows `<YYYY-MM-DD>-<source>-<topic>.<ext>` pattern.
- [ ] Hash recorded and verified after upload.
- [ ] Source email or ticket ID captured.
- [ ] Classification reviewed (sensitive, internal, public).
- [ ] Stored locally (no external links as primary copy).

## Suggested folders

- `Uploads/Policies/` — raw policy drafts or vendor guidance
- `Uploads/Mappings/` — third-party mapping documents
- `Uploads/Checklists/` — checklists provided by auditors or vendors
- `Uploads/Evidence/` — raw evidence not tied to a dated pack yet

## Sample intake entry

| ID | Filename | Source | Date received | Hash (SHA256) | Size | Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UP-010 | 2025-02-01-intune-applocker.xlsx | Security Engineering | 2025-02-01 | `<hash>` | 2.3 MB | Endpoint Eng | Export from Intune; used for AC controls |

## Intake SOP

1. Receive file and verify checksum if provided.
2. Store file in `Uploads/` and update the table above.
3. If the file will support a dated evidence pack, copy to `Evidence/<date>/` and add to that manifest.
4. Create a curated note in `Notes/` to summarize the file.
5. Add any identified gaps to `Gaps-and-Actions.md`.

## Link hygiene

- Use relative links (e.g., `../Evidence/2025-01-01/manifest.md#AC-07`).
- Avoid spaces in filenames; if unavoidable, wrap links in angle brackets.
- Do not rename files after hashes are recorded; if renaming is necessary, re-hash and update references.

## Intake review checklist

- [ ] Metadata complete (source, date, owner, hash).
- [ ] Stored in correct subfolder.
- [ ] Note created or updated.
- [ ] Gap register updated if issues found.
- [ ] Evidence pack references added if applicable.

## Change log

- 2025-02-01: Template created to align uploads with manifests and curated notes.
