# Evidence Playbook and Command Guide

Use this playbook to capture consistent evidence for Essential Eight controls. Include command outputs, screenshots, and metadata (timestamp, hostname, user, tool version).

## General guidance

- Run commands with least privilege; avoid modifying state while collecting evidence.
- Save raw command output as `.txt` or `.log` files with hashes.
- For screenshots, include the full window and clock; avoid cropping out hostnames.
- Record the command used, tool version, and filters applied.

## Application Control commands

1. **List AppLocker effective rules (Windows)**
   - Command: `Get-AppLockerPolicy -Effective | ConvertTo-Xml -As String > applocker-effective.xml`
   - Evidence: `applocker-effective.xml` (hash + manifest entry AC-01/AC-03)
2. **Check WDAC policy state (Windows)**
   - Command: `Get-CIPolicy -PolicyPath "C:\\Windows\\System32\\CodeIntegrity\\SiPolicy.p7b"`
   - Evidence: command output, file hash of `SiPolicy.p7b` (AC-06)
3. **Verify block event in Event Log**
   - Command: `Get-WinEvent -LogName "Microsoft-Windows-AppLocker/EXE and DLL" -MaxEvents 5`
   - Evidence: log export showing block (AC-02, AC-12)
4. **Check Jamf allow list profile (macOS)**
   - Command: `profiles show -type configuration | grep -A3 "Application Control"`
   - Evidence: profile snippet (AC-06)
5. **Hash bespoke binary**
   - Command: `shasum -a 256 <file>`
   - Evidence: hash captured for AC-03 bespoke rules

## Patch Applications commands

1. **Intune patch status (Windows)**
   - Command: `Get-WindowsUpdateLog` and `Get-WUHistory | Select-Object -First 20`
   - Evidence: patch history export (PA-03/PA-04)
2. **WSUS ring assignment**
   - Command: `Get-WSUSUpdate -Classification Security | Select Title,ApprovalAction,CreationDate`
   - Evidence: CSV export (PA-05)
3. **Linux apt history**
   - Command: `grep "upgrade" /var/log/apt/history.log | tail -n 20`
   - Evidence: recent upgrades (PA-03/PA-04)
4. **Yum history**
   - Command: `yum history list security | head -n 15`
   - Evidence: security update history (PA-03)
5. **Third-party hash validation**
   - Command: `curl -sL <url> -o package.rpm && sha256sum package.rpm`
   - Evidence: hash vs vendor signature (PA-09)

## Office Macro controls commands

1. **Check GPO for macro settings (Windows)**
   - Command: `Get-GPResultantSetOfPolicy -ReportType Html -Path rsop.html`
   - Evidence: macro settings section (MO-01/MO-02)
2. **List trusted publishers**
   - Command: `certutil -store TrustedPublisher`
   - Evidence: trusted publisher list (MO-03)
3. **MDM profile for Office macros (macOS)**
   - Command: `profiles show -type configuration | grep -A5 "Office"`
   - Evidence: profile snippet (MO-03/MO-04)
4. **Macro telemetry query (SIEM)**
   - Query: `Event | where Source="Office" and Action="MacroBlocked" | summarize count() by User`
   - Evidence: screenshot/export (MO-05)

## User Application Hardening commands

1. **Chrome policy export**
   - Command: `chrome://policy` (export JSON)
   - Evidence: baseline export (UAH-01/UAH-02/UAH-04)
2. **Edge policy on Windows**
   - Command: `Get-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Edge'`
   - Evidence: registry export (UAH-03)
3. **SmartScreen state**
   - Command: `Get-MpPreference | Select-Object -Property EnableSmartScreen`
   - Evidence: proof of reputation enforcement (UAH-06)
4. **Browser isolation assignment**
   - Command: `Get-WindowsFeature Windows-Defender-Application-Guard`
   - Evidence: feature enabled (UAH-05)
5. **macOS download quarantine**
   - Command: `spctl --status && spctl --assess --type execute <file>`
   - Evidence: Gatekeeper output (UAH-06)

## Restrict Admin Privileges commands

1. **Local admins enumeration**
   - Command: `net localgroup administrators`
   - Evidence: screenshot/export (RAP-01)
2. **Privileged group membership**
   - Command: `Get-ADGroupMember -Identity "Domain Admins"`
   - Evidence: list with timestamps (RAP-02)
3. **JIT elevation log**
   - Command: `Get-PIMRequest -Filter "State eq 'Approved'"`
   - Evidence: PIM/JIT approvals (RAP-03)
4. **Session logging validation**
   - Command: `Get-WinEvent -LogName Security -MaxEvents 10 | Where-Object {$_.Id -eq 4624}`
   - Evidence: admin logon events (RAP-04)
5. **MFA enforcement for privileged**
   - Query: IdP sign-in log filter on privileged roles
   - Evidence: export showing MFA = true (RAP-05)

## Patch Operating Systems commands

1. **Windows Update compliance report**
   - Command: `Get-WUHistory | Group-Object -Property Result`
   - Evidence: counts of successes/failures (PO-03)
2. **Linux unattended upgrades**
   - Command: `grep -i "upgrade" /var/log/unattended-upgrades/unattended-upgrades.log | tail -n 15`
   - Evidence: automated patching proof (PO-03)
3. **Firmware inventory**
   - Command: `wmic bios get smbiosbiosversion, releasedate`
   - Evidence: firmware version record (PO-07)
4. **EOL detection**
   - Command: `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Select ProductName, ReleaseId`
   - Evidence: OS version vs EOL list (PO-08)
5. **Compliance dashboard export (Intune)**
   - Command: `Get-DeviceCompliancePolicy | ConvertTo-Json`
   - Evidence: JSON export (PO-05)

