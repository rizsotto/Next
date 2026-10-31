---
title: Ticket numbers
status: accepted
---

## Intent

Each ticket gets a short number that a customer can read and type: the
service's prefix, then a counter. It identifies one ticket for the day.
The printed ticket shows when it was taken, so an old ticket is easy to
spot.

## Acceptance criteria

- Given a service with prefix A, when tickets are taken for it, then they
  are numbered A001, A002 and so on.
- Given a new day, when the first ticket for a service is taken, then its
  counter starts again.
- Given a prefix used by one service, when the office admin gives it to
  another, then the system refuses.
- Given one service with no prefix, when tickets are taken for it, then
  they are plain numbers. Only one service can be without a prefix.
- Given a number, when staff or the web view look it up, then they get
  today's ticket with that number, never one from an earlier day.
- Given a ticket, when it is printed, then it shows its number, the date
  and the time.
- Given any two tickets, when one is high priority, then their numbers
  come from the same counter.

## Rationale

- [Ticket numbers](../rationale/ticket-numbers.md)
