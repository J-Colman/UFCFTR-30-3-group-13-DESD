# Sprint 1 Traceability

Module: UFCFTR-30-3
Group: 13 - Josh, Izzy, Ada, Aman, Yonas
Date: 2 November 2026
Status: DRAFT — to be updated in Sprint 2
Owner: Joshua
Related issues: `#10` (traceability), `#4` (strategic BPMN), `#12` (FR/NFR), `#13` (operational BPMN), `#11` (scope)

This file links each stakeholder need through the i* models, strategic BPMN, operational BPMN, requirements and backlog. Scope boundaries stay in `docs/planning/scope.md`. Element IDs are in section 5.

**Key:**

- **Stakeholder:** names from `docs/analysis/stakeholder-analysis.docx`
- **F1:** Multi-vendor order assembly, stock validation and checkout
- **F2:** Payment, 5% commission and producer notification
- **R1–R11:** Rank 1–11 in `docs/planning/master-backlog.md`
- **FR/NFR:** IDs in `docs/planning/start_on_the_requirements_shortened.docx`, which also holds the test for each requirement
- **Covered:** every link in the row exists
- **Partial:** every link is named, but at least one needs work
- **Gap:** at least one link is missing

## 1. In-scope traceability

| ID | Stakeholder | Need | i* | Strategic BPMN | Operational BPMN | F | Req | Backlog | Status |
|---|---|---|---|---|---|---|---|---|---|
| T1 | Customers | Customer finds products and builds a multi-vendor basket | Choose products and quantities | Browse for Products | Customer adds stock to basket | F1 | FR1, FR3 | R1, R2 | Partial (no browse/search step) |
| T2 | Customers | Customer sees product details and allergens before buying | Clear prices, fees and delivery options | Browse for Products | Gap | F1 | FR2, NFR9 | R7 | Gap (G7) |
| T3 | Customers | Customer is told when an item is unavailable and can amend the basket | Check availability and reserve stock | Gap | is stock available? → inform customer that stock is no longer available | F1 | FR4 | R2, R3 | Partial (G1) |
| T4 | Customers, Delivery/collection | Customer reviews delivery or collection for each producer, then confirms | Choose delivery or collection | Choose Collection or Delivery | determine delivery / collection → customer reviews order → customer confirms purchase | F1 | FR5, FR6 | R5 | Partial (no per-producer detail) |
| T5 | Local food producers | Order is split by producer | Split order by producer | Create Order | Gap (only create overall marketplace order) | F1 | FR7 | R2, R3, R5 | Gap (G2) |
| T6 | Customers, Payment sandbox | Customer pays once for a multi-vendor order | Pay with card (token) | Pay for Order → Processes Payment | payment submitted to external payment service | F2 | FR8 | R3 | Covered |
| T7 | Customers, Payment sandbox | Customer can retry after a declined or unavailable payment | Retry with another card | Gap | retry payment; inform customer and give option to retry; does customer want to retry | F2 | FR10 | R3 | Partial (G9) |
| T8 | Customers | Customer receives an order confirmation | Order received | Check result of Payment | confirm order (nothing is sent to the customer) | F2 | FR9 | R5 | Partial (G3) |
| T9 | Local food producers | Stock is updated after payment and released if the order ends | Up-to-date stock levels | Update Stock | update stock; release stock | F2 | FR9 | Gap | Gap (G1, G8) |
| T10 | Local food producers | Producers are notified in time to prepare (48 hours) | Order acknowledged in time | Notify Producers | notify producers | F2 | FR9 | Gap | Gap (G8) |
| T11 | Local food producers, Network Admin | Producers receive the right amount and the network receives its 5% | Pay producers minus 5% commission | Commission Payout | calculate commission | F2 | FR7 | R4 | Partial (G5) |
| T12 | Network Admin | Orders, payments and commission are recorded | Gap | Gap | Gap | F2 | FR11, NFR8 | Gap | Gap (G8) |

## 2. Non-functional requirements

