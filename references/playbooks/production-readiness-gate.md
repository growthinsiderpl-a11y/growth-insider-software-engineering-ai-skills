# Production Readiness Gate

Run an explicit readiness gate before shipping a meaningful change by requiring concrete evidence on rollout, rollback, observability, testing, operations, and unresolved risk.

## When To Run It

- shipping infrastructure, migration, auth, payment, or indexability changes
- rollout risk is higher than routine feature work
- teams need a common release approval frame
- a hot path or critical workflow is affected
- incident history suggests extra discipline is warranted
- a public package release needs final validation evidence

## Do Not Run It When

- lightweight low-risk typo or copy fixes
- using a gate as a substitute for doing the engineering work
- assuming a feature flag alone makes everything safe
- treating the checklist as passable without evidence
- mixing launch marketing approvals into engineering release readiness

## Inputs

- test evidence
- rollout method
- rollback path
- observability assets
- operator owner
- known residual risks

## Procedure

1. Collect evidence
   - Gather tests, smoke paths, dashboards, and migration notes.
   - Do not accept implied evidence.
2. Check reversibility
   - Name how exposure can be reduced or undone.
   - Call out one-way effects clearly.
3. Review observability
   - Ensure new paths are visible in logs, metrics, or traces.
   - Require operator-facing clarity.
4. Review operational ownership
   - Name who watches the release and how long.
   - Avoid anonymous accountability.
5. Evaluate residual risk
   - List what remains uncertain and why shipping is still acceptable or not.
   - Separate known risk from ignored work.
6. Decide and document
   - Return ready or not ready with explicit reasons.
   - Record required follow-up if conditionally ready.

## Decision Tests

- Evidence is concrete.
- Rollback posture is honest.
- Observability covers the new path.
- Owner and review window are named.
- Residual risk is accepted consciously.

## Outputs

- gate result
- missing evidence list
- rollout notes
- rollback notes
- follow-up actions

## Failure Modes

- treating documentation as evidence when it was never exercised
- ignoring data migrations during approval
- approving because deadlines are loud
- using vague readiness language
- failing to name the conditions for safe rollout

## Review and Follow-through

- Repeat if the change scope grows.
- Use the gate output during post-release review.
- Improve the checklist after incidents or near-misses.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Readiness Notes

- The gate is strongest when each required item maps to a failure class the team actually cares about.
- Missing evidence should remain visible even if leadership chooses to ship anyway.
- Rollback posture must mention data and background effects, not just application binaries.
- Operator ownership should include who watches the change and how they know when to intervene.
- A release is not ready if observability cannot isolate the changed path.
- Conditional readiness should come with explicit follow-up tasks and timing.
- Keep the gate short enough to be used, but strict enough to block false confidence.
- Review the checklist after incidents so it evolves from lived operating lessons.
- Public package releases deserve the same evidence discipline as service releases.
