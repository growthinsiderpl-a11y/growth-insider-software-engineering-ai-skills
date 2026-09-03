# Observability Baseline

Define the minimum logs, metrics, traces, health indicators, and review windows required so a new or changed software path can be understood in production.

## When To Run It

- adding a new service, worker, API, or critical page flow
- shipping behavior that can fail silently
- moving from development confidence to production confidence
- incident reviews exposed blind spots
- teams need a first production instrumentation baseline
- release readiness depends on post-deploy evidence

## Do Not Run It When

- instrumenting everything without a question to answer
- using observability as a substitute for testing
- discussing vendor dashboards instead of signals
- adding logs with no owner or response expectation
- cases where the change is too small to justify new telemetry

## Inputs

- critical path description
- failure modes
- operator owner
- release method
- existing telemetry assets
- privacy or security constraints

## Procedure

1. Choose questions
   - List what operators must know during normal and failing behavior.
   - Tie signals to decisions, not curiosity.
2. Define events and metrics
   - Select the few signals that prove throughput, success, and failure.
   - Avoid vanity signal expansion.
3. Shape logs
   - Ensure logs identify the path, the outcome, and the correlation keys allowed.
   - Keep privacy boundaries intact.
4. Trace the flow
   - Add tracing or request correlation where multi-step diagnosis matters.
   - Prefer continuity over volume.
5. Set review windows
   - Decide when the new signals must be checked after release.
   - Match intensity to risk.
6. Document operational meaning
   - Explain what bad looks like and what action follows.
   - Without this, telemetry is only decoration.

## Decision Tests

- Signals answer release and incident questions.
- Operators can connect signals to the changed path.
- Telemetry volume is disciplined.
- Privacy and security constraints are respected.
- Review timing and owners are explicit.

## Outputs

- signal list
- log field guidance
- metric definitions
- review window
- operator action notes

## Failure Modes

- logging raw data that no one should store
- adding many metrics with no threshold or owner
- skipping correlation keys for multi-step flows
- making dashboards before defining questions
- assuming traces alone explain business outcomes

## Review and Follow-through

- Revisit after the first incident or noisy alert.
- Trim telemetry that adds no decisions.
- Promote temporary release signals only if they keep proving useful.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Observability Notes

- Signals should answer the first operational questions, not every possible future curiosity.
- Good baselines distinguish success, degraded success, and outright failure paths.
- Correlation identifiers matter most where workflows cross services, jobs, or user-visible retries.
- Telemetry fields should be deliberate enough to survive long-term maintenance.
- Logging that cannot be safely retained should not become the primary diagnostic plan.
- Review windows help teams avoid discovering too late that nobody checked the new path.
- Temporary rollout metrics should be promoted only if they continue to drive decisions.
- Observability quality is visible when on-call engineers can explain what happened without guesswork.
- Revisit the baseline after the first real incident or alert burst.