| Req | Requirement | Where it is handled | Status |
|---|---|---|---|
| NFR1 | Log in before checkout | Not modelled | Gap (G4) |
| NFR2 | Producers see only their own orders | Not modelled | Gap |
| NFR3 | No stored card details; HTTPS | i* Payment token; token-only sandbox payment service in the component diagram | Partial |
| NFR4 | UK GDPR and data minimisation | Not modelled | Gap |
| NFR5 | Orders survive a restart; no double sale of the last item | Class diagram StockReservation | Partial (G1) |
| NFR6 | Stock checks and search under 2 seconds | Test only | Partial |
| NFR7 | Works on mobile; clear error messages | Operational BPMN customer messages | Partial |
| NFR8 | Orders and payments are logged | Component diagram Operate (incidents, audit) | Partial |
| NFR9 | Full price and allergens shown before payment | i* Clear prices, fees and delivery options; customer reviews order | Partial |

## 3. Outside F1/F2

| ID | Need | Strategic BPMN | Backlog | Decision |
|---|---|---|---|---|
| O1 | One producer rejects their part; customer gets the rest and a partial refund | Not modelled | R6 | Deferred in scope, Must Have in backlog (G6) |
| O2 | Trace a food-quality incident to affected orders | Not modelled | None | Case 3 |
| O3 | Single delivery window across producers | Not modelled | R8 | Future |
| O4 | Customer contacts a producer about quality or safety | Not modelled | R9 | Future |
| O5 | Customer sees food miles | Not modelled | R10 | Future |
| O6 | Customer buys discounted surplus produce | Not modelled | R11 | Future |
| O7 | Producer organic certification is verified | Certify Organics | R7 (supporting data) | Case 1 |
| O8 | Producer lists products | Product Listing | None | Case 1 |
| O9 | Weekly producer payout | Commission Payout | None | Deferred in scope |

## 4. Open gaps

| Gap | Description | Action | Suggested owner |
|---|---|---|---|
| G1 | Stock is held in the requirements, class diagram and i*, but scope leaves it open. The operational BPMN has no check-stock or hold step, yet releases stock | Agree the hold, update scope, add the steps | Group / Ada |
| G2 | The operational BPMN never splits the order, although FR7 and scope F1 require it | Add a split step before payment | Ada |
| G3 | No customer confirmation is sent after payment | Add the step | Ada |
| G4 | Login is required by NFR1 but has no process step | Add the step or state where it is handled | Ada / Izzy |
| G5 | Commission only runs for multi-vendor orders in the BPMN. The SD image uses goods + delivery; scope says order value | Agree when it applies and what it is based on | Group |
| G6 | R6 is deferred in scope, Must Have in the backlog and absent from the FR/NFRs | Downgrade it or add it to F2 | Aman / Josh |
| G7 | R7 is out of scope in `scope.md`, but its product data is required by FR2 and NFR9 | Bring it into F1 or change the requirements | Aman / Josh |
| G8 | No backlog items for producer notification, stock updates or order records | Add them | Aman |
| G9 | Operational gateway errors remain in the repo, and the strategic BPMN has no retry path | Commit the `#13` fixes; add the path or justify leaving it out | Ada |
| G10 | One operational model covers F1 and F2, but the brief needs one per functionality | Build the second model | Ada / Izzy |
| G11 | i* has 3 actors against 6 stakeholders and 6 strategic pools. The SD image shows actor internals and has no source file | Complete SD and SR | Yonas |
| G12 | Network Admin is a stakeholder, but the strategic pool is now Marketplace Platform | Agree how they map | Izzy / Ada |
| G13 | Requirements use the wrong folder and have no stakeholder links. Two files reuse the same IDs | Make the shortened file canonical and complete `#12` | Izzy |
| G14 | Component diagram workers use Node.js; the repo is set up for Python | Choose one before Camunda work starts | Group |

Closed by Ada's 28 October update: marketplace platform pool, producer listing and fulfilment tasks, commission process, and moving the payment result check to the platform.

## 5. Element ID index

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

## 6. Sources

- **Stakeholders:** `docs/analysis/stakeholder-analysis.docx`
- **i*:** `docs/models/case-2-i-star-sr-model.json`, `case-2-i-star-sr-model.png`, `case-2-i-star-sd-model.png`
- **Scope:** `docs/planning/scope.md`
- **Backlog:** `docs/planning/master-backlog.md`
- **UML:** `docs/models/case-2-class-diagram.pdf`, `case-2-component-diagram.pdf`, `case-2-sequence-diagram.pdf`, `case-2-use-case-diagram.pdf`

## 7. Version history

| Date | Author | Change |
|---|---|---|
| 2 November 2026 | Josh |  |