# Essential Eight Control Matrix and Crosswalk

This matrix links each Essential Eight strategy to maturity levels (M0–M3) and aligns them with NIST CSF, ISO 27001, CIS v8, and PCI-DSS 4.0. Use it as the canonical reference when building curated notes, checklists, or evidence packs.

## How to use this matrix

- Start with the **Maturity Overview** section to see the intent of each level.
- Drill into the **Control Requirements** table per strategy for the authoritative control text and mapping references.
- Use the **Implementation Patterns** tables to pick controls by platform (Windows server, workstation, macOS, Linux, SaaS).
- Leverage **Evidence Suggestions** to decide which screenshots, exports, or configs to attach to manifests.
- Trace **Framework Crosswalks** when answering auditors that ask for CSF/ISO/CIS/PCI alignment.

## Maturity overview

| Strategy | M0 (Not implemented) | M1 (Partially aligned) | M2 (Mostly aligned) | M3 (Fully aligned/managed) |
| --- | --- | --- | --- | --- |
| Application Control | No allow/deny lists; unknown binaries execute. | Allow list for high-risk apps; pilot scope. | Publisher or hash-based rules applied to user devices; change control present. | Centralized allow lists with integrity monitoring, signed updates, and rapid rollback. |
| Patch Applications | Patching is ad hoc; no coverage tracking. | Patch cadence exists for critical apps; manual validation. | Automated deployment with compliance reporting within 14–30 days. | SLA-based patching with risk-based prioritization, exceptions, and continuous compliance reporting. |
| Configure Office Macros | Macros unrestricted. | Macros blocked from internet; trusted locations partially used. | Signed macros only; trusted publishers governed; threat intel filters. | Enforced signed macros with monitored trust stores and automated revocation. |
| User Application Hardening | Browser/plug-in defaults permissive. | Blocking of Flash/Java legacy components; partial URL filtering. | Standardized browser baselines, download restrictions, and isolation for high-risk content. | Adaptive controls with sandboxing, isolation containers, and telemetry-driven policy updates. |
| Restrict Admin Privileges | Users have standing admin rights. | Admin rights removed for most users; break-glass unmanaged. | Just-in-time elevation with approvals and logging. | Fully managed PAM with session recording, analytics, and rapid revocation. |
| Patch Operating Systems | OS patching is reactive. | Critical patches within 30 days for servers; workstations delayed. | Automated patching with staged rings, health checks, and rollback plans. | Continuous compliance with SLAs, live telemetry, and exception governance. |
| Multi-factor Authentication | MFA absent or optional. | MFA enforced for remote access only. | MFA for privileged accounts and administrative portals; device trust in scope. | MFA everywhere feasible with conditional access, phishing resistance, and monitored risk signals. |
| Regular Backups | Backups inconsistent; restores untested. | Daily backups of critical systems; ad hoc restore tests. | Immutable backups, replicated copies, and quarterly restore tests. | Tiered backups with isolation, ransomware detection, and monthly full-restore validation. |

## Control requirements by strategy

