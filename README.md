# Bristol Regional Food Network — Digital Marketplace

## UFCFTR-30-3 Distributed and Enterprise Software Development

The Bristol Regional Food Network is a community digital marketplace connecting around 40 local food producers with consumers within 20 miles of Bristol, helping small producers reach customers beyond farmers’ markets and farm-gate sales. It lets producers list seasonal products and manage availability, while customers browse by category, place single or multi-vendor orders, and check out through a sandbox payment service, with traceability, food-miles reporting and surplus-produce features.

## The Team - Group 13

| Name | GitHub Handle | Role |
| --- | --- | --- |
| Joshua | [@J-Colman](https://github.com/J-Colman) | Lead/Integration |
| Izzy | [@Awesometeapot1](https://github.com/Awesometeapot1) | Business Analyst |
| Ada | [@aido77](https://github.com/aido77) | Strategic BPMN |
| Aman | [@N30NW1LD-2005](https://github.com/N30NW1LD-2005) | Product Owner/Planning |
| Yonas | [@yonas1212](https://github.com/yonas1212) | Product Owner/Planning |

---

## Case 2 — Customer Multi-Vendor Order, Checkout and Payment

Two major functionalities: TBC - pending confirmation with the module team (#11)

---

## Repository Structure

```
UFCFTR-30-3-group-13-DESD/
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── docs/
    ├── assessment/
    │   ├── assessment-brief-task-1.pdf
    │   ├── case-study.pdf
    │   ├── task-1-use-cases.pdf
    │   └── contributions-matrix-template.docx
    ├── analysis/
    │   ├── stakeholder-analysis.docx
    │   └── case-2-use-case-diagram.pdf
    ├── models/
    │   ├── operational-bpmn-use-case-2.bpmn
    │   ├── operational-bpmn-use-case-2.png
    │   └── sequence-diagram.pdf
    ├── planning/
    │   ├── sprint-1-week-1-plan.md
    │   └── task-1-gantt-chart.pdf
    └── contribution-matrix/
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
| Case 2 Use Case Diagram | Yonas | [docs/analysis/case-2-use-case-diagram.pdf](docs/analysis/case-2-use-case-diagram.pdf) | Committed |
| Case 2 Operational BPMN | Ada | [docs/models/operational-bpmn-use-case-2.bpmn](docs/models/operational-bpmn-use-case-2.bpmn) | Committed |
| Case 2 Operational BPMN Image | Ada | [docs/models/operational-bpmn-use-case-2.png](docs/models/operational-bpmn-use-case-2.png) | Committed |
| Sequence Diagram | Yonas | [docs/models/sequence-diagram.pdf](docs/models/sequence-diagram.pdf) | Committed |
| Task 1 Gantt Chart | Aman | [docs/planning/task-1-gantt-chart.pdf](docs/planning/GANTT%20CHART.png) | Committed |
| Sprint 1 Plan | Joshua | [docs/planning/sprint-1-week-1-plan.md](docs/planning/sprint-1-week-1-plan.md) | Committed |
| Sprint 1 MoSCow Prioritisation | Aman | [docs/planning/sprint-1-week-1-plan.md](docs/planning/MOSCOW%20PRIORITISATION.png) | Committed |
| Sprint 1 Sprint Checklist | Aman | [docs/planning/sprint-1-week-1-plan.md](docs/planning/SPRINT%20CHECKLIST.png) | Committed |
| README | Joshua | [README.md](README.md) | Committed |
| Sprint 1 Kanban | Joshua | [GitHub Project](https://github.com/users/J-Colman/projects/4) | Public, linked to repo, 11 items |
| Strategic BPMN | Ada | `docs/models/strategic-bpmn.bpmn` not yet in repo | Pending #4 |
| Major Process List | Yonas | `docs/analysis/major-process-list.md` | Pending #5 |
| Product Backlog | Aman | `docs/planning/product-backlog.md` | Pending #6 |
| Contribution Matrix Draft | Joshua | `docs/contribution-matrix/contribution-matrix-sprint-1-draft.docx` | Pending #9 |
| Traceability Table | Joshua | `docs/analysis/traceability.md` | Pending #10, blocked by #4 |
| Functionality Confirmation | Joshua | `docs/planning/scope.md` | Pending #11 |

---

## Project Management

- [Kanban Board](https://github.com/users/J-Colman/projects/4)
- [Gantt Chart](https://github.com/J-Colman/UFCFTR-30-3-group-13-DESD/blob/main/docs/planning/GANTT%20CHART.png)
- [Sprint Plan](https://github.com/J-Colman/UFCFTR-30-3-group-13-DESD/blob/main/docs/planning/sprint-1-week-1-plan.md)
- [MoSCoW Prioritisation](https://github.com/J-Colman/UFCFTR-30-3-group-13-DESD/blob/main/docs/planning/MOSCOW%20PRIORITISATION.png)

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

