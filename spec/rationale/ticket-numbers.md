# Ticket numbers

## Context

The web view finds a ticket from its number alone, so a number must point
to one ticket across all services for the day. Options were a prefix and
counter per service, or a plain counter for the whole office. Prefixes let
customers spot calls for their service, and each service's numbers run in
order on the display.

Numbering could also be a choice of generators: no prefix, or no daily
reset. A blank prefix for a single service gives the first with no extra
rule. Never resetting only makes numbers longer.

## Decision

Use a prefix per service and a counter per service, reset each day. There
are no generators to configure.

## Consequences

Numbers repeat from day to day, so anyone holding yesterday's A042 holds
the same number as today's A042. Lookups only find today's ticket, and the
printed ticket shows its date, so staff can spot an old one before bringing
back a no-show.

Revisit if an office needs a different format. The rule lives in one
requirement, so the change stays small.
