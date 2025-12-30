# Evidence Capture Checklist by Strategy

Use this checklist while collecting artifacts so every claim is backed by verifiable evidence. Pair each item with a manifest ID and hash.

## Application Control (AC)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Allow list policy export (XML/JSON) | Includes version, hash, target groups | Evidence/<date>/manifest.md#AC-01 | |
| 2 | Path rule block log | Log entry showing block from user-writable path | Evidence/<date>/manifest.md#AC-02 | |
| 3 | Publisher rule configuration | Screenshots or exports for vendor rules | Evidence/<date>/manifest.md#AC-03 | |
| 4 | Installer control proof | Block log or approval ticket for MSI/PKG | Evidence/<date>/manifest.md#AC-04 | |
| 5 | EDR correlation | Alert showing unsigned binary blocked | Evidence/<date>/manifest.md#AC-05 | |
| 6 | Central deployment scope | MDM/ConfigMgr assignment list | Evidence/<date>/manifest.md#AC-06 | |
| 7 | Integrity monitoring | Alert, rollback log, and restored file hash | Evidence/<date>/manifest.md#AC-07 | |
| 8 | Tiered policy matrix | Differentiation for servers/workstations | Evidence/<date>/manifest.md#AC-08 | |
| 9 | Break-glass SOP and log | Approval, expiry, SIEM log | Evidence/<date>/manifest.md#AC-09 | |
| 10 | Post-update validation | Test results after major app updates | Evidence/<date>/manifest.md#AC-10 | |
| 11 | Exception register | Documented exceptions with expiry | Evidence/<date>/manifest.md#AC-11 | |
| 12 | Blocked execution telemetry | SIEM query export with retention noted | Evidence/<date>/manifest.md#AC-12 | |
| 13 | Reputation feed config | Config showing reputation enforcement | Evidence/<date>/manifest.md#AC-13 | |
| 14 | Quarterly review minutes | Notes and action items | Evidence/<date>/manifest.md#AC-14 | |
| 15 | CI/CD integration proof | Pipeline logs updating allow list | Evidence/<date>/manifest.md#AC-15 | |

## Patch Applications (PA)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Application inventory export | Includes version/vendor and owner fields | Evidence/<date>/manifest.md#PA-01 | |
| 2 | Advisory subscription proof | Email/webhook or RSS log | Evidence/<date>/manifest.md#PA-02 | |
| 3 | Critical patch compliance report | Shows ≤14-day adoption | Evidence/<date>/manifest.md#PA-03 | |
| 4 | Non-critical patch compliance | Shows ≤30-day adoption | Evidence/<date>/manifest.md#PA-04 | |
| 5 | Deployment ring plan | Document or export defining rings | Evidence/<date>/manifest.md#PA-05 | |
| 6 | Rollback/health check log | Test evidence for rollback | Evidence/<date>/manifest.md#PA-06 | |
| 7 | Risk board snapshot | CVSS/EPSS plus asset criticality | Evidence/<date>/manifest.md#PA-07 | |
| 8 | SOAR/SIEM automation run | Job output generating reports | Evidence/<date>/manifest.md#PA-08 | |
| 9 | Hash verification of sources | Checksum and signature logs | Evidence/<date>/manifest.md#PA-09 | |
| 10 | Exception register | Expiry, compensating control, approval | Evidence/<date>/manifest.md#PA-10 | |
| 11 | Virtual patching record | Firewall/EDR rule and ticket | Evidence/<date>/manifest.md#PA-11 | |
| 12 | User impact metrics | Telemetry or survey results | Evidence/<date>/manifest.md#PA-12 | |
| 13 | Mirror integrity check | apt/yum/npm mirror validation | Evidence/<date>/manifest.md#PA-13 | |
| 14 | SaaS change log | Admin portal export | Evidence/<date>/manifest.md#PA-14 | |
| 15 | Effectiveness review minutes | SLA trend charts | Evidence/<date>/manifest.md#PA-15 | |

## Configure Office Macros (MO)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Internet macro block proof | Test doc blocked + log | Evidence/<date>/manifest.md#MO-01 | |
| 2 | Email macro block proof | Quarantine/log evidence | Evidence/<date>/manifest.md#MO-02 | |
| 3 | Trusted publisher list | Export of trusted CAs/publishers | Evidence/<date>/manifest.md#MO-03 | |
| 4 | Trusted location config | Registry/MDM profile export | Evidence/<date>/manifest.md#MO-04 | |
| 5 | Telemetry to SIEM | Query screenshot and alert sample | Evidence/<date>/manifest.md#MO-05 | |
| 6 | Revocation workflow | SOP and test log | Evidence/<date>/manifest.md#MO-06 | |
| 7 | High-risk OU policy | Assignment list for finance/execs | Evidence/<date>/manifest.md#MO-07 | |
| 8 | Attestation record | Quarterly attestation output | Evidence/<date>/manifest.md#MO-08 | |
| 9 | User training proof | Training completion list | Evidence/<date>/manifest.md#MO-09 | |
| 10 | Sandbox evidence | Isolation config and log | Evidence/<date>/manifest.md#MO-10 | |
| 11 | DLP incident | Blocked exfil attempt evidence | Evidence/<date>/manifest.md#MO-11 | |
| 12 | Automated test output | CI pipeline results | Evidence/<date>/manifest.md#MO-12 | |
| 13 | Network access alert | Alert details for macro network call | Evidence/<date>/manifest.md#MO-13 | |
| 14 | Template inventory | List of macro-enabled templates | Evidence/<date>/manifest.md#MO-14 | |
| 15 | Exception review minutes | Finance/legal review notes | Evidence/<date>/manifest.md#MO-15 | |

