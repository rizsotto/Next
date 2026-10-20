# Rationale directory

Rules for decision records. The format is in [`TEMPLATE.md`](TEMPLATE.md);
copy it for a new entry. Keep entries short.

## IDs

The filename without `.md` is the ID, in short kebab case, with no number
prefix. A superseded entry is not renamed; edit it to say so and link its
replacement.

## When to write one

Write one when a design choice is not obvious and a future reader would
otherwise have to rebuild the reasoning:

- several options had real trade-offs, and the choice is not clear from
  the code;
- an option was rejected that someone will propose again;
- outside research informed the decision.

Not for details clear from the code, or for restating acceptance criteria.
