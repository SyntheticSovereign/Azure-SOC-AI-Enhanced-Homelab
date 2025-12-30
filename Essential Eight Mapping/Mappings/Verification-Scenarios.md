# Essential Eight Verification Scenarios and Evidence Capture

Use these scenarios to validate control effectiveness. Each scenario includes steps, expected evidence, and cross-references to the control matrix.

## Application Control (AC) scenarios

1. **Block unsigned executable in user profile**
   - Deploy unsigned EXE to `%LOCALAPPDATA%` and attempt execution.
   - Expect block event logged in AppLocker/WDAC and SIEM (AC-02, AC-12).
   - Capture screenshot of block dialog and SIEM query.
2. **Validate publisher rule for signed vendor app**
   - Install signed vendor app in pilot ring.
   - Confirm allow via publisher rule without hash update (AC-03).
   - Capture policy assignment and execution logs.
3. **Installer control enforcement**
   - Attempt MSI install without approval.
   - Expect block and change request reference (AC-04).
   - Capture change ticket and event log.
4. **Integrity monitoring drift alert**
   - Modify allow list XML; verify alert and rollback (AC-07).
   - Capture SIEM alert, rollback log, and restored hash.
5. **Break-glass expiry validation**
   - Approve temporary allow list bypass with 24h expiry (AC-09).
   - Verify automatic expiry and log entries.
   - Capture SOP reference and SIEM search.
6. **Server vs workstation policy separation**
   - Confirm server assignment excludes workstation rules (AC-08).
   - Capture CM baseline mappings and scope definitions.
7. **EDR correlation for unsigned binary**
   - Trigger EDR alert for unknown EXE and verify linkage to allow list (AC-05).
   - Capture EDR alert, SIEM correlation, and ticket.
8. **CI/CD packaged app allow list update**
   - Release new signed package through CI; ensure allow list auto-updates (AC-15).
   - Capture pipeline logs and deployment status.
9. **Quarterly rule effectiveness review**
   - Aggregate block/allow telemetry and tune rules (AC-14).
   - Capture review minutes and metrics.
10. **Trusted path enforcement**
    - Attempt execution from untrusted path; confirm block (AC-02).
    - Capture log entry and user-facing prompt.
11. **User notification clarity**
    - Verify user message explains why execution blocked and where to request access (AC-01).
    - Capture screenshot and helpdesk knowledge article.
12. **Local hash rule for bespoke app**
    - Deploy bespoke app with hash rule; confirm execution allowed (AC-03).
    - Capture hash entry and validation output.
13. **Remote code execution attempt via script**
    - Run script from network share; ensure policy blocks (AC-02).
    - Capture event logs and SIEM alert.
14. **GPO/MDM policy integrity**
    - Validate policy hashes match expected (AC-06).
    - Capture CM report and hash file.
15. **Rollback success path**
    - Intentionally break allow list and trigger rollback (AC-07).
    - Capture before/after config and alert timeline.
16. **App allow list change approval workflow**
    - Submit request for new app; verify approvals documented (AC-11).
    - Capture approval record and deployment time.
17. **Privilege boundary test**
    - Attempt allow list bypass with local admin removed (AC-08, RAP-01).
    - Capture failure logs and SIEM alert.
18. **Reputation-based blocking**
    - Execute low-reputation binary; ensure block (AC-13).
    - Capture reputation feed update and block log.
19. **Telemetry retention review**
    - Confirm 180-day retention for block logs (AC-12).
    - Capture SIEM retention setting.
20. **Cross-platform parity**
    - Validate macOS and Windows parity for allow list scope (AC-06).
    - Capture Jamf/Intune assignments.

## Patch Applications (PA) scenarios

1. **Critical patch within 14 days validation**
   - Select critical CVE; verify deployment in ≤14 days (PA-03).
   - Capture compliance report and change ticket.
2. **Non-critical patch within 30 days validation**
   - Validate random non-critical patch deployed in ≤30 days (PA-04).
   - Capture report and exception notes.
3. **Ring deployment health check**
   - Canary ring patch, then broad deployment (PA-05).
   - Capture health metrics and rollback criteria.
4. **Rollback execution**
   - Simulate bad patch; execute rollback (PA-06).
   - Capture rollback log and post-validation.
5. **Risk board prioritization**
   - Show EPSS/CVSS sorting with business criticality (PA-07).
   - Capture board screenshot and decisions.
