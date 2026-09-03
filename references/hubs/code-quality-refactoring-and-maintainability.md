# Code Quality, Refactoring, and Maintainability

Use this hub when code already works, but the cost of change is rising: unclear names, deep functions, hidden coupling, unstable seams, noisy dependencies, and refactors that need to improve the code without breaking delivery momentum.

## What This Hub Owns

- maintainability diagnosis grounded in visible code traits
- refactor sequencing and safety boundaries
- naming, function shape, and information hiding decisions
- module-level cohesion and interface slimming
- error-handling clarity and failure-path readability
- reduction of accidental complexity in everyday change flow
- test seam creation to make future refactors cheaper
- duplication review based on cause rather than aesthetics
- technical debt articulation without fake scores
- review standards for changeability and design clarity
- pragmatic clean-code guidance tied to repository context
- maintainability support for long-lived delivery teams

## What This Hub Does Not Own

- vanity rewrites without operational or change pressure
- abstract style arguments that do not affect change cost
- marketing copy quality
- product feature selection
- infrastructure procurement choices
- search ranking strategy without code changes
- design taste critiques that do not affect implementation
- organization change unrelated to repository health

## Questions To Answer First

- What change became expensive, and why?
- Which files attract edits because the structure forces them to?
- Where are names hiding meaning rather than clarifying it?
- What branch of logic is hardest to test or reason about?
- Which duplication reflects missing abstraction, and which reflects healthy separation?
- What information should stay hidden behind a deeper module?
- Which refactor can pay down friction without opening large blast radius?
- Where do error paths sprawl across unrelated responsibilities?
- What accidental dependencies make local reasoning hard?
- How much of the problem is readability versus architecture versus missing tests?
- Which risks require characterization tests before movement?
- What proof will show the refactor improved changeability?

## Required Inputs

- representative files or diffs showing the pain
- existing test coverage or its absence
- recent review comments repeating the same quality issue
- hotspot files with frequent churn
- naming conventions or team standards already in force
- language-specific constraints that affect idiomatic structure
- production incidents linked to complexity or hidden behavior
- module boundaries that are repeatedly bypassed
- error patterns visible from logs or bug history
- areas where onboarding time is highest
- performance constraints that limit naive refactors
- release pressure that bounds how much can change now

## Evidence Signals

- function length, nesting, and argument count
- debug leftovers, TODO markers, and duplicated branches
- files that mix domain policy and transport glue
- naming mismatches between code and business language
- implicit contracts enforced only by comments
- test brittleness or absence around critical seams
- control flow that hides failure handling
- interfaces that reveal implementation detail
- churn concentrated in oversized modules
- operator pain caused by unreadable recovery logic

## Working Rules

- Refactor for a concrete next change, not to display taste.
- Prefer smaller interfaces to broader inheritance.
- Comments should explain intent or constraint, not restate code.
- Reduce branches by making states explicit.
- A deep module is good when callers need to know less.
- Use naming to compress domain meaning, not to inflate ceremony.
- Delete dead paths before optimizing live ones.
- One refactor should have one reviewable objective.
- If the tests are weak, strengthen the seam before large movement.
- Do not collapse duplication until you understand why it exists.
- Visible complexity is sometimes safer than hidden magic.
- Keep recovery paths readable because operators use them under stress.

## Recommended Workflow

- Describe the expensive change in operational terms.
- Inspect the smallest code surface that explains the cost.
- Mark smells that are facts, not preferences.
- Separate naming, structure, and coupling issues.
- Choose a refactor boundary with acceptable blast radius.
- Add characterization tests where needed.
- Move one design decision at a time.
- Re-read the code as a future maintainer would.
- Check whether the next likely change became simpler.
- Capture follow-on refactors without forcing them into one PR.

## Common Failure Modes

- rewriting stable code just because it looks old
- introducing abstraction to avoid making a decision
- shrinking functions while scattering the narrative across files
- mistaking lint cleanliness for maintainability
- using comments to patch naming failures
- removing duplication while creating shared mutable helpers
- coupling tests to refactor internals
- deleting context that future debugging depends on
- combining refactor and behavior change without explicit safeguards
- hiding complexity in utility modules with no owner

## Expected Deliverables

- maintainability findings list
- refactor target ordering
- risk-aware sequence of changes
- characterization test recommendations
- interface simplification plan
- naming corrections tied to domain meaning
- error-path cleanup opportunities
- module-depth rationale
- review checklist for future changes
- evidence-backed reasons to defer work that is not yet justified

## Hand-offs and Escalation

- to testing when safeguards must expand before refactoring
- to architecture when maintainability pain reveals boundary issues
- to implementation planning when the refactor should be phased
- to release work when risk requires gating or feature flags
- to frontend quality if component maintainability is the bottleneck
- to security review if the cleanup touches sensitive code paths
- to product only when behavior ambiguity blocks safe cleanup
- to developer workflow when repeated review defects need automation

## Playbooks To Load Next

- `references/playbooks/code-maintainability-review.md`
- `references/playbooks/refactor-plan.md`
- `references/playbooks/secure-coding-review.md`
- `references/playbooks/dependency-direction-review.md`

## Deterministic Tools

- `scripts/quality/find_maintainability_violations.py`
- `scripts/architecture/validate_dependency_direction.py`

## Review Checklist

- Every finding points to observable code, not taste.
- Large files are flagged with the risk they create.
- Deep nesting is traced to a responsibility problem.
- Names are evaluated against domain meaning.
- Abstractions are justified by call-site simplification.
- Refactor plan includes rollback posture if risky.
- Tests protect current behavior before internal movement.
- Comments are reviewed for usefulness and drift.
- Error handling is readable from top to bottom.
- Dependencies exposed by public interfaces are minimized.
- Utilities have owners or are kept local.
- Deferred cleanup is recorded instead of forgotten.
- One PR can explain its maintainability goal clearly.
- No opaque debt score is used as proof.
- Outputs help future reviewers preserve the gains.
- Complexity is reduced where change actually happens.
- Performance-sensitive paths are not casually destabilized.
- The resulting code is simpler to extend, not only prettier.
- Module contracts are more stable after the refactor.
- Future work is framed as evidence-backed opportunities.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Refactoring Field Notes

- Maintainability work earns priority when it shortens future change paths, narrows review scope, or clarifies recovery behavior.
- The cleanest-looking abstraction can still be harmful if it forces readers to jump across too many files to understand one rule.
- Information hiding is practical only when callers truly need less knowledge after the refactor than before it.
- Refactors should preserve the debugging story; removing signal-rich structure for elegance alone is usually a loss.
- Naming reviews are most useful when they tie code to stable domain meaning instead of stylistic preference.
- Large helpers that absorb unrelated branching often deserve to be split by decision type rather than by line count alone.
- A useful maintainability finding should tell a future engineer what change would likely go wrong in the current code.
- Comment cleanup matters most where stale comments actively mislead implementation or operations.
- Good refactoring notes make it clear what was intentionally left alone and why.
