# Evidence and Uncertainty

Use the philosophy sequence:

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`

## Evidence classes

- `FACT_USER`: directly provided by the user
- `FACT_FILE`: supported by repository files, generated artifacts, or static output
- `FACT_TOOL`: produced by a deterministic local script in this package
- `FACT_EXTERNAL`: grounded in an external source only when the runtime explicitly provides one
- `CALCULATION`: arithmetic or deterministic transformation from supplied facts
- `ASSUMPTION`: a working assumption required to move forward
- `HYPOTHESIS`: a proposed explanation or remediation that still needs verification
- `UNKNOWN`: something material that cannot be honestly inferred yet

Additional optional labels:

- `POLICY`
- `EXAMPLE`
- `HEURISTIC`
- `BENCHMARK`

## Rules

- Never turn `ASSUMPTION` into `FACT_FILE`.
- Never present a local artifact check as proof of production behavior.
- When the issue crosses into product strategy or marketing ownership, say so explicitly.
- When release risk is material, connect evidence to rollout, rollback, and review timing.
- When the task is technical SEO, keep claims inside code-owned artifact quality and site architecture.
