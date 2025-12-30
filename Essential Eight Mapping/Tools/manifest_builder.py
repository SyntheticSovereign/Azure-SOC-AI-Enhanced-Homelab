"""
manifest_builder.py

Generate evidence manifest tables from a structured YAML input. The tool normalizes filenames,
computes SHA256 hashes, and produces Markdown ready for inclusion under Evidence/<date>/manifest.md.

Usage:
    python manifest_builder.py --input manifest.yml --output Evidence/2025-03-31/manifest.md

The YAML schema expects a top-level `entries` list and optional `metadata` fields.
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import pathlib
import sys
import textwrap
from typing import Iterable, List, Optional


@dataclasses.dataclass
class ManifestEntry:
    entry_id: str
    file_path: pathlib.Path
    description: str
    scope: str
    control_mapping: str
    owner: str
    notes: str = ""
    sha256: Optional[str] = None

    def compute_hash(self) -> None:
        if not self.file_path.exists() or not self.file_path.is_file():
            raise FileNotFoundError(f"File not found for hashing: {self.file_path}")
        digest = hashlib.sha256()
        with self.file_path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(8192), b""):
                digest.update(chunk)
        self.sha256 = digest.hexdigest()


@dataclasses.dataclass
class ManifestMetadata:
    scope_period: str
    owner: str
    systems: str
    reviewers: str
    manifest_id: str


def parse_yaml(input_path: pathlib.Path) -> tuple[ManifestMetadata, List[ManifestEntry]]:
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - dependency managed externally
        raise SystemExit("PyYAML is required: pip install pyyaml") from exc

    data = yaml.safe_load(input_path.read_text())
    meta = data.get("metadata", {})
    metadata = ManifestMetadata(
        scope_period=meta.get("scope_period", ""),
        owner=meta.get("owner", ""),
        systems=meta.get("systems", ""),
        reviewers=meta.get("reviewers", ""),
        manifest_id=meta.get("manifest_id", input_path.stem),
    )

    entries: List[ManifestEntry] = []
    for row in data.get("entries", []):
        entry = ManifestEntry(
            entry_id=row["id"],
            file_path=input_path.parent / row["file"],
            description=row.get("description", ""),
            scope=row.get("scope", ""),
            control_mapping=row.get("control_mapping", ""),
            owner=row.get("owner", ""),
            notes=row.get("notes", ""),
        )
        entries.append(entry)
    return metadata, entries


def render_markdown(metadata: ManifestMetadata, entries: Iterable[ManifestEntry]) -> str:
    lines = [
        f"# Evidence Pack – {metadata.manifest_id}",
        "",
        f"- **Scope period**: {metadata.scope_period}",
        f"- **Systems**: {metadata.systems}",
        f"- **Owner**: {metadata.owner}",
        f"- **Reviewers**: {metadata.reviewers}",
        "",
        "| ID | File | Description | Scope period | Control mapping | Owner | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        file_name = entry.file_path.name
        lines.append(
            f"| {entry.entry_id} | `{file_name}` | {entry.description} | {entry.scope} | {entry.control_mapping} | {entry.owner} | {entry.notes} |"
        )

    lines.extend(["", "## Hashes (SHA256)", "", "| File | SHA256 |", "| --- | --- |"])
    for entry in entries:
        hash_value = entry.sha256 or "<hash>"
        lines.append(f"| `{entry.file_path.name}` | `{hash_value}` |")

    return "\n".join(lines)


def normalize_entries(entries: Iterable[ManifestEntry], hash_files: bool) -> List[ManifestEntry]:
    normalized: List[ManifestEntry] = []
    for entry in entries:
        if hash_files:
            entry.compute_hash()
        normalized.append(entry)
    return normalized


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Evidence manifest markdown from YAML.")
    parser.add_argument("--input", type=pathlib.Path, required=True, help="Path to YAML input file")
    parser.add_argument("--output", type=pathlib.Path, required=True, help="Path to write Markdown output")
    parser.add_argument("--hash", action="store_true", help="Compute SHA256 hashes for listed files")
    args = parser.parse_args(argv)

    metadata, entries = parse_yaml(args.input)
    normalized = normalize_entries(entries, hash_files=args.hash)
    markdown = render_markdown(metadata, normalized)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(textwrap.dedent(markdown))
    print(f"Manifest written to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