## User Application Hardening (UAH)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Browser baseline export | Policy export showing disabled plugins | Evidence/<date>/manifest.md#UAH-01 | |
| 2 | Download block proof | Test download blocked | Evidence/<date>/manifest.md#UAH-02 | |
| 3 | Baseline assignment list | OU/device scope details | Evidence/<date>/manifest.md#UAH-03 | |
| 4 | Extension allow/deny list | Policy export and test result | Evidence/<date>/manifest.md#UAH-04 | |
| 5 | Isolation policy | Isolation config and telemetry | Evidence/<date>/manifest.md#UAH-05 | |
| 6 | Reputation block logs | SmartScreen/rep logs | Evidence/<date>/manifest.md#UAH-06 | |
| 7 | Add-in allow list | Office add-in control proof | Evidence/<date>/manifest.md#UAH-07 | |
| 8 | Containerization log | Isolation for risky files | Evidence/<date>/manifest.md#UAH-08 | |
| 9 | TLS inspection exemptions | List with approvals | Evidence/<date>/manifest.md#UAH-09 | |
| 10 | Messaging app restriction | Block log for unapproved app | Evidence/<date>/manifest.md#UAH-10 | |
| 11 | PDF hardening settings | Reader config export | Evidence/<date>/manifest.md#UAH-11 | |
| 12 | Telemetry tuning record | Policy adjustment log | Evidence/<date>/manifest.md#UAH-12 | |
| 13 | File association policy | Mapping of file types to apps | Evidence/<date>/manifest.md#UAH-13 | |
| 14 | Threat feed updates | Block list update logs | Evidence/<date>/manifest.md#UAH-14 | |
| 15 | Monthly review minutes | SOC review outcomes | Evidence/<date>/manifest.md#UAH-15 | |

## Restrict Admin Privileges (RAP)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Local admin removal report | Compliance export | Evidence/<date>/manifest.md#RAP-01 | |
| 2 | Privileged account inventory | CMDB/Directory extract | Evidence/<date>/manifest.md#RAP-02 | |
| 3 | JIT workflow evidence | Approval flow screenshot | Evidence/<date>/manifest.md#RAP-03 | |
| 4 | Admin session logs | SIEM query export | Evidence/<date>/manifest.md#RAP-04 | |
| 5 | Privileged MFA proof | Conditional access report | Evidence/<date>/manifest.md#RAP-05 | |
| 6 | Session recording sample | Recording metadata | Evidence/<date>/manifest.md#RAP-06 | |
| 7 | Break-glass SOP and alert | SOP + SIEM alert | Evidence/<date>/manifest.md#RAP-07 | |
| 8 | Quarterly review record | Review minutes | Evidence/<date>/manifest.md#RAP-08 | |
| 9 | Lifecycle automation log | Provision/deprovision evidence | Evidence/<date>/manifest.md#RAP-09 | |
| 10 | Vault checkout log | PAM vault checkout evidence | Evidence/<date>/manifest.md#RAP-10 | |
| 11 | Device posture enforcement | Policy export showing posture requirement | Evidence/<date>/manifest.md#RAP-11 | |
| 12 | Jump host enforcement | Denial log for non-jump host access | Evidence/<date>/manifest.md#RAP-12 | |
| 13 | Cached credential control | Registry/policy proof | Evidence/<date>/manifest.md#RAP-13 | |
| 14 | Analytics dashboard | Privilege anomaly detection | Evidence/<date>/manifest.md#RAP-14 | |
| 15 | Dual-identity separation | Proof of separate admin accounts | Evidence/<date>/manifest.md#RAP-15 | |

## Patch Operating Systems (PO)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | OS inventory export | Includes lifecycle status | Evidence/<date>/manifest.md#PO-01 | |
| 2 | Critical patch compliance | ≤14-day report | Evidence/<date>/manifest.md#PO-02 | |
| 3 | 30-day patch compliance | Report for internal assets | Evidence/<date>/manifest.md#PO-03 | |
| 4 | Ring validation results | Canary vs production health | Evidence/<date>/manifest.md#PO-04 | |
| 5 | Compliance dashboard | Continuous compliance output | Evidence/<date>/manifest.md#PO-05 | |
| 6 | Rollback log | Automated rollback evidence | Evidence/<date>/manifest.md#PO-06 | |
| 7 | Firmware update proof | Vendor confirmation and logs | Evidence/<date>/manifest.md#PO-07 | |
| 8 | EOL tracking | Upgrade plan and approvals | Evidence/<date>/manifest.md#PO-08 | |
| 9 | Remote device compliance | Roaming device coverage | Evidence/<date>/manifest.md#PO-09 | |
| 10 | Channel integrity proof | TLS/signing evidence | Evidence/<date>/manifest.md#PO-10 | |
| 11 | MTTR metrics | Trend charts | Evidence/<date>/manifest.md#PO-11 | |
| 12 | Vuln scan linkage | Mapping to patch IDs | Evidence/<date>/manifest.md#PO-12 | |
| 13 | Maintenance change approvals | CAB records | Evidence/<date>/manifest.md#PO-13 | |
| 14 | Monthly report distribution | Email or portal posting | Evidence/<date>/manifest.md#PO-14 | |
| 15 | Auto-remediation log | Remediation run output | Evidence/<date>/manifest.md#PO-15 | |

