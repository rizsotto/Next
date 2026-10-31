---
title: Priority is the sum of reason weights
status: accepted
---

## Intent

A ticket's [reasons](priority-reason.md#terms) turn into one priority by
adding up their weights, so each extra reason moves a customer further
ahead.

## Terms

- _normal_: the priority of a ticket with no reason.

## Acceptance criteria

- Given a ticket with no reason, when it waits, then it has normal
  priority.
- Given a ticket with a reason, when it waits, then its priority comes
  from that reason's weight.
- Given a ticket with several reasons, when it waits, then its priority
  comes from the sum of their weights.
- Given "elderly person" and "small child", when one ticket has both and
  another has only one of them, then the ticket with both has the higher
  priority.
- Given a ticket that already has a reason, when the office admin changes
  that reason's weight, then the ticket keeps the priority it had.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
