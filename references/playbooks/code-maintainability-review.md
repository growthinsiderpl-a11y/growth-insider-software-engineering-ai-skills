# Code Maintainability Review

Review code for maintainability using explicit, observable traits that affect change cost rather than opinion or composite debt scores.

## When To Run It

- reviewing a risky or growing code area
- preparing a refactor plan
- auditing repeated review or bug patterns
- estimating why simple changes have become slow
- screening a codebase before handing it to a broader team
- turning vague quality complaints into concrete findings

## Do Not Run It When

- performing line-by-line style policing
- assessing generated code with the same criteria as hand-written code
- reviewing without representative files or diffs
- using a fake numerical quality score
- treating every smell as urgent regardless of context

## Inputs

- representative files or changed files
- hotspot modules if known
- test coverage clues
- recent bugs or incidents linked to the area
- repository standards already accepted
- delivery constraints on how much can change

## Procedure

1. Choose the scope
   - Limit the review to a coherent surface.
   - Prefer hotspots or active change areas.
2. Collect facts
   - Use deterministic checks for obvious violations.
   - Read code for naming, cohesion, and hidden contracts.
3. Group findings
   - Separate naming, structure, coupling, and recovery-path issues.
   - Keep findings actionable.
4. Assess change cost
   - Explain how each finding slows implementation, review, or debugging.
   - Avoid generic cleanliness language.
5. Prioritize
   - Order work by risk and expected payoff.
   - Keep low-value cleanup out of the critical path.
6. Recommend safeguards
   - Add tests or validators if they reduce repeat defects.
   - Document what should remain manual judgment.
7. Close with next steps
   - Define which fixes belong now, later, or never.
   - Make the deferral logic explicit.

## Decision Tests

- Every finding points to a concrete code trait.
- Review output distinguishes severe issues from niceties.
- Recommendations reduce future change cost.
- No composite quality score replaces explanation.
- Deferred work has a reason, not only a placeholder.

## Outputs

- maintainability findings
- risk-ranked priorities
- refactor candidates
- validator suggestions
- deferred-work notes

## Failure Modes

- equating maintainability with personal style
- reviewing too much code too shallowly
- recommending rewrites instead of targeted fixes
- missing how tests or architecture drive the problem
- using generic clean-code slogans as evidence

## Review and Follow-through

- Repeat after refactors to confirm the change actually helped.
- Use findings to seed a narrow refactor plan.
- Feed recurring defect classes into repository automation where appropriate.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Maintainability Notes

- Prefer findings that describe how the current code impedes the next change or obscures a failure path.
- Long files are not automatically bad; explain the specific reasoning cost they create.
- Record whether the main pain is coupling, naming, structure, or validation gaps.
- Keep lower-priority cleanup visible but separate from high-risk maintainability defects.
- A good review can recommend leaving stable code alone when the payoff is weak.
- Distinguish code that is dense because the problem is hard from code that is dense because design choices drifted.
- If tooling catches a pattern reliably, prefer that over repeating the same manual review comment forever.
- Use examples sparingly and only to make a finding concrete.
- Review again after a refactor to confirm the predicted change-cost reduction happened.
