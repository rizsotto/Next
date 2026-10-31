---
title: Who can set priority
status: accepted
---

## Intent

Customers cannot set priority. Only floor workers can. The office admin
decides who they are, and can change that at any time: one person at the
kiosk today, every office worker tomorrow.

## Acceptance criteria

- Given a customer alone at the kiosk, when they take a ticket, then the
  ticket has normal priority and they are not offered a choice.
- Given an office worker, when the office admin gives them the priority
  credential, then they can set priority from then on.
- Given a floor worker, when the office admin takes the credential away,
  then they can no longer set priority.
- Given an office worker without the credential, when they try to set
  priority, then the system refuses.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
