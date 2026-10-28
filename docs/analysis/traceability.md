# Sprint 1 Traceability

Module: UFCFTR-30-3
Group: 13 — Josh, Izzy, Ada, Aman, Yonas
Date: 28 October 2026
Status: DRAFT — Sprint 1 evidence, to be updated in Sprint 2
Owner: Josh (integration)
Related issues: `#10` (traceability), `#4` (strategic BPMN), `#11` (scope confirmation)

This file is the detailed evidence link between stakeholder needs, the strategic BPMN, the two agreed functionalities (F1/F2), the operational BPMN and the product backlog. The scope-level summary stays in `docs/planning/scope.md`.

## 1. ID scheme

### Functionalities

| ID | Functionality |
|---|---|
| F1 | Multi-vendor order assembly, stock validation and checkout |
| F2 | Payment, 5% commission and producer notification |

### Backlog items

| ID | Backlog item |
|---|---|
| R1 | Product Catalog & Search |
| R2 | Multi-Vendor Shopping Cart |
| R3 | Secure Single-Transaction Checkout |
| R4 | Automated 5% Commission Deduction |
| R5 | Split Delivery/Collection Instructions |
| R6 | Partial Order Failure (Exception Handling) |
| R7 | Product Traceability & Safety Data |
| R8 | Consolidated Delivery Synchronization |
| R9 | Direct Vendor Communication |
| R10 | Postcode-based Food Miles |
| R11 | Dynamic Surplus Integration |

### Strategic processes

These are descriptive placeholders. Replace them with Ada's actual strategic process names/IDs when the strategic BPMN is finalised. Participant process IDs below are from the current exported draft.

| ID | Meaning | Current BPMN participant/process |
|---|---|---|
| SP-ORD | Sell and fulfil multi-vendor orders | Customer `Process_1az2jql`, Producer `Process_08z95qh`, Delivery/collection `Process_1ay8z2p` |
| SP-PAY | Process payment and settle commission | Payment sandbox `Process_0vmeexz` |
| SP-CERT | Verify organic certification | Organic-certification verification `Process_1fttwi9` |
| SP-ADMIN | Maintain marketplace and monitor orders | Network Admin `Process_1raw8t0` |
| SP-CAT | Manage catalogue and stock | Not modelled — GAP |
| SP-QUAL | Handle food-quality incidents and traceability | Not modelled — out of F1/F2 scope |

### Status definitions

| Status | Meaning |
|---|---|
| Covered | The need has a strategic process, an operational step and a backlog item. |
| Partial | Some links exist, but one or more artefacts are incomplete. |
| Gap | The need is in scope, but an artefact or backlog item is missing. |
| Out of scope | Deliberately outside F1/F2, normally because it belongs to Case 1/Case 3 or a future sprint. |

## 2. Traceability matrix

