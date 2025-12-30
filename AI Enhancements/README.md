# AI Enhancements for the SOC Homelab

This folder documents AI-assisted workflows that speed up investigations while keeping analysts in control. The examples assume Microsoft Sentinel incidents and Logic Apps/Functions for orchestration, but the prompts are vendor-neutral.

## Quickstart
1. **Decide the use case**: summarizing incidents, proposing KQL, drafting user comms, or building checklists.
2. **Collect context**: include incident title, severity, entities (accounts, hosts, IPs, URLs), timeline, and any enrichment (threat intel, ANY.RUN, AV verdicts).
3. **Call the LLM with guardrails**: use system prompts below to force structured output and require citations to input fields.
4. **Log inputs/outputs** for auditability and to retrain or tune prompts.
5. **Keep humans in the loop**: require analyst approval before containment or user messaging.

## Common Integration Pattern
- **Trigger**: Sentinel incident creation/ update.
- **Context builder** (Logic App/Function): fetch incident JSON, entities, related alerts, ticket IDs, and enrichment results; normalize into a single payload.
- **LLM step**: send structured prompt (below) with temperature 0–0.3 and max tokens sized for short responses.
- **Post-process**: validate required fields, check for hallucinations (e.g., references to entities not in input), and add a confidence flag.
- **Output destinations**: incident comment, Teams/Slack message, ticket system, or a PDF case file. Always include a “reviewed by” field for analyst sign-off.

## Prompt Templates
> Replace bracketed placeholders with your values. Keep the **Policies** block intact to reduce hallucinations.

### Incident Summary (for ticket/shift handoff)
```
You are a Tier 2 SOC analyst writing a concise incident summary.

POLICIES:
- Only use facts from the provided incident payload.
- Cite each statement with the originating field name (e.g., Entity.Account, Alert.Title).
- If data is missing, say "unknown" instead of guessing.
- Output JSON with fields: summary, impact, key_events (list), confirmed_iocs (list), uncertainties (list), next_actions (list).

INCIDENT PAYLOAD:
{incident_json}
```

### KQL Query Generator (hypothesis-driven hunting)
```
You are a KQL assistant helping an analyst test a hypothesis.

POLICIES:
- Ask for missing parameters instead of inventing them.
- Return: description, assumptions, required_data (tables/columns), kql, validation_steps (list), false_positive_considerations (list).
- KQL must align to Microsoft Sentinel schemas.

HYPOTHESIS:
{hypothesis}
CONTEXT:
{entity_context}
```

### User Communication Draft (containment notice)
```
You are preparing a user-facing message for an impacted employee.

POLICIES:
- Keep it under 120 words, plain language, and action-oriented.
- Include: what happened, what we did, what the user must do, and who to contact.
- Avoid sharing internal detection details.

INCIDENT FACTS:
{facts}
```

### Evidence Checklist (per ATT&CK stage)
```
You are creating an evidence collection checklist.

POLICIES:
- Group items by MITRE ATT&CK tactic.
- For each item, include: source (e.g., Sysmon, Zeek, Defender), query_hint, and why_it_matters.
- Limit to the tactics present in the incident data.

INCIDENT DATA:
{incident_data}
```

## Validation Steps
- **Schema check**: Ensure JSON outputs match expected keys before posting back to Sentinel.
- **Entity echo test**: Fail the step if the model references entities not present in input.
- **Length limit**: Truncate or reject responses that exceed channel limits (Teams, ticketing).
- **Human approval**: Block automated containment/messages until an analyst approves the AI suggestion.

## Evaluation Playbook
1. Run the prompts against 3–5 historical incidents (phishing, credential theft, malware, insider threat).
2. Score for **accuracy** (no invented entities), **coverage** (all major events mentioned), and **actionability** (clear next steps).
3. Capture before/after investigation times and note where AI reduced toil.
4. Iterate prompts where errors occur; lower temperature or tighten policies for high-risk actions.

## Logging & Governance
- Store prompt, input payload hash, model version, and output in a central log (e.g., Storage Account + Kusto table) for audit.
- Add PII handling rules; redact passwords/keys before sending to the model.
- Define escalation paths for when the model output conflicts with analyst judgment.

## Ready-to-Use Assets
- **Logic App workflow**: `templates/logic-app-incident-summarizer.json` ingests Sentinel incident updates, builds a payload, calls Azure OpenAI, and posts the AI summary back as a comment.
- **CLI helper**: `scripts/run_ai_assistant.py` sends prompt templates to Azure OpenAI for summaries, KQL suggestions, user comms, and evidence checklists.
- **Sample payload**: `templates/sample-incident.json` matches Sentinel incident schema for local testing and prompt tuning.
- **Python deps**: `scripts/requirements.txt` pins the OpenAI SDK.

### Deploy the Logic App
1. Import `templates/logic-app-incident-summarizer.json` into the Logic Apps (Consumption) designer.
2. Create or reuse the **Microsoft Sentinel** connection when prompted and supply three parameters:
   - `azureOpenAIEndpoint` (e.g., `https://contoso-openai.openai.azure.com`)
   - `azureOpenAIDeployment` (e.g., `gpt-4o` or `gpt-4o-mini`)
   - `azureOpenAIApiKey`
3. Add an approval step after the AI call if you want human review before posting the comment. The template already scopes the AI request to incident fields and rejects hallucinated entities via the policies in the system prompt.

### Use the CLI Helper
```bash
python scripts/run_ai_assistant.py \
  --mode summary \
  --input templates/sample-incident.json \
  --deployment gpt-4o \
  # requires AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY env vars
```

- Modes: `summary`, `kql`, `user-comm`, `evidence` (adds the right system policy automatically).
- Change `--hypothesis` (for KQL) or `--facts` (for user comms) to tighten context.
- Pipe output into `az sentinel incident comment create` or your ticketing webhook to automate updates.

### Extend and Evaluate
- Swap the system prompts in `scripts/run_ai_assistant.py` with your few-shot examples or org-specific policies.
- Add extra post-processing in the Logic App (schema validation, profanity filter, or entity echo test) before publishing comments.
- Log prompt/response pairs into a Kusto table to measure accuracy and response times across incidents.
