# Route Selection Layer v0.1.0 Architecture Audit

## Decision

**B — modify before entering `mathmodel-pro v0.5.0-alpha`.**

The prototype is useful as a contract for recording route alternatives and
decisive evidence, but it must not be merged as a new Router, Decision Engine,
or Freeze Engine. `mathmodel-pro v0.4.1` already owns the global
`candidate -> decisive unknown -> cheap probe -> evidence -> flip/fallback`
loop and the final freeze decision.

## Boundary audit

| Area | Finding | Required treatment |
|---|---|---|
| Coach / SkillHub | The prototype correctly places route selection in Coach, but its adapter contract does not define the handoff shape or authority fields. | Add an explicit request/response boundary. SkillHub may execute local probes and return evidence, risk, and handoff; Coach retains priority, route acceptance, freeze, and rollback decisions. |
| Existing Decision Engine | The protocol's incumbent/challenger comparison and freeze language overlaps v0.4.1. Its score fields could become a competing numeric decision engine. | Reuse v0.4.1 state-first decisions. Treat scores as optional, dimension-level evidence only; no aggregate score may freeze or promote a route. |
| Upstream route-selection ideas | The prototype carries the already-selected upstream ideas: route-led comparison, feasibility, risk, fallback, and challenger comparison. It does not add a distinct algorithm. | Keep these ideas as named fields and checks. Do not import fixed weights, near-tie thresholds, fixed search counts, or mandatory multi-route exploration. |
| Adapter / schema / validator | The supplied YAML examples are documentation fragments: fields have no types, requiredness, enums, provenance, or validation semantics. | Add a minimal versioned contract and a validator for route records and decision records. External adapters must normalize into this contract before Coach consumes them. |
| Competition Workspace | The flow ends at “Competition Repo” but does not define promotion safety. | Integrate with the existing Template Selection Workspace. Archive selection evidence; promote only confirmed facts, probe evidence, baseline, fallback, and revisit condition. Never auto-write guesses to `problem/FACTS.md`. |

## Why not A or C?

Direct inclusion (A) would duplicate the existing Selection/Decision contract
and make `final_score` look authoritative. Keeping it as an experimental
plugin (C) would leave a small, immediately useful schema/adapter gap
unaddressed while providing no meaningful runtime isolation. The modified
contract belongs in the Coach repository as an alpha compatibility layer.

## Upstream absorption assessment

Absorbed sufficiently: route-led selection, executable route, engineering
feasibility, strongest objection/refutation, flip condition, fallback, and
incumbent/challenger comparison.

Not absorbed, intentionally: fixed scoring weights, fixed thresholds, fixed
Day-One gates, mandatory route counts, automatic topic choice, and any
SkillHub authority over global decisions. These exclusions preserve the
existing v0.4.1 design and its documented upstream selection rationale.

## v0.5.0-alpha merge plan

1. Keep the existing Selection Workspace as the only exploration workspace and
   the Competition Template as its factory.
2. Use `references/route-selection-contract.md` for the normalized route and
   decision records.
3. Use `scripts/validate_route_selection.py` at adapter/workspace boundaries.
4. Route local technical probes through SkillHub registry events such as
   `MODELS_NEED_COMPARISON`; do not hard-code SkillHub paths here.
5. Archive and promote through the existing Template workflow. The alpha
   contract must not create or mutate formal facts automatically.

## File-level recommendations

| Prototype file | v0.5.0-alpha treatment |
|---|---|
| `ROUTE_SELECTION_PROTOCOL.md` | Adapt into the Coach contract; remove implication of a second freeze engine. |
| `schemas/route-candidate.yaml` | Replace example-only fields with typed, versioned fields and explicit evidence links. |
| `schemas/route-evaluation.yaml` | Keep dimensions as optional evidence; remove any implication that `final_score` is authoritative. |
| `schemas/decision-record.yaml` | Add status enum, authority, deciding evidence, objection, flip condition, and promotion policy. |
| `integrations/external-route-selection-adapter.md` | Add normalized request/response and rejection conditions. |
| `scoring/*.md` | Keep as optional proxy guidance, subordinate to evidence and hard constraints. |
