---
title: The office worker starts a call
status: accepted
---

## Intent

An office worker who is free presses "next". They do not choose the
customer or see any strategy; the system picks the ticket and calls it to
their counter.

## Acceptance criteria

- Given a worker at a counter and a ticket they can serve, when they press
  "next", then that ticket is called and the display shows its number and
  the worker's counter.
- Given a worker with no ticket they can serve, when they press "next",
  then no ticket is called and the worker can see that nothing is waiting.
- Given a free worker, when a ticket they can serve is waiting, then
  nothing is called until they press "next".
