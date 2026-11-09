# Sprint 1 Traceability

Group 13: Josh, Izzy, Ada, Aman, Yonas  
Date: 2 November 2026  
Status: draft, to be updated in Sprint 2  
Owner: Josh

This document connects each stakeholder need to the i\* models, the strategic and operational BPMN, the requirements and the backlog. The short version: F1 traces through browsing, the basket and delivery or collection, but stock holding and order splitting are not handled yet. F2 traces payment and commission, but customer confirmation, backlog items for producer notification and stock updates, and the audit trail still have gaps. None of the non-functional requirements is fully covered yet. The gaps are listed in section 5.

The requirements IDs come from `docs/planning/start_on_the_requirements_shortened.docx`, which also contains the test and pass criteria for each requirement. `R1`–`R11` are the backlog ranks in `docs/planning/master-backlog.md`. A row is **Covered** when every link exists, **Partly covered** when the links are named but at least one needs work, and **Missing** when at least one link is absent. Gap numbers refer to section 5.

## 1. F1: order assembly, stock and checkout

| ID | Stakeholder | Need | i\* | Strategic BPMN | Operational BPMN | Requirements and backlog | Status |
|---|---|---|---|---|---|---|---|
| T1 | Customers | Customer finds products and builds a multi-vendor basket | Choose products and quantities | Browse for Products | Customer adds stock to basket | FR1, FR3; R1, R2 | Partly covered (no browse/search step) |
| T2 | Customers | Customer sees product details and allergens before buying | Clear prices, fees and delivery options | Browse for Products | Missing | FR2, NFR9; R7 | Missing (G7) |
| T3 | Customers | Customer is told when an item is unavailable and can amend the basket | Check availability and reserve stock | Missing | is stock available? then inform customer that stock is no longer available | FR4; R2, R3 | Partly covered (G1) |
| T4 | Customers, Delivery/collection | Customer reviews delivery or collection for each producer, then confirms | Choose delivery or collection | Choose Collection or Delivery | determine delivery / collection, customer reviews order, customer confirms purchase | FR5, FR6; R5 | Partly covered (no per-producer detail) |
| T5 | Local food producers | Order is split by producer | Split order by producer | Create Order | Missing (only creates the overall marketplace order) | FR7; R2, R3, R5 | Missing (G2) |

## 2. F2: payment, commission and producer notification

| ID | Stakeholder | Need | i\* | Strategic BPMN | Operational BPMN | Requirements and backlog | Status |
|---|---|---|---|---|---|---|---|
| T6 | Customers, Payment sandbox | Customer pays once for a multi-vendor order | Pay with card (token) | Pay for Order, then Processes Payment | payment submitted to external payment service | FR8; R3 | Covered |
| T7 | Customers, Payment sandbox | Customer can retry after a declined or unavailable payment | Retry with another card | Missing | retry payment, inform customer and give option to retry, does customer want to retry | FR10; R3 | Partly covered (G9) |
| T8 | Customers | Customer receives an order confirmation | Order received | Check result of Payment | confirm order (nothing is sent to the customer) | FR9; R5 | Partly covered (G3) |
| T9 | Local food producers | Stock is updated after payment and released if the order ends | Up-to-date stock levels | Update Stock | update stock, release stock | FR9; no backlog item | Missing (G1, G8) |
| T10 | Local food producers | Producers are notified in time to prepare (48 hours) | Order acknowledged in time | Notify Producers | notify producers | FR9; no backlog item | Missing (G8) |
| T11 | Local food producers, Network Admin | Producers receive the right amount and the network receives its 5% | Pay producers minus 5% commission | Commission Payout | calculate commission | FR7; R4 | Partly covered (G5) |
| T12 | Network Admin | Orders, payments and commission are recorded | Missing | Missing | Missing | FR11, NFR8; no backlog item | Missing (G8) |

## 3. Non-functional requirements

| ID | Requirement | Where it is handled | Status |
|---|---|---|---|
| NFR1 | Log in before checkout | Not modelled | Missing (G4) |
| NFR2 | Producers see only their own orders | Not modelled | Missing |
| NFR3 | No stored card details; HTTPS | i\* payment token; token-only sandbox payment service in the component diagram | Partly covered |
| NFR4 | UK GDPR and data minimisation | Not modelled | Missing |
| NFR5 | Orders survive a restart; no double sale of the last item | `StockReservation` in the class diagram | Partly covered (G1) |
| NFR6 | Stock checks and search under 2 seconds | Test only | Partly covered |
| NFR7 | Works on mobile; clear error messages | Customer messages in the operational BPMN | Partly covered |
| NFR8 | Orders and payments are logged | Operate element in the component diagram (incidents, audit) | Partly covered |
| NFR9 | Full price and allergens shown before payment | i\* clear prices, fees and delivery options; customer reviews order | Partly covered |

## 4. Outside F1 and F2

| ID | Need | Where it appears | Backlog | Decision |
|---|---|---|---|---|
| O1 | One producer rejects their part; customer gets the rest and a partial refund | Not modelled | R6 | Deferred in scope, Must Have in the backlog (G6) |
| O2 | Trace a food-quality incident to affected orders | Not modelled | None | Case 3 |
| O3 | Single delivery window across producers | Not modelled | R8 | Future |
| O4 | Customer contacts a producer about quality or safety | Not modelled | R9 | Future |
| O5 | Customer sees food miles | Not modelled | R10 | Future |
| O6 | Customer buys discounted surplus produce | Not modelled | R11 | Future |
| O7 | Producer organic certification is verified | Certify Organics | R7 (supporting data) | Case 1 |
| O8 | Producer lists products | Product Listing | None | Case 1 |
| O9 | Weekly producer payout | Commission Payout | None | Deferred in scope |