6. **Third-party source integrity**
   - Verify hash/signature of external package (PA-09).
   - Capture checksum output.
7. **SaaS release tracking**
   - Document SaaS change log review (PA-14).
   - Capture admin portal screenshot.
8. **Exception register accuracy**
   - Validate exceptions have expiry and compensating controls (PA-10).
   - Capture register entry.
9. **Compliance reporting automation**
   - Show SIEM/SOAR job generating compliance report (PA-08).
   - Capture playbook run log.
10. **Vulnerability scanner linkage**
    - Map scanner findings to patch IDs (PA-12).
    - Capture ticket linkage.
11. **Package manager mirror integrity**
    - Verify apt/yum mirror hash (PA-13).
    - Capture command output.
12. **User impact assessment**
    - Collect telemetry on user impact and adjust schedule (PA-12).
    - Capture survey/telemetry report.
13. **Advisory subscription validation**
    - Show vendor advisory subscription functioning (PA-02).
    - Capture email or webhook log.
14. **Inventory completeness check**
    - Verify CMDB/software inventory completeness (PA-01).
    - Capture inventory export.
15. **Quarterly effectiveness review**
    - Review SLA adherence trends (PA-15).
    - Capture meeting notes and KPIs.
16. **Virtual patching**
    - Apply compensating firewall/EDR rule when patch delayed (PA-11).
    - Capture rule and review date.
17. **Mac/Linux parity test**
    - Confirm patch cadence covers macOS/Linux (PA-05, PA-13).
    - Capture compliance report.
18. **Change control alignment**
    - Ensure change records reference patch KB/CVE (PA-03/04).
    - Capture change log entry.
19. **Notification to stakeholders**
    - Validate communication plan for high-risk patches (PA-07).
    - Capture email template.
20. **Metrics publication**
    - Publish patch metrics dashboard to stakeholders (PA-08).
    - Capture dashboard screenshot.

## Configure Office Macros (MO) scenarios

1. **Block macro from internet**
   - Download macro-enabled doc from internet; expect block (MO-01).
   - Capture block prompt and log.
2. **Block macro from email attachment**
   - Send macro-enabled doc via email; verify block (MO-02).
   - Capture mail gateway/quarantine log.
3. **Trusted publisher enforcement**
   - Run unsigned macro; expect block; sign macro and retest (MO-03).
   - Capture trust list and execution result.
4. **Trusted location restriction**
   - Attempt macro from untrusted location; expect block (MO-04).
   - Capture registry/MDM profile and log.
5. **Telemetry streaming**
   - Verify macro telemetry flows to SIEM (MO-05).
   - Capture SIEM query and alert.
6. **Publisher revocation**
   - Revoke compromised certificate; verify block (MO-06).
   - Capture CRL/OCSP settings and test log.
7. **High-risk group policy**
   - Apply stricter policy to finance; validate enforcement (MO-07).
   - Capture assignment scope and logs.
8. **Attestation workflow**
   - Run quarterly attestation of trusted publishers (MO-08).
   - Capture attestation record.
9. **User training prompt**
   - Ensure enablement prompt includes rationale (MO-09).
   - Capture screenshot of prompt text.
10. **Sandboxed macro execution**
    - Execute macro in sandbox; verify isolation (MO-10).
    - Capture isolation log.
11. **DLP integration**
    - Trigger macro attempting exfiltration; DLP block (MO-11).
    - Capture DLP incident.
12. **Automated testing pre-deployment**
    - Run macro policy test suite (MO-12).
    - Capture CI output.
13. **Network access alert**
    - Macro attempts network call; alert fired (MO-13).
    - Capture alert evidence.
14. **Template inventory accuracy**
    - Validate macro-enabled template inventory (MO-14).
    - Capture inventory list.
15. **Finance/legal exception review**
    - Review exceptions semi-annually (MO-15).
    - Capture meeting minutes.

## User Application Hardening (UAH) scenarios

1. **Disable legacy plug-ins validation**
   - Verify Flash/Java disabled in browsers (UAH-01).
   - Capture baseline profile export.
2. **Block executable download**
   - Attempt EXE download; expect block (UAH-02).
   - Capture browser prompt and log.
3. **Baseline deployment scope**
   - Confirm GPO/MDM baseline applied to all OUs (UAH-03).
   - Capture assignment list.