### Application Control (AC)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC-01 | M1 | Establish baseline allow/deny list for high-risk apps (e.g., unsigned executables). | PR.AC-1 | A.5.15, A.8.14 | 2.3, 10.1 | 2.2.5 | Allow list policy, initial AppLocker config, test screenshots |
| AC-02 | M1 | Block scripts from user writeable locations. | PR.PT-3 | A.8.28 | 10.3 | 2.2.5 | AppLocker path rules, audit logs showing blocks |
| AC-03 | M2 | Apply publisher-based rules for supported vendors; hash rules for bespoke apps. | PR.AC-3 | A.8.16 | 2.6, 2.7 | 6.3.2 | Rule set exports, change requests, sample validation logs |
| AC-04 | M2 | Enforce allow list for installers (.msi, .pkg) with change control. | PR.IP-1 | A.8.32 | 2.5 | 6.3.3 | Installer control policy, approvals, deployment ring notes |
| AC-05 | M2 | Integrate with EDR to alert on unsigned binaries. | DE.CM-7 | A.8.16 | 10.6 | 10.7.2 | EDR rule exports, alert screenshots, SIEM correlation |
| AC-06 | M3 | Centralize allow list via configuration management (Intune, Jamf, Puppet). | PR.DS-5 | A.5.36 | 4.5 | 2.5 | CM baseline files, assignment scopes, deployment status |
| AC-07 | M3 | Monitor integrity of allow list, alert on drift, and auto-rollback. | PR.IP-4 | A.5.30 | 4.6 | 2.5 | Integrity monitor reports, rollback logs |
| AC-08 | M3 | Apply differentiated policies for servers, workstations, and privileged hosts. | PR.AC-4 | A.8.1 | 4.4 | 7.2.5 | Policy matrix, assignment groups, server baselines |
| AC-09 | M3 | Establish emergency bypass with approvals, expiry, and audit trail. | ID.AM-6 | A.5.44 | 5.2 | 7.2.5 | Break-glass SOP, approval tickets, SIEM session logs |
| AC-10 | M2 | Validate allow list after each major application update. | PR.IP-2 | A.8.32 | 4.5 | 6.3.3 | Change record, validation checklist, signed approvals |
| AC-11 | M1 | Document exception handling and review cadence. | ID.GV-3 | A.5.1 | 2.6 | 6.3.3 | Exception register, approval matrix |
| AC-12 | M2 | Log blocked executions to SIEM; retain 90–180 days. | DE.AE-3 | A.8.16 | 8.2 | 10.7.2 | SIEM queries, retention settings |
| AC-13 | M3 | Apply reputation-based rules (catalog reputation, code signing CA trust). | PR.AC-6 | A.5.20 | 2.7 | 6.4.2 | Reputation policy, CA trust list, telemetry snapshots |
| AC-14 | M3 | Conduct quarterly rule effectiveness review using block/allow telemetry. | PR.IP-6 | A.5.18 | 3.4 | 12.10.4 | Review minutes, metrics dashboard |
| AC-15 | M3 | Integrate allow list changes with CI/CD for packaged apps. | PR.DS-6 | A.8.28 | 4.7 | 6.3.4 | Pipeline config, signed packages, approval logs |

### Patch Applications (PA)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PA-01 | M1 | Inventory applications with vendor/version metadata. | ID.AM-1 | A.5.9 | 1.1 | 2.3.1 | Inventory export, CMDB snapshot |
| PA-02 | M1 | Track vendor advisories and CVEs for in-scope software. | ID.RA-3 | A.8.7 | 7.1 | 6.3.1 | Advisory subscriptions, triage board |
| PA-03 | M2 | Apply critical security updates within 14 days. | PR.IP-12 | A.8.8 | 7.3 | 6.3.3 | Patch deployment reports, SLA definitions |
| PA-04 | M2 | Apply other security updates within 30 days. | PR.IP-12 | A.8.8 | 7.3 | 6.3.3 | Compliance dashboards, exception list |
| PA-05 | M2 | Use automated deployment tools with staging (rings). | PR.MA-1 | A.5.36 | 7.4 | 6.3.4 | Deployment profiles, ring definitions |
| PA-06 | M3 | Implement rollback and health-check logic per update. | PR.MA-1 | A.5.28 | 7.5 | 6.3.3 | Rollback SOP, health check monitors |
| PA-07 | M3 | Risk-based prioritization using CVSS/EPSS and asset criticality. | ID.RA-1 | A.8.6 | 7.2 | 12.5.2 | Risk model, prioritization board |
| PA-08 | M3 | Continuous compliance reporting with SIEM/SOAR integration. | DE.CM-8 | A.5.30 | 2.3 | 10.7.2 | SOAR playbook, SIEM dashboards |
| PA-09 | M2 | Validate third-party patch sources with integrity checks. | PR.DS-6 | A.8.28 | 7.7 | 6.3.2 | Hash validation logs, vendor signatures |
| PA-10 | M1 | Document exception handling with expiry and approvals. | ID.GV-3 | A.5.1 | 7.3 | 6.3.3 | Exception log, approvals |
| PA-11 | M3 | Apply virtual patching/mitigations when full patching is delayed. | RS.MI-3 | A.8.16 | 7.1 | 12.10.4 | Compensating control record, firewall/EDR rules |
| PA-12 | M3 | Measure user impact via telemetry and adjust schedules. | PR.PT-1 | A.8.33 | 7.6 | 6.3.5 | User impact report, deployment metrics |
| PA-13 | M2 | Ensure package managers mirror integrity (apt/yum/npm). | PR.DS-6 | A.8.28 | 7.7 | 6.3.2 | Mirror configs, hash checks |
| PA-14 | M2 | Include SaaS app updates in inventory and cadence. | ID.AM-5 | A.5.29 | 15.1 | 12.3.3 | SaaS change logs, admin center reports |
| PA-15 | M3 | Quarterly patch cadence effectiveness review. | PR.IP-10 | A.5.18 | 7.6 | 12.10.4 | Review minutes, KPIs |

