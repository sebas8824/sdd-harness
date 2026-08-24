# AGENTS.md

Canonical, always-loaded instructions for **any** coding agent (Claude Code, Codex, OpenCode, Qwen
Code, Gemini CLI, …). `CLAUDE.md` — and any other harness's instruction file — is a thin pointer to
this file. **Edit HERE, never there.**

> **This file is a template.** Replace every `<…>` placeholder with your project's reality, delete
> what does not apply, and keep the *shape*: a thin index plus rules no gate can catch.

This file is a **thin index**: it holds only what an agent needs every session, and points to
on-demand files for the rest, so it never bloats the context window. Load the linked files only when
the task needs them.

**`<project-name>`** — `<one sentence: what this product is and who it is for>`.

On-demand references (load when relevant):
- Architecture overview: `docs/architecture/` (canonical design spec: `docs/specs/<YYYY-MM-DD>-<topic>.md`)
- Decision records (ADRs): `docs/architecture/adr/`
- Project config (vision, stack, roles): `docs/PROJECT.md`
- Roadmap (phases, green criteria): `docs/ROADMAP.md`
- Deferred work log (implementation-level punts, by target feature/phase): `docs/DEFERRED.md`
- Lessons log (process failures and the convention each one changed): `docs/LESSONS.md`
- Skills index: `.claude/skills/README.md`
- Session start prompt: `docs/session/START.md`

## Language Policy

**Everything written to disk is in `<language, e.g. English>`**: code, doc comments, specs, roadmap
entries, commit messages, docs, tool descriptions, UI copy defaults. Conversation with the developer
may be in any language; artifacts are not.

## Response & Editing Style

Applies to every response, and to every subagent report.

- **Lead with the answer.** No preamble, no restatement of the request, no closing summary of work
  already described. Skip "I'll now…" and "Great question".
- **Never paste code into the response.** Edits land in files; the response says what changed, where,
  and why it is correct. Show source only when asked, or when a few lines *are* the answer.
- **Comment the non-obvious `why`, nothing else — and say it once.** Default to no comment. A change
  that alters no behaviour alters no comment. Cite an ADR id rather than re-arguing it. **Writing,
  revising or deleting any comment: load the `code-commenter` skill.**

## Diagrams

