# Reference Index for Essential Eight Mapping

Use this index to track authoritative and supporting references used in mappings, checklists, and policies.

## Authoritative sources

| Source | Link | Relevance | Last checked |
| --- | --- | --- | --- |
| ASD Essential Eight Strategies | https://www.cyber.gov.au/resources-business-and-government/essential-eight | Primary framework | 2025-01-01 |
| ASD Essential Eight Maturity Model | https://www.cyber.gov.au/resources-business-and-government/essential-eight/essential-eight-maturity-model | Maturity criteria | 2025-01-01 |
| NIST Cybersecurity Framework 2.0 | https://www.nist.gov/cyberframework | Crosswalk mapping | 2025-01-01 |
| ISO/IEC 27001:2022 | https://www.iso.org/standard/82875.html | Control alignment | 2025-01-01 |
| CIS Controls v8 | https://www.cisecurity.org/controls/v8 | Control alignment | 2025-01-01 |
| PCI-DSS v4.0 | https://www.pcisecuritystandards.org | Payment-related mappings | 2025-01-01 |

## Supporting references

| Source | Link | Purpose | Notes |
| --- | --- | --- | --- |
| Microsoft WDAC/AppLocker documentation | https://learn.microsoft.com/windows/security/threat-protection/windows-defender-application-control/wdac-and-applocker-overview | Application control implementation patterns | Include baseline XML/Intune profile links |
| Microsoft Intune patching guidance | https://learn.microsoft.com/mem/intune/protect/software-updates-windows | Patch ring setup for Windows | Capture deployment ring screenshots |
| Jamf patch management guide | https://learn.jamf.com | macOS patch baselines | Include MDM profile samples |
| Office macro security settings | https://learn.microsoft.com/deployoffice/security/office-file-validation | Macro configuration references | Include trusted location examples |
| Browser baseline docs (Chromium) | https://chromeenterprise.google/policies/ | User application hardening | Note download restriction keys |
| Azure AD Conditional Access | https://learn.microsoft.com/azure/active-directory/conditional-access/overview | MFA and device posture | Capture policy export steps |
| Backup immutability best practices | https://www.ncsc.gov.uk/guidance/ransomware-mitigations | Backups and ransomware | Include object-lock references |

## Citation guidance

- Record the exact URL and version (e.g., document revision, commit hash, publication date).
- If a source is paywalled (e.g., ISO standard), record the clause number and citation text used for mapping.
- For screenshots or exports derived from these sources, add them to `Evidence/<date>/` and cite the manifest entry.

## Change log

- 2025-02-01: Initial index created to support mapping crosswalks.
