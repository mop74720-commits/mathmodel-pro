# Coach Boundary — v0.4.0

Coach manages **global decisions**: current priority, risk acceptance, question switching, freeze/rollback, resource allocation and submission readiness.

SkillHub manages **local technical execution**: algorithms, implementation, numerical checks, experiments, visualization, writing transformations and independent review.

Competition Repo is the factual source of truth.

## Non-negotiable boundary

- Coach may request an event, but must not invent or hard-code a Skill path; read SkillHub `registry.yaml`.
- SkillHub may return risks and a recommended handoff, but must not decide to abandon a question, freeze the global model or submit.
- Stage/time playbooks are references only. They cannot override current repo evidence.
- Global strategy content belongs here/Coach, not as a first-class SkillHub event.
