# Release, Reliability, and Production Readiness

Use this hub when shipping safely is the core problem: release gates, rollout strategy, rollback posture, observability minimums, reliability trade-offs, dependency failure handling, and determining whether the change can be trusted in production.

## What This Hub Owns

- production-readiness criteria for software changes
- release gating with explicit evidence
- rollout patterns such as dark launch, canary, or flagging
- rollback design and migration safety
- operational reliability expectations and failure containment
- observability baselines for new paths and components
- incident-informed release hardening
- dependency failure policy and user impact containment
- runbook expectations for high-risk changes
- release validation and smoke sequencing
- post-release review signals and stop conditions
- production readiness for code-driven technical SEO changes

## What This Hub Does Not Own

- release announcements or launch marketing
- business go-to-market timing decisions
- product positioning for the feature
- support staffing decisions absent code impacts
- procurement or vendor negotiation
- analytics interpretation that does not affect deployment
- roadmap sequencing beyond operational risk
- research synthesis unrelated to release safety

## Questions To Answer First

- What can go wrong in production that cannot be reproduced locally?
- Which parts of the change are reversible, and which are not?
- What evidence is required before enabling exposure broadly?
- Which user cohorts or traffic slices should absorb first risk?
- How will operators detect a silent failure early?
- What dashboards or logs are missing for first-day support?
- Which dependencies can degrade gracefully, and which cannot?
- What migration steps need ordering, isolation, or pause points?
- What stop condition would trigger rollback or disablement?
- How will the team separate feature defects from environment noise?
- What incident history makes this change especially sensitive?
- Which post-release review window fits the actual risk profile?

## Required Inputs

- deployment method and environment topology
- feature flag or configuration control availability
- migration or data backfill requirements
- known reliability objectives or error budgets
- operator ownership and on-call expectations
- dependency map for third-party and internal services
- existing monitoring, logging, and alerting assets
- release window constraints and change freeze rules
- smoke test plan and rollback capabilities
- security or compliance controls affecting exposure
- expected traffic patterns during the rollout
- customer segments with elevated sensitivity to errors

## Evidence Signals

- prior incidents linked to similar changes
- missing dashboards or high-cardinality blind spots
- database changes with one-way semantics
- integration limits and failure responses
- manual steps that introduce operator error
- gaps in rollback automation
- release notes showing repeated failure classes
- health checks that do not exercise the risky path
- dependency saturation or timeout indicators
- post-release support burden from earlier launches

## Working Rules

- No high-risk release without a named rollback position.
- Ship evidence, not optimism.
- A feature flag is not a substitute for migration safety.
- Observe the new path before broadening exposure.
- Release checklists should prove readiness, not merely exist.
- Graceful degradation must be designed before failure.
- Keep first-day operator questions answerable from telemetry.
- Prefer narrow blast radius over clever rollout theatrics.
- Alert on user impact and critical pipeline health, not vanity noise.
- One-way data changes deserve extra review friction.
- A smoke test that misses the risky path is theater.
- Post-release review is part of the release, not an optional memory.

## Recommended Workflow

- Define the production risk in user and operator terms.
- Collect release evidence across tests, telemetry, and rollback.
- Choose rollout method that matches reversibility.
- Verify migrations and background work ordering.
- Prepare dashboards, logs, and on-call notes.
- Run decisive smoke checks before wider exposure.
- Observe leading indicators during early traffic.
- Trigger stop conditions if evidence turns negative.
- Complete post-release review while context is fresh.
- Fold lessons into future readiness gates.

## Common Failure Modes

- calling something low risk because the code diff is small
- relying on canary without representative traffic
- shipping schema changes with no downgrade thought
- adding alerts that no one will trust
- hiding operational debt behind weekend heroics
- forgetting background jobs when validating a release
- using dashboards that cannot isolate the new feature path
- confusing rollback of code with rollback of data effects
- skipping post-release review after a lucky outcome
- treating observability as documentation instead of runtime evidence

## Expected Deliverables

- production readiness gate
- release evidence summary
- rollout and rollback plan
- observability minimum set
- smoke test sequence
- migration risk notes
- dependency failure posture
- operator handoff notes
- post-release review template
- residual risk statement

## Hand-offs and Escalation

- to testing when additional gate evidence is missing
- to observability baseline work when telemetry gaps dominate
- to architecture when reliability risk reflects structural issues
- to workflow automation when release steps should be scripted
- to security review for trust-boundary sensitive launches
- to frontend teams for user-facing degradation behavior
- to product only if exposure order depends on business rules
- to support readiness if operator communication is needed

## Playbooks To Load Next

- `references/playbooks/production-readiness-gate.md`
- `references/playbooks/release-validation.md`
- `references/playbooks/observability-baseline.md`
- `references/playbooks/ci-delivery-workflow.md`

## Deterministic Tools

- `scripts/release/validate_release_readiness.py`
- `scripts/seo/check_technical_seo_artifacts.py`

## Review Checklist

- Rollback position is explicit.
- Migration directionality is understood.
- Feature flags or controls are documented.
- Smoke checks hit the risky path.
- Dashboards exist for first-day support.
- Alerts emphasize user impact or safety-critical failures.
- Dependencies have timeout and fallback posture.
- Release notes include operator-relevant detail.
- On-call owner knows the change window.
- Stop conditions are objective and actionable.
- Post-release review window is scheduled.
- Residual risk is accepted consciously.
- No readiness claim relies on invisible tribal knowledge.
- Technical SEO changes have crawlable output checks if relevant.
- Manual steps are minimized or rehearsed.
- Sensitive data or auth changes got extra scrutiny.
- Health checks are not mistaken for full validation.
- Early exposure cohort is chosen intentionally.
- Operational documentation matches the release reality.
- Production readiness is demonstrated with evidence.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Reliability Field Notes

- Production readiness is partly about code quality, but just as much about whether operators can understand the new path while it is live.
- Rollback notes are weak if they do not distinguish code rollback from data or queue side effects.
- A release plan should identify the first bad signal worth acting on, not only the ideal success dashboard.
- Reliability decisions deserve plain language because incident responders often use them under time pressure.
- Feature flags reduce exposure only when the surrounding migrations and background work respect the same boundary.
- Observability is incomplete if it cannot separate the newly changed path from ambient platform noise.
- High-risk changes should document who can stop the rollout and by what evidence.
- Good release validation keeps the team from shipping blind optimism dressed as confidence.
- Post-release review is where release engineering compounds; skipped reviews force teams to relearn the same lessons later.
