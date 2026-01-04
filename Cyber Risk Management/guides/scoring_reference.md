# Scoring Reference

Use these tables to drive consistent scoring during workshops. Adjust thresholds to align with your organization’s risk appetite, regulatory expectations, and business impact criteria.

## Likelihood scale (1–5)

| Score | Descriptor        | Example indicators                                           |
|-------|-------------------|--------------------------------------------------------------|
| 1     | Rare              | Exploitation requires advanced attacker and multiple controls must fail. |
| 2     | Unlikely          | Observed in industry but requires chaining weaknesses.        |
| 3     | Possible          | Plausible with current control posture and threat activity.   |
| 4     | Likely            | Active targeting or repeated control failures exist.          |
| 5     | Almost Certain    | High attacker interest and control gaps; exploit attempts frequent. |

## Impact scale (1–5)

| Score | Descriptor | Financial                                             | Operational                                    | Regulatory/Legal                                 | Reputational                                        |
|-------|------------|--------------------------------------------------------|------------------------------------------------|---------------------------------------------------|------------------------------------------------------|
| 1     | Minor      | <$10k; negligible revenue loss                        | Minimal service disruption (<30 minutes)       | No reporting obligations                          | Limited to internal audience                         |
| 2     | Moderate   | $10k–$250k; localized cost                            | Short outage (<4 hours) or small manual effort | Minor contract issues; minimal data exposure      | Brief customer concern; contained                    |
| 3     | Significant| $250k–$1M; regional impact                            | Multi-hour outage; delayed orders              | Reportable incident in one jurisdiction           | Negative press in niche outlets                      |
| 4     | Major      | $1M–$5M; national impact                              | Sustained outage (>1 day) or large rework      | Regulator inquiry or multiple jurisdiction reports| Widespread press; customer attrition                |
| 5     | Severe     | >$5M; strategic impact                                | Multi-day outage or safety concerns            | Consent decrees, fines, litigation                | Major trust loss; board/market impact                |

## Control effectiveness

| Score | Descriptor           | Guidance                                                                             |
|-------|----------------------|--------------------------------------------------------------------------------------|
| 1     | Strong               | Automated, monitored, and tested; integrates with detection and response workflows.  |
| 2     | Moderate             | Partially automated; periodic validation; minor gaps.                                |
| 3     | Needs improvement    | Manual process; limited monitoring; known gaps.                                      |
| 4     | Weak                 | Ad hoc control; low assurance.                                                       |
| 5     | Missing              | Control not present.                                                                 |

## Example risk rating calculation

- **Inherent risk** = Likelihood × Impact (before considering controls).
- **Residual risk** = Inherent risk adjusted by control effectiveness or mitigating factors.
- **Risk priority** can be represented as: residual risk × business criticality (1–3).
- Heat map thresholds: 1–5 (Low), 6–10 (Medium), 11–15 (High), 16–25 (Critical).

## Qualitative to quantitative hints

- Convert ordinal scores to ranges (e.g., Likely = annual probability 0.2–0.4) for quantitative models.
- Use log-based scoring for scenarios where impact scales non-linearly (e.g., data breach volumes).
- Track error bars: note confidence level when data is sparse.

## Workshop reminders

- Keep scoring time-boxed and consistent across teams.
- Document rationale for likelihood/impact changes over time.
- Capture assumptions and data sources used for scoring.
