---
title: Priority comes from a reason
status: accepted
---

## Intent

Staff do not pick a priority. They give a ticket one or more reasons, like
labels, from a list the office admin sets up, and the reasons decide the
priority. So the office sets its idea of fairness once, and calling only
needs the priority.

## Terms

- _reason_: why a ticket should go ahead, for example "elderly person". A
  ticket can have several.
- _weight_: the value of one reason. A reason's weight feeds the ticket's
  priority.

## Acceptance criteria

- Given the office admin, when they add a reason, then they give it a
  weight above zero, and staff can use it from then on.
- Given two reasons, when the office admin sets them up, then they can
  have the same weight or different ones.
- Given a ticket with a reason, when it is shown to customers, on the
  display or on the printed ticket, then neither its reasons nor its
  priority are shown.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
