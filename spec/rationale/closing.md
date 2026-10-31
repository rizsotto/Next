# Closing

## Context

Tickets can still be waiting when the office closes. Numbers and no-shows
also need a meaning for "today". A calendar day breaks for an office open
past midnight, and a button to close the day can be forgotten, which leaves
yesterday's line waiting in the morning.

## Decision

The office admin sets the hours, and they run the day on their own. Tickets
still waiting at closing end as not served, a state apart from no-show,
since the customer did nothing wrong.

The office admin can end a day early or extend it, and so can holders of a
closing credential. It is apart from the priority credential: someone who
helps at the kiosk should not be able to end the day for everyone.

## Consequences

Reports show when an office ran out of time. Customers left at closing have
to come back and take a new ticket; nothing carries over.

Holidays have no setting of their own. Staff end the day early on them.
Revisit if that proves clumsy.