### Configure Office Macros (MO)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MO-01 | M1 | Block macros from the internet zone. | PR.DS-5 | A.8.30 | 10.6 | 2.2.5 | GPO/Intune settings, test screenshots |
| MO-02 | M1 | Disable macros in files from email and untrusted sources. | PR.AC-1 | A.8.30 | 10.6 | 2.2.5 | Mail gateway policy, client screenshots |
| MO-03 | M2 | Allow only signed macros from trusted publishers. | PR.AC-3 | A.8.16 | 10.7 | 6.4.2 | Trusted publisher list, CA chain |
| MO-04 | M2 | Define trusted locations with restricted write access. | PR.AC-4 | A.8.32 | 10.6 | 2.2.5 | Trusted location registry/policy exports |
| MO-05 | M2 | Monitor macro execution telemetry and block suspicious behavior. | DE.CM-7 | A.8.16 | 10.6 | 10.7.2 | SIEM queries, EDR detections |
| MO-06 | M3 | Automate revocation of compromised publishers. | PR.IP-4 | A.8.28 | 10.7 | 12.10.4 | Revocation SOP, CRL/OCSP config |
| MO-07 | M3 | Apply differentiated macro policy for high-risk users (finance, execs). | PR.AC-4 | A.5.36 | 10.6 | 7.2.5 | Assignment groups, policy matrix |
| MO-08 | M3 | Quarterly attestation of macro trust stores. | PR.IP-11 | A.5.19 | 10.7 | 12.10.4 | Attestation records, screenshots |
| MO-09 | M1 | Educate users on macro risks; require justification for enablement. | PR.AT-1 | A.6.3 | 14.7 | 12.6.1 | Training records, enablement prompts |
| MO-10 | M2 | Configure sandbox or isolation for unknown macro sources. | PR.PT-5 | A.8.12 | 10.6 | 13.1 | Isolation policy, sandbox logs |
| MO-11 | M3 | Integrate macro controls with DLP to prevent exfiltration. | PR.DS-1 | A.8.12 | 10.7 | 3.4.2 | DLP rules, incident tickets |
| MO-12 | M3 | Automated testing of macro policies before deployment. | PR.IP-3 | A.8.28 | 10.6 | 6.3.4 | Test plan, CI job output |
| MO-13 | M2 | Alert when macros attempt network access or file writes outside trusted locations. | DE.AE-2 | A.8.16 | 10.6 | 10.7.2 | Alert rules, blocked event logs |
| MO-14 | M1 | Maintain inventory of macro-enabled templates. | ID.AM-1 | A.8.9 | 10.6 | 2.3.1 | Template inventory, repository snapshot |
| MO-15 | M3 | Semi-annual review with finance and legal for exceptions. | ID.GV-2 | A.5.24 | 10.6 | 7.3 | Review minutes, approvals |

