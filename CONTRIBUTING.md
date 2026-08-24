# Contributing to sdd-harness

This repository is a harness, so it holds itself to the harness. Changes are welcome; changes that
make the harness heavier need an argument.

## The bar for a new rule

A rule earns a place in `AGENTS.md` only if **no gate can catch it** and its failure is silent. If a
script can check it, contribute the script instead — a gate costs no context and never forgets.

A rule earns a place at all only if the same correction has been needed **twice**. A rule added on the
first occurrence is a guess, and guesses are what make an instruction file too expensive to load.

## Working here

- Branch as `feature/NNN-name`; never push to `master` directly.
- Enable the local gate once per clone: `git config core.hooksPath .githooks`.
- A change to a path in [`docs/architecture/adr/SENSITIVE-PATHS.md`](docs/architecture/adr/SENSITIVE-PATHS.md)
  carries an `ADR-NNNN` reference **in the commit message**.
- Diagrams are Mermaid, never ASCII art. Everything written to disk is in English.
- Templates use `<angle-bracket placeholders>` for what an adopter must fill in. Keep them concrete
  enough to be useful and generic enough to be true of any stack — a template that names a framework
  is not a template.

## What does not belong here

- Stack-specific skills. This repository defines the shape; your stack's depth lives in your repository.
- Anything vendored from [Agent Skills](https://github.com/addyosmani/agent-skills). It is an installed
  dependency; vendoring it forks it and freezes the fork.
- Project-specific examples with real product names, domains, or internal references.
