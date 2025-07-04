# Planning Commands Guide

The planning commands transform requirements into structured work by creating milestones, sprints, and tasks. These commands implement the core PRD → Milestone → Sprint → Task workflow.

## Command Overview

| Command                         | Purpose                           | Use Case                                             |
| ------------------------------- | --------------------------------- | ---------------------------------------------------- |
| `create_milestone`              | Create project milestone from PRD | Transform requirements into major project phases     |
| `create_sprints_from_milestone` | Break milestone into sprints      | Structure milestone work into development iterations |
| `create_sprint_tasks`           | Generate tasks from sprint        | Create specific implementation tasks for sprint work |
| `create_general_task`           | Create standalone task            | Add individual tasks outside sprint structure        |

## Workflow Progression

The planning commands follow a hierarchical workflow:

```
PRD Document
    ↓ /project:create_milestone -prd "PRD_Example.md"
Milestone (M01)
    ↓ /project:create_sprints_from_milestone -m M01
Sprints (M01_S01, M01_S02, M01_S03)
    ↓ /project:create_sprint_tasks -s M01_S01
Tasks (M01_S01_T01, M01_S01_T02, M01_S01_T03)
    ↓ /project:do_task -t M01_S01_T01
Implementation
```

## Command Details

### 1. `/project:create_milestone` - PRD to Milestone

**Purpose**: Analyze PRD documents and create comprehensive milestones with intelligent sprint suggestions

**Key Features**:
- **PRD Analysis**: Parse title, purpose, goals, and requirements
- **Auto-naming**: "PRD:  Wallet Pass" → `M01_AppWalletPass`
- **Sprint suggestions**: Analyze functional requirements for logical breakdown
- **Context integration**: Load core configuration for project-specific constraints

**Usage Examples**:
```bash
# Create milestone from PRD (recommended)
/project:create_milestone -prd "PRD_AppWalletPass.md"

# Interactive mode with AI conversation
/project:create_milestone -prd "brainstorm_notes.md" --interactive

# Review suggestions before creation
/project:create_milestone -prd "PRD_AppWalletPass.md" --review
```

**Output**:
- `project/milestones/M01_AppWalletPass.md`
- Updated `project/manifest.yml`
- Sprint breakdown suggestions

---

### 2. `/project:create_sprints_from_milestone` - Milestone to Sprints

**Purpose**: Transform milestone requirements into logical sprint structure with clear deliverables

**Key Features**:
- **Intelligent breakdown**: Analyze milestone for sprint boundaries
- **Dependency analysis**: Backend → Integration → Testing patterns
- **Sprint naming**: `M01_S01_BackendAPI`, `M01_S02_MobileIntegration`
- **Gap analysis**: Identify remaining work and dependencies

**Usage Examples**:
```bash
# Create sprints from milestone
/project:create_sprints_from_milestone -m M01

# Interactive sprint planning
/project:create_sprints_from_milestone -m M01 --interactive

# Review sprint breakdown before creation
/project:create_sprints_from_milestone -m M01 --review
```

**Output**:
- `project/sprints/M01_S01_BackendAPI.md`
- `project/sprints/M01_S02_MobileIntegration.md`
- `project/sprints/M01_S03_TestingDeployment.md`
- Updated `project/manifest.yml`

---

### 3. `/project:create_sprint_tasks` - Sprint to Tasks

**Purpose**: Break sprint deliverables into specific, actionable implementation tasks

**Key Features**:
- **Requirement decomposition**: Break sprint goals into specific tasks
- **Task naming**: `M01_S01_T01_SetupQRGeneration`
- **Acceptance criteria**: Define clear completion requirements
- **Technical guidance**: Reference architecture decisions and patterns

**Usage Examples**:
```bash
# Create tasks for sprint
/project:create_sprint_tasks -s M01_S01

# Append tasks to existing sprint
/project:create_sprint_tasks -s M01_S01 --append

# Review task breakdown before creation
/project:create_sprint_tasks -s M01_S01 --review
```