### User Application Hardening (UAH)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UAH-01 | M1 | Disable unnecessary plug-ins (Flash, Java, Silverlight). | PR.PT-3 | A.8.32 | 10.6 | 4.6 | Browser baseline, config export |
| UAH-02 | M1 | Enforce safe file handling (block executable downloads). | PR.PT-4 | A.8.12 | 10.6 | 4.7 | Browser policy, download block proof |
| UAH-03 | M2 | Standardize browser baselines via MDM/Group Policy. | PR.AC-5 | A.8.32 | 10.6 | 4.3 | Baseline profiles, assignment scope |
| UAH-04 | M2 | Enable script and ad blocking for high-risk sites. | PR.PT-4 | A.8.12 | 10.6 | 4.7 | Extension allow list, policy exports |
| UAH-05 | M2 | Isolate browser sessions for privileged users. | PR.AC-4 | A.8.1 | 10.6 | 7.2.5 | Isolation config, session logs |
| UAH-06 | M3 | Enforce download reputation/smart-screen equivalents. | DE.CM-7 | A.8.16 | 10.6 | 4.4 | Reputation settings, alert logs |
| UAH-07 | M3 | Block Office add-ins from untrusted sources. | PR.AC-6 | A.8.30 | 10.6 | 4.6 | Add-in allow list, audit logs |
| UAH-08 | M3 | Containerize risky file types (ISO, VHD, MSI) with virtualization. | PR.DS-5 | A.8.32 | 10.6 | 13.1 | Container policy, isolation logs |
| UAH-09 | M2 | Enforce TLS inspection exemptions with justification. | PR.DS-2 | A.8.24 | 8.1 | 4.6 | Exemption registry, approvals |
| UAH-10 | M1 | Restrict local messaging apps that bypass DLP. | PR.DS-1 | A.8.12 | 10.6 | 3.4.2 | Block list, MDM profile |
| UAH-11 | M2 | Harden PDF readers (disable JavaScript, disable embedded files). | PR.PT-3 | A.8.32 | 10.6 | 4.7 | Reader config, policy export |
| UAH-12 | M3 | Telemetry-driven policy updates based on blocked events. | PR.IP-7 | A.5.31 | 10.7 | 10.7.2 | Telemetry dashboard, change records |
| UAH-13 | M2 | Enforce file type associations to hardened apps. | PR.DS-5 | A.8.32 | 10.6 | 4.7 | File association policy, validation evidence |
| UAH-14 | M3 | Continuous threat intel feeds drive dynamic URL/domain blocks. | DE.CM-6 | A.5.7 | 10.6 | 5.1 | Feed configs, blocked domain reports |
| UAH-15 | M3 | Monthly review of blocked events with SOC to tune controls. | ID.GV-2 | A.5.18 | 10.7 | 12.10.4 | Review minutes, tuning backlog |

