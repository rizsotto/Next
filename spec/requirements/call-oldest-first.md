---
title: Oldest first calling strategy
status: accepted
---

## Intent

With this calling strategy, among tickets of the same priority, the ticket
that has waited longest goes first, so nobody is passed over because of the
service they picked.

## Terms

- _calling strategy_: the rule that picks the next ticket from those a
  worker can serve.

## Acceptance criteria

- Given a worker with one skill and waiting tickets of the same priority,
  when the next ticket is picked for them, then it is the oldest one.
- Given a worker with two skills and waiting tickets of the same priority
  for both, when the next ticket is picked for them, then it is the one
  that has waited longest across both services.

## Rationale

- [Oldest first](../rationale/oldest-first.md)
