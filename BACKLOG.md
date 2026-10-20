# Backlog

Open work items. Each item has a short ID, used to refer to it in commits
and in other files.

An item is done when its answer is recorded where the root
[`CLAUDE.md`](CLAUDE.md) says it lives; for a requirement, once the user
accepts it. Remove the item when it is done; git history keeps it.

## Open questions

- **offices**: Does the system run one office, or many?
- **service-queues**: Can a service feed more than one queue? If so, what
  picks the queue for a new ticket?
- **calling-rule**: Can an office worker call from more than one queue? If
  so, what rule picks the next ticket (oldest first, queue priority, ...)?
- **call-trigger**: Who starts a call: the office worker pressing "next",
  or the system assigning tickets to free counters?
- **recall-limit**: How many recalls before a no-show? Can a no-show
  ticket go back into the queue if the customer turns up late?
- **transfer**: Is transfer supported? Does a transferred customer keep
  their place, or go to the end of the next queue?
- **customer-view**: Can a customer cancel a ticket, or see their position
  and expected wait somewhere other than the display?
- **priority**: Are there priority tickets (for example for elderly or
  disabled customers)?
- **ticket-numbers**: How are ticket numbers built (prefix per service,
  reset each day)?
- **closing**: What happens to tickets still waiting when the office
  closes?
- **service-hierarchy**: Are services in the hierarchy all selectable, or
  only the leaves?
- **manager**: Is the manager who reads reports the same person as the
  office admin?
- **personal-data**: Does a ticket hold any personal data (name, phone
  number)?
- **strategies**: Which queue strategies does the system support at all?
  This is about the product's boundary, not about order of work.

## Tasks

- **interface-format**: Pick the format of the interface definition that
  names wire-level details (record it in rationale).
- **requirement-checks**: Once requirements exist, add scripts that check
  the template headings and dangling requirement IDs.
