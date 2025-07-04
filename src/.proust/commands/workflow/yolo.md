# Command: yolo

**Command**: `/project:yolo`
**Category**: Workflow
**Purpose**: Execute all open tasks autonomously with safety guidelines and comprehensive automation

## Purpose
Execute **all** open tasks autonomously—without user interaction—prioritising completion and adhering to safety guidelines.

## Context Loading

### Required Context
- `project/manifest.yml` - Project state and active work
- `project/sprints/**` - Sprint definitions and task lists
- `project/tasks/**` - All task details and requirements
- `core/guardrails.yml` - Safety constraints and quality standards

### Generated Context
- Autonomous task execution log
- Project review results
- Summary report of all work completed

## Inputs
| Variable      | Description                                     | Example      |
| ------------- | ----------------------------------------------- | ------------ |
| `$ARGUMENTS?` | Optional sprint ID (e.g., `S03`) or extra flags | `S02`        |
| `$DATE`       | Current UTC date                                | `2025-07-04` |

## Safety Guidelines
- Do **NOT** modify critical files (`.env`, migrations, prod configs).
- **STOP** on database schema changes, >5 file deletions, or failing tests post-change.
- Always run `/project:test` after each task.

## Steps

1. **Initial setup**
   - Record start `$DATE`.
   - Run `/project:test` to ensure clean baseline.
   - If fail rate >10 % and fixable quickly → fix; else continue.
   - Capture `git status`; note if dirty.

2. **Determine mode**
   - If `$ARGUMENTS?` contains sprint ID → *Sprint mode* (work only in that sprint).
   - Else → *General mode*: general tasks → active sprint tasks → sprints needing task creation.

3. **Find open work**
   - Sprint mode: locate tasks in `project/tasks/` with matching sprint ID.
     - If none and sprint meta exists → go to **Create sprint tasks**.
     - If sprint missing → exit with error.
   - General mode:
     - Check `project/tasks/` for general tasks (T### pattern).
     - Identify active sprint from manifest and its tasks.
     - Detect sprints with only meta (need tasks).
   - Select lowest-ID open task not yet attempted.

4. **Create sprint tasks** (if sprint has only meta)
   - Invoke `/project:create_sprint_tasks -s $SPRINT_ID`.
   - Return to **Find open work**.

5. **Work on task**
   - If task previously attempted → skip.
   - Create branch `task/<task-id>`.
   - Run `/project:do_task $TASK_ID`.
   - After completion run `/project:test`.
   - Critical failures → attempt fix; non-critical → log & proceed.

6. **Commit work**
   - If tests passing & no critical issues:
     - Call `/project:commit $TASK_ID YOLO`.
     - Merge to main (`git merge task/<task-id>`).
   - On commit failure → log & continue.

7. **Repeat**
   - Sprint mode: iterate tasks until sprint complete, then project review.
   - General mode: loop through general tasks, then active sprint tasks, etc.
   - If no tasks remain → proceed.

8. **Project review**
   - Run `/project:project_review`.
   - If review **FAIL** and quick fixes possible → fix & rerun review.
   - Else create general tasks for issues and return to **Find open work**.
   - On **PASS** proceed.

9. **Summary**
   - Calculate duration (now − start).
   - Report: mode, tasks created, completed, skipped, failures, duration, critical issues, test status, next action.

## Definition of Done
- All accessible tasks processed or project review completed.
- Summary printed.

## Follow-ups
- User may review commits, merged branches, and summary report.
