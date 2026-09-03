# Technical SEO and Site Architecture

Use this hub only when search visibility depends on engineering work: crawlable markup, metadata generation, routing, canonicalization, sitemap and robots artifacts, internal linking structures, and site architecture decisions that must be changed in code.

## What This Hub Owns

- technical SEO tasks that require code or repository changes
- server or build logic for metadata, canonicals, and robots
- routing and URL architecture for crawlable site behavior
- sitemap generation and validation
- structured data implementation in code
- internal-linking mechanics controlled by templates or components
- rendering choices that affect crawlability and discoverability
- migration-safe SEO implementation during releases
- engineering review of duplicate, missing, or conflicting signals
- offline artifact validation for HTML and related files
- site architecture guidance grounded in implementation constraints
- handoffs to marketing when content strategy, not code, is the real issue

## What This Hub Does Not Own

- keyword research, content briefs, or positioning strategy
- link-building or digital PR
- SERP trend prediction or external ranking guarantees
- copywriting quality beyond technical signal checks
- market selection or audience strategy
- analytics storytelling without code implications
- paid acquisition strategy
- general GEO advice that does not touch the repository

## Questions To Answer First

- What search problem exists because of code or site architecture, not content strategy?
- Which signals are missing, duplicated, or contradictory in output HTML?
- Does the rendering model expose the important content to crawlers reliably?
- How are canonicals, alternates, and indexability decided in code?
- What URL patterns or redirects may create waste or confusion?
- Which templates control the repeated problem?
- How will the change be validated offline before deployment?
- What release risk appears if metadata or routes change at scale?
- Where do internal links depend on navigation code rather than editorial process?
- What remains unknowable without live crawl data or external search systems?
- Which user experience or accessibility consequences intersect the SEO fix?
- How will the team prevent regression on future pages?

## Required Inputs

- sample HTML or route outputs
- robots.txt and sitemap artifacts if available
- routing rules and metadata generation logic
- canonical rules, redirect maps, or template configuration
- SSR or prerender strategy for affected pages
- internal-linking components or menus
- known duplication or indexing complaints
- release history involving migrations or URL changes
- environment differences that affect output
- technical constraints of the CMS or framework
- stakeholder goal stated in engineering terms
- baseline examples of correct page output

## Evidence Signals

- missing titles, descriptions, canonicals, or lang tags
- noindex conflicts or accidental robots blocks
- structured data omitted or duplicated by templates
- client-only rendering for critical page content
- sitemap omissions or broken URL formatting
- inconsistent trailing slash, locale, or parameter handling
- navigation elements that fail to create stable internal links
- migration plans that overlook redirects
- headings that do not reflect page hierarchy
- offline checks revealing artifact drift between pages

## Working Rules

- Own only the engineering part of SEO.
- Never imply ranking guarantees from local artifact quality.
- Prefer template or generator fixes over one-page patches.
- Metadata logic must be deterministic and reviewable.
- Crawlability and usability should improve together where possible.
- Canonicals should resolve ambiguity, not mask duplicate architecture.
- Robots rules deserve the same review discipline as access control.
- Do not hide missing content strategy behind technical theatrics.
- Validate artifacts offline before discussing rollout confidence.
- Route changes require migration and redirect thought.
- Structured data should reflect visible truth, not aspiration.
- State clearly what needs live verification beyond the repository.

## Recommended Workflow

- Frame the SEO problem as a code or output problem.
- Inspect the generated artifacts and routing rules.
- Locate the template or build source of the repeated issue.
- Choose the smallest fix that generalizes correctly.
- Validate HTML, robots, sitemap, and metadata offline.
- Check overlap with accessibility and release risk.
- Prepare redirect or migration handling if URLs change.
- Document what remains unknown without live crawl data.
- Add regression validation where practical.
- Hand content-strategy questions back to marketing explicitly.

## Common Failure Modes

- answering keyword strategy with code architecture changes
- adding metadata that contradicts the visible page
- solving one route while leaving the generator broken
- changing URLs without redirect planning
- treating noindex as a cleanup bandage for architecture debt
- using client-side head injection for critical static pages without scrutiny
- assuming sitemaps fix weak internal linking design
- forgetting locale and canonical interactions
- claiming SEO success from artifact checks alone
- mixing marketing ownership back into engineering deliverables

## Expected Deliverables

- technical SEO engineering diagnosis
- artifact validation findings
- template or routing fix plan
- redirect or migration considerations
- regression guard recommendations
- boundary note for marketing-owned follow-up
- structured-data implementation notes
- offline validation evidence
- release-risk implications
- residual unknowns requiring live search tools

## Hand-offs and Escalation

- to marketing when content or keyword strategy is the real blocker
- to frontend implementation when templates or components drive the issue
- to release readiness for large route or metadata changes
- to testing for regression automation
- to accessibility/performance when output quality overlaps
- to architecture when site structure reflects broader design debt
- to observability when live validation is needed post-release
- to product only if route semantics are business-rule driven

## Playbooks To Load Next

- `references/playbooks/technical-seo-engineering.md`
- `references/playbooks/release-validation.md`
- `references/playbooks/repository-scaffolding-workflow.md`
- `references/playbooks/ui-implementation-quality.md`

## Deterministic Tools

- `scripts/seo/check_technical_seo_artifacts.py`
- `scripts/release/validate_release_readiness.py`

## Review Checklist

- The problem is truly code-owned.
- Title, description, and canonical logic are inspectable.
- Indexability signals do not conflict.
- Robots and sitemap artifacts are validated offline.
- Structured data reflects visible content.
- Important content is crawlable from the chosen render model.
- Internal-linking mechanics are considered.
- Route changes include redirect thinking.
- Accessibility overlap is not ignored.
- Release risk is assessed.
- Unknowns needing live verification are stated.
- No ranking promises are implied.
- Templates are fixed before page-by-page patches.
- Metadata logic is deterministic.
- Regression checks can catch repeat issues.
- Marketing handoff boundaries are explicit.
- The implementation remains maintainable.
- Site architecture changes preserve user clarity.
- The answer stays inside engineering ownership.
- The repository gains durable technical SEO discipline.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## SEO Engineering Field Notes

- Technical SEO work is strongest when it improves repeated template output rather than producing one-off metadata patches.
- Route and canonical logic deserve the same precision as API routing because both control how systems interpret public surfaces.
- Structured data is useful only when it reflects visible truth and survives template reuse cleanly.
- Search-facing artifacts should be validated alongside accessibility and release implications when a broad site surface is involved.
- Engineering ownership ends where content strategy begins, and that boundary should remain visible in the deliverable.
- Offline artifact checks are valuable because they catch preventable regressions before deployment, not because they can predict rankings.
- Redirect thinking belongs in the earliest stages of URL architecture changes, not as a launch-week patch.
- SEO regressions often reveal weaknesses in metadata generation discipline that also affect maintainability.
- Durable site-architecture fixes usually simplify both crawler interpretation and human navigation.