4. **Script/ad blocking enforcement**
   - Load site with heavy scripts; confirm block (UAH-04).
   - Capture extension policy and logs.
5. **Isolation for privileged users**
   - Launch privileged browser session; confirm isolation (UAH-05).
   - Capture isolation telemetry.
6. **Reputation enforcement**
   - Download low-reputation file; block event (UAH-06).
   - Capture SmartScreen log.
7. **Office add-in control**
   - Attempt to install untrusted add-in; block (UAH-07).
   - Capture add-in policy.
8. **Containerized risky file**
   - Open ISO in container; confirm isolation (UAH-08).
   - Capture container log.
9. **TLS inspection exemptions**
   - Validate exemptions logged and justified (UAH-09).
   - Capture exemption record.
10. **Messaging app restriction**
    - Block unapproved messaging app; verify (UAH-10).
    - Capture policy and block log.
11. **PDF hardening**
    - Test PDF with JavaScript; verify disabled (UAH-11).
    - Capture reader settings.
12. **Telemetry-driven tuning**
    - Review block telemetry and update policy (UAH-12).
    - Capture change record.
13. **File association enforcement**
    - Ensure risky file types open in hardened apps (UAH-13).
    - Capture file association policy.
14. **Threat intel feed application**
    - Add threat feed domain; verify block (UAH-14).
    - Capture update log.
15. **Monthly SOC review**
    - Hold tuning session; record actions (UAH-15).
    - Capture minutes and ticket IDs.

## Restrict Admin Privileges (RAP) scenarios

1. **Local admin removal validation**
   - Confirm standard users lack local admin (RAP-01).
   - Capture baseline compliance report.
2. **Privileged account inventory check**
   - Cross-check inventory vs directories (RAP-02).
   - Capture inventory export.
3. **Just-in-time elevation test**
   - Request elevation; ensure approval workflow (RAP-03).
   - Capture approval and elevation log.
4. **Session logging verification**
   - Perform admin session; verify SIEM logs (RAP-04).
   - Capture query output.
5. **MFA enforcement on privileged actions**
   - Attempt admin access without MFA; ensure denial (RAP-05).
   - Capture sign-in log.
6. **Session recording capture**
   - Perform admin task; verify recording saved (RAP-06).
   - Capture recording metadata.
7. **Break-glass account monitoring**
   - Use break-glass; ensure alert and expiry (RAP-07).
   - Capture alert log.
8. **Quarterly membership review**
   - Review privileged group memberships (RAP-08).
   - Capture review minutes.
9. **Automatic stale privilege removal**
   - Terminate user; verify privilege removal (RAP-09).
   - Capture IAM logs.
10. **PAM vault checkout**
    - Check out shared account; verify auditing (RAP-10).
    - Capture checkout log.
11. **Device posture enforcement**
    - Require compliant device for admin login (RAP-11).
    - Capture conditional access policy.
12. **Jump host requirement**
    - Attempt admin task off jump host; ensure denial (RAP-12).
    - Capture denial log.
13. **Cached credential disablement**
    - Validate cached credentials disabled (RAP-13).
    - Capture registry/policy proof.
14. **Privilege use analytics**
    - Review anomaly detection dashboard (RAP-14).
    - Capture dashboard.
15. **Separate admin identity test**
    - Attempt admin tasks with user identity; ensure block (RAP-15).
    - Capture SIEM alert.

## Patch Operating Systems (PO) scenarios

1. **Inventory completeness**
   - Validate OS inventory coverage (PO-01).
   - Capture CMDB export.
2. **Critical patch SLA on internet-facing hosts**
   - Verify deployment ≤14 days (PO-02).
   - Capture compliance report.
3. **30-day patch SLA for internal hosts**
   - Verify deployment ≤30 days (PO-03).
   - Capture report.
4. **Ring deployment validation**
   - Patch canary then production (PO-04).
   - Capture ring plan and health check.
5. **Compliance telemetry**
   - Show continuous compliance dashboard (PO-05).
   - Capture dashboard.
6. **Rollback automation**
   - Trigger rollback on failed update (PO-06).
   - Capture rollback log.
7. **Firmware update validation**
   - Apply firmware update with hash verification (PO-07).
   - Capture vendor log.
8. **EOL tracking**
   - Show EOL list and upgrade plans (PO-08).
   - Capture tracker.
