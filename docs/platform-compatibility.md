# Platform Compatibility

Verification date: `2026-09-03`

## Sources
- Agent Skills specification: https://agentskills.io/specification
- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI Build Skills guidance: https://learn.chatgpt.com/docs/build-skills
- GitHub Actions `actions/checkout` v7: https://github.com/actions/checkout/releases
- GitHub Actions `actions/setup-python` v7: https://github.com/actions/setup-python/releases
- Citation File Format 1.2.0 entity author form: `authors[].name`
- pytest 9.1.1: https://github.com/pytest-dev/pytest/releases/tag/9.1.1

## Compatibility claims
- `DESIGNED_FOR`: open Agent Skills compatible runtimes
- `STATICALLY_VALIDATED`: manifests, paths, docs, scripts, and tests are locally checked
- `LOCALLY_TESTED`: deterministic tools and repository tests run locally
- `NOT MODEL TESTED`: no claim is made about live execution quality on any specific hosted model runtime
- `LOCAL WORKFLOW CONTRACT VALIDATED`: GitHub Actions workflow files and pinned CI dependencies are present and locally consistent; remote GitHub CI has not been executed

## Notes
- `agents/openai.yaml` is an adapter-oriented descriptor, not a guarantee of hosted execution behavior
- adapters document intended usage patterns for popular runtimes
- core validation avoids network coupling so the repository remains portable

## Release-engineering contract
| Item | Value |
| --- | --- |
| PYTHON_RUNTIME_SELECTED | 3.12.14 |
| WHY | Matches the Growth Insider Executive AI Skills family CI runtime for consistent validation |
| LOCAL_VALIDATION_HOST | Python 3.11.9 (local workstation) |
| LOCAL_VALIDATION_RESULT | PASS on repository validator, behavioral validator, pytest, and compileall |
| actions/checkout | v7 |
| actions/setup-python | v7 |
| CI dependency file | `requirements-ci.txt` |
| CI dependency pin | `pytest==9.1.1` |
| Workflow permissions | `contents: read` |
| CFF `repository-code` | omitted until a real GitHub repository URL exists |
| CFF author form | entity `name: Growth Insider` |
| Social preview | `assets/github-social-preview.jpg` (1280×640) |
