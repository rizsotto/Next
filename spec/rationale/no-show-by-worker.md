# No-show by the worker

## Context

The system could mark a no-show on its own, after a set number of recalls
or a timer. That needs rules that fit every office, and a customer can be
closed while the worker is still looking for them.

A late customer could also just take a new ticket, but then they start
over, which often ends in an argument at the desk.

## Decision

The office worker decides: no limit on recalls, no automatic no-show. Any
office worker can bring back a no-show ticket the same day, with its
original time.

## Consequences

The office stays in charge, and the system has no timers to tune. A worker
can spend time on recalls that a limit would have cut short. Someone can
walk off, come back late and go ahead of others, if the worker allows it.
