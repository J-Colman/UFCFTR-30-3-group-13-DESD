# Bristol Regional Food Network — Digital Marketplace

## UFCFTR-30-3 Distributed and Enterprise Software Development

The Bristol Regional Food Network is a community digital marketplace connecting around 40 local food producers with consumers within 20 miles of Bristol, helping small producers reach customers beyond farmers’ markets and farm-gate sales. It lets producers list seasonal products and manage availability, while customers browse by category, place single or multi-vendor orders, and check out through a sandbox payment service, with traceability, food-miles reporting and surplus-produce features.

## The Team — Group 13

| Name | GitHub Handle | Role |
| --- | --- | --- |
| Joshua | [@J-Colman](https://github.com/J-Colman) | Lead / Integration / BPMN |
| Izzy | [@Awesometeapot1](https://github.com/Awesometeapot1) | Business Analyst / Requirements / F2 BPMN|
| Ada | [@aido77](https://github.com/aido77) | BPMN Modeller / Camunda Automation |
| Aman | [@N30NW1LD-2005](https://github.com/N30NW1LD-2005) | Product Owner / Planning, Camunda Forms |
| Yonas | [@yonas1212](https://github.com/yonas1212) | Modelling / Analysis |

---

## Case 2 — Customer Multi-Vendor Order, Checkout and Payment

Chosen use case: **Case 2**.

The two major functionalities are confirmed with the module team (Dr Khoa Phung, 26 October 2026):

- **F1 — Multi-vendor order assembly, stock validation and checkout**
- **F2 — Payment, 5% commission and producer notification**

Both functionalities are scoped from Case 2. See [docs/planning/scope.md](docs/planning/scope.md) for the boundaries and assumptions.

---

## Repository Structure

```text
UFCFTR-30-3-group-13-DESD/
├── README.md
├── requirements.txt
├── .gitignore
├── automation/
    ├── main.py
    ├── test_workers.py
    └── workers.py
├── docs/
    └── analysis/
        ├── stakeholder-analysis.docx
        └── traceability-matrix.docx
    └── assessment/
        ├── assessment-brief-task-1.pdf
        ├── case-study.pdf
        ├── contributions-matrix-draft.docx
        └── task-1-use-cases.pdf
    └── meetings/
        └── meeting-notes-04-11-2026.docx
    └── planning/
        ├── gantt-chart.png
        ├── master-backlog-sprint-3.pdf
        ├── moscow-prioritisation.md
        ├── scope.md
        ├── sprint-1-checklist.png
        ├── sprint-1-week-1-plan.md
        ├── sprint-2-checklist.png
        ├── start on the requirements.docx
        ├── start_on_the_requirements_shortened.docx
        └── Whats to be done.txt
└── models/
    └── camunda/
        └── bpmn/
            └── sub-processes/
                ├── bpmn-authenticate-customer.bpmn
                └── bpmn-authenticate-customer.png
            ├── operational-bpmn-f1-checkout.bpmn
            ├── operational-bpmn-f1-checkout.png
            ├── operational-bpmn-f2-payment.bpmn
            ├── operational-bpmn-f2-payment.png
            ├── strategic-bpmn.bpmn
            └── strategic-bpmn.png
        └── dmn/
            └── delivery-options-table.dmn
        └── forms/
            ├── add-to-basket.form
            ├── amend-basket.form
            ├── browse-products.form
            ├── choose-delivery-options.form
            ├── enter-payment-details.form
            ├── login-or-signup.form
            ├── login.form
            ├── proceed-to-checkout.form
            ├── retry-or-cancel-payment.form
            ├── review-order.form
            └── sign-up.form
    └── istar
        ├── brfn-istar-SD1.text
        ├── brfn-istar-SR1.text
        ├── Goal_Diagram_i*SD1_Model_Case_2.pdf
        └── Goal_Diagram_i*SR1_Model_Case_2.pdf
    └── uml
        ├── case-2-class-diagram.pdf
        ├── case-2-component-diagram.pdf
        ├── case-2-sequence-diagram.pdf
        └── case-2-use-case-diagram.pdf

```

---

## Artefacts

| Artefact | Owner | Location | Status |
| --- | --- | --- | --- |
| Assessment Brief | Module team | [docs/assessment/assessment-brief-task-1.pdf](docs/assessment/assessment-brief-task-1.pdf) | 📄 Reference copy |
| Case Study | Module team | [docs/assessment/case-study.pdf](docs/assessment/case-study.pdf) | 📄 Reference copy |
| Task 1 Use Cases | Module team | [docs/assessment/task-1-use-cases.pdf](docs/assessment/task-1-use-cases.pdf) | 📄 Reference copy |
| Stakeholder Analysis | Izzy | [docs/analysis/stakeholder-analysis.docx](docs/analysis/stakeholder-analysis.docx) | ✅ Complete |
| FR/NFR Analysis (draft) | Izzy | [docs/planning/start on the requirements.docx](<docs/planning/start on the requirements.docx>) | Superseded by the shortened version |
| FR/NFR Analysis with Test Criteria | Izzy | [docs/planning/start_on_the_requirements_shortened.docx](docs/planning/start_on_the_requirements_shortened.docx) | ✅ Complete (#12) |
| Scope and Functionality Confirmation | Joshua | [docs/planning/scope.md](docs/planning/scope.md) | Confirmed with module team (#11) |
| Major Process List | Yonas | — | ❌ Not delivered (#5) |
| Traceability Matrix | Joshua | [docs/analysis/traceability-matrix.docx](docs/analysis/traceability-matrix.docx) | Sprint 2 version (#20) |
| i\* Strategic Dependency Model | Yonas | [models/istar/Goal_Diagram_i\*SD1_Model_Case_2.pdf](<models/istar/Goal_Diagram_i*SD1_Model_Case_2.pdf>) | ✅ Complete |
| i\* Strategic Dependency Source (piStar) | Yonas | [models/istar/brfn-istar-SD1.text](models/istar/brfn-istar-SD1.text) | ✅ Complete |
| i\* Strategic Rationale Model | Yonas | [models/istar/Goal_Diagram_i\*SR1_Model_Case_2.pdf](<models/istar/Goal_Diagram_i*SR1_Model_Case_2.pdf>) | ✅ Complete |
| i\* Strategic Rationale Source (piStar) | Yonas | [models/istar/brfn-istar-SR1.text](models/istar/brfn-istar-SR1.text) | ✅ Complete |
| Strategic BPMN | Ada | [models/camunda/bpmn/strategic-bpmn.bpmn](models/camunda/bpmn/strategic-bpmn.bpmn) | ✅ Complete (#4) |
| Strategic BPMN Image | Ada | [models/camunda/bpmn/strategic-bpmn.png](models/camunda/bpmn/strategic-bpmn.png) | ✅ Complete |
| Operational BPMN F1: Checkout | Joshua, Yonas | [models/camunda/bpmn/operational-bpmn-f1-checkout.bpmn](models/camunda/bpmn/operational-bpmn-f1-checkout.bpmn) | Deployed and tested in Camunda |
| Operational BPMN F1 Image | Joshua, Yonas | [models/camunda/bpmn/operational-bpmn-f1-checkout.png](models/camunda/bpmn/operational-bpmn-f1-checkout.png) | ✅ Complete |
| Operational BPMN F2: Payment | Joshua, Izzy | [models/camunda/bpmn/operational-bpmn-f2-payment.bpmn](models/camunda/bpmn/operational-bpmn-f2-payment.bpmn) | 🟡 Modelled; workers in progress |
| Operational BPMN F2 Image | Joshua, Izzy | [models/camunda/bpmn/operational-bpmn-f2-payment.png](models/camunda/bpmn/operational-bpmn-f2-payment.png) | ✅ Complete |
| Authenticate Customer Sub-process | Joshua | [models/camunda/bpmn/sub-processes/bpmn-authenticate-customer.bpmn](models/camunda/bpmn/sub-processes/bpmn-authenticate-customer.bpmn) | Deployed and tested in Camunda |
| Authenticate Customer Image | Joshua | [models/camunda/bpmn/sub-processes/bpmn-authenticate-customer.png](models/camunda/bpmn/sub-processes/bpmn-authenticate-customer.png) | ✅ Complete |
| Delivery Options Decision (DMN) | Joshua | [models/camunda/dmn/delivery-options-table.dmn](models/camunda/dmn/delivery-options-table.dmn) | Deployed and tested in Camunda |
| Camunda Forms (11) | Aman, Joshua | [models/camunda/forms/](models/camunda/forms/) | ✅ Complete |
| Job Workers | Ada, Aman | [automation/workers.py](automation/workers.py) | 🟡 F1 and login in progress; 🟡 F2 in progress |
| Worker Entry Point | Ada, Aman, Joshua | [automation/main.py](automation/main.py) | ✅ Complete |
| Worker Tests | Ada, Aman | [automation/test_workers.py](automation/test_workers.py) | 🟡 In progress |
| Python Dependencies | Ada, Aman | [requirements.txt](requirements.txt) | ✅ Complete |
| UML Use Case Diagram | Yonas | [models/uml/case-2-use-case-diagram.pdf](models/uml/case-2-use-case-diagram.pdf) | ✅ Complete |
| UML Class Diagram | Yonas | [models/uml/case-2-class-diagram.pdf](models/uml/case-2-class-diagram.pdf) | ✅ Complete |
| UML Component Diagram | Yonas | [models/uml/case-2-component-diagram.pdf](models/uml/case-2-component-diagram.pdf) | ✅ Complete |
| UML Sequence Diagram | Yonas | [models/uml/case-2-sequence-diagram.pdf](models/uml/case-2-sequence-diagram.pdf) | ✅ Complete |
| Master Backlog | Aman, Joshua | [docs/planning/master-backlog-sprint-3.pdf](docs/planning/master-backlog-sprint-3.pdf) | Sprint 3 version |
| MoSCoW Prioritisation | Aman | [docs/planning/moscow-prioritisation.md](docs/planning/moscow-prioritisation.md) | ✅ Complete |
| Sprint 1 Plan | Ada | [docs/planning/sprint-1-week-1-plan.md](docs/planning/sprint-1-week-1-plan.md) | ✅ Complete |
| Gantt Chart | Aman | [docs/planning/gantt-chart.png](docs/planning/gantt-chart.png) | ✅ Complete |
| Sprint 1 Checklist | Aman | [docs/planning/sprint-1-checklist.png](docs/planning/sprint-1-checklist.png) | ✅ Complete |
| Sprint 2 Checklist | Aman | [docs/planning/sprint-2-checklist.png](docs/planning/sprint-2-checklist.png) | ✅ Complete |
| Meeting Notes (4 Nov) | Joshua | [docs/meetings/meeting-notes-04-11-2026.docx](docs/meetings/meeting-notes-04-11-2026.docx) | ✅ Complete |
| Contribution Matrix | Joshua | [docs/assessment/contributions-matrix-draft.docx](docs/assessment/contributions-matrix-draft.docx) | Pending group agreement and signatures (#9) |
| Kanban Board: Sprint 1 | Joshua | [GitHub Project 4](https://github.com/users/J-Colman/projects/4) | ✅ Complete |
| Kanban Board: Sprint 2 | Joshua, Ada | [GitHub Project 6](https://github.com/users/J-Colman/projects/6) | ✅ Complete |
| Kanban Board: Sprint 3 | Joshua, Ada | [GitHub Project 7](https://github.com/users/J-Colman/projects/7) | 🟡 In progress |
| README | Joshua | [README.md](README.md) | Updated |

---

## Project Management

- [Kanban Board - Sprint 1](https://github.com/users/J-Colman/projects/4)
- [Kanban Board - Sprint 2](https://github.com/users/J-Colman/projects/6)
- [Kanban Board - Sprint 3](https://github.com/users/J-Colman/projects/7)
- [Traceability Matrix](docs/analysis/traceability-matrix.docx)
- [Contribution Matrix](docs/assessment/contributions-matrix-draft.docx)
- [Gantt Chart](docs/planning/gantt-chart.png)
- [Master Backlog](docs/planning/master-backlog-sprint-3.pdf)

---

## Process Automation

F1 and F2 run on Camunda 8 (SaaS cluster). User tasks are completed in Tasklist and service tasks are handled by Python job workers in `automation/`.

**Deploy order** (Web Modeler, same cluster): Authenticate Customer sub-process -> delivery-options DMN -> forms -> F1 -> F2.

### Running the job workers

Requires Python 3.12+ and client credentials for the cluster (Camunda Console -> cluster -> API -> Create client).

```bash
python3 -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp automation/.env.example automation/.env # env.example is your own filename e.g. josh-colman.env.sh
python automation/main.py
```

Required environment variables: `CAMUNDA_REST_ADDRESS`, `CAMUNDA_CLIENT_ID`, `CAMUNDA_CLIENT_SECRET`, `CAMUNDA_OAUTH_URL`, `CAMUNDA_TOKEN_AUDIENCE`. Never commit `.env`.

### Job types

| Process | Job type | Should return | Implemented |
|---|---|---|---|
| Login | `job-check-credentials` | `credentialsValid`, `loginAttempts`, `customerId`, `loggedIn` | Stub |
| Login | `job-create-account` | `customerId`, `loggedIn` | Stub |
| F1 | `job-check-stock` | `stockStatus` (`EMPTY`, `PARTIAL` or other), `unavailableItems` | Stub |
| F1 | `job-show-unavailable-items` | Nothing (shows the unavailable items) | Stub |
| F1 | `job-identify-producers` | `producers` (list with `name`, `offersDelivery`; feeds the DMN) | Stub |
| F1 | `job-prepare-order-summary` | `orderSummary` | Stub |
| F1 | `job-reserve-stock` | `reservationId` (or throws `STOCK_UNAVAILABLE`) | Stub |
| F1 | `job-create-order` | `orderId` | Stub |
| F1 | `job-split-by-producer` | `producerOrders` (list with `producer`, `total`) | Stub |
| F1 | `job-publish-order-ready` | Publishes `OrderReadyForPayment` with `orderId`, `customerId`, `producerOrders` | Stub |

F2 jobs yet to be implemented.

### Running a demo
1. Start the workers.
2. Start an instance of F1 from Web Modeler or Operate.
3. Complete the user tasks in Tasklist. Follow progress and variables in Operate.

### Testing
`pytest` will run the worker unit tests in `automation/`, but isn't currently implemented.

### Known limitations
- F2 job workers are not yet implemented.
- Camunda Forms cannot mask passwords or card numbers, so use test data only. Task 2 handles these in Django.
- One delivery choice applies to the whole order, not per producer.

---

## Academic Integrity Note

No AI-generated BPMN or i* diagrams. AI may be used for code only if usage is disclosed and understood. Work must be the group’s own, don’t share with other groups.