### Restrict Admin Privileges (RAP)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RAP-01 | M1 | Remove local admin rights for standard users. | PR.AC-6 | A.5.18 | 5.4 | 7.2.5 | MDM/GPO baseline, exception list |
| RAP-02 | M1 | Maintain inventory of privileged accounts and groups. | ID.AM-3 | A.5.9 | 5.2 | 5.5 | Privileged account list, CMDB link |
| RAP-03 | M2 | Use just-in-time elevation with approval workflow. | PR.AC-4 | A.5.39 | 5.4 | 6.5 | JIT tool config, approval tickets |
| RAP-04 | M2 | Log all admin sessions to SIEM with session metadata. | DE.CM-3 | A.8.16 | 8.2 | 10.7.2 | SIEM queries, sample logs |
| RAP-05 | M3 | Enforce MFA on all privileged access. | PR.AC-7 | A.5.17 | 6.3 | 8.4.2 | Conditional Access policy, MFA reports |
| RAP-06 | M3 | Session recording for high-risk systems (domain controllers, production DB). | DE.CM-7 | A.8.16 | 8.2 | 10.7.2 | Session recording outputs, approvals |
| RAP-07 | M2 | Break-glass accounts with time-bound access and monitoring. | PR.AC-4 | A.5.44 | 5.4 | 7.2.5 | Break-glass SOP, alert rules |
| RAP-08 | M1 | Quarterly review of privileged groups membership. | PR.IP-11 | A.5.19 | 5.2 | 12.10.4 | Review records, approvals |
| RAP-09 | M3 | Automate removal of stale privileges via identity lifecycle. | PR.AC-1 | A.8.16 | 6.1 | 7.2.2 | Identity sync configs, revocation logs |
| RAP-10 | M2 | Enforce PAM for shared accounts with vaulting. | PR.AC-5 | A.5.39 | 5.5 | 8.3.5 | Vault config, checkout logs |
| RAP-11 | M3 | Risk-based access with device posture checks. | PR.AC-7 | A.5.36 | 5.4 | 6.3 | Conditional policies, device compliance |
| RAP-12 | M2 | Require privileged tasks to occur on hardened jump hosts. | PR.PT-5 | A.8.1 | 5.4 | 7.2.5 | Jump host baseline, access controls |
| RAP-13 | M2 | Disable cached credentials on privileged hosts. | PR.AC-5 | A.8.32 | 5.4 | 8.2.8 | Registry/policy exports |
| RAP-14 | M3 | Analytics on privilege use with anomaly detection. | DE.AE-3 | A.5.7 | 8.2 | 10.7.2 | SIEM dashboards, tuning notes |
| RAP-15 | M1 | Separate admin and user identities (no dual-use). | PR.AC-1 | A.5.15 | 5.4 | 6.3 | Identity inventory, policy statement |

### Patch Operating Systems (PO)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PO-01 | M1 | Maintain OS inventory with lifecycle status. | ID.AM-1 | A.5.9 | 1.1 | 2.3.1 | Inventory export, lifecycle tags |
| PO-02 | M1 | Apply critical OS patches within 14 days for internet-facing assets. | PR.IP-12 | A.8.8 | 7.3 | 6.3.3 | Patch reports, SLA doc |
| PO-03 | M2 | Apply all OS patches within 30 days for internal assets. | PR.IP-12 | A.8.8 | 7.3 | 6.3.3 | Compliance report, exception list |
| PO-04 | M2 | Use deployment rings with pre-prod validation. | PR.MA-1 | A.5.36 | 7.4 | 6.3.4 | Ring definitions, test logs |
| PO-05 | M3 | Real-time posture via MDM/CM tools with enforcement. | DE.CM-8 | A.5.30 | 2.3 | 10.7.2 | Compliance dashboard, enforcement logs |
| PO-06 | M3 | Automated rollback for failed updates with alerts. | PR.IP-10 | A.8.8 | 7.5 | 6.3.3 | Rollback logs, alert rules |
| PO-07 | M2 | Validate kernel/firmware updates where supported. | PR.DS-6 | A.8.28 | 7.7 | 6.3.2 | Firmware update logs, vendor advisories |
| PO-08 | M1 | Track EOL/ESU status and plan upgrades. | ID.BE-5 | A.5.9 | 1.1 | 6.3.1 | EOL tracker, project plan |
| PO-09 | M3 | Continuous compliance for remote and roaming devices. | PR.AC-4 | A.5.36 | 7.6 | 12.3.3 | Device compliance reports |
| PO-10 | M2 | Harden patch channels (WSUS/SCCM/Intune/Jamf) with integrity checks. | PR.DS-6 | A.8.28 | 7.7 | 6.3.2 | Channel config, TLS settings |
| PO-11 | M3 | Measure MTTR for critical patches and track trends. | ID.RA-6 | A.5.20 | 7.6 | 12.10.4 | Metrics dashboard, trend reports |
| PO-12 | M2 | Integrate patching with vulnerability findings. | ID.RA-3 | A.8.8 | 7.1 | 6.3.1 | Vuln scanner exports, ticket links |
| PO-13 | M3 | Enforce maintenance windows with business approvals. | PR.IP-1 | A.5.19 | 7.5 | 6.3.3 | Change records, approvals |
| PO-14 | M1 | Monthly reporting on patch status by business unit. | PR.MA-1 | A.5.18 | 7.6 | 12.10.4 | Monthly report, distribution list |
| PO-15 | M3 | Automated remediation for out-of-compliance hosts. | PR.PT-5 | A.8.32 | 7.6 | 6.3.5 | Auto-remediation rules, logs |

