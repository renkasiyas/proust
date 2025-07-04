# CLAUDE.md - Milestones Folder Guide

## Overview
This folder contains milestone definition files that represent major project phases or feature sets. Each milestone defines high-level goals, requirements, and sprint breakdown.

## Naming Convention
**CRITICAL**: Milestone files MUST follow this exact pattern:
```
M##_Milestone_Name.md
```

- `M##` - Two-digit milestone number (M01, M02, etc.)
- `_` - Single underscore separator
- `Milestone_Name` - Descriptive name using underscores for spaces

### Examples:
- ✅ `M01_Core_Features.md`
- ✅ `M02_User_Authentication.md`
- ✅ `M03_Payment_System.md`
- ❌ `M1_Core.md` (missing leading zero)
- ❌ `M01-Core-Features.md` (wrong separator)
- ❌ `Core_Features.md` (missing M## prefix)

## Milestone Structure
Each milestone file MUST contain:

### 1. YAML Frontmatter (REQUIRED)
```yaml
---
id: "M##"
type: "milestone"
title: "Milestone Name"
status: "open | in_progress | done | blocked"
created: "YYYY-MM-DDTHH:MM:SSZ"
updated: "YYYY-MM-DDTHH:MM:SSZ"
priority: "high | medium | low"
---
```

### 2. Content Sections
- **Milestone Overview** - What this milestone accomplishes
- **Goals** - Primary objectives and success criteria
- **Requirements Analysis** - Key features and user stories
- **Sprint Breakdown** - How work is divided into sprints
- **Technical Considerations** - Dependencies and risks
- **Definition of Done** - Completion criteria

## Creating New Milestones

### Step 1: Use Template
Copy from ` _templates/milestone_meta_template.md` and customize:
```bash
cp  _templates/milestone_meta_template.md milestones/M##_Your_Milestone.md
```

### Step 2: Update Project Manifest
Always update `project/manifest.yml` when creating milestones:
- Add to `milestones.planned` array
- Update `current_state.milestone` if this becomes active

### Step 3: Plan Sprint Structure
Define how the milestone will be broken into sprints (M##_S01, M##_S02, etc.)

## Hierarchical Relationships
```
Milestone (M01)
├── Sprint 1 (M01_S01)
│   ├── Task 1 (M01_S01_T01)
│   ├── Task 2 (M01_S01_T02)
│   └── Task 3 (M01_S01_T03)
├── Sprint 2 (M01_S02)
│   ├── Task 1 (M01_S02_T01)
│   └── Task 2 (M01_S02_T02)
└── Sprint 3 (M01_S03)
    └── Task 1 (M01_S03_T01)
```

## Status Workflow
```
open → in_progress → done
  ↓         ↓         ↑
blocked ←---+         |
  ↓                   |
done ←-----------------+
```

## Important Notes for AI

1. **Sequential numbering** - Don't skip milestone numbers
2. **Update manifest** - Always update project/manifest.yml
3. **Sprint planning** - Define sprint breakdown within milestone
4. **Context loading** - Milestone files provide context for all commands
5. **Requirements focus** - Milestones should be requirement-driven, not task-driven

## Common Mistakes to Avoid
- Creating milestones without M## prefix
- Using hyphens instead of underscores
- Forgetting to update project manifest
- Creating milestones without clear requirements
- Making milestones too small (should contain multiple sprints)
- Making milestones too large (should be completable in 2-8 weeks)

## Integration with Commands
Milestone files are automatically loaded by commands:
- `/project:create_sprints -m M01` reads M01 milestone
- `/project:do_task -t M01_S01_T01` loads M01 context
- `/project:status` shows milestone progress

This folder is central to project organization - milestones drive everything else.