# Sprint 1 Scope

Module: UFCFTR-30-3
Group: 13 — Josh, Izzy, Ada, Aman, Yonas
Date: 28 October 2026
Status: CONFIRMED by module team
Owner: Josh (integration)

## 1. Chosen use case

Source: `docs/assessment/task-1-use-cases.pdf`, Use Case 2.

A customer browses/searches, then adds products from one or more producers to a basket, checks availability, reviews delivery or collection arrangements, confirms the purchase, and pays through a sandbox service. The system then creates the overall order and producer-specific elements, updates stock, calculates the 5% commission, and notifies producers.

## 2. Module-team confirmation

Emailed Khoa Phung and Dilshan Jayatilake on 19 October 2026.

Reply from Dr Khoa Phung on 26 October 2026:

> “The two major functionalities should be associated with Use Case 2, and all the
> detailed logic of these functionalities should be considered within the chosen use case.”

Interpretation:
- Both functionalities are scoped from Use Case 2.
- All detailed operational/Camunda logic stays within Use Case 2.
- Case 1 (producer listing/inventory) and Case 3 (food-quality incident/traceability) are not part of the two assessed functionalities.
- Tracking issue: `#11` — close with this confirmation.

## 3. The two major functionalities

### F1 — Multi-vendor order assembly, stock validation and checkout

**Outcome:** The customer can build a basket from multiple producers and reach a confirmed order split by producer, that is ready for payment.

**Trigger:** The customer proceeds to checkout.

**In scope:**
- Browse/search and add products to a basket
- Multi-vendor basket
- Product availability and stock validation
- Identify producers involved
- Determine delivery or collection arrangements
- Customer reviews and confirms the order
- Create the overall marketplace order
- Split it into producer-specific order elements

**Out of scope:**
- Payment processing
- Commission calculation
- Producer notification and payout
- Food-quality incident handling

**Actors and systems:** Customer, marketplace platform, inventory/stock service, producer records, delivery/collection logic.

**Main exceptions:** Item unavailable, insufficient stock, customer amends basket, no valid delivery/collection option, producer no longer able to fulfil the order.

**Stakeholders:** Customers, producers, delivery/collection.

**Strategic process:** `SP-ORD (TBC — align to strategic BPMN)`
**Operational model:** `docs/models/case-2-operational-bpmn.bpmn` (draft)
**Backlog items:** `R1`, `R2`, `R3`, `R5`
**Acceptance basis:**
- A customer can add products from two or more producers to one basket.
- Checkout identifies unavailable or insufficient stock before the order is confirmed.
- A confirmed order produces one marketplace order and one order element per producer.
- The chosen delivery or collection arrangement is recorded for the order.

### F2 — Payment, 5% commission and producer notification

**Outcome:** Payment is taken through a sandbox service and the order is confirmed or declined, stock is updated, the 5% commission and producer amounts are calculated, and the relevant producers are notified.

**Trigger:** Customer confirms the purchase.

**In scope:**
- Submit payment to an external or simulated payment service
- Handle payment success, decline, retry and service-unavailable paths
- Confirm or decline the order
- Update inventory quantities after successful payment
- Calculate each producer’s amount and the 5% marketplace commission
- Notify the relevant producers
- Record the transaction/audit trail

**Out of scope:**
- Live payments or real financial data
- Weekly producer payout execution
- Food-quality incident handling
- Full refunds and partial-order failure (deferred: `R6` must be downgraded or separately agreed as an F2 exception before it is modelled)

**Actors and systems:** Customer, payment sandbox, marketplace platform, producers, notification service.

**Main exceptions:** Payment declined, payment service unavailable, timeout, customer retries, duplicate payment/idempotency, producer notification failure.

**Stakeholders:** Customers, producers, payment sandbox, network admin.

**Strategic process:** `SP-PAY (TBC — align to strategic BPMN)`
**Operational model:** `docs/models/case-2-operational-bpmn.bpmn` (draft; gateway fixes required in Sprint 2)
**Backlog items:** `R3`, `R4`, plus a new backlog item for producer notification (currently a gap)
**Acceptance basis:**
- A sandbox payment accepted by the payment service confirms the order, updates stock and notifies the relevant producers.
- A declined or unavailable payment offers the customer a retry and does not decrement stock.
- The 5% commission is calculated and recorded separately from the producer amounts.
- Each producer’s payable amount is recorded for the confirmed order.

## 4. Scope traceability summary

| Functionality | Main stakeholder need | Strategic process | Backlog items |
|---|---|---|---|
| F1 | Multi-vendor ordering, stock validation and delivery/collection | `SP-ORD (TBC)` | `R1`, `R2`, `R3`, `R5` |
| F2 | Payment, 5% commission and producer notification | `SP-PAY (TBC)` | `R3`, `R4`, plus new producer-notification item |
| Out of scope | Case 1/Case 3 processes, food miles, surplus, direct vendor communication | `SP-CAT` / `SP-QUAL (TBC)` | `R7`, `R9`–`R11` |

Detailed element-level traceability is maintained separately in `docs/analysis/traceability.md` (`#10`).

## 5. Assumptions and boundaries

- Payments use Stripe test, PayPal sandbox or a mocked service; never live payments.
- The 5% commission applies to the order value and is recorded separately from producer amounts.
- Producers require at least 48 hours’ lead time to prepare orders.
- Weekly producer payout execution is a case-study requirement but is not part of F1/F2; it is deferred to a later sprint or Task 2.
- Multi-vendor orders are split per producer, with delivery/collection arrangements recorded per order.
- Stock availability is checked at checkout; the exact reservation/decrement timing is an open question.
- The strategic BPMN represents the whole enterprise; F1 and F2 are the two Case 2 slices selected for detailed operational modelling and Camunda automation.
- All detailed logic for the two functionalities remains within Case 2.

## 6. Dependencies and open questions

- Stock reservation timing: reserve at checkout or decrement only after successful payment?
- Exact delivery/collection rules and whether producers set their own arrangements.
- Which sandbox payment provider will be used.
- Whether partial-order failure/partial refund (`R6`) stays a Must Have; if so, add it to F2 as a boundary-error exception.
- Whether weekly payout settlement belongs in F2 or Task 2.
- Producer notification channel and failure handling.

## 7. Change control

Any change to F1/F2 scope must be agreed by the group and recorded here. If it changes the agreed functionalities, confirm it with the module team and update `#11`.

## 8. Version history

| Date | Author | Change |
|---|---|---|
| 28 October 2026 | Josh | Initial confirmed scope after module-team reply |