### Multi-factor Authentication (MFA)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MFA-01 | M1 | Enforce MFA for remote access (VPN, VDI). | PR.AC-7 | A.5.17 | 6.3 | 8.4.2 | VPN config, MFA logs |
| MFA-02 | M1 | Enforce MFA for administrative portals. | PR.AC-7 | A.5.17 | 6.3 | 8.4.2 | Portal settings, test screenshots |
| MFA-03 | M2 | Require MFA for privileged accounts across all systems. | PR.AC-6 | A.5.39 | 6.3 | 8.4.2 | Conditional access, PAM integration |
| MFA-04 | M2 | Enforce MFA for cloud SaaS and federated apps. | PR.AC-7 | A.5.17 | 6.3 | 8.4.2 | IdP policy exports, sign-in logs |
| MFA-05 | M3 | Phishing-resistant MFA for high-risk roles. | PR.AC-7 | A.5.17 | 6.3 | 8.4.2 | FIDO2 config, attestation reports |
| MFA-06 | M3 | Risk-based conditional access integrating device posture. | PR.AC-4 | A.5.36 | 6.3 | 8.4.2 | Risk policy, device compliance |
| MFA-07 | M2 | Enforce MFA for APIs/automation via service principals. | PR.AC-1 | A.5.39 | 6.3 | 8.4.2 | Token policy, credential audit |
| MFA-08 | M1 | Educate users on MFA fatigue and social engineering. | PR.AT-1 | A.6.3 | 14.7 | 12.6.1 | Training materials, phishing drills |
| MFA-09 | M3 | Alert on anomalous sign-ins and impossible travel. | DE.AE-3 | A.5.7 | 8.2 | 10.7.2 | SIEM alerts, risk events |
| MFA-10 | M2 | Enforce MFA for backup/DR consoles. | PR.AC-4 | A.5.15 | 6.3 | 8.4.2 | Backup console policy, screenshots |
| MFA-11 | M3 | Quarterly resilience tests (token loss, revocation). | PR.IP-10 | A.5.18 | 6.3 | 12.10.4 | Test plan, results |
| MFA-12 | M2 | Require MFA for code repositories and CI/CD. | PR.AC-6 | A.5.39 | 6.3 | 8.4.2 | Repo settings, audit logs |
| MFA-13 | M3 | Integrate MFA with PAM for elevation workflows. | PR.AC-4 | A.5.39 | 6.3 | 8.4.2 | PAM workflow screenshots |
| MFA-14 | M1 | Document exception process for unsupported systems. | ID.GV-3 | A.5.1 | 6.3 | 8.2.8 | Exception register |
| MFA-15 | M3 | Monitor MFA adoption metrics and user friction. | PR.IP-7 | A.5.31 | 6.3 | 12.10.4 | Adoption dashboard, tuning notes |

### Regular Backups (RB)

