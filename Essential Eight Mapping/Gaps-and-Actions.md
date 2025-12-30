# Gaps and Actions (Essential Eight)

Use this register to track alignment status, evidence, and remediation. Link to supporting artifacts in `Uploads/`, `Notes/`, and dated `Evidence/` packs.

## How to use this register

1. Add rows for every identified gap, with explicit control IDs (AC/PA/MO/UAH/RAP/PO/MFA/RB).
2. Link to the manifest entry or curated note that proves the gap exists.
3. Define the desired maturity level and closure criteria.
4. Assign owners, due dates, and reviewers; update status as work progresses.

## Gap register

| ID | Control / Practice | Current state | Desired state | Evidence links | Owner | Target date | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GAP-001 | PA-03 (Critical app patching) | Patches applied within 30 days only | Critical patches not within 14 days | [Notes/patch-program-note.md](Notes/README.md) | IT Ops | 2025-02-15 | In progress | Testing expedited ring |
| GAP-002 | AC-07 (Allow list integrity) | Integrity monitoring disabled | Drift alerts and auto-rollback enabled | Evidence/2025-01-01/manifest.md#AC-07 | Endpoint Eng | 2025-03-01 | Not started | Waiting for SIEM rule |
| GAP-003 | MFA-05 (Phish-resistant MFA) | Only OTP MFA in place | FIDO2 keys for execs/admins | [Notes/mfa-uplift-note.md](Notes/README.md) | IAM | 2025-04-01 | In progress | Hardware key procurement |
| GAP-004 | RB-05 (Restore testing) | Partial restore test last quarter | Quarterly full restore with success criteria | Evidence/2025-01-01/manifest.md#RB-05 | DR Lead | 2025-02-28 | In progress | Awaiting maintenance window |
| GAP-005 | UAH-06 (Reputation enforcement) | SmartScreen disabled on legacy hosts | Enforce reputation-based blocking | Evidence/2025-01-01/manifest.md#UAH-06 | Desktop Eng | 2025-03-15 | Not started | Legacy OS constraint |
| GAP-006 | RAP-06 (Session recording) | PAM recording not configured | Enable recording on domain controllers | [Notes/pam-config-note.md](Notes/README.md) | IAM | 2025-02-20 | In progress | Vendor PS engagement |
| GAP-007 | MO-03 (Signed macros) | Unsigned macros allowed for finance | Signed macros only, trusted publishers enforced | Evidence/2025-01-01/manifest.md#MO-03 | Messaging | 2025-02-28 | In progress | Pilot underway |
| GAP-008 | PO-02 (Critical OS patching) | Servers patched in 30 days | Critical patches within 14 days | [Notes/patch-rings-note.md](Notes/README.md) | Server Ops | 2025-02-18 | In progress | Ring automation under test |
| GAP-009 | RB-13 (Backup network segmentation) | Shared network with production | Segmented network with firewall rules | Evidence/2025-01-01/manifest.md#RB-13 | Network | 2025-03-30 | Not started | Requires change window |
| GAP-010 | AC-09 (Emergency bypass) | No approvals/expiry | Break-glass with expiry and audit | [Notes/allowlist-change-note.md](Notes/README.md) | SecOps | 2025-02-25 | In progress | SOP drafting |

_Add more rows as gaps are identified. Use IDs consistently for traceability._

## Action items and validation steps

- [ ] **Action GAP-001**: Enable expedited patch ring for critical apps — **Owner**: IT Ops — **Due**: 2025-02-15 — **Validation**: Compliance report shows ≥95% critical patch adoption within 14 days.
- [ ] **Action GAP-002**: Deploy integrity monitor on allow lists — **Owner**: Endpoint Eng — **Due**: 2025-03-01 — **Validation**: SIEM rule firing on tamper events; rollback test logged in Evidence/2025-03-01.
- [ ] **Action GAP-003**: Issue FIDO2 keys to execs/admins — **Owner**: IAM — **Due**: 2025-04-01 — **Validation**: MFA report shows >98% compliant; SIEM risk alerts reduced.
- [ ] **Action GAP-004**: Conduct full restore test — **Owner**: DR Lead — **Due**: 2025-02-28 — **Validation**: Restore test report with RTO/RPO achieved; evidence logged in manifest.
- [ ] **Action GAP-005**: Enforce SmartScreen on legacy hosts — **Owner**: Desktop Eng — **Due**: 2025-03-15 — **Validation**: Policy status shows enabled; block events seen in SIEM.
- [ ] **Action GAP-006**: Enable PAM session recording — **Owner**: IAM — **Due**: 2025-02-20 — **Validation**: Recording files available; sample reviewed by SOC.
- [ ] **Action GAP-007**: Enforce signed macros for finance — **Owner**: Messaging — **Due**: 2025-02-28 — **Validation**: Trusted publishers list enforced; macro blocks reduced.
- [ ] **Action GAP-008**: Shorten server critical patch SLA to 14 days — **Owner**: Server Ops — **Due**: 2025-02-18 — **Validation**: Patch report meets SLA for two consecutive cycles.
- [ ] **Action GAP-009**: Isolate backup network — **Owner**: Network — **Due**: 2025-03-30 — **Validation**: Firewall rules deployed; penetration test validates isolation.
- [ ] **Action GAP-010**: Implement emergency bypass with expiry — **Owner**: SecOps — **Due**: 2025-02-25 — **Validation**: Break-glass SOP approved; audit log shows expirations enforced.

## Status definitions

- **Not started**: No work begun; owner assigned.
- **In progress**: Work underway; partial evidence captured.
- **Blocked**: Progress halted; specify blocker and target unblock date.
- **Complete**: Closure criteria met; evidence stored in dated manifest.

## Change management

- Update this register after every sprint review and audit walkthrough.
- When closing a gap, add the manifest link and date of validation.
- If an action is deferred, record the decision and next review date.

## Review cadence

- **Weekly**: Control owners update statuses and blockers.
- **Monthly**: Program manager reviews trends and escalates blockers.
- **Quarterly**: Alignment to evidence packs and major platform releases.

## Metrics to track

- Gap aging (days open per GAP ID)
- SLA adherence (patch, MFA enablement, backup restores)
- Evidence freshness (oldest evidence in manifest per control)
- Exception volume and expiry compliance
- Number of controls at M2 vs M3 per strategy

## Escalation

- Raise blockers to Program Manager and GRC Lead if due dates slip by >14 days.
- Flag high-risk items (e.g., MFA gaps on privileged accounts) for executive review.

## History

- 2025-02-01: Register expanded with 10 sample gaps and validation steps.
