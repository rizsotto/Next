---
title: End of the office day
status: accepted
---

## Intent

At closing time the [office day](office-hours.md#terms) ends, and no ticket
carries over to the next day. Staff can end a day early, or extend it, when
the day does not go to plan.

## Terms

- _closing credential_: the right to end an office day early or extend it.
  The office admin gives it and takes it back.
- _not served_: the office day ended while the ticket was waiting. The
  ticket is closed without serving.

## Acceptance criteria

- Given a waiting ticket, when the closing time comes, then it ends as not
  served, which reports show apart from [no-shows](call-recall.md#terms).
- Given a ticket being called or served, when the closing time comes, then
  it is not touched and the worker finishes as normal.
- Given an office day that has ended, when a new office day starts, then
  no ticket from the old day is waiting.
- Given an open office, when the office admin or a holder of the closing
  credential ends the day early, then it ends at once, as it would at
  closing time.
- Given an open office, when the office admin or a holder of the closing
  credential extends the day, then the closing time moves, for that day
  only.
- Given an extended day, when they also extend the last-ticket time, then
  the kiosk issues tickets until the new time.
- Given an office worker, when the office admin gives them the closing
  credential or takes it back, then they can or can no longer end or
  extend the day.
- Given an office worker without the closing credential, when they try to
  end or extend the day, then the system refuses.

## Rationale

- [Closing](../rationale/closing.md)
