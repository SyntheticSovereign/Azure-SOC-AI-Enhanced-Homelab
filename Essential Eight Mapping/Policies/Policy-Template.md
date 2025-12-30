# Essential Eight Policy and Standard Template

Use this template to publish or update policies aligned to Essential Eight controls. Each policy should cite the relevant control IDs and provide enforceable statements, roles, and exceptions.

## Document metadata

- **Title**: <Policy title>
- **Version**: <vX.Y>
- **Owner**: <Team/Role>
- **Approver**: <GRC Lead / CISO>
- **Effective date**: <YYYY-MM-DD>
- **Review date**: <YYYY-MM-DD>
- **Scope**: <Systems, users, environments>
- **Related controls**: <AC/PA/MO/UAH/RAP/PO/MFA/RB IDs>

## Purpose

State why this policy exists and how it supports Essential Eight objectives (e.g., mitigating malware, ensuring rapid patching, enforcing least privilege).

## Policy statements (examples)

### Application Control
- Approved software must be enforced via allow lists for workstations and servers (AC-01, AC-03, AC-06).
- Emergency bypasses require documented approvals, expiry, and SIEM logging (AC-09).

### Patch Management
- Critical application and OS patches must be deployed within 14 days; all other security patches within 30 days (PA-03, PA-04, PO-02, PO-03).
- Deployment rings and rollback procedures are mandatory for all production platforms (PA-05, PO-04).

### Office Macros
- Macros from the internet or email are blocked by default; only signed macros from trusted publishers are permitted (MO-01, MO-03).
- Trusted locations must be read-only for standard users (MO-04).

### User Application Hardening
- Browsers must enforce download reputation and block untrusted add-ins; legacy plug-ins are disabled (UAH-02, UAH-06, UAH-07).
- High-risk file types must execute in containers or isolation environments (UAH-08).

### Restrict Admin Privileges
- Standard users are not granted local admin rights; privileged access uses JIT workflows and MFA (RAP-01, RAP-03, RAP-05).
- Admin activities must be logged to SIEM with session metadata and recording where feasible (RAP-04, RAP-06).

### Patch Operating Systems
- All managed operating systems must be enrolled in centralized patching with compliance reporting (PO-03, PO-05).
- EOL/EUS systems require documented upgrade plans and compensating controls if still in use (PO-08).

### Multi-factor Authentication
- MFA is mandatory for remote access, admin portals, privileged accounts, and SaaS applications (MFA-01 to MFA-04).
- Phishing-resistant factors are required for executives and administrators (MFA-05).

### Regular Backups
- Critical systems must be backed up daily with immutability, offsite copies, and quarterly restore tests (RB-02, RB-03, RB-04, RB-05).
- Backup admin access must be protected by MFA and least privilege (RB-09).

## Roles and responsibilities

| Role | Responsibilities |
| --- | --- |
| Policy Owner | Maintains policy text, coordinates reviews, and publishes updates. |
| Control Owner | Implements controls, maintains evidence, and reports exceptions. |
| Evidence Librarian | Maintains manifests and ensures evidence immutability. |
| GRC Lead | Approves policy updates, validates alignment to frameworks, and manages exceptions. |
| SOC | Monitors control telemetry and reports deviations. |
| System Owners | Ensure systems comply with the policy and participate in testing. |

## Standards and procedures

Document the enforceable configurations, scripts, and procedures that implement the policy statements. Reference checklists and manifests for evidence.

- **Configuration standards**: e.g., AppLocker XML, Intune profiles, WSUS ring definitions, PAM workflows.
- **Operational procedures**: e.g., change management steps, emergency bypass approvals, restore testing steps.
- **Monitoring standards**: e.g., SIEM queries, alert routing, health checks, dashboards.

## Exceptions

- Describe how to request an exception, required compensating controls, expiry dates, and approval authority.
- Maintain an exception register linking to `Gaps-and-Actions.md` and evidence packs.

## Compliance and auditing

- Reference `Mappings/Essential8-Control-Matrix.md` for framework crosswalks.
- Align evidence to dated manifests under `Evidence/`.
- Specify attestation cadence (e.g., quarterly for macro controls, monthly for MFA adoption).

## Review and approval

- **Drafted by**: <Name/Role> on <date>
- **Reviewed by**: <Roles> on <date>
- **Approved by**: <Name/Role> on <date>
- **Revision history**: <Table of changes>

## Revision history

| Version | Date | Description | Author | Approver |
| --- | --- | --- | --- | --- |
| v1.0 | 2025-02-01 | Initial publication aligned to Essential Eight controls. | <Name> | <Approver> |
| v1.1 | 2025-02-15 | Added phishing-resistant MFA requirement for admins. | <Name> | <Approver> |
| v1.2 | 2025-03-01 | Updated restore testing cadence. | <Name> | <Approver> |

## Related documents

- `Checklists/Implementation-Checklist.md`
- `Mappings/Essential8-Control-Matrix.md`
- `Gaps-and-Actions.md`
- `Evidence/<date>/manifest.md`

## Distribution

List where this policy is published (wiki, PDF, onboarding portal) and how staff are notified of changes (email, change advisory board, security champions).
