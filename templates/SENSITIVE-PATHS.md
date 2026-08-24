# Sensitive paths — ADR-required changes

Paths whose modification carries architectural or security weight. Changing one in a PR **must be
accompanied by an `ADR-NNNN` reference** (or a clear justification in the PR description where an ADR
is disproportionate).

> **Status: enforced.** The `commit-msg` hook (`.githooks/commit-msg`) and the `config-policy` CI
> workflow fail a change touching a listed path unless an `ADR-NNNN` reference appears in the commit
> message or the PR body.
>
> **Put the reference in the commit message.** The local hook only ever sees the message, so a
> body-only reference fails before it reaches CI. In CI the body is accepted, but the check re-runs on
> an edit only because the workflow opts into the `edited` event — the default `pull_request` types do
> not include it, so a body added after a red run would otherwise leave the gate red until an
> unrelated push. The commit message is the carrier that works in both places.

## Listed paths

Backtick-quoted globs in this section are what the gate reads. `**` spans directories; `*` stays
within a path segment; a single `{a,b}` group is expanded.

| Path (glob) | Why it is sensitive |
|-------------|---------------------|
| `.env`, `.env.local` | Hold real local credentials (gitignored). Structural changes to what they carry matter. |
| `.env.example` | The committed config surface. A new key here signals a new credential or tunable. |
| `<app>/**/config/**`, `<app>/**/application*.{yml,yaml,properties}` | Service configuration: secret references, ports, wiring. |
| `docker-compose.yml` | Local infrastructure: credentials and exposed ports. |
| `.github/workflows/**` | CI policy: what runs on a PR, and any use of repository secrets. |
| `.githooks/**` | Local enforcement hooks — changing a gate is an architectural act. |
| `docs/architecture/adr/SENSITIVE-PATHS.md` | This governance list itself. |
| `AGENTS.md`, `.claude/agents/**` | The always-loaded instructions and the reviewer roster: changing what every agent is told, or which reviewer sees a change, governs every later PR. |
| `<app>/**/identity/**`, `<app>/**/tenant/**` | Identity and tenant resolution — the invariants nothing else can restore. |

## Anticipated (add when the code lands)

- `<security configuration, once it exists>`
- `<data isolation / provisioning code, once it exists>`

## How to use it

Enable the local gate once per clone:

```bash
git config core.hooksPath .githooks
```

Adding a path is itself a listed change: reference the ADR that justifies the policy edit.
