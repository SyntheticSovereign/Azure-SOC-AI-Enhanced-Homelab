# Risk Assessment Playbook

This playbook outlines a repeatable approach to assess cyber risk for business services, including workshop prompts and deliverables aligned to ISO 27005 and COBIT governance objectives.

## 1. Scope and prepare

- Define objectives (e.g., regulatory assessment, board reporting, product launch readiness).
- Confirm applicable frameworks: ISO 27001/27005, NIST CSF, COBIT 2019, SOC 2, PCI DSS, or sector-specific requirements.
- Identify stakeholders: service owner, asset custodians, security architects, privacy officer, legal, IT operations, and vendors.
- Collect reference material: architecture diagrams, data flow maps, threat models, logging maturity, vulnerability scans, and incident history.
- Establish rating scales from the scoring reference and tailor them to risk appetite.

## 2. Inventory and classify assets

- Map business services to supporting applications, data stores, infrastructure, and third parties.
- Assign owners, data classifications (Public, Internal, Confidential, Restricted), and CIA ratings (1–5).
- Note dependencies on cloud services (IaaS/PaaS/SaaS), integrations, and privileged access paths.
- Capture control coverage (identity, endpoint, network, application, data, monitoring, resilience).

## 3. Identify threats and vulnerabilities

- Use threat catalogs (e.g., ransomware, phishing, insider misuse, configuration drift, supply chain compromise).
- For each asset, list relevant vulnerabilities or weaknesses (patch backlog, lack of MFA, shadow IT, weak segregation, missing backups).
- Identify existing controls and their effectiveness. Note compensating controls and gaps.
- Consider business context: revenue impact, regulatory exposure, safety implications, and customer trust.

## 4. Develop risk scenarios

- Write risk statements in "If/Then/Result" form tied to business outcomes.
- Link scenarios to threat events, vulnerabilities, and impacted assets.
- Capture detection points, current controls, residual likelihood/impact, and inherent vs. residual risk.
- Map each scenario to frameworks to demonstrate compliance coverage.

## 5. Score and prioritize

- Use the scoring reference to assign likelihood and impact (1–5) or qualitative equivalents (Rare to Almost Certain; Minor to Severe).
- Calculate inherent and residual risk ratings (e.g., Likelihood × Impact or logarithmic scoring).
- Use business criticality, regulatory exposure, and control gaps to prioritize remediation.
- Build a top risks summary with heat maps and control coverage views.

## 6. Plan treatment and track actions

- Define treatment options: mitigate, transfer, accept, or avoid.
- Document control owners, milestones, budget estimates, and target dates.
- Create measurable acceptance criteria and key risk indicators (KRIs).
- Align treatment plans with COBIT governance components (process, organizational structures, policies, information, services, infrastructure).

## 7. Report and iterate

- Produce executive summaries with business outcomes, risk trends, and major gaps.
- Share detailed risk register entries with action plans and dependencies.
- Schedule quarterly reviews, tabletop exercises, and control validation checks.
- Update artifacts following incidents, architecture changes, or new regulatory obligations.

## Workshop prompts

- "What business outcome would be disrupted if this system failed for a day?"
- "What adversary behavior do we currently detect late or not at all?"
- "Which third parties hold our sensitive data, and how do we monitor their controls?"
- "Where could privileged access be abused or misconfigured?"
- "How do backup, recovery, and resilience tests compare to RPO/RTO targets?"

## Deliverables checklist

- Current-state architecture and data flow diagrams annotated with trust boundaries
- Asset inventory with CIA ratings and owners
- Risk register with inherent/residual scoring and treatment plans
- Control mappings to ISO 27001 Annex A, NIST CSF, and COBIT objectives
- Executive summary with top risks, heat maps, and remediation roadmap
