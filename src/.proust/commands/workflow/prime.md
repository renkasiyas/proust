# Command: prime

**Command**: `/project:prime`
**Category**: Workflow
**Purpose**: Quickly prime agent context with high-level project information and current status

## Purpose

Quickly **prime the agent's context** with high-level project information and current status before executing any project commands.

## Context Loading

### Required Context
- `core/architecture.yml` - Technical stack and architecture decisions
- `project/manifest.yml` - Current project state and active work
- `core/ethos.md` - Project principles and values

### Generated Context
- High-level project summary for AI context
- Current milestone and sprint status
- Active task count and project momentum

## Parameters

*(none)* – this command is non-interactive and requires no parameters.

## Execution

1. **Parallel read** architecture and manifest files.

2. Extract key information:
   - Project name, domain, tech stack from `core/architecture.yml`
   - Current milestone, active sprint, task counts from `project/manifest.yml`
   - Development principles from `core/ethos.md`

3. **Print concise summary** to console:
   ```
   🛠  Project: <name>  |  Stack: <tech stack>
   🚩 Milestone: <id>  |  Active Sprint: <sprint id>  |  Tasks Open: <n>
   📋 Principle: <key ethos statement>
   ```

4. Set internal session variables so subsequent commands inherit these facts.

## Validation

- [ ] Summary printed with project, milestone, and sprint information
- [ ] Tech stack and architecture details loaded
- [ ] No modifications made to any project files
- [ ] AI context primed for subsequent commands

## Related Commands

- `/project:do_task` - Process tasks after context is primed
- `/project:create_general_task` - Create new tasks with context
- `/project:context_management` - More comprehensive context operations

## Notes

- Use at the start of each work session for quick context
- Lightweight alternative to full context refresh
- Essential before task execution in new AI sessions