## 5. Open gaps

| Gap | What is missing and why it matters | Action | Owner |
|---|---|---|---|
| G1 | Stock is held in the requirements, the class diagram and the i\* model, but scope leaves it open. The operational BPMN has no check-stock or hold step, yet it releases stock. This affects FR4 and NFR5 and makes the current model inconsistent. | Agree the hold, update scope, add the steps | Group / Ada |
| G2 | The operational BPMN never splits the order, although FR7 and the F1 scope require it. Without the split, there is no per-producer order for F2 to pay or notify. | Add a split step before payment | Ada |
| G3 | No customer confirmation is sent after payment, although FR9 requires one. | Add the step | Ada |
| G4 | Login is required by NFR1 but there is no process step for it. | Add the step, or state where it is handled | Ada / Izzy |
| G5 | Commission only runs for multi-vendor orders in the BPMN. The SD image uses goods plus delivery, while scope says order value. The calculation basis needs to be agreed before it is automated. | Agree when it applies and what it is based on | Group |
| G6 | `R6` is deferred in scope, Must Have in the backlog and absent from the FR/NFRs. That contradiction will show up in the Sprint 2 review if it is not resolved. | Downgrade it, or add it to F2 | Aman / Josh |
| G7 | `R7` is out of scope in `scope.md`, but its product data is required by FR2 and NFR9. | Bring it into F1 | Aman / Josh |
| G8 | No backlog items for producer notification, stock updates or order records. This leaves F2 acceptance criteria without backlog coverage. | Add them | Aman |
| G9 | Operational gateway errors remain in the repo, and the strategic BPMN has no retry path. The operational model cannot be presented as executable until these are fixed. | Commit the `#13` fixes, and add the retry path or justify leaving it out | Ada |
| G10 | One operational model covers F1 and F2, but the brief needs one per functionality. | Build the second model | Ada / Izzy |
| G11 | The i\* model has 3 actors against 6 stakeholders and 6 strategic pools. The SD image shows actor internals and has no source file. This weakens the traceability chain at the top. | Complete the SD and SR models | Yonas |
| G12 | Network Admin is a stakeholder, but the strategic pool is now Marketplace Platform. | Agree how they map | Izzy / Ada |
| G13 | The requirements are in the wrong folder and have no stakeholder links. Two requirement files reuse the same IDs. | Make the shortened file canonical and complete `#12` | Izzy |
| G14 | The component diagram workers use Node.js, but the repo is set up for Python. | Choose one before Camunda work starts | Group |

Ada's 28 October update closed four of the original strategic-BPMN gaps: the marketplace platform pool, producer listing and fulfilment tasks, the commission process, and moving the payment result check to the platform.

## 6. Appendix

### Strategic BPMN (`docs/models/strategic-bpmn.bpmn`)

| Element | ID |
|---|---|
| Browse for Products | `Activity_0n7z413` |
| Choose Collection or Delivery | `Activity_1ljogur` |
| Pay for Order | `Activity_0ieui19` |
| Processes Payment | `Activity_1vyq53b` |
| Check result of Payment (accepted / declined) | `Activity_1cnlaam` |
| Create Order | `Activity_0shsw8c` |
| Update Stock | `Activity_1hy2bfm` |
| Commission Payout (if available) | `Activity_0wtng6p` |
| Prepare Order For Collection / Delivery | `Activity_05edle0` |
| Product Listing | `Activity_1mmsm75` |
| Certify Organics | `Activity_0vtdrcs` |

Notify Producers is the message flow from Create Order to Prepare Order For Collection / Delivery.

### Operational BPMN (`docs/models/case-2-operational-bpmn.bpmn`)

| Element | ID |
|---|---|
| Customer adds stock to basket | `Activity_0rr2lt4` |
| is stock available? | `Gateway_1qgl4sy` |
| inform customer that stock is no longer available | `Activity_1xfn19p` |
| determine delivery / collection | `Activity_06e8i07` |
| customer reviews order | `Activity_1qsbbl2` |
| customer confirms purchase | `Activity_0l2g082` |
| create overall marketplace order | `Activity_1dnmvp0` |
| payment submitted to external payment service | `Activity_0ao6m0r` |
| retry payment | `Activity_1gma2lm` |
| inform customer and give option to retry | `Activity_1o2bvfq` |
| does customer want to retry | `Gateway_12tjvls` |
| confirm order | `Activity_00enf9b` |
| update stock | `Activity_1wy6dof` |
| release stock | `Activity_1lnt4wn` |
| notify producers | `Activity_1vwfzpc` |
| calculate commission | `Activity_1fg0pe2` |

## 7. Sources

- Stakeholders: `docs/analysis/stakeholder-analysis.docx`
- i\*: `docs/models/case-2-i-star-sr-model.json`, `case-2-i-star-sr-model.png`, `case-2-i-star-sd-model.png`
- Scope: `docs/planning/scope.md`
- Backlog: `docs/planning/master-backlog.md`
- Requirements: `docs/planning/start_on_the_requirements_shortened.docx`
- UML: `docs/models/case-2-class-diagram.pdf`, `case-2-component-diagram.pdf`, `case-2-sequence-diagram.pdf`, `case-2-use-case-diagram.pdf`

## 8. Version history

| Date | Author | Change |
|---|---|---|
| 28 October 2026 | Josh | Created and populated the file |
| 2 November 2026 | Josh | Restructured around F1 and F2 and added plain language statuses and gap explanations |
