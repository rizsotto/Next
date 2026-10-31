# Personal data

## Context

The system never contacts a customer, so no rule needs a name or a phone
number. Two things on a ticket may still count as personal data: reasons,
which can describe a customer's condition, and the worker who served it,
which reports need to evaluate performance.

This is a design that keeps the risk low, not legal advice. Check it
against the rules of each market, above all before selling to public
offices.

## Decision

Tickets hold no name or phone number. Reasons stay only for the office day,
then only totals per reason remain. The worker stays on the ticket, visible
only to those who can read reports.

## Consequences

No record remains of one customer's condition. So nobody can look back at
a single ticket to see why it went first, for example after a complaint.
Revisit with a set number of days if offices need that.

If a mobile channel returns, it may need contact details; this decision
has to be looked at again then.
