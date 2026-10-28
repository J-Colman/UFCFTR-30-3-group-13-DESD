# Bristol Regional Food Network — Digital Marketplace

## UFCFTR-30-3 Distributed and Enterprise Software Development

The Bristol Regional Food Network is a community digital marketplace connecting around 40 local food producers with consumers within 20 miles of Bristol, helping small producers reach customers beyond farmers’ markets and farm-gate sales. It lets producers list seasonal products and manage availability, while customers browse by category, place single or multi-vendor orders, and check out through a sandbox payment service, with traceability, food-miles reporting and surplus-produce features.

## The Team — Group 13

| Name | GitHub Handle | Role |
| --- | --- | --- |
| Joshua | [@J-Colman](https://github.com/J-Colman) | Lead/Integration |
| Izzy | [@Awesometeapot1](https://github.com/Awesometeapot1) | Business Analyst |
| Ada | [@aido77](https://github.com/aido77) | Strategic BPMN |
| Aman | [@N30NW1LD-2005](https://github.com/N30NW1LD-2005) | Product Owner/Planning |
| Yonas | [@yonas1212](https://github.com/yonas1212) | Product Owner/Planning |

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
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── docs/
    ├── analysis/
    │   ├── stakeholder-analysis.docx
    │   └── traceability.md
    ├── assessment/
    │   ├── assessment-brief-task-1.pdf
    │   ├── case-study.pdf
    │   ├── contributions-matrix-template.docx
    │   └── task-1-use-cases.pdf
    ├── models/
    │   ├── strategic-bpmn.bpmn
    │   ├── strategic-bpmn.png
    │   ├── case-2-use-case-diagram.pdf
    │   ├── case-2-class-diagram.pdf
    │   ├── case-2-component-diagram.pdf
    │   ├── case-2-sequence-diagram.pdf
    │   ├── case-2-i-star-sd-model.png
    │   ├── case-2-i-star-sr-model.png
    │   ├── case-2-i-star-sr-model.json
    │   ├── case-2-operational-bpmn.bpmn
    │   └── case-2-operational-bpmn.png
    └── planning/
        ├── gantt-chart.pdf
        ├── gantt-chart.png
        ├── master-backlog.md
        ├── moscow-prioritisation.md
        ├── product-backlog.md
        ├── scope.md
        ├── sprint-1-checklist.png
        └── sprint-1-week-1-plan.md
```

---

## Artefacts

| Artefact | Owner | Location | Status |
| --- | --- | --- | --- |
| Assessment Brief | Module team | [docs/assessment/assessment-brief-task-1.pdf](docs/assessment/assessment-brief-task-1.pdf) | Reference copy committed |
| Case Study | Module team | [docs/assessment/case-study.pdf](docs/assessment/case-study.pdf) | Reference copy committed |
| Task 1 Use Cases | Module team | [docs/assessment/task-1-use-cases.pdf](docs/assessment/task-1-use-cases.pdf) | Reference copy committed |
| Contribution Matrix Template | Module team | [docs/assessment/contributions-matrix-template.docx](docs/assessment/contributions-matrix-template.docx) | Reference copy committed |
| Stakeholder Analysis | Izzy | [docs/analysis/stakeholder-analysis.docx](docs/analysis/stakeholder-analysis.docx) | Committed |
| Traceability Matrix | Joshua | [docs/analysis/traceability.md](docs/analysis/traceability.md) | Draft committed (#10) |
| FR/NFR Analysis | Izzy | `docs/analysis/requirements.md` | Pending #12 |
| Major Process List | Yonas | `docs/analysis/major-process-list.md` | Pending #5 |
| Strategic BPMN | Ada | [docs/models/strategic-bpmn.bpmn](docs/models/strategic-bpmn.bpmn) | Draft committed (#4); gaps in traceability |
| Strategic BPMN Image | Ada | [docs/models/strategic-bpmn.png](docs/models/strategic-bpmn.png) | Draft committed |
| Case 2 Use Case Diagram | Yonas | [docs/models/case-2-use-case-diagram.pdf](docs/models/case-2-use-case-diagram.pdf) | Committed |
| Case 2 Class Diagram | Yonas | [docs/models/case-2-class-diagram.pdf](docs/models/case-2-class-diagram.pdf) | Committed |
| Case 2 Component Diagram | Yonas | [docs/models/case-2-component-diagram.pdf](docs/models/case-2-component-diagram.pdf) | Committed |
| Case 2 Sequence Diagram | Yonas | [docs/models/case-2-sequence-diagram.pdf](docs/models/case-2-sequence-diagram.pdf) | Committed |
| i* SD Model | Yonas | [docs/models/case-2-i-star-sd-model.png](docs/models/case-2-i-star-sd-model.png) | WIP committed; Sprint 2 summative |
| i* SR Model | Yonas | [docs/models/case-2-i-star-sr-model.png](docs/models/case-2-i-star-sr-model.png) | WIP committed; Sprint 2 summative |
| i* SR piStar Source | Yonas | [docs/models/case-2-i-star-sr-model.json](docs/models/case-2-i-star-sr-model.json) | Committed |
| Case 2 Operational BPMN | Ada | [docs/models/case-2-operational-bpmn.bpmn](docs/models/case-2-operational-bpmn.bpmn) | Draft committed; gateway fixes in Sprint 2 |
| Case 2 Operational BPMN Image | Ada | [docs/models/case-2-operational-bpmn.png](docs/models/case-2-operational-bpmn.png) | Draft committed |
| Scope and Functionality Confirmation | Joshua | [docs/planning/scope.md](docs/planning/scope.md) | Confirmed (#11) |
| Master Backlog | Aman | [docs/planning/master-backlog.md](docs/planning/master-backlog.md) | Committed; canonical backlog |
| Product Backlog | Aman | [docs/planning/product-backlog.md](docs/planning/product-backlog.md) | Committed; legacy view |
| MoSCoW Prioritisation | Aman | [docs/planning/moscow-prioritisation.md](docs/planning/moscow-prioritisation.md) | Committed |
| Sprint 1 Plan | Joshua | [docs/planning/sprint-1-week-1-plan.md](docs/planning/sprint-1-week-1-plan.md) | Committed |
| Gantt Chart | Aman | [docs/planning/gantt-chart.png](docs/planning/gantt-chart.png) | Committed |
| Sprint 1 Checklist | Aman | [docs/planning/sprint-1-checklist.png](docs/planning/sprint-1-checklist.png) | Committed |
| Contribution Matrix Draft | Joshua | `docs/contribution-matrix/contribution-matrix-sprint-1-draft.docx` | Pending #9 |
| Sprint 1 Kanban | Joshua | [GitHub Project](https://github.com/users/J-Colman/projects/4) | Public, linked to repo, 12 items |
| README | Joshua | [README.md](README.md) | Committed |

---

## Project Management

- [Kanban Board](https://github.com/users/J-Colman/projects/4)
- [Scope and Functionality Confirmation](docs/planning/scope.md)
- [Traceability Matrix](docs/analysis/traceability.md)
- [Gantt Chart](docs/planning/gantt-chart.png)
- [Sprint 1 Plan](docs/planning/sprint-1-week-1-plan.md)
- [MoSCoW Prioritisation](docs/planning/moscow-prioritisation.md)

---

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (manages Python 3.12 and dependencies)
- Camunda 8.10 Web Modeler is used for BPMN modelling. Access is via the module Camunda organisation

### Python Environment

```bash
uv sync                      # creates .venv with the exact locked versions
uv add <package>             # add a dependency (never use pip install)
uv run <command>             # run a command inside the environment

```

---

## Commit Conventions

- **Commit your own work.** Each member should push their own artefacts so the commit history reflects individual contribution.
- **If you commit someone else’s file**, credit them as a co-author:
  ```text
  Co-authored-by: Name <email>
  ```
- Keep commits small and focused. One artefact or logical change per commit, don’t dump everything into one final commit.
- Use clear prefixes:
  - `docs`: documentation, analysis, plans and models
  - `feat`: new executable functionality
  - `fix`: corrections to a model or code
  - `chore`: repo setup, tooling and cleanup
- Reference the issue where relevant, for example:
  ```text
  docs(analysis): add major process list (#5)
  docs(planning): add initial product backlog (#6)
  docs(models): add operational BPMN for case 2
  ```
- Commit source artefacts, not just screenshots or exports. For example .bpmn, .md, and the assessment .pdf/.docx files.
- Never commit .venv, .env, keys, databases or .DS_Store.
- Push regularly. A steady history is stronger evidence than one large commit at the end.
- Once a commit is pushed to main, don’t amend or force-push it. Add a follow-up commit instead.
- Every member should have at least one commit per sprint. Co-author credit is useful, but it is not a substitute for your own commit.

---

## Academic Integrity Note

No AI-generated BPMN or i* diagrams. AI may be used for code only if usage is disclosed and understood. Work must be the group’s own, don’t share with other groups.
