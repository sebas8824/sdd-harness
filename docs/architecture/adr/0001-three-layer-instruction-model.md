# ADR-0001 — Three instruction layers, split by what a gate can catch

- **Status:** accepted
- **Date:** 2026-08-23

## Context

An agent's instruction file is paid for on every turn of every session. Left ungoverned it grows:
each incident adds a rule, each rule reads as reasonable in isolation, and within months the file
costs more than the work it guides — while the rules that actually matter are buried among reminders
that a linter already enforces.

The opposite failure is just as common. Rules pushed entirely into on-demand documents are never
loaded at the moment they would have prevented the defect, because the agent does not know it needs
them. "Read the conventions first" is not a mechanism.

## Decision

**1. Three layers, and one question decides which.** *Can a gate catch it?* → **Layer 3**, a hook or
CI job. *Does it need a trigger to be relevant?* → **Layer 2**, a skill or document. *Neither, and
failure is silent?* → **Layer 1**, `AGENTS.md`.

The rejected alternative was topical organization — architecture here, style there — which produces
files that are individually coherent and collectively unaffordable, because nothing in a topic tells
you when it is loaded.

**2. `AGENTS.md` is canonical for every harness; every other instruction file is a pointer.** Two
files of rules means two agents enforcing two versions of them, and the divergence reports itself to
nobody. Where a second tree is mechanically required, one is canonical and a gate holds the
project-authored copies byte-identical (`.githooks/skills-sync-check.py`).

**3. A rule enters Layer 1 only on the second occurrence of the correction.** A rule written on the
first occurrence is a guess, and guesses are what make the file too expensive to load. The evidence
that a rule earned its place lives in `docs/LESSONS.md`, so it can be audited or re-derived later.

**4. When a Layer 1 rule becomes mechanically checkable, write the gate and delete the rule.** A rule
kept "for emphasis" alongside its gate is duplicated cost for zero added safety.

## Consequences

- The always-loaded file stays thin as the project grows — the only outcome that keeps this
  sustainable over years.
- Adding a rule now requires an argument (twice-seen, ungateable), which is friction by design.
- A skill's `description` becomes load-bearing: it is the trigger, so it must name situations and
  symbols, not topics. A badly-described skill is an unloaded skill.
- Rules that *could* be gated but are not yet remain visible as `CONTRIBUTING.md` **SIGNAL** entries,
  so the gap between convention and enforcement is stated rather than assumed.

## Alternatives considered

- **One large instruction file.** Rejected: unbounded context cost, and no signal about which rules
  matter for the change at hand.
- **Everything in on-demand skills.** Rejected: the rules that prevent silent corruption are exactly
  the ones an agent does not know to load.
- **Rules as documentation only, no gates.** Rejected: a rule with no enforcement decays to a rule
  people argue about in review, which is the most expensive place to enforce anything.
