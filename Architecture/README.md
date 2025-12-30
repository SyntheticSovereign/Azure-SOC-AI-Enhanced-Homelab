# Homelab Architecture Overview

🎯 **Architecture Goals**

This homelab is designed to demonstrate:

- Multi-signal detection instead of single-alert reliance
- How Microsoft Sentinel functions as a true SOC SIEM/SOAR
- The role of network telemetry alongside endpoint and identity logs
- How interactive malware analysis improves detection confidence
- A full incident lifecycle from initial access to lessons learned

🔁 **High-Level Architecture Flow**

1️⃣ **Initial Access & Execution**

Attack scenarios begin with realistic phishing and business email compromise (BEC) techniques.

User interaction (clicks, macro execution, credential entry) leads to malware execution or token abuse, generating observable behaviour across multiple security layers.

This stage establishes the attack surface and seeds telemetry for downstream detection.

2️⃣ **Telemetry Collection Layer**

Multiple telemetry sources operate in parallel inside an Azure virtual network:

- 🖥 **Windows Endpoints (Azure VMs)**
  - Windows Event Logs
  - Sysmon telemetry
  - Microsoft Defender for Endpoint signals

- 👤 **Identity & Cloud Logs**
  - Microsoft Entra ID sign-in activity
  - Risky authentication events
  - Cloud audit logs

- ✉ **Email Security Signals**
  - Phishing verdicts
  - Message trace data
  - URL and attachment indicators

- 🌐 **Network Detection & Response (NDR)**
  - Linux sensor running Zeek and Suricata
  - DNS, HTTP, TLS, and flow visibility
  - IDS alerts and behavioural indicators

All telemetry is forwarded into a central Log Analytics workspace.

3️⃣ **SIEM Detection & Correlation**

Microsoft Sentinel acts as the central SOC platform, responsible for:

- Log ingestion and normalisation
- KQL-based analytics rules
- Cross-signal correlation (endpoint, identity, email, network)
- Incident creation and prioritisation

Low-confidence signals become high-confidence incidents through correlation.

4️⃣ **Alert Enrichment & Automation**

Detected incidents are enriched to improve analyst decision-making:

- 🧪 **Malware & IOC Enrichment**
  - ANY.RUN interactive malware analysis
  - Execution behaviour and process trees
  - IOC extraction and validation

- 🤖 **SOAR Automation**
  - Sentinel Logic Apps playbooks
  - Automated triage and enrichment
  - IOC blocking and containment actions
  - Analyst notifications and ticket creation

Automation is used to accelerate response, not replace human judgement.

5️⃣ **Response, DFIR & Documentation**

Confirmed incidents progress into full investigation and response:

- 🚨 **Containment & Remediation**
  - Account credential resets
  - Endpoint isolation
  - IOC blocking

- 🔍 **DFIR with Velociraptor**
  - Live endpoint hunts
  - Artifact collection
  - Evidence preservation

- 📝 **Incident Reporting**
  - Markdown-based case files
  - Timeline reconstruction
  - Detection logic explanation
  - Mapping to ACSC Essential Eight controls

Each incident feeds back into defensive improvement.
