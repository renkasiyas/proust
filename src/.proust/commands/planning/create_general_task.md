# Command: create_general_task

**Command**: `/project:create_general_task`
**Category**: Project Planning
**Purpose**: Create standalone tasks outside the milestone/sprint structure for maintenance, bugs, or one-off work

## Purpose

Create individual tasks that don't fit within the planned milestone/sprint workflow. These tasks handle reactive work like bug fixes, technical debt, maintenance, or urgent features that emerge during development.

## Context Loading

### Required Context
- `project/manifest.yml` - Current project state
- `project/tasks/` - Existing general tasks for duplicate detection
- `core/architecture.yml` - Technical constraints and patterns
- `core/guardrails.yml` - Coding standards and quality requirements
- Current codebase state for implementation context

### Generated Context
- Task integration with existing project structure
- Implementation guidance based on codebase patterns
- Updated project manifest with new task

## Parameters

### Required Arguments
- `task_title` - Description of the task to create

### Optional Flags
- `--interactive` / `-i` - Interactive task planning with AI guidance
- `--research` / `-r` - Analyze codebase for implementation context
- `--priority` / `-p` - Set task priority (high, medium, low)
- `--complexity` / `-c` - Indicate task complexity (low, medium, high)
- `--review` - Show task details before creation

## Execution

### 1. Task Analysis & ID Assignment
Analyze task request and assign unique identifier:
- Parse task title and extract key information
- Scan existing general tasks for highest T### ID
- Assign next sequential ID (T001, T002, etc.)
- Ensure no ID gaps in sequence

**Output task analysis:**
```
Creating General Task: "Add logging middleware"
Assigned ID: T003
Category: Infrastructure enhancement
Estimated complexity: Medium
```

### 2. Duplicate Detection
Search for similar existing tasks:
- **General tasks**: Check `project/tasks/T###_*.md` files
- **Sprint tasks**: Search `project/tasks/M##_S##_T##_*.md` files
- **Keyword matching**: Look for similar functionality or components
- **Scope analysis**: Determine if task overlaps with planned work

### 3. Project Context Integration
Analyze task within current project context:
- **Architecture alignment**: Ensure task fits project architecture
- **Quality standards**: Apply project coding and testing standards
- **Dependency analysis**: Identify connections to existing systems
- **Priority assessment**: Evaluate urgency relative to planned work

### 4. Codebase Research (if --research flag)
Analyze existing codebase for implementation guidance:
- **Pattern identification**: Find similar implementations
- **Integration points**: Identify affected modules and interfaces
- **Testing patterns**: Reference existing test structures
- **Documentation standards**: Follow established documentation patterns

### 5. Task File Creation
Generate comprehensive task file with structured content:

**File naming**: `project/tasks/T###_TaskName.md`

**Task metadata:**
```yaml
---
id: "T003"
type: "general_task"
title: "Add logging middleware"
status: "open"
priority: "medium"
complexity: "medium"
created: "2024-12-27T15:30:00Z"
updated: "2024-12-27T15:30:00Z"
estimated_hours: 4
tags: ["infrastructure", "logging", "middleware"]
---
```

**Task content structure:**
- **Task overview**: Purpose and business justification
- **Technical requirements**: Implementation specifications
- **Acceptance criteria**: Clear completion requirements
- **Implementation guidance**: Architecture references and patterns
- **Testing requirements**: Quality validation criteria
- **Integration considerations**: Impact on existing systems

### 6. Project Manifest Update
Update project state with new general task:
- Add task to general tasks tracking
- Update project metadata and statistics
- Record task creation timestamp
- Maintain task sequence integrity

## Output

### Task Creation Summary
```
✅ General task created: T003_AddLoggingMiddleware

Task Details:
- ID: T003
- Title: Add logging middleware
- Priority: Medium
- Complexity: Medium
- Estimated: 4 hours

Implementation Context:
- Architecture: Express.js middleware pattern
- Integration: Existing error handling system
- Testing: Unit tests + integration tests
- Documentation: API docs + README updates

Files Created:
- project/tasks/T003_AddLoggingMiddleware.md

Next Steps:
1. Review task details: project/tasks/T003_AddLoggingMiddleware.md
2. Begin implementation: /project:do_task -t T003
3. Track progress: /project:self-assessment
```

## Success Criteria

- [ ] Task clearly defined with specific requirements
- [ ] Unique ID assigned without conflicts
- [ ] No duplicate tasks identified
- [ ] Implementation guidance provided
- [ ] Acceptance criteria clearly defined
- [ ] Project manifest updated
- [ ] Integration considerations documented

## Error Handling

### Task Definition Issues
- **Vague description**: Interactive mode to clarify requirements
- **Duplicate detected**: Show existing task and offer to update or cancel
- **Scope too large**: Suggest breaking into multiple tasks

### Integration Problems
- **Architecture conflicts**: Highlight issues and suggest resolution
- **Priority conflicts**: Help prioritize against existing planned work
- **Resource constraints**: Consider team capacity and current workload

### System Issues
- **ID sequence errors**: Repair sequence and assign correct next ID
- **File system errors**: Handle permission and storage issues
- **Manifest conflicts**: Resolve project state inconsistencies

## Examples

### Bug Fix Task
```bash
/project:create_general_task "Fix user login timeout issue"
# Creates: T004_FixUserLoginTimeout
# Priority: High (bugs typically high priority)
# Focus: Problem investigation → Fix → Testing
```

### Technical Debt
```bash
/project:create_general_task "Refactor legacy API endpoints" --research
# Creates: T005_RefactorLegacyAPIs
# Includes: Codebase analysis for affected endpoints
# Focus: Code quality improvement
```

### Infrastructure Enhancement
```bash
/project:create_general_task "Add database connection pooling" --interactive
# Creates: T006_AddDatabasePooling
# Interactive: Clarify performance requirements and constraints
# Focus: Performance optimization
```

### Security Update
```bash
/project:create_general_task "Update authentication library" --priority high
# Creates: T007_UpdateAuthLibrary
# Priority: High for security updates
# Focus: Dependency update → Testing → Validation
```

## Related Commands

- `/project:create_sprint_tasks` - Create planned sprint tasks
- `/project:do_task` - Execute general or sprint tasks
- `/project:project_review` - Assess task prioritization
- `/project:analyze_codebase` - Research implementation context

## Notes

General tasks provide flexibility for reactive development needs while maintaining project structure and quality standards. They should be used for:

1. **Bug fixes**: Issues discovered during development
2. **Technical debt**: Code quality improvements
3. **Maintenance**: Dependency updates, refactoring
4. **Urgent features**: Business-critical additions outside planned scope

**Best practices:**
- **Clear scope**: Keep tasks focused and achievable
- **Priority awareness**: Consider impact on planned milestone work
- **Quality standards**: Apply same standards as sprint tasks
- **Documentation**: Maintain clear record of reactive work

General tasks ensure project agility while preserving the benefits of structured planning.