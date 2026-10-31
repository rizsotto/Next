---
title: Set priority at the kiosk
status: accepted
---

## Intent

A floor worker who notices a customer's condition can create the ticket
for them at the kiosk, and give it reasons as it is created.

## Acceptance criteria

- Given a floor worker in staff mode at the kiosk, when they create a
  ticket, then they can choose one or more reasons for it, or none.
- Given a ticket created with reasons at the kiosk, when it joins its
  queue, then it has those reasons from the start.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