| ID | Maturity | Control requirement | NIST CSF | ISO 27001 | CIS v8 | PCI-DSS 4.0 | Evidence suggestions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RB-01 | M1 | Identify critical systems and data for backup scope. | ID.BE-5 | A.5.9 | 11.1 | 10.5.1 | Asset list, data classification |
| RB-02 | M1 | Perform daily backups of critical systems. | PR.IP-4 | A.8.13 | 11.2 | 10.5.1 | Backup job configs, logs |
| RB-03 | M2 | Retain backups with immutable storage (WORM/snapshots). | PR.DS-5 | A.8.12 | 11.3 | 10.5.1 | Storage policy, immutability config |
| RB-04 | M2 | Replicate backups to secondary region/offline vault. | PR.IP-4 | A.8.13 | 11.3 | 10.5.1 | Replication config, topology diagram |
| RB-05 | M3 | Quarterly full restore tests with success criteria. | PR.IP-9 | A.8.15 | 11.4 | 12.10.4 | Test results, sign-offs |
| RB-06 | M3 | Ransomware detection on backup data and pipelines. | DE.CM-7 | A.8.16 | 11.3 | 10.7.2 | Detection alerts, tuning notes |
| RB-07 | M2 | Backup encryption in transit and at rest with key rotation. | PR.DS-2 | A.8.25 | 11.3 | 3.6.6 | Key rotation logs, KMS policy |
| RB-08 | M1 | Document backup RPO/RTO and map to business tiers. | ID.BE-4 | A.5.20 | 11.1 | 12.10.1 | RPO/RTO matrix, approvals |
| RB-09 | M2 | Protect backup admin access with MFA and least privilege. | PR.AC-6 | A.5.36 | 6.3 | 8.4.2 | Access policy, audit logs |
| RB-10 | M3 | Immutable backup catalogs with chain-of-custody. | PR.DS-5 | A.5.25 | 11.3 | 10.5.1 | Catalog exports, integrity checks |
| RB-11 | M2 | Automated reporting on backup success/failure. | DE.CM-5 | A.5.30 | 11.3 | 12.10.4 | Reports, alert routing |
| RB-12 | M1 | Quarterly review of backup scope vs new systems. | ID.AM-5 | A.5.19 | 11.1 | 12.10.4 | Review notes, updated scope |
| RB-13 | M3 | Segmented backup network with firewall rules and monitoring. | PR.AC-5 | A.8.1 | 11.3 | 1.3.7 | Network diagram, firewall rules |
| RB-14 | M2 | Validate backup application versions and patches. | PR.IP-12 | A.8.8 | 11.3 | 6.3.3 | Version inventory, patch logs |
| RB-15 | M3 | Simulate attack scenarios (credential theft, ransomware) against backup stack. | RS.IM-1 | A.5.30 | 11.4 | 12.10.4 | Test plans, red team findings |

## Implementation patterns (platform-specific)

### Windows workstations
- Enforce AppLocker or WDAC allow lists with publisher rules for standard apps.
- Deploy patch rings via Intune/ConfigMgr with 7/14/30-day cadence.
- Block Office macros from the internet; allow only signed macros for finance.
- Harden browsers with SmartScreen and isolation for admin accounts.
- Remove local admin rights; JIT via LAPS and PIM.
- Use Windows Update for Business telemetry for continuous compliance.
- Require MFA for Azure AD sign-ins and VPN.
- Configure OneDrive/SharePoint versioning plus VSS and offline backup copies.

### Windows servers
- WDAC/AppLocker allow lists enforced on critical servers with exception workflows.
- WSUS/ConfigMgr rings with pre-prod servers; maintenance windows documented.
- Macro usage minimal; block by default on jump hosts.
- Privileged access via PAM/jump boxes with session recording.
- Backup agents with immutable snapshots and offsite replication.

