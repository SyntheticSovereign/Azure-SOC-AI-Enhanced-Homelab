"""Command-line helper for sending SOC prompts to Azure OpenAI.

Usage examples:
  python run_ai_assistant.py --mode summary --input incident.json --deployment gpt-4o-mini
  python run_ai_assistant.py --mode kql --input incident.json --hypothesis "User executed encoded PowerShell" --deployment gpt-4o

Environment variables required:
  AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com
  AZURE_OPENAI_API_KEY=<api-key>

Outputs are printed to stdout and can be redirected into Sentinel comments or tickets.
"""

import argparse
import json
import os
from pathlib import Path

from openai import AzureOpenAI


SYSTEM_PROMPTS = {
    "summary": (
        "You are a Tier 2 SOC analyst writing a concise incident summary. Only use facts from the provided "
        "incident payload. Cite each statement with the originating field name (e.g., properties.title). If data "
        "is missing, say 'unknown' instead of guessing. Respond in JSON with fields: summary, impact, "
        "key_events (list), confirmed_iocs (list), uncertainties (list), next_actions (list)."
    ),
    "kql": (
        "You are a KQL assistant helping an analyst test a hypothesis. Ask for missing parameters instead of "
        "inventing them. Return: description, assumptions, required_data (tables/columns), kql, "
        "validation_steps (list), false_positive_considerations (list). KQL must align to Microsoft Sentinel schemas."
    ),
    "user-comm": (
        "You are preparing a user-facing message for an impacted employee. Keep it under 120 words, plain "
        "language, and action-oriented. Include: what happened, what we did, what the user must do, and who to contact. "
        "Avoid sharing internal detection details."
    ),
    "evidence": (
        "You are creating an evidence collection checklist. Group items by MITRE ATT&CK tactic. For each item, include: "
        "source (e.g., Sysmon, Zeek, Defender), query_hint, and why_it_matters. Limit to the tactics present in the "
        "incident data."
    ),
}


def build_messages(mode: str, incident_payload: dict, hypothesis: str | None, facts: str | None) -> list[dict[str, str]]:
    system = SYSTEM_PROMPTS[mode]
    if mode == "summary":
        user = f"INCIDENT PAYLOAD: {json.dumps(incident_payload, indent=2)}"
    elif mode == "kql":
        user = (
            "HYPOTHESIS: "
            + (hypothesis or "<add hypothesis>")
            + "\nCONTEXT: "
            + json.dumps(incident_payload, indent=2)
        )
    elif mode == "user-comm":
        user = "INCIDENT FACTS: " + (facts or json.dumps(incident_payload, indent=2))
    elif mode == "evidence":
        user = "INCIDENT DATA: " + json.dumps(incident_payload, indent=2)
    else:
        raise ValueError(f"Unsupported mode: {mode}")

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def call_model(client: AzureOpenAI, deployment: str, messages: list[dict[str, str]]) -> str:
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.2,
        max_tokens=600,
        response_format={"type": "json_object" if "summary" in messages[0]["content"] else "text"},
    )
    return completion.choices[0].message.content


def main() -> None:
    parser = argparse.ArgumentParser(description="Send SOC AI prompts to Azure OpenAI.")
    parser.add_argument("--mode", choices=SYSTEM_PROMPTS.keys(), required=True, help="Prompt to run")
    parser.add_argument("--input", required=True, help="Path to incident JSON payload")
    parser.add_argument("--deployment", required=True, help="Azure OpenAI deployment name (e.g., gpt-4o)")
    parser.add_argument("--hypothesis", help="Hypothesis for kql mode")
    parser.add_argument("--facts", help="Explicit facts for user-comm mode")
    args = parser.parse_args()

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not endpoint or not api_key:
        raise SystemExit("Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY")

    incident_path = Path(args.input)
    incident_payload = json.loads(incident_path.read_text())

    messages = build_messages(args.mode, incident_payload, args.hypothesis, args.facts)
    client = AzureOpenAI(api_key=api_key, api_version="2024-02-15-preview", azure_endpoint=endpoint)
    result = call_model(client, args.deployment, messages)
    print(result)


if __name__ == "__main__":
    main()