**Documentation diagrams MUST use Mermaid** in fenced ` ```mermaid ` blocks — flows, sequences,
component diagrams — never ASCII art: it renders on GitHub and stays maintainable. Directory trees
may stay as plain ASCII in a code fence; Mermaid is for relationships and flows, not file listings.

## Git — Mandatory Rule

**NEVER run `git push` without the developer's explicit confirmation.** Local commits and branches
are allowed without asking. Never push directly to `<mainline>`; always work on a
`feature/NNN-name` branch.

**Never commit a secret or a large binary artifact.** Tokens, session secrets and API keys live only
in a gitignored `.env` (chmod 600). `.env.example` carries names, never values.

## Spec-Driven Development (SDD)

SDD runs on **[Agent Skills](https://github.com/addyosmani/agent-skills)** (MIT), adopted as an
installed dependency — not vendored into this repo. It provides the lifecycle commands and craft
skills: `/spec → /plan → /build → /test → /review → /ship`, which auto-activate the right skills by
context.

**Rules of use:**
- Use `/build` (a human reviews between tasks) — **never `/build auto`**. No vibecoding.
- Specs: `docs/specs/YYYY-MM-DD-<topic>.md`. Plans/tasks: `tasks/<feature>/plan.md`, `tasks/<feature>/todo.md`.
- Reviewer roles live in `.claude/agents/`, read as portable role prompts by every harness.
- One-time install per machine; the repo-local skill index is `.claude/skills/README.md`.

## Key Development Rules

> **What lives here:** only rules **no gate catches**, whose failure is silent and corrupting.
> Anything a gate already enforces, and all examples and rationale, live in a skill. When unsure, put
> it here — a redundant reminder costs tokens, a missing one costs a review pass.

Keep the ones below; add your own the same way — each earned by a failure that happened more than once.

- Do not write code without enough context — it avoids trial-and-error loops.
- Validate functionality before calling it done.
- **Count the database roundtrips.** A request's query count must not grow with the number of rows it
  returns. Batch by id into a map before the per-row loop; never query inside a loop. **Never read
  back what you just wrote** — a write returns what it stored. State the fixed query count in the
  doc comment of any method that assembles a page, so a later edit that breaks it is visible in review.
- **A bulk write owns what the ORM would have done for it.** A set-based `update` bypasses lifecycle
  callbacks, audit columns and optimistic-lock version bumps, so the statement must set them by hand.
  Left implicit, the row's audit columns name whoever last wrote it through the entity — worse than
  no audit trail at all.
- **`Object` is not a type — never put one in a signature you own.** No `Object`, `Object[]`, or
  `Map<String, Object>` as a parameter, return type, or field of code this repository writes. A
  positional array obliges every caller to index into it by hand and casts blind. Use a record, a
  projection, or a sealed type. An `unchecked` suppression is the same smell wearing a hat — if you
  need one, the type is wrong. `<List your narrow exceptions explicitly.>`
- **Never defer without a target.** Every `docs/DEFERRED.md` row states a **feature id or phase**, or
  is marked **Landed** or **Dropped (decision)**. Decide by blast radius: small and contained → do it
  now rather than write the row; large or blocked on a decision → schedule it in `docs/ROADMAP.md`.
  "No fixed target yet" is not an option — an untargeted row is a note nobody will action.

## Working Agreements

*How* to work here, as distinct from what the code must look like. Each of these is a correction the
developer had to make more than once, so it is written down rather than re-learned per agent.

- **Lead with a recommendation, not an option menu.** When there is a design choice, name the option
  you would pick and the trade-off that decides it. Make the reversibility argument explicit — a list
  of equally-weighted alternatives just hands the work back.
- **Deprecated APIs and code smells are standing review criteria**, not a per-task request. Before
  calling any task done, hunt for deprecated calls in the frameworks in use and name the current
  replacement. Green tests are not the bar.
- **Never claim a verification you did not run.** "`<verify command>` passes" in a PR body, commit
  message, or summary means the command was executed and its output read. Report failures with the
  output; say plainly when a step was skipped. A false green costs more than a red build. **And an
  incremental build is not a verification** — a non-clean run can execute stale test classes, so a new
  test can report green having never run.
- **Plan before a multi-file change.** For refactors and anything touching more than a couple of
  files, present the proposed change and wait for approval before editing — even when the request
  reads as a direct instruction. Read-only analysis is not the edit.
- **A deferral is the developer's call.** State the finding, recommend now-vs-later, and wait. "Needs
  a decision" describes the decision's difficulty, not the change's size — when the resulting edit is
  trivial, make it instead of recording it.
- **Propose the complete module, not the minimal slice.** For foundational concerns (identity,
  tenancy, persistence boundaries) the smallest thing that works reshapes everything landing on top of
  it. Name the target architecture, then sequence toward it.
- **Bulk edits run from a script file**, never an inline `sed -i` / `perl -i -pe` one-liner — command
  hooks mangle quoted one-liners into silent no-ops. Verify with `git grep` afterwards.
- **Spell dependencies in full** — never a bare short name; exact coordinates in declarations.
- **Answer short, and edit surgically.** Prefer the simple solution that works. Do not rewrite whole
  files, and do not repeat code already given in the same response.
- **A review pass produces a record.** State in the PR what was fixed, what was deferred and to which
  phase, and what was rejected with the reason. If the pass falsified something in
  `docs/architecture/**`, amend it in the same PR.
- **Review workflow:** every implementation PR gets independent, risk-matched review after a stable
  implementation and its targeted checks. See the `subagent-driven-development` skill.

## Architecture Invariants (PR-blocking)

Summary only — detail lives in the project's architecture skill and the architecture spec. Replace
these with yours; keep them few, absolute, and phrased so a reviewer can check one in a minute.

1. `<Invariant: a boundary that must never be crossed.>`
2. `<Invariant: where identity/tenant comes from, and where it must never come from.>`
3. `<Invariant: what extension looks like, and what "fix the abstraction instead" means here.>`
4. `<Invariant: what a new public contract must pass before it ships.>`
5. `<Invariant: where tunables live; what must be regenerated in the same PR.>`

## Knowledge-graph tools

This repository has a knowledge graph. Query the **code-review-graph** MCP tools before Grep/Glob/Read;
fall back to file scanning only where the graph does not reach. Tool-by-tool guidance lives in the
`explore-codebase`, `debug-issue`, `refactor-safely` and `review-changes` skills, and the same
reminder is injected on every prompt by the `UserPromptSubmit` hook in `.claude/settings.json` — a
harness without that hook must apply this rule from here.
