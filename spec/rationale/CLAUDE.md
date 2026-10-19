# Rationale directory

This directory records the *why* behind system design. Requirements under
[`../requirements/`](../requirements/) say what the software must do; the
code says how. This is the home for the reasoning that connects them -
the trade-offs weighed and the option chosen, including the cases where
the chosen option is the least-bad of several imperfect ones, or where a
tempting alternative was rejected.

## File naming

```
short-kebab-case-title.md
```

The filename is the entry's ID - unique and descriptive, the same
convention requirements use. No number prefix: git history gives
chronology, and a memorable name links better than `0007`. A superseded
entry is edited to say so and link its replacement, not renamed.

## Structure

Keep entries short. Most need four parts, in this order:

- **Context** - the problem and the forces at play: constraints, what we
  knew, what alternatives were on the table. Enough that a reader who was
  not in the room can judge the decision.
- **Decision** - what we chose, in one or two plain sentences.
- **Consequences** - what this makes easy, what it makes hard, what it
  puts out of scope, and when to revisit.
- **References** - the requirement(s) this supports, plus
  external docs. Link source files only when unavoidable; paths drift and
  these entries are meant to outlast them.

Start with a `# Title` heading and no front matter.

## How agents should use this

Write one when a design decision is non-obvious and a future reader would
otherwise have to reconstruct the reasoning. Typically:

- You chose one approach among several with real trade-offs, and the
  choice is not self-evident from the code.
- You rejected an alternative that someone will later propose again.
- External research informed the decision and would otherwise be lost
  in a PR thread.

Do **not** write one for: a detail obvious from the code, a restatement
of an acceptance criterion, or a to-do. Those belong in a code comment,
the requirement, or the backlog respectively.
