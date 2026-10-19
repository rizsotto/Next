# Next project overview

This document orients the reader: the problem, who is involved, the words
we use, and what the system does. It does not say when or in what order
things get built. Planning lives in GitHub milestones and issues; what is
committed lives in [`requirements/`](requirements/).

## Purpose

Next is a queue management system for businesses that offer walk-in
service. Customers arrive without an appointment, take a ticket, and wait
to be called to a counter.

## What value it provides

It keeps customers from leaving. This matters most, since it shows up
directly as lost revenue when it is missing. People mind waiting far less
when they can see their position and use the time for something else.

It gives staff back their actual job. An office worker who spends half a
shift answering "how much longer?" and "who is next?" is not doing the
work they were hired for. Automated position tracking and routing answer
those questions before anyone has to ask.

It gives managers real data instead of a guess. Every ticket, call and
serving leaves a timestamp. From these it is possible to see the peak
hours instead of predicting them, and to find which counter or service is
consistently the bottleneck.

## Actors

- _customer_, who walks in to the office to get something done.
- _office worker_, who serves customers at a counter.
- _office admin_, who sets up the office and manages the office workers.

## Glossary

- _office_: one physical place where customers are served. It has its own
  counters, queues and office workers.
- _service_: what the customer comes to get done, for example "passport
  renewal". The customer picks a service when taking a ticket. Services
  can be grouped into a hierarchy so customers find them easily.
- _ticket_: a customer's place in line for one service. It carries a
  number, which the display shows when the ticket is called.
- _queue_: an ordered list of waiting tickets, first in, first out. A
  queue can hold tickets for one or more services.
- _counter_: the place where serving happens, for example a desk or a
  room.
- _call_: the system tells the customer, through the display, to go to a
  given counter.
- _recall_: calling the same ticket again when the customer did not come.
- _no-show_: the customer did not come after the call and any recalls.
  The ticket is closed without serving.
- _serving_: the time the customer and the office worker spend together
  at the counter.
- _transfer_: sending a customer on to another service after a serving,
  without a new ticket.
- _visit_: the customer's whole stay, from taking the ticket to leaving.
  One visit can include more than one serving, when there is a transfer.
- _wait time_: the time from taking the ticket to the first call.
- _service time_: the length of one serving.
- _kiosk_: the device where the customer picks a service and gets a
  ticket.
- _display_: the screen in the waiting area that shows calls and waiting
  tickets.

A ticket moves through these states: waiting, called, serving, done. A
called ticket can also end as a no-show.

## How a visit works

1. The customer picks a service at the kiosk and gets a ticket.
2. The ticket joins the queue for that service. The display shows the
   waiting tickets.
3. When an office worker is free, they call the next ticket. The display
   shows the ticket number and the counter.
4. The customer goes to the counter and the serving starts. If they do
   not come, the office worker can recall the ticket, or mark it as a
   no-show.
5. When done, the office worker closes the serving, or transfers the
   customer to another service.

Behind this, the office admin sets up the services, queues, counters and
office workers. The timestamps from each step feed reports on wait times,
service times and busy hours.

## Queue strategies

Common ways to organize queues, for reference:

- single queue: all customers wait in one line, no matter which service
  they need.
- multiple queues: customers are grouped by service.
- mobile queuing: customers take a ticket and get called on their own
  phone.
- hybrid: booked appointments are mixed with walk-in tickets.

## Open questions

Answer these while writing requirements. Move each answer into this
document or a requirement, then remove the question.

1. Does the system run one office, or many?
2. Can a service feed more than one queue? If so, what picks the queue
   for a new ticket?
3. Can an office worker call from more than one queue? If so, what rule
   picks the next ticket (oldest first, queue priority, ...)?
4. Who starts a call: the office worker pressing "next", or the system
   assigning tickets to free counters?
5. How many recalls before a no-show? Can a no-show ticket go back into
   the queue if the customer turns up late?
6. Is transfer supported? Does a transferred customer keep their place,
   or go to the end of the next queue?
7. Can a customer cancel a ticket, or see their position and expected
   wait somewhere other than the display?
8. Are there priority tickets (for example for elderly or disabled
   customers)?
9. How are ticket numbers built (prefix per service, reset each day)?
10. What happens to tickets still waiting when the office closes?
11. Are services in the hierarchy all selectable, or only the leaves?
12. Is the manager who reads reports the same person as the office admin?
13. Does a ticket hold any personal data (name, phone number)?
14. Which queue strategies does the system support at all? This is about
    the product's boundary, not about order of work.
