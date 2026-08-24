# Lessons log

A running record of **process failures worth not repeating** — what happened, why it happened, and
which convention changed as a result. Distinct from [`DEFERRED.md`](DEFERRED.md), which tracks work
punted to a later feature: this file tracks *how we work*, not *what is left to build*.

> **Why this file exists.** Skills carry the **shape** of a failure and never a PR number, branch,
> feature id, or symbol from this codebase. That evidence has to live somewhere or the rule becomes an
> assertion nobody can audit — so it lives here. When a lesson changes a skill, the entry names the
> skill, so the rule can be re-derived if it is ever trimmed or a maintainer asks "why is this here?".

> **What earns an entry.** A failure whose cause was *procedural*, not a one-off mistake: something a
> convention could have prevented, or that an existing convention failed to prevent. A bug found and
> fixed by a working gate is not a lesson — that is the gate doing its job.

## Entry format

Each entry states: **What happened** (concrete, with the evidence), **Root cause** (the procedural
gap, not the symptom), **Change made** (which skill or convention — or explicitly none), and
**Durable lesson** (the sentence worth carrying to another repository).

---

## YYYY-MM-DD — `<short title: the failure, not the feature>`

**What happened.** `<Concrete. Name the artifacts. A number the reader can check beats an adjective.>`

**Root cause.** `<The procedural gap. "The reviewer missed it" is a symptom; "nothing required the fix
to carry a failing test" is a cause.>`

**Change made.** `<Which skill, gate, or convention changed — or explicitly "none, and why".>`

**Durable lesson.** `<One sentence, portable to a repository that shares none of this context.>`
