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

It gives managers real data instead of a guess. Every ticket, call and
serving leaves a timestamp. From these it is possible to see the peak
hours instead of predicting them, and to find which counter or service is
consistently the bottleneck.

## Actors

- _customer_, who walks in to the office to get something done.
- _office worker_, who serves customers at a counter.
- _floor worker_, an office worker who holds the priority credential. This
  can be one person at the kiosk, or every office worker.
- _office admin_, who sets up the office and manages the office workers.
- _manager_, who reads reports. Anyone who holds the reports credential; in
  a small office this is the office admin.

## Glossary

- _office_: one physical place where customers are served. It has its own
  counters, queues and office workers. One install runs one office; see
  [`rationale/single-office.md`](rationale/single-office.md).
- _service_: what the customer comes to get done, for example "passport
  renewal". The customer picks a service when taking a ticket.
- _group_: a menu of services and other groups at the kiosk, so customers
  find a service easily.
- _skill_: a service that an office worker can do.
- _priority_: a ticket's rank in the call order. A ticket is normal unless
  it has a reason.
- _reason_: why a ticket should go ahead, for example "elderly person".
  The office admin sets up the list and gives each reason a weight. A
  ticket can have several, and their weights add up to its priority.
- _priority credential_: the right to set priority. The office admin gives
  it and takes it back.
- _ticket_: a customer's place in line for a visit. It carries a
  number, which the display shows when the ticket is called.
- _queue_: the tickets waiting for one service, first in, first out. Each
  service has one queue; there is nothing to set up.
- _counter_: the place where serving happens, for example a desk or a
  room.
- _call_: the system tells the customer, through the display, to go to a
  given counter.
- _calling strategy_: the rule that picks the next ticket from those a
  worker can serve.
- _recall_: calling the same ticket again when the customer did not come.
- _no-show_: the customer did not come after the call and any recalls.
  The ticket is closed without serving.
- _not served_: the office day ended while the ticket was waiting. The
  ticket is closed without serving.
- _office day_: the time from the office's opening to its closing. "Today"
  and "new day" mean this, not a calendar day.
- _closing credential_: the right to end an office day early or extend it.
  The office admin gives it and takes it back.
- _report_: what the system shows about how the office ran, built from the
  timestamps of tickets and servings.
- _reports credential_: the right to read reports, and nothing else. The
  office admin gives it and takes it back.
- _serving_: the time the customer and the office worker spend together
  at the counter.
- _transfer_: sending a customer on to another service after a serving,
  without a new ticket.
- _visit_: the customer's whole stay, from taking the ticket to leaving.
  One visit can include more than one serving, when there is a transfer.
- _wait time_: the time a ticket spends waiting before it is called.
- _service time_: the length of one serving.
- _kiosk_: the device where the customer picks a service and gets a
  ticket.
- _staff mode_: a state of the kiosk that a floor worker unlocks by
  authenticating, to do what customers cannot.
- _authentication_: staff proving who they are, by hardware such as a badge
  or by software such as a login.
- _display_: the screen in the waiting area that shows calls, and more if
  the office chooses.
- _web view_: a web page where a customer follows a service on their own
  phone.

A ticket moves through these states: waiting, called, serving, done. A
called ticket can also end as a no-show, and an office worker can bring it
back to waiting. A transfer moves a serving ticket back to waiting. A
waiting ticket ends as not served when the office day ends.

## How a visit works

A typical visit, as most queue systems run it. Items in the backlog may
change the details.

1. The customer picks a service at the kiosk and gets a ticket.
2. The ticket joins the queue for that service.
3. When an office worker is free, they call the next ticket. The display
   shows the ticket number and the counter.
4. The customer goes to the counter and the serving starts. If they do
   not come, the office worker can recall the ticket, or mark it as a
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
