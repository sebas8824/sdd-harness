# Contributing to `<project>`

`<One paragraph: what this is and what it is built on.>` Work is **spec-driven** and every artifact
written to disk is in `<language>`.

This document explains what is **MANDATORY** (PR-blocking) and what is a **SIGNAL** (a convention to
follow, not yet a gate). Being explicit about which is which is what stops signals from being treated
as optional, and gates from being argued with. Architecture invariants live in [`AGENTS.md`](AGENTS.md);
decisions live in [`docs/architecture/adr/`](docs/architecture/adr/).

---

## TL;DR

- **Never push directly to `<mainline>`.** Branch as `feature/NNN-name` and merge via PR.
- Every PR needs **passing CI** and one approval.
- The gate is `<the exact clean command>`. An incremental build is not a verification.
- Enable the local hooks once per clone: `git config core.hooksPath .githooks`.
- Copy `.env.example` to `.env` (gitignored) before running the stack.
- `<language>` only — code, comments, docs, commit messages, UI copy defaults.

## Branching & merge

```
<mainline>              ← the single, protected mainline
  └── feature/NNN-name  ·  fix/NNN-name
```

- All changes land via pull request; a PR merges only with green CI.
- Do not merge a PR into another feature branch — retarget a stacked PR to the mainline first, or its
  work never reaches the mainline.
- Keep commits scoped: one logical change per commit, one commit per planned task.

## MANDATORY — PR-blocking gates

| Gate | What it requires | Enforced by |
|------|------------------|-------------|
| **Build** | Everything compiles, tests pass, formatting is clean | `<command>` — `.github/workflows/<file>` |
| **Sensitive-paths ADR gate** | A change to a path in [`SENSITIVE-PATHS.md`](docs/architecture/adr/SENSITIVE-PATHS.md) carries an `ADR-NNNN` reference in the commit message or PR body | `.github/workflows/config-policy.yml` |
| **Agent instructions in sync** | Project-owned skills and the reviewer roster are identical across agent trees | `.github/workflows/config-policy.yml` |
| **`<contract regeneration>`** | Generated contracts are regenerated in the same PR as the change | `<command>` |

## SIGNAL — conventions, not yet gated

- Comment only the non-obvious *why*, once (`code-commenter`).
- No `Object`-shaped types in a signature you own.
- A request's query count does not grow with the rows it returns.
- Every deferral names a target feature or phase.
- Deprecated APIs are a standing review criterion, not a per-task request.

## Review

Every implementation PR gets independent, risk-matched review after a stable implementation and its
targeted checks. See [`AGENTS.md`](AGENTS.md) and the `subagent-driven-development` skill. The PR body
records what was fixed, what was deferred and to where, and what was rejected with the reason.
