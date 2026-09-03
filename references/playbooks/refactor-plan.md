# Refactor Plan

Turn maintainability or architecture findings into a risk-aware refactor sequence that improves the code without disguising behavior changes or destabilizing release flow.

## When To Run It

- the code needs internal improvement before major feature work
- an architecture correction must be phased
- legacy behavior needs preservation while structure changes
- a single cleanup attempt would create too much blast radius
- teams need to align on refactor steps before coding
- tests and rollout strategy matter as much as code movement

## Do Not Run It When

- big-bang rewrite proposals without strong evidence
- cosmetic cleanup with no future change benefit
- cases where the cheapest answer is a direct feature implementation
- refactors that depend on product choices still unresolved
- efforts with no available safety net or characterization path

## Inputs

- maintainability or architecture findings
- current tests and critical behavior notes
- release or migration constraints
- team capacity and timeline pressure
- known hotspots and integration risks
- acceptable residual debt after this phase

## Procedure

1. Define the payoff
   - State what future change becomes easier.
   - Reject vanity refactors.
2. Protect behavior
   - Add characterization or contract tests first where needed.
   - Document fragile paths.
3. Slice the work
   - Break changes by seam, not by personal convenience.
   - Keep each slice reviewable.
4. Sequence dependencies
   - Do enabling moves before large internal shifts.
   - Separate behavior changes from structural changes when possible.
5. Plan validation
   - Match each slice to tests and local checks.
   - Include rollout safeguards for risky parts.
6. Plan reversibility
   - Name what can be rolled back cleanly and what cannot.
   - Avoid irreversible movement without strong reason.
7. Close the loop
   - Define the after-state and what debt remains intentionally.
   - Record follow-on opportunities without forcing them now.

## Decision Tests

- The plan names a concrete payoff.
- Behavior safety steps precede risky movement.
- Each slice is independently understandable.
- Validation matches the risk of the slice.
- The team can stop after a slice and still ship.

## Outputs

- refactor objective
- slice sequence
- safety plan
- validation plan
- deferred debt register

## Failure Modes

- front-loading all abstract cleanup before any payoff
- mixing hidden behavior changes into a structural plan
- overslicing into meaningless tiny moves
- underslicing into a risky mega-PR
- failing to define success beyond 'cleaner code'

## Review and Follow-through

- Re-evaluate after each slice for new information.
- Stop if the expected payoff is no longer worth the remaining risk.
- Escalate to architecture review if local refactoring uncovers systemic design issues.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Refactor Notes

- Plan slices around safety and comprehension, not only around folder ownership.
- If characterization tests are impossible, narrow the refactor until the risk becomes explainable.
- State which debt will remain after the plan so stakeholders do not assume total cleanup.
- Sequence enabling changes before structural moves that depend on them.
- The best refactor plan reduces review complexity one slice at a time.
- Use rollback language whenever a slice can affect production behavior indirectly.
- Keep behavior changes visible even when they feel small.
- Reassess after each slice because new understanding often changes the next best move.
- Stop if the refactor objective no longer justifies the remaining disturbance.
