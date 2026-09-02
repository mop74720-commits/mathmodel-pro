#!/usr/bin/env python3
"""Validate normalized route-selection records without deciding the route."""
from pathlib import Path
import argparse
import sys

try:
    import yaml
except ImportError:
    print("ROUTE_SELECTION_VALIDATION_FAIL: PyYAML is required")
    raise SystemExit(1)

ROUTE_REQUIRED = {
    "schema", "route_id", "problem_id", "baseline_or_minimal_witness",
    "primary_route", "binding_constraints", "deciding_probe",
    "deciding_evidence", "strongest_objection", "refutation_test",
    "flip_condition", "fallback_trigger", "fallback_action",
    "judge_visible_evidence",
}
DECISION_REQUIRED = {
    "schema", "status", "incumbent_route", "challenger_route",
    "deciding_evidence", "strongest_objection", "flip_condition",
    "promotion_policy",
}


def validate(root: Path) -> list[str]:
    errors = []
    route_path = root / "route.yaml"
    decision_path = root / "decision.yaml"
    if not route_path.exists():
        errors.append("missing route.yaml")
    if not decision_path.exists():
        errors.append("missing decision.yaml")
    if errors:
        return errors

    route = yaml.safe_load(route_path.read_text(encoding="utf-8")) or {}
    decision = yaml.safe_load(decision_path.read_text(encoding="utf-8")) or {}
    missing = ROUTE_REQUIRED - set(route)
    errors.extend(f"route.yaml missing {key}" for key in sorted(missing))
    if route.get("schema") != "mathmodel-pro/route-selection/v1":
        errors.append("route.yaml schema mismatch")
    missing = DECISION_REQUIRED - set(decision)
    errors.extend(f"decision.yaml missing {key}" for key in sorted(missing))
    if decision.get("schema") != "mathmodel-pro/route-selection-decision/v1":
        errors.append("decision.yaml schema mismatch")
    if decision.get("status") not in {"PROVISIONAL", "SELECTED", "ARCHIVED", "REOPENED"}:
        errors.append("decision.yaml status invalid")
    if decision.get("promotion_policy") != "archive_then_promote_confirmed_evidence_only":
        errors.append("promotion policy must prohibit automatic fact promotion")
    if decision.get("status") == "SELECTED" and not decision.get("freeze_reason"):
        errors.append("SELECTED decision requires freeze_reason")
    if "final_score" in route and route.get("proxy_only") is not True:
        errors.append("final_score must be explicitly marked proxy_only")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("ROUTE_SELECTION_VALIDATION_FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("ROUTE_SELECTION_VALIDATION_PASS: normalized Coach contract; no route decision made")
    return 0


if __name__ == "__main__":
    sys.exit(main())
