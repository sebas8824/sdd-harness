# Adopting the harness

Four steps, in this order. Each asks a decision of you; none of them is a copy-paste job on its own.

## Step 1 — The instruction layer

Copy `AGENTS.md` and `CLAUDE.md` to your repository root. Then fill in `AGENTS.md`:

- **The one-line product statement.** What it is, who it is for.
- **The architecture invariants.** Few, absolute, checkable in a minute by a reviewer. These are the
  PR-blocking ones — a boundary that must never be crossed, where identity comes from, what extension
  looks like, what a new public contract must pass, where tunables live.
- **The key development rules.** Start with the shipped ones and delete what does not apply. Add your
  own only when the same correction has been made **twice** — a rule added on the first occurrence is
  a guess.
- **The verification command.** Name the exact clean command that counts as a gate run.

Apply the filter for every line you add: *can a gate catch it?* Then it belongs in Step 3, not here.

## Step 2 — The documentation model

```bash
mkdir -p docs/architecture/adr docs/specs docs/session docs/api tasks
```

Copy from [`../templates/`](../templates/): `adr-0000-template.md`, `adr-README.md`,
`SENSITIVE-PATHS.md`, `ROADMAP.md`, `DEFERRED.md`, `LESSONS.md`, `PROJECT.md`,
`session-START.md`, `spec-template.md`, `plan.md`, `todo.md`, `handoff.md`.

Decisions this step asks of you:

- **Your phases and their green criteria.** A phase without an observable green criterion never ends.
- **Your sensitive paths.** Start with config, secrets templates, CI workflows, the hooks directory,
  the instruction file, the reviewer roster, and any identity/tenancy code. The list itself is listed.
- **Write ADR-0001 today**, before there is a backlog: the shape of the repository and the boundary
  that defines it. The first ADR is the one that makes the rest feel natural to write.

Then read [`DOCUMENTATION-MODEL.md`](DOCUMENTATION-MODEL.md) once, in full. It is the part of the
harness that will not survive being skimmed.

## Step 3 — The gates

```bash
cp -R ../sdd-harness/.githooks .
cp ../sdd-harness/.github/workflows/config-policy.yml .github/workflows/
git config core.hooksPath .githooks     # once per clone — say so in CONTRIBUTING.md
```

- The **sensitive-paths** gate works as shipped; it reads your `SENSITIVE-PATHS.md`.
- The **skills-sync** gate only matters if you maintain a mirror tree for a second harness. Set
  `PROJECT_OWNED` and the tree paths at the top of the script; if you have no mirror, delete the job.
- Add your build/test workflows beside it and list every gate in `CONTRIBUTING.md`, split into
  **MANDATORY** (PR-blocking, with the command and the workflow file) and **SIGNAL** (a convention,
  not yet a gate). Being explicit about which is which is what stops signals from being treated as
  optional and gates from being argued with.

## Step 4 — The agent layer

```bash
cp -R ../sdd-harness/.claude .
mv .claude/settings.example.json .claude/settings.json
mv .mcp.example.json .mcp.json          # set the absolute cwd for your repo
```

- Install [Agent Skills](https://github.com/addyosmani/agent-skills) — see [`TOOLS.md`](TOOLS.md).
- Fill in the two project-owned skill stubs: `project-architecture` and `project-code-standards`.
  They are the on-demand half of `AGENTS.md` — the examples, the rationale, the long checklists.
- Keep the reviewer roles as shipped unless a real surface is missing one. **Do not invent roles for
  surface you do not have**: a role for infrastructure you have never written is a reviewer that
  reports on nothing. Delete them and recover them from git history if that changes.

## Step 5 — The first session

Write `docs/session/START.md` at the end of your first real session, while you still remember what a
cold agent would not know. Then start every subsequent session by reading it, and update it as work
moves. Everything in it that turns out to be durable gets promoted — to `AGENTS.md`, an ADR, or a
skill — and deleted from there.

---

## What "done adopting" looks like

- An agent opening the repo cold reads `AGENTS.md`, then `docs/session/START.md`, and knows what to do.
- Every rule in `AGENTS.md` fails **silently** if broken — nothing there duplicates a gate.
- The last three decisions you argued about are ADRs.
- Nothing was deferred without a target.
- The last review pass left a record in the PR of what was fixed, deferred, and rejected.
