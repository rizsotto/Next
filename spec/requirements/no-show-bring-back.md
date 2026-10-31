---
title: Bring back a no-show ticket
status: accepted
---

## Intent

A customer who turns up late does not have to start over. An office worker
can bring back their no-show ticket, or refuse to.

## Acceptance criteria

- Given a no-show ticket from today, when an office worker enters its
  number and brings it back, then it waits again for its service.
- Given a ticket brought back, when it waits again, then it has the same
  number, reasons and original time.
- Given a no-show ticket from an earlier day, when an office worker tries
  to bring it back, then the system refuses.

## Rationale

- [No-show by the worker](../rationale/no-show-by-worker.md)
