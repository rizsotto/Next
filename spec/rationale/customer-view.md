# What customers see

## Context

Customers want to know how long they will wait, so they can step out. A
strict position in line does not work: priority tickets go ahead, and
skills mean tickets are not called in a simple line. A position could even
go backwards, which would show that someone got priority, and priority is
not public.

Offices also differ: some have one waiting area, others have counters in
different buildings, where a display for every service makes no sense.

A cancel option would need a way to find a ticket at the kiosk, and would
only save a recall or two.

## Decision

Displays show calls for the services they cover. Average time, waiting
count and a QR code are office options. The waiting count leaves out
priority tickets. One QR code opens a web view on the customer's phone,
where they type their ticket number to follow its service and get an
estimate. A QR code per service was rejected: a customer can scan the
wrong one, which needs a warning and a redirect.

Customers cannot cancel; one who leaves becomes a no-show.

## Consequences

The estimate treats every ticket as normal, so it never gives priority
away, and pretending to grant priority stays safe. The price is a rougher
number.

The web view is meant to be reachable from anywhere, which matters for how
Next is installed. The requirements presume a customer can reach it, even
if the MVP does not deliver that yet.

A mobile app is out of the MVP, and the system does not contact customers;
see [Queue strategies](queue-strategies.md).
