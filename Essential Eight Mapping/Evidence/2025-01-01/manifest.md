# Evidence Pack – 2025-01-01

Use this manifest to describe the evidence snapshot collected on 2025-01-01. Add links to files stored alongside this manifest or in `../Uploads/`. Keep this pack immutable once published.

## Scope and ownership

- **Scope period**: 2024-12-01 to 2025-01-01
- **Systems**: Workstations (Windows/macOS), Domain Controllers, VPN, Backup platform, PAM, Intune, WSUS
- **Owner**: Evidence Librarian (SecOps)
- **Reviewers**: Control owners for AC, PA/PO, MO, UAH, RAP, MFA, RB
- **Notes**: Use this manifest ID `EVD-2025-01-01` when referencing entries from notes or the gap register.

## Manifest entries

| ID | File | Description | Scope period | Control mapping | Owner | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| AC-07 | `allowlist-integrity-report.csv` | Integrity monitor output showing drift alerts and remediation events. | 2024-12-15 to 2025-01-01 | AC-07 (M3) | Endpoint Eng | Stored locally; hash recorded below |
| AC-10 | `applocker-validation.xlsx` | Validation of allow list after app updates (hash/publisher rules). | 2024-12-20 | AC-10 (M2) | Endpoint Eng | Includes change record IDs |
| PA-03 | `patch-compliance-critical.csv` | Critical app patch adoption rates. | 2024-12-01 to 2024-12-31 | PA-03 (M2) | IT Ops | Excludes Linux fleet |
| PA-04 | `patch-compliance-noncritical.csv` | Non-critical app patch adoption rates. | 2024-12-01 to 2024-12-31 | PA-04 (M2) | IT Ops | SaaS apps tracked separately |
| PA-07 | `risk-based-prioritization-board.md` | CVSS/EPSS risk board for apps. | 2024-12-05 to 2024-12-20 | PA-07 (M3) | GRC | Includes exception IDs |
| MO-03 | `macro-trusted-publishers.txt` | Trusted publisher list for signed macros. | 2024-12-29 | MO-03 (M2) | Messaging | Generated from Intune/GPO |
| MO-05 | `macro-telemetry.json` | Macro execution telemetry with suspicious block logs. | 2024-12-15 to 2024-12-31 | MO-05 (M2) | SOC | Filtered for finance OU |
| UAH-06 | `smartscreen-telemetry.csv` | Reputation-based blocking events on workstations. | 2024-12-01 to 2024-12-31 | UAH-06 (M2) | Desktop Eng | Includes legacy OS exceptions |
| RAP-04 | `admin-session-logs.ndjson` | Admin session logs shipped to SIEM. | 2024-12-01 to 2024-12-31 | RAP-04 (M2) | SOC | Masks PII |
| RAP-06 | `pam-session-recording-guide.md` | Steps and screenshots for session recording setup. | 2024-12-18 | RAP-06 (M3) | IAM | Used for GAP-006 closure |
| PO-03 | `os-patch-compliance.csv` | OS patching status across servers/workstations. | 2024-12-01 to 2024-12-31 | PO-03 (M2) | Server Ops | Includes ring assignment |
| PO-08 | `eol-tracker.xlsx` | EOL/EUS status and upgrade plans. | 2024-12-01 | PO-08 (M1) | Architecture | Business sign-offs pending |
| MFA-02 | `admin-portal-mfa-report.pdf` | MFA enforcement on admin portals. | 2024-12-10 | MFA-02 (M1) | IAM | Contains sign-in test screenshots |
| MFA-09 | `risk-event-export.csv` | Anomalous sign-in detections and resolutions. | 2024-12-01 to 2024-12-31 | MFA-09 (M3) | SOC | Linked to SIEM cases |
| RB-05 | `backup-restore-test.md` | Restore test results for tier-1 apps. | 2024-12-15 | RB-05 (M2) | DR Lead | RTO/RPO achieved |
| RB-07 | `backup-encryption-kms.txt` | KMS key rotation log for backups. | 2024-12-01 to 2024-12-31 | RB-07 (M2) | DR Lead | KMS policy ID noted |
| RB-11 | `backup-reporting-dashboard.png` | Screenshot of backup success/failure dashboard. | 2024-12-31 | RB-11 (M2) | DR Lead | Includes alert routes |

## Hashes (SHA256)

| File | SHA256 |
| --- | --- |
| `allowlist-integrity-report.csv` | `<hash>` |
| `applocker-validation.xlsx` | `<hash>` |
| `patch-compliance-critical.csv` | `<hash>` |
| `patch-compliance-noncritical.csv` | `<hash>` |
| `risk-based-prioritization-board.md` | `<hash>` |
| `macro-trusted-publishers.txt` | `<hash>` |
| `macro-telemetry.json` | `<hash>` |
| `smartscreen-telemetry.csv` | `<hash>` |
| `admin-session-logs.ndjson` | `<hash>` |
| `pam-session-recording-guide.md` | `<hash>` |
| `os-patch-compliance.csv` | `<hash>` |
| `eol-tracker.xlsx` | `<hash>` |
| `admin-portal-mfa-report.pdf` | `<hash>` |
| `risk-event-export.csv` | `<hash>` |
| `backup-restore-test.md` | `<hash>` |
| `backup-encryption-kms.txt` | `<hash>` |
| `backup-reporting-dashboard.png` | `<hash>` |

## Intake notes

- Intake verified by: Evidence Librarian on 2025-01-02.
- Files stored in this folder; duplicates in `../Uploads/` for common reuse.
- Sensitive data masked in `admin-session-logs.ndjson` prior to storage.
- Macro telemetry filtered to finance OU to avoid over-collection.

## Validation checklist

- [ ] All files present and hashes verified.
- [ ] Scope period aligns with assessment window.
- [ ] Owners acknowledged receipt.
- [ ] Links referenced in `Notes/` and `Gaps-and-Actions.md` are valid.
- [ ] Evidence is immutable (no edits after this manifest date).

## Future packs

- Next pack planned for `Evidence/2025-03-31/` with expanded PAM recording and backup isolation evidence.
