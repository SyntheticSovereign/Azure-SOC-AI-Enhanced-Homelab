# Example Risk Profile: Acme Manufacturing

Use this example to understand how to populate the templates for a mid-sized manufacturing company operating in North America and Europe.

## Business context
- **Critical services:** ERP for production planning, MES for shop floor control, supplier portal, customer ordering portal.
- **Crown jewels:** CAD files for proprietary designs, OT control systems, supplier pricing data, customer PII.
- **Key dependencies:** Azure AD/Microsoft 365, SAP S/4HANA, manufacturing execution system, OT network with PLCs and HMIs, managed SOC provider.
- **Regulatory drivers:** SOX, GDPR, ITAR, contractual SLAs with OEM partners.

## Top risks (illustrative)
1. **Ransomware disrupts OT and ERP:** If ransomware spreads from IT to OT networks, production halts, causing missed SLAs and contractual penalties.
2. **Supplier portal account takeover:** Weak MFA enforcement enables credential stuffing, leading to data exposure and fraudulent purchase orders.
3. **Unpatched OT assets:** Legacy PLCs and HMIs lack timely patching, increasing risk of safety impacts and downtime.
4. **Insider misuse of design files:** Excessive access to CAD shares leads to unauthorized exfiltration and IP loss.

## Control priorities
- Segment OT/IT with firewalls and one-way gateways; enforce MFA and PAM for remote access.
- Implement application allowlisting and strict change control on OT endpoints.
- Validate backup and recovery for both ERP and OT controllers; test RPO/RTO quarterly.
- Expand detection engineering for lateral movement, privilege escalation, and data exfiltration.
- Strengthen vendor risk management for managed service providers and critical suppliers.

## Evidence to collect
- Network diagrams showing segmentation and data flows between IT and OT.
- Access review reports for privileged accounts and supplier portal users.
- Patch management status and vulnerability scan results for OT and IT assets.
- Backup validation reports and recovery drill outcomes.
- SOC playbooks and detection rules for ransomware behaviors.
