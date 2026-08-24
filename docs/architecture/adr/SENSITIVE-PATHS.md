# Sensitive paths — ADR-required changes

Paths in **this** repository whose modification carries governance weight. Changing one must be
accompanied by an `ADR-NNNN` reference in the commit message (or the PR body). This file is the
harness dogfooding its own gate; the copy-ready version for your project is
[`../../../templates/SENSITIVE-PATHS.md`](../../../templates/SENSITIVE-PATHS.md).

> **Status: enforced.** `.githooks/commit-msg` and `.github/workflows/config-policy.yml` read the
> globs below. **Put the reference in the commit message** — the local hook never sees the PR body.

## Listed paths

| Path (glob) | Why it is sensitive |
|-------------|---------------------|
| `AGENTS.md` | The always-loaded instruction template — the thing this project exists to define. |
| `.claude/agents/**` | The reviewer roster and its governing contract clauses. |
| `.claude/skills/**` | On-demand instruction modules shipped to adopters. |
| `.githooks/**` | The gates themselves — changing a gate is an architectural act. |
| `.github/workflows/**` | CI policy. |
| `docs/architecture/adr/SENSITIVE-PATHS.md` | This governance list. |
| `templates/**` | What every adopting repository copies; a change here propagates. |

## How to use it

```bash
git config core.hooksPath .githooks
```
