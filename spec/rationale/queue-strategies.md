# Queue strategies

## Context

Four common strategies were on the table: single queue, multiple queues,
mobile queuing and hybrid. Each service has its own queue (see
[One queue per service](one-queue-per-service.md)), which is the multiple
queues strategy. An office whose workers can do every service gets the
effect of a single queue, since the oldest ticket goes first. The real
choice was about the other two.

Hybrid brings booked appointments, which is a much larger product:
calendars, slots and their own no-show rules. Next is for walk-in service.

Mobile queuing looks like a small add-on but is not. Calling a customer
on their phone only works if they are back at the office in time, and
making sure of that (for example, that they are near the office 5 minutes
before the call) raises several open problems.

## Decision

Use multiple queues, one per service. Leave out mobile queuing and hybrid
for now. Customers follow their wait on the display, or on a web view they
open themselves; see [What customers see](customer-view.md).

## Consequences

The system stays simple: no booking, no calls to phones, and no need for a
customer's contact details to reach them.

Customers can still step out during the wait, but they have to judge for
themselves when to come back, since the system does not contact them.

Both left-out strategies may return in later versions. Mobile queuing
needs its own design first; do not specify it as a small extension of the
display.
