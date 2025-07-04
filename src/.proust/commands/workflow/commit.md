# Command: commit

**Command**: `/project:commit`
**Category**: Workflow
**Purpose**: Analyze Git changes, create logical commits with proper messages, and manage version control

## Purpose
Analyze current Git changes, group them into logical commits, obtain user confirmation (unless **YOLO** flag provided), create the commits, and report results.

## Context Loading

### Required Context
- `core/ethos.md` - Commit message standards and conventions
- `project/manifest.yml` - Current sprint and milestone context
- `project/tasks/**` - Task details for commit context

### Generated Context
- Logical commit groupings based on changes
- Conventional commit messages with proper formatting
- Commit history for future reference

## Inputs
| Variable          | Description                                                             | Example                       |
|-------------------|-------------------------------------------------------------------------|-------------------------------|
| `$ARGUMENTS?`     | Optional context identifier(s) &/or `YOLO` flag                         | `T03_S02 YOLO`                |
| `$DATE`           | UTC date                                                                | `2025-07-04`                  |

### Argument Interpretation
* **YOLO** present → skip user-approval step.
* Other tokens → treated as Task-ID or Sprint-ID for scoping (patterns below).

| Pattern                  | Meaning                         | Folder(s) searched                             |
|--------------------------|---------------------------------|-----------------------------------------------|
| `M##_S##_T##`            | Sprint Task                     | `project/tasks/`                                   |
| `T###`                   | General Task                    | `project/tasks/`                                   |
| `M##_S##`                | Entire Sprint                   | `project/sprints/` (all tasks in sprint)          |
| `M##`                    | Entire Milestone                | `project/milestones/` (all related changes)       |

## Preconditions
1. Git repo initialized; commands `git status`, `git diff`, `git add`, `git commit` available.
2. Pre-commit hooks may run; violations must be fixed, **do not bypass**.
3. Agent can run shell commands.

## TODO (execute in order)
1. **Parse arguments & analyze git status**
   - Run concurrently:
     ```bash
     git status --porcelain > /tmp/status.txt
     git diff --staged > /tmp/diff_staged.patch
     git diff > /tmp/diff_unstaged.patch
     ```
   - List changed files hierarchically.
   - If context token present, state: `Context provided: '$ARGUMENTS'`.
   - If no matching files → inform user & exit.

2. **Review changes & group by logical commits**
   - **Context filtering first**: separate `related` vs `unrelated` files.
   - Group related files into minimal logical sets (task completion, bug fix, docs, config, etc.).
   - Defer unrelated files until user asks.

3. **Propose commit structure & messages**
   - For each proposed commit:
     - **Context** (task/sprint)
     - **Files** list
     - **Commit message** (conventional commits, no AI attribution)
     - **Reasoning** one-liner
   - If YOLO flag absent → present plan to user for approval.

4. **User approval check**
   - If YOLO → auto-approve.
   - Else prompt user: *“Approve commit plan? (yes/no/modify)”*
   - Handle modifications; re-prompt until explicit `yes`.

5. **Execute approved commits**
   For each approved commit set:
   ```bash
   git add <files>
   pre-commit run --all-files  # fix issues if hook fails
   git commit -m "<message>"
   ```
   - If additional files remain, loop back to Step 3.

6. **Report commit results**
   Output summary:
   - Commits created (SHA & message)
   - Files committed count
   - Remaining uncommitted changes
   - `git status -sb` snapshot

## Definition of Done
- All intended commits created successfully.
- No pre-commit violations remain.
- Summary printed to console.

## Follow-ups
- If critical issues arise during hooks, create a task via `/project:create_general_task`.
- If unrelated changes remain, ask user whether to run `/commit` again for the rest.
