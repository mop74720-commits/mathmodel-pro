# External Route Selection Adapter

External tools may propose routes, but Coach consumes only a normalized record.
The adapter is a boundary translator, not a decision-maker.

## Request

The adapter receives a problem or route candidate, the current incumbent (if
any), relevant constraints, and the requested local probe. It must preserve
provenance for every returned evidence item and must not silently turn an
assumption into a formal fact.

## Response

The adapter returns a `route.yaml` and, when a comparison was requested, a
`decision.yaml` conforming to `references/route-selection-contract.md`.
Responses may include:

- normalized route candidates;
- local evaluation evidence and limitations;
- strongest objection and refutation result;
- fallback and flip-condition recommendations;
- a SkillHub handoff event for unresolved local technical work.

The adapter must reject or mark invalid responses that:

- select or abandon a problem without Coach approval;
- force a fixed algorithm or fixed route count;
- claim `SELECTED` without deciding evidence and a freeze reason;
- use an aggregate score without `proxy_only: true`;
- write directly to Competition Repo `problem/FACTS.md`;
- declare `SUBMISSION_READY`.

After validation, Coach decides whether to continue exploration, select a
route, reopen a prior selection, or promote confirmed evidence through the
Competition Template workflow.
