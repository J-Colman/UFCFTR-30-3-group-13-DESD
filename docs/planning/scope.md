# Sprint 1 Scope

Group 13: Josh, Izzy, Ada, Aman, Yonas  
Date: 28 October 2026, updated 2 November 2026  
Status: confirmed with the module team  
Owner: Josh

## What we're building

We're working from Case 2 of the assessment: a customer browses the marketplace, adds products from one or more producers to a basket, goes through checkout, and confirms the purchase. The system creates the overall order and the producer-specific parts of it, then sends payment to a sandbox service. After a successful payment it updates stock, works out the 5% commission, and notifies the producers involved.

We split that into two functionalities so the operational models and Camunda work have a clear boundary. F1 stops at a confirmed order that is ready to pay. F2 starts with payment and covers what happens afterwards.

## Confirming the scope with the module team

The brief asks groups to complete one use case but also to identify two major functionalities, so we emailed Khoa Phung and Dilshan Jayatilake on 19 October 2026 to check what that meant. Khoa replied on 26 October:

> "The two major functionalities should be associated with Use Case 2, and all the
> detailed logic of these functionalities should be considered within the chosen use case."

We're taking that to mean both functionalities come from Case 2 and that all the detailed operational and Camunda logic stays inside it. That puts Case 1 (producer listing and inventory) and Case 3 (food-quality incidents) outside the two assessed functionalities. The confirmation is tracked on issue `#11`.

## F1: Multi-vendor order assembly, stock validation and checkout

F1 is the path from browsing to an order that is ready to pay. The customer builds a basket, goes to checkout, the system checks availability, works out which producers are involved, asks the customer to review delivery or collection, and creates one marketplace order split by producer.

It starts when the customer begins browsing. The main actors are the customer, the marketplace platform and the stock/inventory service.

A simple example: a basket might contain eggs from one producer and bread from another. Checkout has to confirm both are still available, record that there are two suppliers, and capture how each part will be delivered or collected.

### What's in scope

- Browsing, searching and adding products to a basket
- A basket containing items from more than one producer
- Checking product availability and stock
- Identifying the producers involved
- Displaying product allergen and nutritional information
- Working out delivery or collection arrangements
- The customer reviewing and confirming the order
- Creating the overall marketplace order
- Splitting it into producer-specific order elements

### What's not

We're leaving payment, commission, producer notification and payout out of F1 because they all depend on a confirmed order. They belong to F2 or later work. Food-quality incident handling is also out because it is Case 3 work.

### What can go wrong

The main exceptions are an item being unavailable, not enough stock, the customer changing the basket, no valid delivery or collection option, and a producer no longer being able to fulfil their part of the order.

### Who is involved

Customers, producers and delivery/collection are the main stakeholders. The platform and the stock service do the work behind the scenes.

### Where it is modelled

- Strategic BPMN: Browse for Products, Choose Collection or Delivery, Create Order
- Operational BPMN: `docs/models/case-2-operational-bpmn.bpmn` (draft)
- Backlog items: `R1`, `R2`, `R3`, `R5`

### How we'll know it works

- A customer can add products from two or more producers to one basket.
- Checkout identifies unavailable or insufficient stock before the order is confirmed.
- A confirmed order produces one marketplace order and one order element per producer.
- The chosen delivery or collection arrangement is recorded for the order.

## F2: Payment, 5% commission and producer notification

F2 starts when the customer confirms the purchase. Payment goes to a sandbox service and comes back accepted or declined. If it succeeds, the order is confirmed, stock is updated, each producer's amount and the network's 5% are worked out, and the producers are notified. If it fails, the customer can retry or the process waits rather than losing the order. If the customer chooses not to retry, stock is released and the order ends.

The main actors are the customer, the payment sandbox, the marketplace platform, the producers and the notification service.

### What's in scope

- Submitting payment to an external or simulated payment service
- Handling success, decline, retry and service-unavailable paths
- Confirming or declining the order
- Updating inventory quantities after successful payment
- Calculating each producer's amount and the 5% marketplace commission
- Notifying the relevant producers
- Recording the transaction and audit trail