## Multi-factor Authentication commands

1. **Conditional Access policy export**
   - Command: `Get-AzureADMSConditionalAccessPolicy | ConvertTo-Json`
   - Evidence: export showing MFA requirement (MFA-02/MFA-03)
2. **Sign-in log query**
   - Query: `SigninLogs | where Status.errorCode == 0 | summarize count() by authenticationRequirement`
   - Evidence: MFA coverage snapshot (MFA-03)
3. **FIDO2 registration list**
   - Command: `Get-AzureADUserAuthenticationMethod -All $true | where {$_.MethodType -eq 'Fido2'} | Measure-Object`
   - Evidence: adoption metrics (MFA-05)
4. **Risk event export**
   - Query: `IdentityProtectionEvents | summarize count() by riskLevel, detectionType`
   - Evidence: risk-based enforcement (MFA-06/MFA-09)
5. **API authentication checks**
   - Command: `az ad sp list --query "[?passwordCredentials]"`
   - Evidence: service principal auth method review (MFA-07)

## Regular Backups commands

1. **Backup job status (Veeam)**
   - Command: `Get-VBRBackupSession | Sort-Object EndTime -Descending | Select -First 5`
   - Evidence: recent job states (RB-02)
2. **Immutable repository check**
   - Command: `Get-VBRBackupRepository | Select Name,Type,Immutable` 
   - Evidence: immutability flag (RB-03)
3. **Restore test record**
   - Command: `Get-VBRRestoreSession | Sort-Object EndTime -Descending | Select -First 3`
   - Evidence: recent restores (RB-05)
4. **KMS key rotation log**
   - Command: `aws kms describe-key --key-id <id>`
   - Evidence: key rotation status (RB-07)
5. **Offsite copy verification**
   - Command: `aws s3api get-bucket-versioning --bucket <bucket>`
   - Evidence: versioning/replication status (RB-04/RB-10)

## Packaging outputs

- Save command outputs under `Evidence/<date>/commands/` with the naming pattern `<control>-<command>.txt`.
- Add each file to the dated manifest with description, scope, and hash using `manifest_builder.py`.
- For screenshots, save to `Evidence/<date>/screenshots/` and include context in the manifest notes.

## Hashing reference

- Windows: `Get-FileHash <path> -Algorithm SHA256`
- macOS/Linux: `shasum -a 256 <path>`
- Verify hashes before and after transfer to evidence pack storage.

## Chain-of-custody notes

- Record who captured the evidence, when, and on which system.
- If evidence is redacted, describe the method (e.g., blurred hostnames) and reason.
- Store originals separately with restricted access and reference the redacted copy in manifests.

## Review checklist

- [ ] Command outputs stored with timestamps and hashes.
- [ ] Screenshots include hostnames and clocks.
- [ ] Manifest entries updated with IDs and scope periods.
- [ ] Links to curated notes added for context.
- [ ] No secrets or credentials present in captured outputs.

## Logging and export tips

- When exporting from portals, include filter criteria and time range in the screenshot caption.
- Prefer raw JSON/CSV exports over PDF; include SHA256 hashes for files.
- If screenshots show user data, mask with blur and note the masking tool used.
- Store SIEM queries alongside results to aid reproducibility.

## Sample manifest YAML snippet

```yaml
metadata:
  scope_period: 2025-03-01 to 2025-03-31
  owner: Evidence Librarian
  systems: Workstations, Servers, Azure AD, Backup
  reviewers: Control owners (AC/PA/MO/UAH/RAP/PO/MFA/RB)
  manifest_id: EVD-2025-03-31
entries:
  - id: AC-12
    file: logs/applocker-blocks.csv
    description: AppLocker block events for unsigned binaries
    scope: 2025-03-01 to 2025-03-15
    control_mapping: AC-12 (M2)
    owner: Endpoint Eng
    notes: Includes SIEM query + hash
  - id: PO-03
    file: reports/patch-compliance-march.csv
    description: OS patch compliance report
    scope: 2025-03-01 to 2025-03-31
    control_mapping: PO-03 (M2)
    owner: Server Ops
    notes: Includes ring breakdown
```

## File naming conventions for commands

| Control | Example filename |
| --- | --- |
| AC-02 | `AC-02-applocker-blocks.txt` |
| PA-03 | `PA-03-intune-patch-history.txt` |
| MO-05 | `MO-05-macro-telemetry-query.txt` |
| UAH-06 | `UAH-06-smartscreen-status.txt` |
| RAP-04 | `RAP-04-admin-session-logs.txt` |
| PO-03 | `PO-03-windows-update-history.txt` |
| MFA-03 | `MFA-03-signinlog-mfa-coverage.csv` |
| RB-05 | `RB-05-restore-session-log.txt` |

## Troubleshooting checklist

- [ ] Command fails due to permissions → rerun with appropriate admin role and log the role used.
- [ ] Output empty → confirm scope/time filter; capture screenshot of filter settings.
- [ ] Portal export unavailable → take full-page screenshot and note limitation.
- [ ] Time skew detected → record NTP status and adjust timestamps in notes.
- [ ] Large outputs → compress with ZIP; store hash of ZIP and inner file.
- [ ] Sensitive fields → apply redaction and document method.
- [ ] Multi-tenant context → label tenant ID and subscription in file header.

## Reviewer prompts

- Does the evidence clearly map to a control and maturity level?
- Is the scope period explicit and within the assessment window?
- Are hashes present for every file? If not, is the reason documented?
- Do screenshots include hostnames and timestamps?
- Is there at least one curated note referencing this evidence?
