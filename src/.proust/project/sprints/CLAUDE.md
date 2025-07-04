# CLAUDE.md - Sprints Folder Guide

## Overview
This folder contains sprint definition files that represent focused development iterations within milestones. Each sprint defines specific goals, tasks, and deliverables for a 1-2 week development cycle.

## Naming Convention
**CRITICAL**: Sprint files MUST follow this exact pattern:
```
M##_S##_Sprint_Name.md
```

- `M##` - Parent milestone number (M01, M02, etc.)
- `S##` - Sprint number within milestone (S01, S02, etc.)
- `_` - Single underscore separators
- `Sprint_Name` - Descriptive name using underscores for spaces

### Examples:
- ✅ `M01_S01_Foundation_Setup.md`
- ✅ `M01_S02_Core_Features.md`
- ✅ `M02_S01_Authentication_System.md`
- ❌ `S01_Foundation.md` (missing milestone prefix)
- ❌ `M01-S01-Foundation.md` (wrong separator)
- ❌ `M1_S1_Foundation.md` (missing leading zeros)

## Sprint Structure
Each sprint file MUST contain:

### 1. YAML Frontmatter (REQUIRED)
```yaml
---
id: "M##_S##"
type: "sprint"
title: "Sprint Name"
status: "open | in_progress | done | blocked"
parent_id: "M##"
milestone_id: "M##"
goal: "Primary sprint objective"
created: "YYYY-MM-DDTHH:MM:SSZ"
updated: "YYYY-MM-DDTHH:MM:SSZ"
priority: "high | medium | low"
---
```

### 2. Content Sections
- **Sprint Overview** - What this sprint accomplishes
- **Sprint Goal** - Clear, focused objective
- **Sprint Tasks** - Embedded or referenced tasks (M##_S##_T##)
- **Key Deliverables** - Expected outcomes
- **Technical Considerations** - Dependencies and risks
- **Definition of Done** - Sprint completion criteria
- **Sprint Retrospective** - Post-completion analysis

## Task Organization Options

### Option 1: Embedded Tasks (Recommended for Simple Tasks)
```markdown
### M01_S01_T01: Setup Project Structure
**Status**: open
**Description**: Create basic project directory structure
**Acceptance Criteria**:
- [ ] Directory structure created
- [ ] Basic configuration files added
```

### Option 2: Referenced Tasks (For Complex Tasks)
```markdown
### M01_S01_T01: Setup Authentication System
**Status**: in_progress
**Description**: Implement user authentication
**File**: `../tasks/M01_S01_T01_Setup_Authentication.md`
```

## Creating New Sprints

### Step 1: Use Template
Copy from ` _templates/sprint_meta_template.md` and customize:
```bash
cp  _templates/sprint_meta_template.md sprints/M##_S##_Your_Sprint.md
```

### Step 2: Link to Parent Milestone
Ensure the sprint aligns with its parent milestone goals and requirements.

### Step 3: Define Clear Goal
Each sprint should have one primary, achievable objective.

### Step 4: Plan Tasks
Break sprint goal into specific, actionable tasks (3-8 tasks per sprint).

## Sprint Planning Guidelines

### Sprint Scope
- **Duration**: 1-2 weeks of development work
- **Focus**: Single primary objective with supporting tasks
- **Size**: 3-8 tasks that can realistically be completed
- **Dependencies**: Minimal external dependencies

### Task Breakdown
- **Simple tasks**: Embed directly in sprint file
- **Complex tasks**: Create separate files in ../tasks/
- **Task naming**: M##_S##_T## (e.g., M01_S01_T01, M01_S01_T02)

## Status Workflow
```
open → in_progress → done
  ↓         ↓         ↑
blocked ←---+         |
  ↓                   |
done ←-----------------+
```

## Sprint Retrospectives
Complete after sprint ends:

### What Went Well
- What worked effectively
- Positive outcomes and achievements

### What Could Be Improved
- Challenges encountered
- Process improvements needed

### Action Items for Next Sprint
- Specific changes to implement
- Process adjustments

## Important Notes for AI

1. **Sprint focus** - Each sprint should have one clear, primary goal
2. **Task breakdown** - Break goal into specific, actionable tasks
3. **Milestone alignment** - Sprint must contribute to parent milestone
4. **Realistic scope** - Don't overcommit; better to under-promise and over-deliver
5. **Context loading** - Sprint files provide context for task execution

## Integration with Commands
Sprint files are automatically loaded by commands:
- `/project:create_tasks -s M01_S01` reads sprint for task generation
- `/project:do_task -t M01_S01_T01` loads sprint context
- `/project:status` shows sprint progress
- `/project:switch_sprint M01_S02` changes active sprint

## Common Mistakes to Avoid
- Creating sprints without clear, focused goals
- Making sprints too large (should be completable in 1-2 weeks)
- Forgetting milestone prefix (must start with M##_S##)
- Using wrong separators (use underscores, not hyphens)
- Not defining clear acceptance criteria for tasks
- Creating dependencies between parallel sprints

This folder organizes the actual development work within the project's milestone structure.