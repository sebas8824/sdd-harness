---
name: project-code-standards
description: <project> language and code conventions. Use when writing or reviewing any code in this repository — naming, tunables, data access, error handling, component patterns, and the stack-constraint checklist.
---

# `<project>` code standards

> **Stub — fill this in.** Everything a gate already enforces (formatting, lint, import order) belongs
> in the gate, not here. This file carries what a reviewer would otherwise have to say out loud on
> every PR. Rename to `<project>-code-standards` and update `.claude/skills/README.md`.

## Stack constraints

| Constraint | Version / choice | What breaks if it is quietly changed |
|---|---|---|
| `<…>` | `<…>` | `<…>` |

## Naming

`<The conventions that are not obvious from the language: what a file, a type, a test, and a public
contract are each called, with one example of each.>`

## Data access

- `<The query-count rule, with the shape that violates it.>`
- `<What a write returns, and why nothing reads back.>`
- `<What a bulk write owns that the ORM would otherwise have done.>`

## Types

- `<The banned shapes in a signature you own, and the two or three real exceptions.>`
- `<Where a record / sealed type / projection replaces a loose map.>`

## Errors

`<The error model: the type, the status mapping, what a client can bind to, what is logged where.>`

## Tunables

`<Where configuration lives, how a new tunable is declared, and what its default must be so the day it
ships nothing behaves differently.>`

## Tests

- `<The slice to reach for first, and when to escalate.>`
- **Prove a new test bites** — remove the behaviour it names, watch it fail, restore it.

## Review checklist

- [ ] Deprecated APIs: none introduced; current replacement named for any found.
- [ ] Comments: non-obvious *why* only, once (`code-commenter`).
- [ ] Contracts regenerated in this PR.
- [ ] Every punt has a target in `DEFERRED.md`.
