# API and Service Design

Design or review an API or service contract so responsibilities, payloads, errors, idempotency, and evolution paths are coherent for both implementers and consumers.

## When To Run It

- adding a new endpoint, service operation, or event contract
- payloads and errors are inconsistent across similar paths
- client coupling or versioning concern is rising
- service boundaries need consumer-facing clarity
- integration design matters before implementation proceeds
- operators need reliable behavior under retries or partial failure

## Do Not Run It When

- database schema tuning with no contract change
- pure UI component design work
- endpoint naming bikeshedding absent deeper contract issues
- cases where product semantics are not yet decided at all
- using API design to paper over architecture confusion elsewhere

## Inputs

- use cases and callers
- current data model and ownership
- failure and retry expectations
- security and authorization posture
- evolution constraints
- observability needs for the contract

## Procedure

1. Frame the contract
   - Name the consumer task the API or service supports.
   - Clarify ownership of the underlying action.
2. Design payload boundaries
   - Keep inputs and outputs specific to the use case.
   - Avoid leaking persistence detail.
3. Design outcomes
   - Specify success, validation errors, business-rule failures, and transient failures distinctly.
   - Do not collapse everything into generic errors.
4. Handle retries and idempotency
   - Define keys, duplicate handling, or conflict posture where relevant.
   - Make at-least-once realities explicit.
5. Plan evolution
   - Consider optionality, versioning, or additive change posture.
   - Prefer contracts that can grow without surprise.
6. Add verification and observability
   - Define tests and signals that confirm contract behavior.
   - Make production diagnosis feasible.

## Decision Tests

- The contract serves a clear consumer task.
- Payloads avoid unnecessary internal detail.
- Error categories help callers act correctly.
- Retry and idempotency behavior are explicit when relevant.
- Evolution path is considered.

## Outputs

- contract outline
- payload guidance
- error model
- idempotency notes
- verification plan

## Failure Modes

- mirroring the database instead of designing an interface
- using one generic error path for all outcomes
- forgetting consumer impact during internal refactors
- ignoring retries until incidents force the issue
- creating versioning policy with no actual change strategy

## Review and Follow-through

- Re-run when a second consumer or integration arrives.
- Pair with architecture review if service ownership is unclear.
- Tie release and observability notes into readiness work for risky contracts.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## API Design Notes

- Contracts should help callers act correctly under both success and partial failure, not simply expose available fields.
- Error models are part of the interface shape and should not be treated as afterthoughts.
- Payload boundaries are healthier when they reveal domain intent rather than storage convenience.
- Idempotency guidance matters most on operations users or systems may retry automatically.
- Keep consumer needs visible when discussing internal service evolution.
- Operational diagnostics belong in the contract conversation when failures cross network boundaries.
- If the underlying ownership is unclear, fix that before expanding the public interface surface.
- Prefer additive evolution paths that do not surprise existing consumers.
- Reassess the contract when a second class of consumer begins using it differently.