**Output**:
- `project/tasks/M01_S01_T01_SetupQRGeneration.md`
- `project/tasks/M01_S01_T02_ImplementWalletAPI.md`
- `project/tasks/M01_S01_T03_AddErrorHandling.md`
- Updated sprint and manifest files

---

### 4. `/project:create_general_task` - Standalone Tasks

**Purpose**: Create individual tasks outside the milestone/sprint structure for maintenance, bugs, or one-off work

**Key Features**:
- **Context awareness**: Integration with existing project architecture
- **Duplicate detection**: Avoid creating redundant tasks
- **Flexible naming**: `T001_AddLoggingMiddleware`
- **Standalone tracking**: Independent of milestone/sprint progress

**Usage Examples**:
```bash
# Create general task
/project:create_general_task "Add logging middleware"

# Interactive task creation
/project:create_general_task --interactive

# Research mode (analyze codebase first)
/project:create_general_task "Optimize database queries" --research
```

**Output**:
- `project/tasks/T001_AddLoggingMiddleware.md`
- Updated `project/manifest.yml`

## Integration Patterns

### With Core Commands
- **Framework setup**: Use after `/project:initialize` completes
- **Health validation**: `/project:self-assessment` validates structure
- **Context management**: `/project:context_management` keeps AI updated

### With Workflow Commands
- **Task execution**: `/project:do_task -t M01_S01_T01` implements created tasks
- **Code review**: `/project:code_review` validates task completion
- **Progress tracking**: Tasks update automatically on completion

### With Analysis Commands
- **Requirements analysis**: `/project:analyze_codebase` informs task creation
- **Project review**: `/project:project_review` assesses planning effectiveness

## File Structure Integration

Planning commands create and manage files in the unified Proust structure:

```
.proust/
├── project/
│   ├── manifest.yml          # Updated with milestone/sprint/task state
│   ├── milestones/
│   │   └── M01_ProjectName.md # Milestone definition and requirements
│   ├── sprints/
│   │   ├── M01_S01_SprintName.md # Sprint goals and deliverables
│   │   └── M01_S02_SprintName.md
│   └── tasks/
│       ├── M01_S01_T01_TaskName.md # Specific implementation tasks
│       ├── M01_S01_T02_TaskName.md
│       └── T001_GeneralTask.md     # Standalone tasks
```

## Best Practices

### Milestone Creation
1. **Use PRDs**: Always start with requirements documents when possible
2. **Review mode**: Use `--review` for important milestones
3. **Context alignment**: Ensure milestone fits project ethos and architecture

### Sprint Planning
1. **Logical boundaries**: Sprints should deliver independent value
2. **Dependency awareness**: Consider technical dependencies in sprint order
3. **Size management**: Target 1-2 week sprint durations

### Task Breakdown
1. **Actionable specificity**: Tasks should be implementable in 4-8 hours
2. **Clear criteria**: Define unambiguous completion requirements
3. **Context linking**: Reference relevant architecture decisions

### General Tasks
1. **Avoid duplication**: Check existing tasks before creating new ones
2. **Categorize properly**: Use sprints for planned work, general tasks for reactive work
3. **Integration awareness**: Consider impact on existing milestone/sprint work

## Quick Reference

### Complete Workflow
```bash
# From PRD to working code
/project:create_milestone -prd "requirements.md"    # M01_FeatureName
/project:create_sprints_from_milestone -m M01       # M01_S01, M01_S02, M01_S03
/project:create_sprint_tasks -s M01_S01             # M01_S01_T01, M01_S01_T02, M01_S01_T03
/project:do_task -t M01_S01_T01                     # Implementation
```

### Maintenance Tasks
```bash
# Add one-off tasks
/project:create_general_task "Fix login bug"
/project:create_general_task "Update dependencies"
```

### Planning Review
```bash
# Review current planning state
/project:self-assessment                            # Overall health
/project:context_management analyze                 # Planning consistency
```

These planning commands transform abstract requirements into concrete, actionable development work while maintaining project coherence and intelligent AI assistance throughout the process.