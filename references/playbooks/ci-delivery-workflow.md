# CI Delivery Workflow

Shape a continuous-integration and delivery workflow that catches meaningful defects quickly, aligns with local development, and supports reliable releases without needless ceremony.

## When To Run It

- CI is slow, noisy, or missing critical checks
- local and remote validation disagree
- repository rules should be enforced automatically
- release confidence depends on better pipeline structure
- public package maintenance needs stable validation gates
- teams repeatedly hit the same preventable merge blockers

## Do Not Run It When

- treating CI as a dumping ground for every script
- adding remote-only checks when local reproduction is impossible
- workflow changes unrelated to real delivery defects
- cases where architecture or test design is the actual bottleneck
- turning approval policy debates into pipeline design work

## Inputs

- current local commands
- current CI steps and pain points
- test and validator runtime costs
- release expectations
- repository contract rules
- recurring defect patterns

## Procedure

1. Map the loop
   - List what developers run locally and what CI runs remotely.
   - Spot duplication, gaps, and timing problems.
2. Prioritize signal
   - Keep only checks that answer a real merge or release question.
   - Separate must-block from advisory outputs.
3. Align environments
   - Make local commands mirror CI where practical.
   - Avoid unreproducible failures by design.
4. Structure the pipeline
   - Order fast decisive checks before slower broader ones.
   - Fail clearly when the repository contract breaks.
5. Support release needs
   - Add or preserve gates for versioning, packaging, or readiness evidence.
   - Do not overload every PR with release-only weight if not needed.
6. Review the operator experience
   - Check whether failures teach the fix.
   - Pipeline output should reduce, not increase, confusion.

## Decision Tests

- CI checks map to real decisions.
- Developers can reproduce failures locally.
- Fast checks fail early.
- Release-sensitive checks are present where needed.
- Failure output is actionable.

## Outputs

- workflow diagnosis
- pipeline structure recommendation
- local-command contract
- blocking-versus-advisory split
- follow-up automation ideas

## Failure Modes

- optimizing minutes while losing trust in the results
- using CI to compensate for absent contributor docs
- keeping checks no one believes in
- making pipelines platform-dependent for no reason
- forgetting public-release validation needs

## Review and Follow-through

- Review after incidents, flaky periods, or major repo shifts.
- Tune the workflow when a check becomes noisy or obsolete.
- Keep the smallest effective pipeline for the repository's risk level.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## CI Workflow Notes

- Pipelines should fail early on repository-contract breaks and later on broader behavioral checks when both are needed.
- Local reproducibility is part of CI quality because it determines whether failures teach or frustrate.
- Keep blocking checks tied to clear risk; everything else should be advisory or removed.
- Public package repositories should validate docs and metadata with the same seriousness as code structure.
- Use workflow changes to eliminate repeated contributor pain, not to display process sophistication.
- Cross-platform simplicity helps both adoption and maintenance of the pipeline.
- If a validator becomes noisy, improve the rule or downgrade the gate rather than teaching contributors to ignore it.
- Treat pipeline output as product copy for engineers: concise, specific, and corrective.
- Revisit the workflow after major repo shifts or repeated false negatives.
