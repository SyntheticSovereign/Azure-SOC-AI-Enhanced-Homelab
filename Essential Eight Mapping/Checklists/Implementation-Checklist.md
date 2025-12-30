# Essential Eight Implementation Checklist

Use this checklist to guide uplift activities and evidence collection. Each section aligns to the control matrix and includes acceptance criteria, owners, and validation steps.

## How to use this checklist

- Assign owners and due dates per item.
- Link each completed item to an evidence manifest entry.
- Mark partial items with blockers and next steps.
- Review weekly during sprint ceremonies.

## Application Control (AC)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Inventory executable types and high-risk paths | Endpoint Eng | 2025-02-05 | Inventory exists for all workstation builds | `Notes/application-inventory-note.md` |
| 2 | Baseline allow/deny list drafted | Endpoint Eng | 2025-02-07 | Draft reviewed with security/GRC | `Uploads/2025-02-01-applocker-draft.docx` |
| 3 | Pilot AppLocker/WDAC allow list on canary ring | Endpoint Eng | 2025-02-14 | Pilot success report; no critical breakage | `Evidence/2025-01-01/manifest.md#AC-01` |
| 4 | Enable script blocking in user-writable paths | Endpoint Eng | 2025-02-15 | GPO/MDM deployed; audit logs show blocks | `Evidence/2025-01-01/manifest.md#AC-02` |
| 5 | Implement publisher rules for standard apps | Endpoint Eng | 2025-02-20 | Publisher rules enforced; change control exists | `Notes/publisher-rules-note.md` |
| 6 | Implement installer controls (.msi/.pkg) | Endpoint Eng | 2025-02-22 | Installer rules enforced with approvals | `Evidence/2025-01-01/manifest.md#AC-04` |
| 7 | Integrate EDR with allow list alerts | SOC | 2025-02-25 | Alerts in SIEM; test alert documented | `Evidence/2025-01-01/manifest.md#AC-05` |
| 8 | Centralize allow list deployment (Intune/Jamf) | Endpoint Eng | 2025-03-01 | Policy assigned to all managed devices | `Notes/centralized-allowlist-note.md` |
| 9 | Integrity monitoring and rollback configured | Endpoint Eng | 2025-03-05 | Integrity alerts firing; rollback tested | `Evidence/2025-01-01/manifest.md#AC-07` |
| 10 | Break-glass process with expiry and audit | SecOps | 2025-03-10 | SOP approved; SIEM logs show expirations | `Gaps-and-Actions.md#GAP-010` |
| 11 | Quarterly review cadence defined | GRC | 2025-03-15 | Review schedule agreed; metrics captured | `Notes/allowlist-review-note.md` |

## Patch Applications (PA)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Application inventory completed with owners | IT Ops | 2025-02-01 | 100% coverage for managed apps | `Evidence/2025-01-01/manifest.md#PA-01` |
| 2 | Advisory tracking process documented | IT Ops | 2025-02-02 | CVE/advisory board established | `Notes/patch-advisory-note.md` |
| 3 | Critical patch SLA (≤14 days) implemented | IT Ops | 2025-02-10 | SLA signed; reporting enabled | `Evidence/2025-01-01/manifest.md#PA-03` |
| 4 | Non-critical patch SLA (≤30 days) implemented | IT Ops | 2025-02-15 | SLA signed; reporting enabled | `Evidence/2025-01-01/manifest.md#PA-04` |
| 5 | Automated deployment with rings in place | IT Ops | 2025-02-18 | Ring plan executed; rollback path defined | `Uploads/2025-02-05-wsus-ring-plan.docx` |
| 6 | Rollback/health checks tested | IT Ops | 2025-02-20 | Documented test results | `Notes/patch-rollback-note.md` |
| 7 | Risk-based prioritization board live | GRC | 2025-02-22 | CVSS/EPSS + asset criticality scored | `Evidence/2025-01-01/manifest.md#PA-07` |
| 8 | SaaS app patching covered | IT Ops | 2025-02-25 | SaaS update procedure documented | `Notes/saas-patching-note.md` |
| 9 | Exceptions documented with expiry | IT Ops | 2025-02-28 | Exception register approved | `Gaps-and-Actions.md` |
| 10 | Quarterly effectiveness review scheduled | IT Ops | 2025-03-05 | Review invites sent; agenda set | `Notes/patch-review-note.md` |

