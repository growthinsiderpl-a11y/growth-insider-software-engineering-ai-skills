# Contributing

## Principles

- preserve Growth Insider identity and authorship
- keep engineering scope separate from product and marketing skill families
- prefer deterministic tooling over opaque scoring
- label evidence, assumptions, heuristics, and unknowns explicitly
- avoid mandatory network dependencies in the core package

## Before opening a change

Run:

```text
python scripts/validate_repository.py
python -m pytest tests/ -q
```