| # | Stakeholder need | Strategic process | Functionality | Operational step (element ID and label) | Backlog item | Status | Evidence |
|---|---|---|---|---|---|---|---|
| T1 | Customer can find products and build a multi-vendor basket | SP-ORD: Customer `Process_1az2jql` — `Activity_0n7z413` “Browse for Products”; `Activity_1ljogur` “Choose Collection or Delivery” | F1 | `Activity_0rr2lt4` “Customer adds stock to basket” → `Activity_0ndn96p` “customer goes to checkout” | R1, R2 | Partial | Strategic model has browse but no basket/checkout detail |
| T2 | Customer is told when an item is unavailable and can amend the basket | SP-ORD — no explicit stock-check process in strategic model | F1 | `Gateway_1qgl4sy` “is stock available?”; `Activity_1xfn19p` “inform customer that stock is no longer available”; `Activity_0qz3viy` “check producers involved” | R2, R3 | Partial | No strategic stock-check process; operational draft covers it |
| T3 | Customer knows the delivery/collection arrangement per producer | SP-ORD: Delivery/collection `Process_1ay8z2p` — `Activity_18voaud` “Delivers orders”; collection path is incorrectly labelled “Moves Collections from the Depot to Stores” | F1 | `Activity_06e8i07` “determine delivery / collection”; `Activity_1qsbbl2` “customer reviews order” | R5 | Partial | Delivery exists, collection/BRFN wording is wrong, per-producer detail missing |
| T4 | Customer pays once for a multi-vendor order | SP-PAY: Payment sandbox `Process_0vmeexz` — `Activity_1vyq53b` “Processes Payment”; Customer `Activity_0ieui19` “Pay for Order” | F2 | `Activity_0ao6m0r` “payment submitted to external payment service”; `Gateway_0rfi80j` “is payment accepted” | R3 | Partial | Strategic model has payment, but no multi-vendor split or order confirmation |
| T5 | Customer can retry after a declined or unavailable payment | SP-PAY — no retry path in strategic model | F2 | `Activity_1gma2lm` “retry payment”; `Gateway_12tjvls` “does customer want to retry”; `Activity_1lnt4wn` “release stock”; `Activity_1o2bvfq` “inform customer and give option to retry” | R3 | Partial | No strategic retry path; operational path lacks default flow/timeout |
| T6 | Producer is notified in time to prepare the order (48-hour lead time) | SP-ORD/SP-PAY — no producer-notification process in strategic model; `Process_08z95qh` only “Produce food for supply” | F2 | `Activity_1vwfzpc` “notify producers” | GAP — no backlog item | Gap | No producer-notification process/backlog item; operational task exists |
| T7 | Producer receives the correct amount after the 5% commission | SP-PAY — no commission/settlement process in strategic model | F2 | `Activity_1fg0pe2` “calculate commission” | R4 | Partial | No strategic commission/settlement process; operational task exists |
| T8 | Network receives its 5% commission | SP-PAY — no commission process in strategic model | F2 | `Activity_1fg0pe2` “calculate commission” | R4 | Partial | No strategic commission process; operational task exists |
| T9 | Order is split into producer-specific order elements | SP-ORD — no explicit split in strategic model | F1 | `Activity_1dnmvp0` “create overall marketplace order”; `Gateway_0aaetje` “are there multiple vendors in order” | R2, R3, R5 | Partial | No strategic split; operational split occurs after payment/notification — review sequence |
| T10 | One producer rejects their portion; customer receives the rest and a partial refund | SP-ORD/SP-PAY — no exception path modelled | F2 (deferred exception) | GAP — no boundary error event in operational BPMN | R6 | Gap | No boundary error event; scope currently defers R6 |
| T11 | Customer/producer can trace a food-quality incident to affected orders | SP-QUAL — not modelled | Out of F1/F2 | N/A | R7 | Out of scope | Future/strategic |
| T12 | Consolidated delivery windows across producers | SP-ORD — not modelled | Out of F1/F2 | N/A | R8 | Out of scope | Future/Should; not required for F1/F2 core |
| T13 | Customer can contact a producer about quality/safety | SP-QUAL — not modelled | Out of F1/F2 | N/A | R9 | Out of scope | N/A |
| T14 | Customer can see food miles | SP-CAT/SP-ORD — not modelled | Out of F1/F2 | N/A | R10 | Out of scope | Future/Could |
| T15 | Customer can buy discounted surplus produce | SP-CAT — not modelled | Out of F1/F2 | N/A | R11 | Out of scope | Future/Could |
| T16 | Producer organic certification is verified | SP-CERT: `Process_1fttwi9` — `Activity_0vtdrcs` “Certify Organics” | Out of F1/F2 | N/A | R7 (supporting product data) | Out of scope | Strategic model only; Case 1/future |

## 3. Gap log

| Gap | Description | Action | Owner |
|---|---|---|---|
| G1 | No **marketplace platform** pool in the strategic BPMN; “Network Admin” is being used as the platform | Add a platform participant and separate platform operations from admin maintenance | Ada |
| G2 | Producer process only “Produce food for supply”; no **product listing, stock/availability or order fulfilment** | Add high-level producer processes | Ada |
| G3 | No **commission/payout/settlement** process in the strategic BPMN | Add a finance/settlement process or sub-process | Ada |
| G4 | No **producer notification** in the strategic BPMN and no backlog item | Add a backlog item and a strategic notification interaction | Aman/Ada |
| G5 | **Partial-order failure** is a Must Have in the backlog but has no boundary event or exception path | Decide: downgrade `R6` or add an F2 exception path | Aman/Josh |
| G6 | **Food-quality traceability** is a Must Have in the backlog but outside the confirmed F1/F2 scope | Mark as strategic/future or explain its supporting role | Josh |
| G7 | Delivery process contains an **unnamed orphan user task** and splits unconditionally into delivery and collection | Remove/named the task and model the choice explicitly | Ada |
| G8 | Payment result is checked inside the **Payment sandbox** pool; responsibility should sit with the marketplace platform | Move “check result” to platform; label request/result message flows | Ada |
| G9 | Operational BPMN has **missing default flows** and gateway semantic errors (parallel gateway used as a decision/join) | Fix before claiming executable | Ada/Josh |
| G10 | No explicit **per-producer delivery/collection** detail in the strategic model | Add or mark as operational detail for F1 | Ada |

## 4. Evidence notes

- Strategic BPMN source: `docs/models/strategic-bpmn.bpmn` (draft export). Participant IDs above are from that file.
- Operational BPMN source: `docs/models/operational-bpmn-use-case-2.bpmn` (draft; known gateway issues).
- Backlog source: `docs/planning/Master_Backlog.md` (currently no `R` IDs; add them to make this table auditable).
- Scope source: `docs/planning/scope.md`.
- Stakeholder source: `docs/analysis/stakeholder-analysis.docx`.
- i* source: `docs/models/iSR model-case-2.json` and the two exported diagrams.

## 5. Review checklist

- [ ] Add `R1`–`R11` IDs to `Master_Backlog.md`.
- [ ] Replace `SP-ORD`/`SP-PAY` placeholders with Ada’s final strategic process names.
- [ ] Add the missing producer-notification backlog item.
- [ ] Decide the fate of `R6` partial-order failure.
- [ ] Mark `R7`, `R8`, `R9`, `R10`, `R11` as future/out of F1/F2 in the backlog.
- [ ] Re-run this table after the strategic BPMN is finalised and after the operational gateway fixes.
