---
title: Oldest first calling strategy
status: accepted
---

## Intent

A calling strategy picks the next ticket from those a worker can serve.
With oldest first, among tickets of the same priority, the ticket that has
waited longest goes first, so nobody is passed over because of the service
they picked.

## Acceptance criteria

- Given a worker with one skill and waiting tickets of the same priority,
  when the next ticket is picked for them, then it is the oldest one.
- Given a worker with two skills and waiting tickets of the same priority
  for both, when the next ticket is picked for them, then it is the one
  that has waited longest across both services.

## Rationale

- [Oldest first](../rationale/oldest-first.md)