## Configure Office Macros (MO)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Block macros from internet zone | Messaging | 2025-02-05 | Policy applied; test file blocked | `Evidence/2025-01-01/manifest.md#MO-01` |
| 2 | Block macros from email attachments | Messaging | 2025-02-06 | Policy applied; sample blocked | `Evidence/2025-01-01/manifest.md#MO-02` |
| 3 | Trusted publisher list enforced | Messaging | 2025-02-10 | Signed macros only; publishers documented | `Evidence/2025-01-01/manifest.md#MO-03` |
| 4 | Trusted locations configured (read-only) | Messaging | 2025-02-12 | Locations locked down; validation logs | `Notes/macro-locations-note.md` |
| 5 | Macro telemetry streaming to SIEM | SOC | 2025-02-15 | Alerts exist; sample correlation | `Evidence/2025-01-01/manifest.md#MO-05` |
| 6 | Revocation workflow for publishers | Messaging | 2025-02-20 | Revocation SOP approved; test run complete | `Notes/macro-revocation-note.md` |
| 7 | High-risk user group policy applied | Messaging | 2025-02-22 | Exec/finance OUs targeted; logs show enforcement | `Notes/macro-highrisk-note.md` |
| 8 | Quarterly attestation process documented | GRC | 2025-02-25 | Attestation schedule defined | `Notes/macro-attestation-note.md` |

## User Application Hardening (UAH)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Disable legacy plug-ins (Flash/Java) | Desktop Eng | 2025-02-05 | Browser baselines updated; validation screenshots | `Notes/browser-baseline-note.md` |
| 2 | Enforce download restrictions | Desktop Eng | 2025-02-07 | Executable downloads blocked for standard users | `Evidence/2025-01-01/manifest.md#UAH-02` |
| 3 | Standardize browser baselines via MDM/GPO | Desktop Eng | 2025-02-10 | Baselines applied; assignment list complete | `Notes/browser-baseline-note.md` |
| 4 | Deploy script/ad blocking extensions | Desktop Eng | 2025-02-12 | Allowed extensions list enforced | `Notes/browser-extension-note.md` |
| 5 | Isolate browser sessions for privileged users | Desktop Eng | 2025-02-15 | Isolation working on jump hosts | `Notes/browser-isolation-note.md` |
| 6 | Enable download reputation/SmartScreen | Desktop Eng | 2025-02-18 | Reputation enforced; telemetry available | `Evidence/2025-01-01/manifest.md#UAH-06` |
| 7 | Block Office add-ins from untrusted sources | Messaging | 2025-02-20 | Add-in allow list enforced | `Notes/addin-allowlist-note.md` |
| 8 | Containerize risky file types | Desktop Eng | 2025-02-25 | Container policy enabled; logs verified | `Notes/container-policy-note.md` |
| 9 | Review blocked events monthly with SOC | Desktop Eng | 2025-03-01 | Meeting minutes stored | `Notes/ua-hardening-review-note.md` |

## Restrict Admin Privileges (RAP)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Remove local admin from standard users | IAM | 2025-02-05 | Baseline enforced; exceptions logged | `Notes/local-admin-removal-note.md` |
| 2 | Privileged account inventory validated | IAM | 2025-02-07 | Inventory signed off by GRC | `Evidence/2025-01-01/manifest.md#RAP-02` |
| 3 | Implement JIT elevation | IAM | 2025-02-12 | JIT workflow operational; approvals recorded | `Notes/jit-elevation-note.md` |
| 4 | Send admin session logs to SIEM | SOC | 2025-02-14 | Logs visible; sample query documented | `Evidence/2025-01-01/manifest.md#RAP-04` |
| 5 | Enforce MFA for privileged access | IAM | 2025-02-18 | MFA mandatory; adoption >98% | `Evidence/2025-01-01/manifest.md#MFA-03` |
| 6 | Enable session recording for high-risk systems | IAM | 2025-02-20 | Recording captures sessions; reviewed by SOC | `Evidence/2025-01-01/manifest.md#RAP-06` |
| 7 | Break-glass accounts controlled | IAM | 2025-02-22 | Time-bound access; alerts configured | `Notes/breakglass-note.md` |
| 8 | Quarterly privileged access review | GRC | 2025-02-28 | Review completed; remediation tickets filed | `Notes/privileged-review-note.md` |

