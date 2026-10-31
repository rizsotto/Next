---
title: Sign in and out of a counter
status: accepted
---

## Intent

An office worker signs in at a counter to start work, and signs out when
they leave, even for a short break. The system then knows who is working
where.

## Acceptance criteria

- Given a free counter, when an office worker signs in, then they can press
  "next" there, and calls go to that counter.
- Given a worker signed in at a counter, when another worker tries to sign
  in there, then the system refuses.
- Given a worker signed out, when they try to press "next", then the system
  refuses.
- Given a worker in a serving, when they try to sign out, then the system
  refuses until the serving ends.
- Given a worker signed out, when an estimate is made, then they do not
  count as serving.
- Given a worker signed out, when the worker report is built, then that
  time does not count as time with nothing to do.
- Given a worker still signed in, when the [office
  day](office-hours.md#terms) ends, then they are signed out.