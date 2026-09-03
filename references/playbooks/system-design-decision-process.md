# System Design Decision Process

Make a bounded architecture or system-design choice using explicit constraints, few serious options, operational trade-offs, and measurable follow-through.

## When To Run It

- an implementation needs a design choice before coding
- scale, reliability, or consistency constraints are material
- multiple valid shapes exist and trade-offs matter
- leaders need a concise, reviewable recommendation
- a migration or topology change affects more than one component
- the current design works but will not survive the next demand level

## Do Not Run It When

- generic interview-style system design exercises
- small implementation details that do not change the operating model
- product requirement debates with no architecture trade-off
- requests that only need repository scaffolding
- cases where key constraints are still unknown and analysis must come first

## Inputs

- goal, scope horizon, and non-goals
- latency, throughput, correctness, and cost constraints
- current topology and pain points
- data ownership and integration dependencies
- release and migration limits
- operational maturity of the team

## Procedure

1. Frame the decision
   - Name the decision and the consequence of getting it wrong.
   - List hard constraints separately from preferences.
2. Describe the current state
   - Summarize how the system works now.
   - Note where evidence is weak or missing.
3. Generate few options
   - Keep to the minimum serious options.
   - Ensure each option is implementable, not rhetorical.
4. Evaluate trade-offs
   - Compare options on correctness, operability, simplicity, and future change.
   - Use explicit failure-mode thinking.
5. Select minimum-sufficient design
   - Choose the option that meets constraints with the least permanent complexity.
   - Record why other options lost.
6. Translate into delivery
   - Break the design into reviewable implementation slices.
   - Specify tests, telemetry, and rollout controls.
7. Plan review
   - Define signals that confirm or falsify the decision.
   - Schedule a later re-evaluation if uncertainty is material.

## Decision Tests

- The decision statement is precise enough to disagree with.
- Rejected options are rejected for clear reasons.
- The chosen design includes migration and rollout thinking.
- Measurement exists to validate the decision after release.
- The result helps coding start, not just discussion continue.

## Outputs

- decision memo
- trade-off table
- implementation slices
- telemetry and rollout notes
- review trigger list

## Failure Modes

- covering too many decisions in one design session
- pretending uncertainty does not exist
- choosing the most complex option because it is future-proof
- ignoring operational competence required by the design
- ending with principles only and no delivery path

## Review and Follow-through

- Reopen if the key constraint changes.
- Revisit after the first release if telemetry contradicts expectations.
- Archive the decision in repository docs if it will matter later.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Decision Notes

- Keep option count low enough that trade-offs can be discussed honestly.
- State the operating burden of the chosen design, not only its theoretical strengths.
- Record which unknowns are acceptable to carry into implementation and which are not.
- Use the same business constraint language from the request when justifying the design choice.
- If an option loses only on team operating maturity, say that plainly.
- Delivery sequencing is part of the design quality, not an appendix.
- Preserve one sentence on why the most obvious alternative was rejected.
- Designs become durable when they make failure behavior easier to reason about.
- Revisit the decision if real traffic or data shape contradicts the original assumptions.