## Patch Operating Systems (PO)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | OS inventory with lifecycle status | Server Ops | 2025-02-05 | Inventory validated; EOL flagged | `Evidence/2025-01-01/manifest.md#PO-01` |
| 2 | Critical patch SLA (internet-facing ≤14 days) | Server Ops | 2025-02-10 | SLA signed; reporting enabled | `Evidence/2025-01-01/manifest.md#PO-02` |
| 3 | General patch SLA (≤30 days) | Server Ops | 2025-02-12 | SLA signed; reporting enabled | `Evidence/2025-01-01/manifest.md#PO-03` |
| 4 | Deploy rings with pre-prod validation | Server Ops | 2025-02-15 | Ring plan executed; rollback plan documented | `Uploads/2025-02-05-wsus-ring-plan.docx` |
| 5 | Continuous compliance for remote devices | Endpoint Eng | 2025-02-20 | Compliance dashboard enabled | `Notes/wufb-compliance-note.md` |
| 6 | Harden patch channels with integrity | Server Ops | 2025-02-22 | TLS/integrity enforced | `Notes/patch-channel-integrity-note.md` |
| 7 | Track EOL/EUS and upgrade plans | Architecture | 2025-02-25 | EOL plan approved | `Evidence/2025-01-01/manifest.md#PO-08` |
| 8 | Auto-remediation for out-of-compliance hosts | Endpoint Eng | 2025-02-28 | Rules enabled; sample remediation logged | `Notes/patch-autofix-note.md` |

## Multi-factor Authentication (MFA)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Enforce MFA for VPN/VDI | IAM | 2025-02-05 | MFA required; test login captured | `Evidence/2025-01-01/manifest.md#MFA-01` |
| 2 | Enforce MFA for admin portals | IAM | 2025-02-06 | MFA required; test login captured | `Evidence/2025-01-01/manifest.md#MFA-02` |
| 3 | Enforce MFA for privileged accounts | IAM | 2025-02-10 | Adoption >98%; exceptions documented | `Evidence/2025-01-01/manifest.md#MFA-03` |
| 4 | Enforce MFA for SaaS/federated apps | IAM | 2025-02-12 | IdP policies applied; logs validated | `Notes/saas-mfa-note.md` |
| 5 | Deploy phishing-resistant MFA for execs/admins | IAM | 2025-02-20 | FIDO2 keys issued; test events captured | `Gaps-and-Actions.md#GAP-003` |
| 6 | Enable risk-based conditional access | IAM | 2025-02-22 | Device posture enforced; risk policy enabled | `Notes/conditional-access-note.md` |
| 7 | Quarterly resilience tests | IAM | 2025-02-28 | Token loss/revocation scenarios validated | `Notes/mfa-resilience-note.md` |

## Regular Backups (RB)

| # | Task | Owner | Due | Acceptance criteria | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Identify backup scope and tiers | DR Lead | 2025-02-05 | RPO/RTO documented; business sign-off | `Notes/backup-scope-note.md` |
| 2 | Daily backups for critical systems | DR Lead | 2025-02-07 | Jobs scheduled and monitored | `Evidence/2025-01-01/manifest.md#RB-02` |
| 3 | Enable immutability/WORM storage | DR Lead | 2025-02-10 | Immutability configured; test write/lock | `Evidence/2025-01-01/manifest.md#RB-03` |
| 4 | Replicate to secondary region/offline vault | DR Lead | 2025-02-12 | Replication logs validated | `Evidence/2025-01-01/manifest.md#RB-04` |
| 5 | Quarterly full restore test | DR Lead | 2025-02-15 | Test results meet RTO/RPO | `Evidence/2025-01-01/manifest.md#RB-05` |
| 6 | Ransomware detection on backup data | SOC | 2025-02-18 | Detection alerts tuned | `Notes/backup-detection-note.md` |
| 7 | Backup admin access secured with MFA | IAM | 2025-02-20 | MFA enforced; logs captured | `Evidence/2025-01-01/manifest.md#RB-09` |
| 8 | Backup reporting automated | DR Lead | 2025-02-22 | Dashboard live; alerts configured | `Evidence/2025-01-01/manifest.md#RB-11` |
| 9 | Backup network segmented | Network | 2025-02-28 | Firewall rules enforced; test logs | `Gaps-and-Actions.md#GAP-009` |

## Weekly stand-up prompts

- What items are blocked? Why?
- Which evidence entries need hashing or relocation into dated packs?
- Are any checklists out of date due to platform updates?
- Do we have new gaps to log in `Gaps-and-Actions.md`?

## Review and sign-off

- Checklist owner: Program Manager
- Reviewers: Control owners (per strategy)
- Last reviewed: 2025-02-01