## Multi-factor Authentication (MFA)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | VPN MFA enforcement | Connection log showing MFA | Evidence/<date>/manifest.md#MFA-01 | |
| 2 | Admin portal MFA | Sign-in log with MFA result | Evidence/<date>/manifest.md#MFA-02 | |
| 3 | Privileged account MFA | Adoption report | Evidence/<date>/manifest.md#MFA-03 | |
| 4 | SaaS MFA policy | IdP export | Evidence/<date>/manifest.md#MFA-04 | |
| 5 | Phishing-resistant MFA | FIDO2 attestation | Evidence/<date>/manifest.md#MFA-05 | |
| 6 | Risk-based access log | Risk event with step-up | Evidence/<date>/manifest.md#MFA-06 | |
| 7 | API/service principal controls | Token policy export | Evidence/<date>/manifest.md#MFA-07 | |
| 8 | Training completion | Attendance or LMS export | Evidence/<date>/manifest.md#MFA-08 | |
| 9 | Anomalous sign-in alerts | SIEM/IdP alert export | Evidence/<date>/manifest.md#MFA-09 | |
| 10 | Backup console MFA | Console log/screenshot | Evidence/<date>/manifest.md#MFA-10 | |
| 11 | Resilience test report | Token loss/recovery test | Evidence/<date>/manifest.md#MFA-11 | |
| 12 | Repo MFA proof | Git provider settings | Evidence/<date>/manifest.md#MFA-12 | |
| 13 | PAM MFA evidence | Elevation prompt logs | Evidence/<date>/manifest.md#MFA-13 | |
| 14 | Exception register | Unsupported system list | Evidence/<date>/manifest.md#MFA-14 | |
| 15 | Adoption dashboard | Metrics screenshot | Evidence/<date>/manifest.md#MFA-15 | |

## Regular Backups (RB)

| # | Evidence item | Proof details | Manifest link | Captured (Y/N) |
| --- | --- | --- | --- | --- |
| 1 | Scope register | Asset/data classification list | Evidence/<date>/manifest.md#RB-01 | |
| 2 | Daily backup logs | Job success/failure | Evidence/<date>/manifest.md#RB-02 | |
| 3 | Immutability proof | WORM/object-lock settings | Evidence/<date>/manifest.md#RB-03 | |
| 4 | Replication logs | Secondary/offline copy proof | Evidence/<date>/manifest.md#RB-04 | |
| 5 | Full restore report | RTO/RPO achieved | Evidence/<date>/manifest.md#RB-05 | |
| 6 | Ransomware detection alert | Alert screenshots/logs | Evidence/<date>/manifest.md#RB-06 | |
| 7 | Encryption/KMS logs | Key rotation evidence | Evidence/<date>/manifest.md#RB-07 | |
| 8 | Backup admin MFA | Console access log | Evidence/<date>/manifest.md#RB-09 | |
| 9 | Catalog integrity | Checksum or validation output | Evidence/<date>/manifest.md#RB-10 | |
| 10 | Reporting output | Dashboard/alert export | Evidence/<date>/manifest.md#RB-11 | |
| 11 | Scope review minutes | Quarterly review notes | Evidence/<date>/manifest.md#RB-12 | |
| 12 | Network segmentation proof | Firewall/ACLs and diagram | Evidence/<date>/manifest.md#RB-13 | |
| 13 | Backup version status | Software version report | Evidence/<date>/manifest.md#RB-14 | |
| 14 | Attack simulation report | Red team outcome | Evidence/<date>/manifest.md#RB-15 | |
| 15 | Offline copy inventory | Storage location and access log | Evidence/<date>/manifest.md#RB-16 | |

## Usage tips

- Mirror manifest IDs in notes to maintain traceability.
- Capture timestamps, hostnames, and tool versions for every artifact.
- Store screenshots as PNG with naming pattern `<date>-<control>-<description>.png`.
- Prefer structured exports (CSV/JSON) over screenshots when possible; include command lines used.
- When masking data, describe the masking method in the notes.

## Review cadence

- Weekly: confirm new evidence added to manifests and hashes recorded.
- Monthly: spot-check three random controls per strategy for freshness.
- Quarterly: full evidence review aligned with `Evidence/<date>/manifest.md` publication.
