# CLAUDE.md - Tasks Folder Guide

## Overview
This folder contains detailed task definition files for complex tasks that need their own dedicated files. Simple tasks can be embedded directly in sprint files, but complex tasks benefit from detailed standalone documentation.

## When to Create Task Files

### Create Separate Task Files For:
- **Complex implementation** requiring detailed planning
- **Multi-step processes** with significant sub-tasks
- **High-risk tasks** needing careful documentation
- **Tasks spanning multiple days** of development work
- **Tasks requiring detailed context** or external resources

### Keep Tasks Embedded in Sprint Files For:
- **Simple, single-step tasks** (< 2 hours work)
- **Configuration changes** or small updates
- **Quick fixes** or minor modifications
- **Documentation updates** or simple additions

## Naming Convention
**CRITICAL**: Task files MUST follow this exact pattern:

### Sprint Tasks:
```
M##_S##_T##_Task_Name.md
```

### General Tasks (not part of sprint):
```
T###_Task_Name.md
```

### Completed Tasks (rename when done):
```
TXM##_S##_T##_Task_Name.md  (for sprint tasks)
TX###_Task_Name.md          (for general tasks)
```

### Examples:
- ✅ `M01_S01_T01_Setup_Authentication.md`
- ✅ `M01_S02_T03_Implement_API_Endpoints.md`
- ✅ `T001_Fix_Button_Color.md`
- ✅ `TXM01_S01_T01_Setup_Authentication.md` (completed)
- ❌ `T1_Setup.md` (wrong format)
- ❌ `M01-S01-T01-Setup.md` (wrong separators)
- ❌ `Setup_Authentication.md` (missing prefix)

## Task Structure
Each task file MUST contain:

### 1. YAML Frontmatter (REQUIRED)
```yaml
---
id: "M##_S##_T##" | "T###"
type: "task"
title: "Task Name"
status: "open | in_progress | done | blocked"
parent_id: "M##_S##" (for sprint tasks)
sprint_id: "M##_S##" (for sprint tasks)
milestone_id: "M##" (for sprint tasks)
complexity: "low | medium | high"
priority: "high | medium | low"
created: "YYYY-MM-DDTHH:MM:SSZ"
updated: "YYYY-MM-DDTHH:MM:SSZ"
---
```

### 2. Content Sections
- **Task Overview** - What this task accomplishes
- **Objectives** - Primary goal and deliverables
- **Acceptance Criteria** - Specific completion requirements
- **Implementation Steps** - Detailed breakdown
- **Technical Requirements** - Dependencies and file changes
- **Context & Resources** - Background and references
- **Progress Log** - Development timeline
- **Completion Notes** - Post-completion summary

## Creating New Tasks

### Step 1: Determine Task Type
- **Sprint task**: Part of specific sprint goal
- **General task**: Standalone improvement or fix

### Step 2: Use Template
Copy from ` _templates/task_template.md` and customize:
```bash
# For sprint tasks
cp  _templates/task_template.md tasks/M##_S##_T##_Your_Task.md

# For general tasks
cp  _templates/task_template.md tasks/T###_Your_Task.md
```

### Step 3: Define Clear Objectives
- Primary goal statement
- Specific deliverables
- Measurable outcomes

### Step 4: Break Down Implementation
- Step-by-step approach
- Sub-tasks and checkpoints
- File changes expected

## Task Lifecycle

### 1. Planning Phase
- Define objectives and acceptance criteria
- Identify dependencies and risks
- Plan implementation approach

### 2. Implementation Phase
- Update progress log regularly
- Track file changes and decisions
- Note issues and solutions

### 3. Completion Phase
- Verify all acceptance criteria met
- Complete progress log
- Add completion notes and lessons learned
- Rename file with TX prefix

## Status Workflow
```
open → in_progress → done
  ↓         ↓         ↑
blocked ←---+         |
  ↓                   |
done ←-----------------+
```

## Task Categories

### Sprint Tasks (M##_S##_T##)
- Part of specific sprint
- Contribute to sprint goal
- Have milestone and sprint context
- Follow sprint timeline

### General Tasks (T###)
- Standalone improvements
- Bug fixes and maintenance
- Infrastructure work
- Documentation updates

### Completed Tasks (TX prefix)
- Keep for reference and learning
- Show what was accomplished
- Preserve lessons learned
- Maintain project history

## Important Notes for AI

1. **Context loading** - Task files automatically load parent sprint/milestone context
2. **Progress tracking** - Update progress log as work proceeds
3. **File changes** - Document all modified/created files
4. **Testing** - Include testing requirements and approach
5. **Completion** - Verify all acceptance criteria before marking done

## Integration with Commands
Task files are automatically loaded by commands:
- `/project:do_task -t M01_S01_T01` loads task file and context
- `/project:status` shows task progress across project
- Task completion updates parent sprint progress

## Common Mistakes to Avoid
- Creating task files for simple tasks (embed in sprint instead)
- Forgetting parent_id linkages for sprint tasks
- Not updating progress log during implementation
- Missing acceptance criteria or making them too vague
- Not documenting file changes and decisions
- Forgetting to rename with TX prefix when complete

## Best Practices
- **Atomic tasks** - Each task should accomplish one clear objective
- **Time-boxed** - Tasks should be completable in 1-3 days
- **Well-defined** - Clear acceptance criteria and implementation steps
- **Context-rich** - Include relevant background and resources
- **Progress-tracked** - Regular updates to progress log

This folder contains the detailed work items that implement the project's goals.