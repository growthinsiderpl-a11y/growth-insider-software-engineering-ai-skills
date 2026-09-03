# Architecture Boundary Assessment

Assess whether the current or proposed system boundaries match responsibility, failure isolation, and change flow.

## When To Run It

- multiple modules change together for one behavior
- business rules leak into frameworks or transport layers
- teams argue about ownership of logic or data
- new features require touching too many services or packages
- testing the core path is expensive because seams are weak
- the architecture diagram looks cleaner than the repository reality

## Do Not Run It When

- pure product scoping questions
- UI polish work without boundary pressure
- requests that only need a bug fix in one small unit
- debates driven by team politics rather than code evidence
- large rewrite ambitions with no named constraint

## Inputs

- repository paths for the affected flow
- current request or event lifecycle
- data ownership cues
- recent changes that crossed boundaries
- constraints on latency, consistency, and release risk
- tests proving or failing to prove current seams

## Procedure

1. State the decision
   - Write the boundary question in one sentence.
   - Tie it to a business or reliability consequence.
2. Trace the flow
   - List entry points, decision points, persistence, and side effects.
   - Mark where ownership is unclear.
3. Map current boundaries
   - Name modules or services by responsibility.
   - Record what each unit must know to do its job.
4. Inspect dependency direction
   - Check whether inner policy depends on outer implementation.
   - Note concrete violations and the import paths involved.
5. Stress the seams
   - Ask how retries, failures, and future changes travel across boundaries.
   - Flag coordination that depends on hidden knowledge.
6. Propose minimum changes
   - Limit options to the few that materially improve ownership.
   - Reject aesthetic reshuffles with no operational gain.
7. Define follow-through
   - Specify implementation slices, tests, and telemetry needs.
   - Record what remains intentionally unchanged.

## Decision Tests

- A boundary exists in code, not only in language.
- The proposed change reduces multi-file or multi-service coordination for a common task.
- Ownership and failure handling are clearer after the change.
- The boundary can be validated with tests or telemetry.
- The change does not introduce more indirection than the real constraint requires.

## Outputs

- boundary map
- violation list
- recommended target structure
- risk notes
- implementation sequence

## Failure Modes

- treating packaging changes as architecture progress
- splitting modules by framework artifact rather than responsibility
- ignoring rollback or migration cost
- adding services to mimic modern architecture trends
- keeping ambiguous ownership because naming sounded good enough

## Review and Follow-through

- Re-run after the first implementation slice if behavior still crosses seams.
- Revisit if the same defect class reappears in adjacent modules.
- Escalate to system design when the boundary issue reveals topology change.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Boundary Review Notes

- Favor evidence from code paths and ownership conflicts over preference for a named architecture pattern.
- If the same business rule crosses multiple handlers, ask whether orchestration has drifted rather than assuming reuse is the answer.
- Document one non-goal so boundary cleanup does not silently turn into a rewrite.
- Keep the assessment readable enough that another engineer can challenge the conclusion precisely.
- Note which seams need tests before structural movement starts.
- Record where release risk begins if the boundary change affects persistence or public contracts.
- If no meaningful ownership conflict exists, say that and avoid forced restructuring.
- Tie the recommendation to the next change the team expects to make.
- Review again once the first slice lands and the code reveals whether the boundary is holding.
