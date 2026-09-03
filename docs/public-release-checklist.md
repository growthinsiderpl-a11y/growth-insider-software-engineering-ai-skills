# Public Release Checklist

Status vocabulary: `PASS` · `FAIL` · `NOT VERIFIED` · `NOT APPLICABLE` · `BLOCKED`

Verification date: 2026-09-03  
Package status: `RELEASE_CANDIDATE` · `STATICALLY_VERIFIED` · `LOCALLY_TESTED` · `NOT MODEL TESTED` · `NOT GIT RELEASED`

## Local package validation

| Check | Status |
| --- | --- |
| `python scripts/validate_repository.py` | PASS |
| `python scripts/validate_behavioral_evals.py` | PASS |
| `python -m pytest tests/ -q` | PASS |
| `python -m compileall -q scripts tests` | PASS |
| Root identity matches `manifest.json` / adapters | PASS |
| License is MIT with Copyright (c) 2026 Growth Insider | PASS |
| Legacy active product authorship scan | PASS |
| Local-path / secret / cache scan | PASS |
| Core tools remain network-independent | PASS |
| README states `NOT MODEL TESTED` | PASS |
| README public Markdown indentation defect absent | PASS |
| Examples are illustrative, not performance promises | PASS |
| `CITATION.cff` has no fake `repository-code` | PASS |
| CI workflow contract present (`requirements-ci.txt` + least-privilege Actions) | PASS (LOCAL WORKFLOW CONTRACT VALIDATED) |

## Not yet verified

| Check | Status |
| --- | --- |
| GitHub Actions run on GitHub-hosted runners | NOT VERIFIED |
| Git repository initialized / pushed | NOT VERIFIED |
| GitHub repository settings / topics / About | NOT VERIFIED |
| Live Agent Skills model selection testing | NOT VERIFIED / NOT MODEL TESTED |
| Social preview uploaded to GitHub | NOT VERIFIED |

## Notes

Do not treat this checklist as proof that GitHub CI has executed. Local validation and the workflow contract are verified; remote CI remains a post-Git task.
