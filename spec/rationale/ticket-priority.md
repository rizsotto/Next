# Ticket priority

## Context

Some customers need to go ahead of others. Options included a priority
button for customers at the kiosk, and a separate "pushed to the front"
state that staff set.

A pushed ticket is just a high priority ticket, so a second state adds
nothing. A customer button would need staff to check it anyway. In real
offices, staff often stand at the kiosk to help, and some offices do not
want priority changed once a ticket exists.

Who may set priority changes by office and by day, so it cannot be tied to
the office admin role. It is not a skill either, since a skill is a
service a worker can do.

Letting staff pick a priority directly would make fairness a call for each
worker at each ticket. A fixed number of levels would not suit every
office either.

A request step was also considered: the customer asks at the kiosk and a
floor worker accepts or rejects it on a screen. It is not needed. The
floor worker notices the condition, or hears the request, and acts. If they
would rather not argue, they can pretend to grant it, or grant it and drop
it later.

## Decision

Priority and time alone decide the call order. Only floor workers raise a
ticket: holders of a credential the office admin can give and take back.
They do it at the kiosk through staff mode, and later too if the office
turns that on.

Staff give one or more reasons, from a list the office admin sets up. Each
reason has a weight, and the weights add up to the ticket's priority. So
an elderly person with a small child goes before someone with only one of
those reasons. The terms stay separate: fairness weighs reasons, while
picking the next ticket only needs the priority. The office decides how
many priorities there are.

The system sets no limit on priority. It shows staff enough context to
decide, and leaves the choice to the office.

## Consequences

Abuse by customers is not possible, and one rule covers both ways of
raising a ticket.

An office can starve normal tickets by overusing priority. That is its
call, not the system's. Revisit if offices ask for a limit.

Taking the highest reason instead of the sum was rejected: it would not
let two reasons beat one. The sum is not an office setting, since no office
needs another rule yet. Revisit if one does.

Staff mode needs staff to authenticate at the kiosk; see
[Authentication](authentication.md).

Reasons can say something sensitive about a customer, such as a
disability, so customers never see reasons or priority. That also keeps
staff free to pretend.
