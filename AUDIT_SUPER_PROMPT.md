# 📓 Context Framework — Examples Playbook
A quick‑reference of the most common artefacts and command flows that live in this repository.  
Copy‑paste, adapt, and go.

---

## 1 · Canonical Simone Workflows

| #     | When you need to…                                  | Command Sequence (happy‑path)                                                                                       |
| ----- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **A** | Bootstrap a **brand‑new repo**                     | `/initialize_new_project` → `/analyze_codebase` → `/create_sprints_from_milestone M01` → `/create_sprint_tasks S01` |
| **B** | Produce a **first health report** on existing code | `/analyze_codebase` → `/project_review`                                                                             |
| **C** | Add a **general enhancement** outside a sprint     | `/create_general_task "Task Title"` → `/do_task T###` → `/commit T###`                                              |
| **D** | Plan the **next sprint** in an active milestone    | `/plan_sprints_from_milestone M02` → `/create_sprint_tasks S02`                                                     |
| **E** | Run the **daily dev loop** on an open task         | `/do_task` *(auto‑selects next task)* → `/commit TASK_ID`                                                           |
| **F** | **Audit tests** & their strategy                   | `/test` → `/test_review`                                                                                            |
| **G** | **Autonomous burst / CI‑style run**                | `/yolo` *(or `/yolo S03`)*                                                                                          |

---

## 2 · Mini‑Snippets from Key Templates

### universal_claude.md (excerpt)

```markdown
### 1. Clarify Scope First
- Map out exactly how you will approach the task…
…
### 5. Deliver Clearly
- Summarize what was changed and why
- List every file modified…
```
@@

### guardrails.yml (excerpt)

```yaml
guidelines:
  always:
    - Read and follow `architecture/*.yaml`
    - Reuse helpers; never create duplicates…
  never:
    - Use raw hex colors inside widgets
    - Hard‑code spacing such as `EdgeInsets(17)`
```
@@

### manifesto.yaml (frontend excerpt)

```yaml
project:
  name: sample_app
  runtime: flutter
  architecture: clean architecture
kaspa_integration:
  sdk_package: kaspa_flutter_core
  key_derivation_path: "m/44'/111111'/0'/0/0"
```
*** End Patch

---

## 3 · Guardrails Banner for Frozen Modules

```dart
// 🚫 FROZEN MODULE!
// Only fix bugs or adjust styles. No refactor without PM approval.
// DESIGN_TOKEN_ENFORCED
// Colors & spacing come from theme/ tokens.
// Strings live in app_strings.dart
```

---

## 4 · Example Brand YAML Call‑out

```yaml
colors:
  primary:   "#2F80ED"   # primary brand hue
  secondary: "#56CCF2"   # secondary hue
  accent:    "#33FFE0"   # accent / highlight
```

---

## 5 · Task Template Front‑Matter

```markdown
---
task_id: T01_S01
title: Implement Send‑Kaspa Flow
status: not_started
created: 2025‑07‑05 12:04
complexity: medium
dependencies: []
---
```

---

## 6 · Quick “Prime + Sprint” Setup

```text
/prime
/create_sprints_from_milestone M01
/create_sprint_tasks S01
```

Run that trio when you jump onto an unfamiliar codebase and want a ready‑to‑work sprint plan.

---

> **Need more?**  
> Check `.proust/templates/` for additional ready‑to‑copy documents.