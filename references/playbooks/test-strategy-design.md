# Test Strategy Design

Design a risk-based validation approach that selects the cheapest faithful test layers for the behavior, failure modes, and rollout profile involved.

## When To Run It

- a new feature or refactor needs planned confidence
- the current tests are noisy, slow, or misaligned
- release-critical behavior lacks clear validation
- legacy behavior needs characterization before movement
- CI should be adjusted to match actual risk
- teams disagree on how much testing is enough

## Do Not Run It When

- defaulting to end-to-end tests for every problem
- coverage target discussions without change context
- testing strategy for code that is not yet technically understood
- audit work that only needs one tactical test suggestion
- requests whose real issue is architecture or dependency direction

## Inputs

- change description and impact radius
- critical workflows and failure paths
- available seams and current tests
- release sensitivity and rollback cost
- integration dependencies and flake risks
- runtime or CI budget constraints

## Procedure

1. Model risk
   - List user, data, and operational failure modes.
   - Rank them by consequence and likelihood.
2. Pick layers
   - Choose unit, integration, contract, UI, or smoke tests intentionally.
   - Explain what each layer must prove.
3. Design fixtures
   - Keep test data minimal and realistic enough.
   - Avoid brittle incidental detail.
4. Protect failure paths
   - Add tests for retries, rollbacks, or edge conditions that matter.
   - Do not test every impossible branch.
5. Align with CI
   - Decide what runs by default locally and remotely.
   - Keep feedback loops proportionate.
6. State residual risk
   - Say what tests cannot prove.
   - Define live verification if needed.
7. Review the strategy
   - Check whether the plan answers reviewer questions.
   - Trim low-value tests before they are written.

## Decision Tests

- Risk drove the strategy, not habit.
- Each test layer has a purpose.
- Default checks are affordable enough to be run.
- Important failure modes are covered somewhere.
- Residual uncertainty is acknowledged honestly.

## Outputs

- risk matrix
- test-layer plan
- fixture guidance
- CI alignment notes
- residual risk statement

## Failure Modes

- treating more layers as automatically better
- writing slow tests to compensate for poor seams
- omitting operator or rollback risks from the plan
- assuming green CI means complete confidence
- forgetting to trim tests that add no decision value

## Review and Follow-through

- Revisit if flakiness or runtime cost grows disproportionately.
- Update after incidents reveal missing failure modes.
- Use the strategy as a review baseline for future related changes.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Strategy Notes

- A short test plan with clear reasons is better than a long checklist disconnected from risk.
- Treat contract and failure-path coverage as first-class when the system integrates with other services.
- Keep the local developer loop in mind so the strategy is actually used.
- Residual uncertainty should point to a live check, a future test, or an accepted risk.
- If the main issue is poor seams, note the design work needed instead of compensating only with heavier tests.
- Clarify which checks block merge and which only inform later review.
- Prefer assertions on invariant behavior over incidental formatting or internal choreography.
- Use historical regressions to justify durable tests, not blanket expansion.
- Revisit strategy after the change ships and the real failure pattern is known.
