---
title: Change reasons after a ticket is created
status: accepted
---

## Intent

The office admin chooses whether a ticket's
[reasons](priority-reason.md#terms) can change after the ticket is created.
Where they can, a [floor worker](priority-credential.md#terms) can take a
customer's ticket number and add reasons, or drop them later. They see the
waiting tickets with enough context to decide. The system does not stop
them from making a poor choice.

## Acceptance criteria

- Given an office where changes are turned off, when a floor worker tries
  to change a waiting ticket's reasons, then the system refuses.
- Given an office where changes are turned on, when a floor worker opens
  the waiting tickets, then each one shows its number, service, reasons,
  priority and wait time.
- Given an office where changes are turned on, when a floor worker enters
  a ticket number, then they get that waiting ticket.
- Given an office where changes are turned on, when a floor worker adds or
  drops a reason on a waiting ticket, then the resulting priority applies
  to the next pick and the ticket keeps its wait time.
- Given many high priority tickets, when a floor worker gives one more
  ticket a reason, then the system allows it.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