### What's not

We're not doing live payments or real financial data, weekly producer payout execution, food-quality incident handling, or full refunds and partial-order failure. Partial-order failure (`R6`) is currently deferred; it needs either downgrading in the backlog or a separate agreement to model it as an F2 exception before it goes into the process.

### What can go wrong

Payment can be declined, the payment service can be unavailable, the request can time out, the customer can retry, a duplicate payment can occur, or producer notification can fail. These are the paths the operational model and Camunda process need to handle.

### Who is involved

Customers, producers, the payment sandbox and network admin.

### Where it is modelled

- Strategic BPMN: Pay for Order, Processes Payment, Check result of Payment, Update Stock, Commission Payout, and the Notify Producers message flow
- Operational BPMN: `docs/models/case-2-operational-bpmn.bpmn` (draft; gateway fixes required in Sprint 2)
- Backlog items: `R3`, `R4`, plus a new item for producer notification

### How we'll know it works

- A sandbox payment accepted by the payment service confirms the order, updates stock and notifies the relevant producers.
- A declined or unavailable payment offers the customer a retry and does not decrement stock.
- The 5% commission is calculated and recorded separately from the producer amounts.
- Each producer's payable amount is recorded for the confirmed order.

## How the two functionalities fit together

The table below is the short version. The detailed row-by-row evidence, including the model elements and requirement links, is in `docs/analysis/traceability.md` (`#10`).

| Functionality | Main stakeholder need | Strategic processes | Backlog items |
|---|---|---|---|
| F1 | Multi-vendor ordering, stock validation and delivery/collection | Browse for Products, Choose Collection or Delivery, Create Order | `R1`, `R2`, `R3`, `R5` |
| F2 | Payment, 5% commission and producer notification | Pay for Order, Processes Payment, Check result of Payment, Update Stock, Commission Payout, Notify Producers (message flow) | `R3`, `R4`, plus a new producer-notification item |
| Outside F1/F2 | Case 1 and Case 3 work, food miles, surplus produce, direct vendor communication | Product Listing, Certify Organics; food-quality incidents not modelled | `R6` (deferred), `R7` (under review, G7 in traceability), `R8`–`R11` |

Everything outside F1/F2 is either Case 1 or Case 3 work, a future sprint, or part of Task 2. That includes food miles, surplus produce, direct vendor communication and food-quality traceability.

## Assumptions and boundaries

Payments use Stripe test, PayPal sandbox or a mocked service. We never use live payments or real financial data.

The 5% commission applies to the order value and is recorded separately from the producer amounts. Producers need at least 48 hours' lead time to prepare orders.

Weekly producer payout execution is a case-study requirement, but it is not part of F1/F2. We're deferring it to a later sprint or Task 2.

Multi-vendor orders are split per producer, and delivery or collection arrangements are recorded per order. Stock is checked at checkout, but the exact reservation and decrement timing is still open.

The strategic BPMN represents the whole enterprise. F1 and F2 are the two Case 2 slices we are taking into detailed operational modelling and Camunda automation. All detailed logic for those two functionalities stays within Case 2.

## Open questions

- Do we reserve stock at checkout, or decrement it only after successful payment?
- Who sets delivery and collection rules, and can producers set their own?
- Which sandbox payment provider are we using?
- Does partial-order failure (`R6`) stay a Must Have? If it does, it needs a boundary-error path in F2.
- Does weekly payout settlement belong in F2 or in Task 2?
- What channel do we use for producer notification, and what happens if it fails?

## Change control

Any change to F1/F2 scope has to be agreed by the group and recorded here. If it changes the functionalities we agreed with the module team, confirm it again and update `#11`.

## Version history

| Date | Author | Change |
|---|---|---|
| 28 October 2026 | Josh | Initial confirmed scope after the module-team reply |
| 2 November 2026 | Josh | Replaced the strategic process placeholders with process names from the strategic BPMN |
