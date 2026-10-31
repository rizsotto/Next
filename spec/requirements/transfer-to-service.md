---
title: Transfer a customer to another service
status: accepted
---

## Intent

When a serving ends and the customer needs something else, the office
worker sends them on to another service. The customer keeps their ticket
and does not lose the time they already waited.

## Acceptance criteria

- Given a serving, when the office worker transfers the customer and picks
  a service, then the ticket waits for that service.
- Given a transferred ticket, when it waits again, then it has the same
  number and the same reasons.
- Given a plain transfer, when the next ticket is picked, then the ticket
  counts as old as it was when first taken.

## Rationale

- [Transfer time](../rationale/transfer-time.md)
