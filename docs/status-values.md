# Framework Status Values Reference

This document defines the standardized status values used throughout the framework.

## Task Status Values

**Used in:** Task files (`T*.md`, `TX*.md`)  
**Location:** Front matter `status` field

| Status           | Meaning                          | Next Status               |
| ---------------- | -------------------------------- | ------------------------- |
| `open`           | Task ready to start              | `in_progress`             |
| `in_progress`    | Currently being worked on        | `pending_review`          |
| `pending_review` | Awaiting code review             | `done` or `failed`        |
| `done`           | Successfully completed           | (final - rename to `TX*`) |
| `failed`         | Could not be completed           | `open` (for retry)        |
| `blocked`        | Cannot proceed due to dependency | `open` (when unblocked)   |

**Example:**
```yaml
---
task_id: T01_S01
status: in_progress
---
```

## Sprint Status Values

**Used in:** Sprint meta files (`S*_sprint_meta.md`)  
**Location:** Front matter `status` field

| Status      | Meaning                            | Next Status              |
| ----------- | ---------------------------------- | ------------------------ |
| `pending`   | Sprint planned but not started     | `active`                 |
| `active`    | Sprint currently in progress       | `completed` or `aborted` |
| `completed` | Sprint successfully finished       | (final)                  |
| `aborted`   | Sprint cancelled before completion | (final)                  |

**Example:**
```yaml
---
sprint_sequence_id: S01
status: active
---
```

## Milestone Status Values

**Used in:** Milestone meta files (`M*_milestone_meta.md`)  
**Location:** Front matter `status` field

| Status      | Meaning                                   | Next Status                          |
| ----------- | ----------------------------------------- | ------------------------------------ |
| `pending`   | Milestone planned but not started         | `active`                             |
| `active`    | Milestone currently in progress           | `completed`, `blocked`, or `on_hold` |
| `completed` | Milestone successfully finished           | (final)                              |
| `blocked`   | Cannot proceed due to external dependency | `active` (when unblocked)            |
| `on_hold`   | Temporarily paused                        | `active` (when resumed)              |

**Example:**
```yaml
---
milestone_id: M01
status: active
---
```

## Project Status Values

**Used in:** Project manifest (`00_PROJECT_MANIFEST.md`)  
**Location:** Front matter `status` field

| Status     | Meaning                             | Description          |
| ---------- | ----------------------------------- | -------------------- |
| `active`   | Project currently under development | Normal working state |
| `on_hold`  | Project temporarily paused          | Can be resumed later |
| `archived` | Project completed or cancelled      | No longer active     |

**Example:**
```yaml
---
project_name: TaskFlow
status: active
---
```

## ADR Status Values

**Used in:** Architecture Decision Records (`ADR*.md`)  
**Location:** Front matter `status` field

| Status       | Meaning                           | Next Status                  |
| ------------ | --------------------------------- | ---------------------------- |
| `proposed`   | Decision under consideration      | `accepted` or `rejected`     |
| `accepted`   | Decision approved and implemented | `deprecated` or `superseded` |
| `deprecated` | No longer recommended             | (final)                      |
| `superseded` | Replaced by newer decision        | (final)                      |

**Example:**
```yaml
---
adr_id: ADR001
status: accepted
---
```

## Status Transition Rules

### Task Lifecycle
```
open → in_progress → pending_review → done
  ↓         ↓              ↓
blocked   failed      failed
  ↓         ↓              ↓  
open      open        open
```

### Sprint Lifecycle
```
pending → active → completed
            ↓
         aborted
```

### Milestone Lifecycle
```
pending → active → completed
            ↓  ↑        
         blocked/     
         on_hold      
```

## Validation Rules

1. **Status values are case-sensitive** - use exact lowercase values
2. **Status must be from approved list** - no custom status values
3. **Transitions must follow rules** - cannot jump arbitrarily between statuses
4. **Completed items are immutable** - don't change status after completion
5. **Use timestamps** - update `last_updated` when changing status

## Common Mistakes

### ❌ Wrong Status Values
```yaml
status: Not Started  # Use: open
status: In Progress  # Use: in_progress
status: Complete     # Use: completed
status: Canceled     # Use: aborted
```

### ❌ Invalid Transitions
```yaml
# Cannot go directly from open to done
status: open → done  # Must go through in_progress

# Cannot reopen completed items
status: completed → in_progress  # Create new task instead
```

### ✅ Correct Usage
```yaml
status: open
status: in_progress
status: pending_review
status: done
```

## Framework Commands and Status

Commands expect these specific status values:

- `/project:simone:do_task` looks for tasks with `status: open`
- Task completion changes status to `done` and renames file to `TX*`
- Code review may change status from `pending_review` to `done` or `failed`

---

_This reference ensures consistent status tracking across all framework components._