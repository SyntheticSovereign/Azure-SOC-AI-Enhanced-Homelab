# Azure-SOC-AI-Enhanced-Homelab


## Overview
This repository documents a cloud-based SOC homelab built on **Microsoft Azure** to detect, investigate, and respond to a range of cyber attacks and demonstrates end-to-end SOC capability, combining **SIEM, SOAR, endpoint telemetry, malware analysis, and incident response playbooks** aligned to how a real Australian SOC operates.
The focus is not just on alerting, but on **investigation quality, decision-making, automation, and documentation**.

---

## Objectives
- Detect infrastructure attacks and their downstream impact (credential theft, malware execution, BEC activity)
- Investigate incidents using correlated email, identity, endpoint, and network telemetry
- Enrich alerts using interactive malware analysis and threat intelligence
- Automate repeatable SOC tasks using SOAR playbooks
- Produce clear, defensible incident case files suitable for audit and reporting
- Align response and prevention recommendations to **ACSC Essential Eight** principles

---

## Architecture Summary
The homelab simulates a small enterprise environment hosted in Azure:

- Azure VNet with Windows endpoints and a Linux network sensor
- Microsoft Sentinel as the central SIEM/SOAR platform
- Microsoft Defender telemetry for endpoint and email security signals
- ANY.RUN for interactive malware analysis
- Centralised logging and automated incident workflows

High-level flow:
**Phishing email → user interaction → identity / endpoint activity → SIEM detection → enrichment → containment → lessons learned**

Architecture and data-flow diagrams are provided in the `architecture/` directory.

---

## Tools & Technologies Used

### SIEM & SOAR
- Microsoft Sentinel
- KQL (Kusto Query Language)
- Logic Apps (Sentinel automation playbooks)

### Email, Identity & Endpoint Telemetry
- Microsoft Defender (endpoint and email signals)
- Microsoft Entra ID (Azure AD) sign-in logs
- Windows Event Logs
- Sysmon

### Malware & Threat Analysis
- ANY.RUN Interactive Malware Sandbox
- IOC extraction and correlation
- Threat intelligence enrichment (hashes, domains, URLs)

### DFIR & Endpoint Visibility
- Velociraptor (endpoint artifact collection and live hunts)

### Network Visibility
- Zeek
- Suricata

### Documentation & Ops
- GitHub for version control and case management
- Markdown-based incident reports
- Diagrams.net for architecture diagrams

---

## Repository Structure

```text
azure-soc-homelab/
├── README.md
├── architecture/                 # Architecture and data-flow diagrams
├── playbooks/                    # Incident response playbooks
├── detections/                   # Sentinel analytics rules and hunting queries
├── automation/                   # Sentinel SOAR playbooks (Logic Apps)
├── malware-analysis/             # ANY.RUN analysis summaries and IOCs
├── endpoint-telemetry/           # Sysmon configs and Velociraptor artifacts
├── case-studies/                 # Full incident case files including malicious files
├── dashboards/                   # Sentinel workbook screenshots
├── essential-eight-mapping/      # ACSC Essential Eight alignment
└── ai-enhancements/              # AI-assisted SOC workflows
```
Each directory contains real artifacts used in detection engineering, investigation, automation, and incident response within the Azure SOC homelab.
Note: Live malware files are uploaded and encrypted for later triage use cases. If you want specific access to them, please email me, as unauthorized use can lead to system compromise which you would be liable for!
