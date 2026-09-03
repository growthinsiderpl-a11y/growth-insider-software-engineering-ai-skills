# Testing, Validation, and Quality Engineering

Use this hub when confidence is the bottleneck: test strategy, behavioral coverage, characterization before refactor, risk-based validation, evidence for release gates, and keeping quality engineering tied to real failure modes instead of ritual coverage growth.

## What This Hub Owns

- test strategy by risk, seam, and change type
- unit, integration, contract, UI, and end-to-end coverage choices
- validation design for migrations, rollouts, and critical workflows
- quality gates that prove readiness without slowing every change equally
- characterization testing ahead of refactors
- boundary and failure-path verification
- fixture discipline and deterministic local evaluation
- quality review for observability, rollback, and smoke paths
- regression prevention tied to known incident classes
- developer-friendly validation loops in the repository
- evidence-backed QA scope, not blanket script accumulation
- test architecture that stays maintainable under product growth

## What This Hub Does Not Own

- manual process theater with no failure model
- coverage percentage worship disconnected from risk
- bug triage ownership beyond quality implications
- performance benchmarking without release or user impact
- product acceptance decisions unrelated to software behavior
- marketing experiments and attribution analysis
- security certifications beyond engineering issue spotting
- roadmap prioritization

## Questions To Answer First

- What can break that matters to users, operators, or data integrity?
- Which risks are best caught in milliseconds, and which require realistic integration?
- Where do we need confidence in contracts rather than implementation details?
- What part of the current behavior is intentionally preserved during change?
- Which tests provide real information before merge?
- What validations are too slow or noisy to be default?
- Where do flaky dependencies require seams or simulators?
- Which release actions need explicit smoke checks?
- What evidence would let a reviewer approve with confidence?
- Which defect classes have happened before and deserve permanent guards?
- What remains unknown after local tests pass?
- How will the team know a failure is a real defect versus fixture drift?

## Required Inputs

- change description and expected blast radius
- critical user journeys and API contracts
- known fragile integrations or environment dependencies
- incident history and recent regressions
- current test pyramid or lack of it
- runtime constraints for local and CI execution time
- migration steps or rollout mechanics
- test data shape and privacy constraints
- observability signals available after deployment
- flaky test history if it exists
- quality expectations from regulated or high-risk domains
- release cadence that influences gate strictness

## Evidence Signals

- defects that escaped earlier test stages
- gaps between stated contracts and asserted behavior
- tests that fail to model failure paths
- fixtures that hide production variability
- areas where review depends on intuition rather than proof
- slow tests that still do not catch the important risk
- missing smoke paths around rollback or migrations
- untested idempotency or retry-sensitive logic
- UI paths with no accessibility or rendering assertions
- CI outputs that are green but uninformative

## Working Rules

- Test the most dangerous thing at the cheapest faithful seam.
- Characterization first when behavior is unclear.
- Use integration tests for contracts and wiring, not every branch.
- A flaky test is a quality defect in the validation system.
- Cover failure and recovery paths that operators rely on.
- Do not promise certainty the evidence does not support.
- Prefer explicit invariants to snapshot sprawl.
- Keep fixtures close to the behavior they prove.
- Smoke paths should be short, decisive, and release-relevant.
- Every test should answer a review question.
- CI should surface evidence, not just pass/fail theater.
- Unknowns after testing must be stated, not implied away.

## Recommended Workflow

- Classify risk by user impact, data impact, and rollback cost.
- Pick the minimum set of test layers that cover that risk.
- Protect current behavior before internal movement.
- Write validations around the contract or invariant.
- Run local checks that mirror the intended gate.
- Inspect failures for signal quality as well as correctness.
- Add targeted smoke tests for rollout-sensitive changes.
- Record residual risk that tests cannot resolve.
- Align CI outputs with reviewer decisions.
- Revisit the test plan when incidents teach something new.

## Common Failure Modes

- adding end-to-end tests because design seams are poor
- asserting implementation trivia instead of behavior
- treating snapshots as a substitute for thinking
- allowing flaky checks to normalize mistrust
- testing only happy paths on high-risk workflows
- copying fixtures that silently drift from real inputs
- using manual QA as a patch for missing engineering discipline
- omitting rollback validation from release-critical changes
- measuring success by count of tests rather than decisions supported
- pretending local green status removes all uncertainty

## Expected Deliverables

- risk-based test strategy
- validation layers mapped to failure modes
- characterization test notes for legacy areas
- CI gate recommendations
- smoke path definitions
- release validation evidence expectations
- residual risk statement
- fixture and data guidance
- review checklist for quality-sensitive changes
- follow-up work if current confidence remains insufficient

## Hand-offs and Escalation

- to release readiness when validation informs the gate
- to maintainability work when poor design drives overtesting
- to observability work when post-release evidence is essential
- to frontend quality when rendering or accessibility needs checks
- to security review when misuse or abuse cases need tests
- to architecture when contract confusion causes test sprawl
- to workflow automation when repeated checks should be scripted
- to product only if expected behavior itself is unresolved

## Playbooks To Load Next

- `references/playbooks/test-strategy-design.md`
- `references/playbooks/production-readiness-gate.md`
- `references/playbooks/release-validation.md`
- `references/playbooks/observability-baseline.md`

## Deterministic Tools

- `scripts/release/validate_release_readiness.py`
- `scripts/validate_behavioral_evals.py`

## Review Checklist

- Tests are chosen by risk, not habit.
- Critical workflows have explicit assertions.
- Failure paths receive purposeful coverage.
- Characterization exists before dangerous refactors.
- Fixtures are deterministic and readable.
- CI checks map to clear review decisions.
- Flaky behavior is treated as a defect.
- Rollback or migration paths have validation evidence.
- Contract tests guard important integrations.
- Accessibility and UI flows are not ignored where relevant.
- Residual uncertainty is written down.
- Validation cost matches change risk.
- Test ownership is clear after merge.
- Signal quality is improved alongside coverage.
- Release gates use explicit evidence.
- The team can rerun important checks locally.
- No false certainty is implied from green pipelines.
- Historical regressions have durable safeguards.
- New tests remain maintainable.
- Quality engineering helps decisions, not ceremony.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Validation Field Notes

- Test strategy improves when every layer exists to answer a distinct review question rather than to satisfy inherited habit.
- Characterization tests are especially valuable in legacy zones where intent is hidden but behavior must be preserved.
- Validation cost should rise with release risk, not with personal anxiety about the code.
- CI checks become durable when developers can explain why each one deserves to block a merge.
- Useful smoke tests are brief enough to run under stress and specific enough to detect the risky failure class quickly.
- Flaky tests damage decision quality even when they fail rarely, because they train teams to discount the signal.
- A failed validation should teach the next action, not merely announce disappointment.
- Residual uncertainty belongs in the engineering output, especially when live conditions can still surprise a well-tested change.
- Strong quality engineering narrows unknowns without pretending to eliminate them.
