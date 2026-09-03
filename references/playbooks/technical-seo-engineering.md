# Technical SEO Engineering

Investigate and remediate code-owned SEO issues by validating generated artifacts, tracing them back to templates or routing logic, and planning safe changes with explicit marketing handoff boundaries.

## When To Run It

- HTML output lacks or conflicts on metadata
- routing or rendering harms crawlability
- sitemap, robots, canonical, or structured-data artifacts need code changes
- site architecture work is required for discoverability
- a release or migration could create indexing regressions
- the request is technical SEO, not content strategy

## Do Not Run It When

- keyword research or editorial prioritization
- guaranteeing ranking changes from code hygiene
- live SERP analysis when only offline artifact work is requested
- one-page manual fixes when the template is broken
- marketing-owned discovery questions

## Inputs

- HTML samples or rendered routes
- robots.txt or sitemap files
- metadata generation code
- routing rules or templates
- known issue examples
- release sensitivity of the change

## Procedure

1. Confirm engineering ownership
   - State the technical artifact that is wrong.
   - Retire content-strategy work to marketing clearly.
2. Validate artifacts
   - Check title, description, canonical, robots, headings, lang, links, and structured data.
   - Use repeatable offline checks where possible.
3. Trace source
   - Find the template, builder, or route logic causing the issue.
   - Prefer fixing the repeated generator.
4. Plan the change
   - Choose the smallest durable fix.
   - Consider routing, locale, and redirect implications.
5. Check release overlap
   - Assess migration, rollout, and regression risk.
   - Treat broad route changes as release-sensitive.
6. Define follow-up
   - State what still requires live verification.
   - Separate marketing-owned next steps.

## Decision Tests

- The issue is code-owned.
- Artifact checks are explicit.
- The fix generalizes beyond one page.
- Release and regression risks are covered.
- Live-search unknowns are acknowledged.

## Outputs

- artifact findings
- template or routing fix plan
- release overlap notes
- marketing handoff note
- regression recommendations

## Failure Modes

- rewriting content to avoid fixing generators
- confusing canonical cleanup with site-architecture repair
- changing routes without redirect thinking
- presenting offline validation as ranking proof
- letting marketing scope flood back into engineering delivery

## Review and Follow-through

- Repeat after major route or template migrations.
- Add repository-level checks if the issue could recur widely.
- Coordinate with accessibility review where semantics overlap.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Technical SEO Notes

- Template fixes are usually more valuable than route-by-route edits because they remove entire classes of regression.
- If the page content itself is weak, say that it is a marketing follow-up instead of stretching engineering scope.
- Route, canonical, and redirect rules should be reviewed together whenever URL behavior changes.
- Structured data should be maintained like code, with repeatable generation and inspection paths.
- Keep artifact findings separate from ranking speculation so the deliverable stays honest.
- Technical SEO changes may require release discipline when they affect large site sections.
- Accessibility and semantics can strengthen the same page outputs that support discoverability.
- Add regression checks when the same metadata bug could recur across templates.
- Revisit after rollout if live crawl or indexing evidence later contradicts the offline expectation.
