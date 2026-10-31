# Authentication

## Context

Staff authenticate at the kiosk and at counters. A badge suits the kiosk,
but counters may have no reader, and hardware should not hold up the rest
of the system.

## Decision

Keep the method apart from what it unlocks. Every method gives the same
result, so kiosk staff mode and counter sign-in do not care which one was
used.

## Consequences

The MVP can ship with a software login alone, and a badge reader can come
later without changing other requirements.

A login on a kiosk happens in front of customers, so a badge is still the
better fit there.
