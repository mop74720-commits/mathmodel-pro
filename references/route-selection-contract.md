# Route Selection Contract v0.5-alpha

This is a normalized record contract for Coach decisions. It is not a Router,
algorithm selector, or Freeze Engine.

## Route record

Required fields:

- `schema`: `mathmodel-pro/route-selection/v1`
- `route_id`: stable identifier within the Selection Workspace
- `problem_id`: candidate problem identifier
- `baseline_or_minimal_witness`: executable baseline or smallest proof of viability
- `primary_route`: current route description
- `binding_constraints`: constraints that can invalidate the route
- `deciding_probe`: cheapest probe expected to change the decision
- `deciding_evidence`: evidence reference, or empty before the probe runs
- `strongest_objection`: strongest known counterargument
- `refutation_test`: test for that objection
- `flip_condition`: condition that would change the current route
- `fallback_trigger`: condition that activates fallback
- `fallback_action`: concrete fallback action
- `judge_visible_evidence`: expected table, figure, metric, or decision artifact

`required_deliverable`, `engineering_risk`, `rejected_alternative`, and
`evidence_refs` are recommended when applicable. A route may be provisional;
the record must not imply that an unverified assumption is a formal fact.

## Evaluation record

Dimension-level values such as feasibility, evidence strength, robustness, and
paper quality may be recorded as qualitative evidence or optional numeric
proxies. They are not a required total score. A `final_score`, if supplied,
must be marked `proxy_only: true` and cannot trigger freeze or promotion.

## Decision record

Required fields:

- `schema`: `mathmodel-pro/route-selection-decision/v1`
- `status`: `PROVISIONAL`, `SELECTED`, `ARCHIVED`, or `REOPENED`
- `incumbent_route`
- `challenger_route` (nullable when no credible challenger exists)
- `deciding_evidence`
- `strongest_objection`
- `flip_condition`
- `freeze_reason` (required only for `SELECTED`)
- `promotion_policy`: `archive_then_promote_confirmed_evidence_only`

The decision is owned by Coach. SkillHub can return local evidence, risks, and
a recommended handoff, but cannot select/abandon a problem, freeze a global
route, or declare submission readiness.

## Competition Workspace handoff

Selection records stay in the Template-generated Selection Workspace. On
promotion, archive the selection files under `audit/selection/` and retain
only confirmed problem facts, deciding probe evidence, baseline, fallback, and
revisit condition for the formal Competition Repo. Never auto-promote route
assumptions into `problem/FACTS.md`.