9. **Remote device compliance**
   - Validate remote devices show compliant (PO-09).
   - Capture report.
10. **Patch channel hardening**
    - Confirm TLS and signing on channels (PO-10).
    - Capture config.
11. **MTTR measurement**
    - Calculate patch MTTR (PO-11).
    - Capture metrics.
12. **Vuln scan linkage**
    - Align vuln scan findings to patches (PO-12).
    - Capture linkage.
13. **Maintenance window enforcement**
    - Verify change approvals for maintenance (PO-13).
    - Capture CAB record.
14. **Monthly reporting**
    - Publish monthly patch report (PO-14).
    - Capture distribution.
15. **Auto-remediation**
    - Demonstrate auto-remediation for out-of-compliance host (PO-15).
    - Capture remediation log.

## Multi-factor Authentication (MFA) scenarios

1. **VPN MFA enforcement**
   - Attempt VPN login without MFA; ensure denial (MFA-01).
   - Capture VPN log and screenshot.
2. **Admin portal MFA enforcement**
   - Attempt admin portal login without MFA; ensure denial (MFA-02).
   - Capture portal log.
3. **Privileged account MFA coverage**
   - Sample admin accounts; verify MFA enforced (MFA-03).
   - Capture report.
4. **SaaS app MFA**
   - Validate SSO app requires MFA (MFA-04).
   - Capture IdP policy.
5. **Phishing-resistant factors**
   - Use FIDO2 for execs; confirm requirement (MFA-05).
   - Capture attestation log.
6. **Risk-based access**
   - Trigger risky sign-in; verify step-up MFA (MFA-06).
   - Capture risk event.
7. **API/service principal MFA equivalent**
   - Enforce token policies or workload identities (MFA-07).
   - Capture policy export.
8. **User education**
   - Conduct MFA fatigue training (MFA-08).
   - Capture attendance.
9. **Anomalous sign-in detection**
   - Review impossible travel alerts (MFA-09).
   - Capture SIEM alert.
10. **Backup console MFA**
    - Verify MFA on backup console (MFA-10).
    - Capture console screenshot.
11. **Resilience testing**
    - Simulate lost token; validate recovery (MFA-11).
    - Capture test plan.
12. **Code repository MFA**
    - Require MFA for Git provider (MFA-12).
    - Capture repo settings.
13. **PAM integration**
    - Verify MFA prompts during elevation (MFA-13).
    - Capture PAM log.
14. **Exception documentation**
    - Check exception log for unsupported systems (MFA-14).
    - Capture register entry.
15. **Adoption metrics**
    - Publish MFA adoption dashboard (MFA-15).
    - Capture dashboard.

## Regular Backups (RB) scenarios

1. **Scope validation**
   - Confirm all tiered systems in backup scope (RB-01).
   - Capture scope document.
2. **Daily backup confirmation**
   - Verify daily job success (RB-02).
   - Capture job log.
3. **Immutability enforcement**
   - Check object-lock/WORM setting (RB-03).
   - Capture storage policy.
4. **Secondary region replication**
   - Confirm replication to offsite (RB-04).
   - Capture replication log.
5. **Full restore test**
   - Perform restore; record RTO/RPO (RB-05).
   - Capture test report.
6. **Ransomware detection**
   - Trigger detection on backup data (RB-06).
   - Capture alert.
7. **Encryption and key rotation**
   - Validate encryption and key rotation (RB-07).
   - Capture KMS log.
8. **Admin access MFA**
   - Verify MFA on backup admin console (RB-09).
   - Capture login record.
9. **Catalog integrity**
   - Validate backup catalog integrity (RB-10).
   - Capture checksum report.
10. **Reporting automation**
    - Confirm automated reports and alerts (RB-11).
    - Capture dashboard.
11. **Scope review**
    - Review scope quarterly (RB-12).
    - Capture meeting notes.
12. **Network segmentation**
    - Validate isolated backup network (RB-13).
    - Capture firewall rules.
13. **Backup app version control**
    - Ensure backup software up to date (RB-14).
    - Capture version report.
14. **Attack simulation**
    - Simulate credential theft against backup platform (RB-15).
    - Capture red team finding.
15. **Offline copy validation**
    - Confirm existence of offline/air-gapped copy (RB-04 extension).
    - Capture inventory and access log.
