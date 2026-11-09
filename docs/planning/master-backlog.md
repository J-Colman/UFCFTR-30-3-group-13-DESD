# Master Backlog: Bristol Regional Food Network

**Current State:** Mid Sprint 2

This backlog factors in technical dependencies and ranks features (IDs 1 to 15) so the rest of the team knows exactly the order in which we can design the system.

## Product Backlog

| ID  | Item                                  | F1/F2                   | MoSCoW        |
|-----|---------------------------------------|-------------------------|---------------|
| R1  | Product Catalog and Search            | F1                      | Must          |
| R2  | Multi-Vendor Shopping Cart            | F1                      | Must          |
| R3  | Secure Single-Transaction Checkout    | F1/F2                   | Must          |
| R4  | Automated 5% Commission               | F2                      | Must          |
| R5  | Split Delivery/Collection Instruction | F1/F2                   | Must          |
| R6  | Partial Order Failure                 | F2 (exception/deferred) | Must (decide) |
| R7  | Product Traceability and Safety Data  | F1                      | Must          |
| R8  | Consolidated Delivery Synchronisation | Future                  | Should        |
| R9  | Direct Vendor Communication           | Future                  | Should        |
| R10 | Postcode Food Miles                   | Future                  | Could         |
| R11 | Dynamic Surplus Integration           | Future                  | Could         |
| R12 | Order Confirmation to Customer        | F2                      | Must          |
| R13 | Stock Update After Payment            | F2                      | Must          |
| R14 | Producer Notification                 | F2                      | Must          |
| R15 | Order and Payment Audit Trail         | F2                      | Must          |

## Sprint 2 Backlog

| ID   | Work-stream                                 | Owner  | Depends on  | Done when                                                                                                     |
|------|---------------------------------------------|--------|-------------|---------------------------------------------------------------------------------------------------------------|
| S2.1 | Camunda (split by F1 Camunda/F2 Camunda)    | TBD    | S2.2, S2.3  | Executable BPMN files, user tasks, Forms                                                                      |
| S2.2 | Two operational BPMN models (F1, F2)        | Izzy   | S2.8, scope | Pools/lanes, user tasks, service tasks, gateways, message flows, boundary events, alternative/exception paths |
| S2.3 | Service-task implementation                 | Ada    | S2.1, S2.2  | Payment, stock, notification, commission service tasks with mock/local services                               |
| S2.4 | GitHub Kanban board                         | Ada    | S2.1 – S2.7 | Sprint 2 columns, items, labels, assignees, status                                                            |
| S2.5 | Backlog and Gantt                           | Joshua | S2.1 – S2.4 | Master backlog IDs and F1/F2 mapping; Sprint 2 backlog; Gantt                                                 |
| S2.6 | Traceability                                | Joshua | S2.1 – S2.5 | i\* → strategic → operational → Camunda → requirements/backlog matrix                                         |
| S2.7 | Process variables, gateways, business logic | Aman   | S2.1, S2.2  | Variables defined, gateways with conditions, business logic                                                   |
| S2.8 | i\* diagrams                                | Yonas  | N/A         | Completed SD and SR, source files, stakeholders mapped                                                        |