### macOS
- Use SwiftDialog/MDM scripts to enforce allow lists and notarized apps.
- Munki/Jamf patch policies with deferrals and health checks.
- Disable unsigned Office macros; trusted publisher list managed via profiles.
- Harden Safari/Chrome with download controls and certificate pinning where possible.
- Enforce admin separation; require device compliance for elevation.
- Time Machine to encrypted volumes plus immutable snapshot replication.

### Linux
- Utilize package allow lists and signed repositories; monitor execve blocks.
- Patch via apt/yum/zypper automation with canary hosts and rollbacks.
- Disable LibreOffice macros from untrusted sources; enforce signed extensions.
- Harden browsers and disable risky plugins for Linux desktops.
- sudoers tightly scoped; PAM with MFA for privileged actions.
- rsync/borg/restic backups with append-only or object-lock storage.

### SaaS and cloud services
- Treat SaaS add-ins/extensions as application control; enforce allow lists.
- Use vendor change logs and service health for patch cadence tracking.
- Enforce MFA/conditional access across all federated apps.
- Export configuration backups and audit logs to immutable storage.

## Evidence suggestions by strategy

- **Application Control**: AppLocker/WDAC policy exports, Intune assignment reports, SIEM blocked events, change approvals.
- **Patch Applications**: Deployment status reports, vulnerability scanner linkage, exception registers, rollback tests.
- **Configure Office Macros**: GPO/MDM settings, trusted publisher lists, macro execution logs, revocation events.
- **User Application Hardening**: Browser baseline profiles, extension allow lists, isolation policy configs, blocked download reports.
- **Restrict Admin Privileges**: Privileged account inventories, JIT/PAM session logs, jump host baselines, MFA enforcement logs.
- **Patch Operating Systems**: Compliance dashboards, ring definitions, health check outputs, EOL/EUS planning records.
- **Multi-factor Authentication**: Conditional access exports, MFA adoption metrics, anomalous sign-in alerts, resilience test reports.
- **Regular Backups**: Backup job history, restore test results, immutability settings, ransomware detection alerts, access controls.

## Cross-framework alignment detail

| Strategy | Key safeguards (CIS v8) | ISO 27001 Annex A references | NIST CSF functions | PCI-DSS 4.0 anchors |
| --- | --- | --- | --- | --- |
| Application Control | 2.3, 2.6, 4.5, 10.1 | A.5.15, A.8.14, A.8.28 | PR.AC, PR.DS, DE.CM | 2.2.5, 6.3.2, 10.7.2 |
| Patch Applications | 7.1, 7.3, 7.5 | A.8.8, A.5.30 | ID.RA, PR.IP, DE.CM | 6.3.3, 6.3.4, 12.10.4 |
| Configure Office Macros | 10.6, 10.7 | A.8.30, A.8.16 | PR.AC, PR.DS, DE.CM | 2.2.5, 10.7.2 |
| User Application Hardening | 4.3, 4.6, 4.7 | A.8.12, A.8.32 | PR.PT, PR.AC | 4.7, 5.1 |
| Restrict Admin Privileges | 5.2, 5.4, 6.5 | A.5.18, A.5.39 | PR.AC, DE.CM | 7.2.2, 8.4.2 |
| Patch Operating Systems | 7.2, 7.4, 7.6 | A.8.8, A.5.36 | ID.AM, PR.IP, DE.CM | 6.3.3, 6.3.4 |
| Multi-factor Authentication | 6.3, 6.7 | A.5.17, A.5.39 | PR.AC, DE.CM | 8.3.5, 8.4.2 |
| Regular Backups | 11.1, 11.3 | A.8.13, A.8.15 | PR.IP, RC | 10.5.1, 12.10.4 |

## Change log

- 2025-01-01: Initial matrix published with cross-framework mappings.
- 2025-02-01: Added SaaS/cloud implementation patterns and evidence suggestions.
- 2025-03-01: Expanded control requirements to 15 controls per strategy and added NIST/ISO/CIS/PCI alignment fields.
