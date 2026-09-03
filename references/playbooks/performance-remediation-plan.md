# Performance Remediation Plan

Plan a code-level remediation of user-facing performance issues by linking symptoms to bottlenecks, selecting the highest-payoff fixes, and defining measurable verification.

## When To Run It

- pages or interactions feel slow
- assets or scripts are suspected to block user tasks
- render churn affects responsiveness
- the team needs a fix order rather than generic optimization advice
- performance work must be balanced with release risk
- technical SEO or UX quality overlaps with rendering efficiency

## Do Not Run It When

- optimizing without any observable symptom
- chasing synthetic scores without user impact
- rewriting architecture when a narrow render fix is enough
- assuming every issue is JavaScript-related
- making performance promises without measurement plans

## Inputs

- affected page or flow
- symptom description
- known measurements if any
- rendering and asset model
- critical user tasks
- release tolerance for change

## Procedure

1. State the symptom
   - Name the slow behavior from the user perspective.
   - Separate load, interaction, and background freshness issues.
2. Find the bottleneck class
   - Determine whether the main suspect is network, execution, render, layout, or data.
   - Avoid generic fixes before classification.
3. List candidate remediations
   - Generate a short list of code changes tied to the bottleneck.
   - Include cost and likely payoff.
4. Prioritize minimum-sufficient fixes
   - Choose changes that materially improve the user path first.
   - Do not default to system-wide rewrites.
5. Define verification
   - Specify local checks, profiling, or user-path observation.
   - State what remains uncertain without production telemetry.
6. Plan release
   - Consider flags, monitoring, and rollback if the path is sensitive.
   - Performance fixes still require safe delivery.

## Decision Tests

- The bottleneck class is named.
- Each remediation targets a cause, not only a symptom.
- Verification exists for before and after.
- Release risk is weighed against performance gain.
- Unknowns are stated honestly.

## Outputs

- prioritized remediation list
- bottleneck classification
- verification plan
- release notes
- follow-up monitoring needs

## Failure Modes

- cargo-cult memoization
- compressing assets while ignoring render thrash
- moving work off-screen without improving the real task
- making broad changes for tiny user benefit
- treating performance work as immune from regression risk

## Review and Follow-through

- Revisit after the first remediation lands.
- Escalate to architecture review if the bottleneck is systemic.
- Capture durable patterns in docs or shared components if they repeat.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Performance Notes

- Remediation should start from the user-visible symptom, not from a favorite optimization technique.
- Separate improvements that reduce work from those that merely delay work.
- Keep expensive broad rewrites off the plan unless narrower fixes cannot address the real bottleneck.
- If performance depends on rendering model choices, say whether the issue is local or architectural.
- Verification plans should mention what local measurement can show and what production telemetry still must confirm.
- Performance wins that harm maintainability should be justified carefully.
- Tie each recommendation to a likely payoff window so teams can order the work rationally.
- Frontend and release implications belong in the same plan when user-critical paths are affected.
- Reorder the plan if early fixes reveal the original bottleneck diagnosis was incomplete.
