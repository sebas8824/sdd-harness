# F<N>-<n> — <What this feature delivers, stated as an outcome>

- **Status:** draft, awaiting approval
- **Date:** YYYY-MM-DD
- **Feature:** F<N>-<n> ([`ROADMAP.md`](../ROADMAP.md))
- **Builds on:** F<N>-<n-1> ([ADR-NNNN](../architecture/adr/NNNN-....md))
- **Closes:** the `<row title>` row in [`DEFERRED.md`](../DEFERRED.md)

---

## 1. The gap

What the product cannot do today, in the user's terms — not the implementation's. Two paragraphs at
most. If the gap cannot be stated without describing the solution, the feature is not understood yet.

## 2. Prior art, and where it is wrong

How a reference implementation solves this — a previous product, a competitor, an OSS project, or an
earlier feature in this repository. Read from source, and say when.

**What is worth carrying.** The concept that earns its place, and the evidence that it works there.

**Where it is wrong, and we invert it.** One lettered paragraph per defect, each with the concrete
evidence (the file, the call, the missing caller). This is where most of a spec's value is: a decision
argued against a real precedent survives review; a decision argued in the abstract does not.

## 3. Decisions

Numbered. Each states the choice, then the alternative that was rejected and why. Anything that
changes a boundary, or whose "why" must outlive the code, is promoted to an **ADR** and cited here
rather than argued twice.

### 3a. <Decision, phrased as the property it buys>

The change. Then: *the alternative was `<X>`; rejected because `<consequence>`.*

Prefer decisions that make a class of bug **unrepresentable** over decisions that fix an instance of it.

### 3b. <…>

## 4. The surface

The contract this feature exposes: endpoints and their status codes, tool signatures, schema changes
and migrations, error/problem types, events. Anything a consumer binds to.

## 5. Out of scope

Each item points at the roadmap row or `DEFERRED.md` target that owns it. "Not now" without an owner
is not a scope boundary.

## 6. Verification

What proves this works, and how each new test is shown to **bite** — remove the behaviour it names,
watch it fail, restore it. Name the gate command that must pass clean.
