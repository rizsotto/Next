# Transfer time

## Context

Oldest first needs a time for a transferred ticket. Keeping the original
time spares the customer a second full wait, but passes people already
waiting for the next service. Restarting the time is fair to them, but the
customer can wait a full round twice in one visit.

## Decision

Keep the original time by default. The office worker can ask to restart
it, or to delay the next call by some minutes.

## Consequences

A customer is not punished for how the office splits its work. The worker
who knows the case decides the exceptions, which adds a choice on their
screen.
