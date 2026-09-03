# Release Validation

Validate the release path itself: preflight checks, smoke sequence, artifact correctness, rollout readiness, and the first signals that confirm the change is behaving in the wild.

## When To Run It

- preparing a risky deployment or public package release
- shipping metadata, routing, or build changes that can break broad surfaces
- migrations or new background jobs are involved
- teams need a short operational checklist distinct from test strategy
- release notes or version artifacts matter to downstream users
- the main concern is shipping safely, not designing the system

## Do Not Run It When

- substituting release validation for real testing
- running full incident retrospectives before any release exists
- long-term architecture decisions
- feature ideation disguised as a release discussion
- changes whose only risk is editorial wording

## Inputs

- version or change identifier
- smoke paths
- artifact expectations
- rollout controls
- monitoring entry points
- operator notes

## Procedure

1. Verify artifacts
   - Check versions, manifests, generated outputs, and static contracts.
   - Ensure the package or build contains what it claims.
2. Run preflight checks
   - Execute validators and targeted tests.
   - Confirm dependencies and configuration are in expected state.
3. Rehearse the smoke path
   - Use the shortest decisive checks that exercise the risky path.
   - Record expected signals and failure interpretation.
4. Confirm rollout controls
   - Verify flags, cohorts, or deployment sequencing.
   - Avoid discovering control gaps during deployment.
5. Prepare first-hour observation
   - Name dashboards, logs, and ownership.
   - Set stop conditions before release.
6. Close the loop
   - Document release outcome and follow-up review timing.
   - Treat validation artifacts as part of the release record.

## Decision Tests

- Artifacts match declared identity.
- Smoke checks are specific and executable.
- Rollout controls are ready before deployment.
- Operators know where to look first.
- The release record is reviewable afterward.

## Outputs

- release checklist result
- artifact verification notes
- smoke sequence
- first-hour observation plan
- release record

## Failure Modes

- mistaking build success for release readiness
- running smoke checks that avoid the changed path
- forgetting public metadata or docs in a package release
- not knowing who owns first-hour observation
- treating release output as disposable memory

## Review and Follow-through

- Use during every meaningful release.
- Trim or expand checks as failure classes become clearer.
- Feed lessons back into repository validators and docs.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Release Notes

- Separate artifact validation from runtime smoke checks so failures are easier to interpret.
- Use the release record as an operational asset, not a disposable announcement checklist.
- First-hour observation should focus on signals that would justify rollback or pause.
- If release controls are weak, note that explicitly instead of assuming careful operators can compensate.
- Package releases should verify identity, docs, and examples alongside tests.
- Smoke steps should be short enough to execute under pressure.
- The same check should ideally be runnable locally before the release window opens.
- Release validation becomes more valuable when it closes the loop into future workflow improvements.
- Re-run after late changes even if the original release candidate looked clean.
