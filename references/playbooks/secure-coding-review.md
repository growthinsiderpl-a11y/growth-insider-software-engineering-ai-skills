# Secure Coding Review

Review software changes for code-level security weaknesses, trust-boundary confusion, risky defaults, and missing validation without pretending to replace a dedicated security program.

## When To Run It

- auth, sessions, permissions, secrets, uploads, or external inputs change
- new endpoints or service integrations are added
- legacy code paths handle sensitive data or privileged actions
- reviewers need a focused secure-coding pass during implementation
- release readiness depends on trust-boundary confidence
- the repository lacks explicit secure-coding heuristics

## Do Not Run It When

- claiming formal assurance from a code review alone
- broad compliance interpretation outside engineering issue spotting
- marketing or product risk analysis
- infrastructure penetration testing tasks
- cases where no code or technical design is available

## Inputs

- changed files or relevant modules
- input sources and trust boundaries
- authz/authn model as implemented
- data sensitivity of affected paths
- error handling behavior
- deployment and logging implications

## Procedure

1. Map trust boundaries
   - Identify external input, privileged operations, and data exits.
   - Mark where assumptions cross boundaries.
2. Review validation and encoding
   - Check parsing, validation, escaping, and canonicalization appropriate to the context.
   - Look for gaps rather than perfection theater.
3. Review authorization posture
   - Confirm privileged actions verify the right actor and scope.
   - Do not assume upstream enforcement without evidence.
4. Review secret and data handling
   - Check whether sensitive material is stored, logged, or exposed unnecessarily.
   - Prefer least disclosure.
5. Review failure behavior
   - Inspect error paths, retries, and defaults for unsafe fallbacks.
   - A graceful failure can still be insecure.
6. Close with remediation
   - Prioritize must-fix findings and residual concerns.
   - State when specialized security review is warranted.

## Decision Tests

- Trust boundaries are named.
- Findings point to concrete code behavior.
- Must-fix issues are separated from good-practice suggestions.
- Logging and error behavior are included.
- Escalation boundaries are explicit.

## Outputs

- secure-coding findings
- trust-boundary notes
- remediation priorities
- release-risk notes
- escalation recommendations

## Failure Modes

- assuming framework defaults solved everything
- focusing only on input validation while ignoring authorization
- logging sensitive failures too helpfully
- marking theoretical issues with no code path or consequence
- confusing security culture statements with code review output

## Review and Follow-through

- Run again when sensitive flows expand.
- Escalate to dedicated security review if critical trust boundaries move.
- Feed stable lessons into repository guidance or validators.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Secure Coding Notes

- Focus first on trust boundaries and privileged outcomes before cataloging lower-severity hygiene issues.
- Authorization checks deserve the same scrutiny as input validation because safe parsing does not prevent unsafe action.
- Error paths can leak capability or data even when happy paths look well guarded.
- Security findings should describe exploitability conditions in concrete repository terms where possible.
- If an issue depends on infrastructure guarantees, note the dependency rather than assuming it holds everywhere.
- Logging recommendations should balance diagnosis with unnecessary data exposure.
- Escalate clearly when the repository review cannot establish enough confidence alone.
- Favor fixes that simplify the trust boundary rather than adding fragile compensating checks.
- Re-run focused review after sensitive interfaces or integrations expand.
