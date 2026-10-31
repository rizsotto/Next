# Next project overview

This document orients the reader: the problem, who is involved, the words
we use, and what the system does. It does not say when or in what order
things get built. Agents may edit it for orientation and vocabulary.

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

It gives the business real data instead of a guess. Every ticket, call and
serving leaves a timestamp. From these it is possible to see the peak
hours instead of predicting them, and to find which counter or service is
consistently the bottleneck.

## Actors

- _customer_, who walks in to the office to get something done.
- _office worker_, who serves customers at a counter.
- _office admin_, who sets up the queue system.
- _staff_, everyone who works in the office. Some hold extra rights, given
  by the office admin.

## Glossary

The basic words. Terms for details live in the
[requirements](requirements/CLAUDE.md#terms).

- _office_: one physical place where customers are served. It has its own
  counters, queues and office workers. One install runs one office; see
  [`rationale/single-office.md`](rationale/single-office.md).
- _service_: what the customer comes to get done, for example "passport
  renewal". The customer picks a service when taking a ticket.
- _skill_: a service that an office worker can do.
- _ticket_: a customer's place in line for a visit. It carries a
  number, which the display shows when the ticket is called.
- _queue_: the tickets waiting for one service, first in, first out. Each
  service has one queue; there is nothing to set up.
- _priority_: a ticket's rank in the call order.
- _counter_: the place where serving happens, for example a desk or a
  room.
- _call_: the system tells the customer, through the display, to go to a
  given counter.
- _serving_: the time the customer and the office worker spend together
  at the counter.
- _transfer_: sending a customer on to another service after a serving,
  without a new ticket.
- _visit_: the customer's whole stay, from taking the ticket to leaving.
  One visit can include more than one serving, when there is a transfer.
- _wait time_: the time a ticket spends waiting before it is called.
- _service time_: the length of one serving.
- _report_: what the system shows about how the office ran, built from the
  timestamps of tickets and servings.
- _kiosk_: the device where the customer picks a service and gets a
  ticket.
- _display_: the screen in the waiting area that shows calls, and more if
  the office chooses.

A ticket moves through these states: waiting, called, serving, done. A
called ticket can also end as a
[no-show](requirements/call-recall.md#terms), and an office worker can bring it
back to waiting. A transfer moves a serving ticket back to waiting. A
waiting ticket ends as
[not served](requirements/office-end-of-day.md#terms) when the
[office day](requirements/office-hours.md#terms) ends.

## How a visit works

A typical visit, as most queue systems run it. Items in the backlog may
change the details.

1. The customer picks a service at the kiosk and gets a ticket.
2. The ticket joins the queue for that service.
3. When an office worker is free, they call the next ticket. The display
   shows the ticket number and the counter.
4. The customer goes to the counter and the serving starts. If they do
   not come, the office worker can
   [recall](requirements/call-recall.md#terms) the ticket, or mark it as a
   no-show.
5. When done, the office worker closes the serving, or transfers the
   customer to another service.

Behind this, the office admin sets up the services, counters and office
workers. The timestamps from each step feed reports on wait times,
service times and busy hours.

## Queue strategies

Common ways to organize queues, for reference. Next uses multiple queues,
one per service; see
[`rationale/queue-strategies.md`](rationale/queue-strategies.md).

- single queue: all customers wait in one line, no matter which service
  they need.
- multiple queues: customers are grouped by service.
- mobile queuing: customers take a ticket and get called on their own
  phone.
- hybrid: booked appointments are mixed with walk-in tickets.
