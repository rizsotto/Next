---
title: Higher priority goes first
status: accepted
---

## Intent

Only priority and time decide the call order. A ticket with higher
priority goes before any ticket with lower priority, however long that
one has waited.

## Acceptance criteria

- Given a worker who can serve two waiting tickets of different priority,
  when the next ticket is picked for them, then it is the one with higher
  priority, even if the other is older.
- Given a high priority ticket and a worker who cannot serve it, when the
  next ticket is picked for them, then it is not picked.

## Known limitations

The system puts no limit on high priority tickets. Too many of them can
leave others waiting without end. The office decides how to use priority.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
