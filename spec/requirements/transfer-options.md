---
title: Advanced transfer options
status: accepted
---

## Intent

A plain transfer suits most cases. When it does not, the office worker can
choose to restart the ticket's time, or to delay its next call by some
minutes.

## Acceptance criteria

- Given a transfer, when the office worker does not ask for an option,
  then it is a plain transfer.
- Given a transfer with restart, when the next ticket is picked, then the
  ticket counts as old as the moment of the transfer.
- Given a transfer with a delay of X minutes, when the next ticket is
  picked before X minutes have passed, then that ticket is not picked.
- Given a transfer with a delay of X minutes, when X minutes have passed,
  then the ticket can be picked like any other.
- Given a transfer, when the office worker asks for both options, then
  both apply.

## Rationale

- [Transfer time](../rationale/transfer-time.md)
