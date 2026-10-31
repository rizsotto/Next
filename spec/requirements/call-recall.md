---
title: Recall and no-show are the worker's choice
status: accepted
---

## Intent

If the customer does not come after a call, the office worker decides what
happens next. They can recall the ticket as often as they like, and they
mark the no-show when they choose to.

## Terms

- _recall_: calling the same ticket again when the customer did not come.
- _no-show_: the customer did not come after the call and any recalls. The
  ticket is closed without serving.

## Acceptance criteria

- Given a called ticket, when the office worker recalls it, then the
  display shows its number and counter again.
- Given a ticket recalled many times, when the office worker recalls it
  again, then the system allows it.
- Given a called ticket, when the office worker marks it as a no-show,
  then the ticket is closed without serving.
- Given a called ticket and any number of recalls, when the worker does
  nothing, then the system does not mark a no-show on its own.

## Rationale

- [No-show by the worker](../rationale/no-show-by-worker.md)
