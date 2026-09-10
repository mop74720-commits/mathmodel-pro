#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "experience/README.md",
    "experience/index.yaml",
    "experience/patterns.yaml",
    "experience/failures.yaml",
    "references/selection-route-decision.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"missing {rel}")

if not errors:
    index = (ROOT / "experience/index.yaml").read_text(encoding="utf-8")
    readme = (ROOT / "experience/README.md").read_text(encoding="utf-8")
    patterns = (ROOT / "experience/patterns.yaml").read_text(encoding="utf-8")
    failures = (ROOT / "experience/failures.yaml").read_text(encoding="utf-8")
    route = (ROOT / "references/selection-route-decision.md").read_text(encoding="utf-8")

    ids = re.findall(r"(?m)^  - id:\s*([A-Z0-9_-]+)\s*$", index)
    if len(ids) < 14:
        errors.append(f"experience cases < 14: {len(ids)}")
    if len(ids) != len(set(ids)):
        errors.append("duplicate case ids")

    for phrase in ["historical_prior_only", "current_evidence_required: true", "prefer_structure_over_topic_name: true"]:
        if phrase not in index:
            errors.append("index policy missing " + phrase)

    for phrase in ["历史经验只能作为 **prior**", "deciding evidence", "Top-3"]:
        if phrase not in readme:
            errors.append("experience README boundary missing " + phrase)

    for phrase in ["experience/index.yaml", "历史经验只能作为 prior", "matched structure", "deciding probe"]:
        if phrase not in route:
            errors.append("route integration missing " + phrase)

    pattern_ids = re.findall(r"(?m)^  - id:\s*([a-z0-9_]+)\s*$", patterns)
    failure_ids = re.findall(r"(?m)^  - id:\s*([a-z0-9_]+)\s*$", failures)
    if len(pattern_ids) < 8:
        errors.append(f"reusable patterns < 8: {len(pattern_ids)}")
    if len(failure_ids) < 8:
        errors.append(f"failure patterns < 8: {len(failure_ids)}")

if errors:
    print("EXPERIENCE_VALIDATION_FAIL")
    for err in errors:
        print("-", err)
    sys.exit(1)

print("EXPERIENCE_VALIDATION_PASS: 14+ structured historical cases + prior-not-evidence route integration")
