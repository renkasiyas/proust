# Claude Code Slash Commands for Proust Framework

This document maps Proust framework commands to Claude Code slash commands for easy access.

## Setup Commands

### /proust-install
**Purpose**: Install Proust framework in current project
**Usage**: `/proust-install`
**Equivalent**: `proust install`

### /proust-status
**Purpose**: Check framework status and validation
**Usage**: `/proust-status`
**Equivalent**: `proust status`

### /proust-validate
**Purpose**: Validate framework integrity
**Usage**: `/proust-validate`
**Equivalent**: `proust validate`

## Project Management Commands

### /simone-initialize
**Purpose**: Initialize new project with Proust framework
**File**: `src/.proust/commands/simone/initialize.md`
**Context**:
- `src/.proust/ethos.md`
- `src/.proust/universal_claude.md`
- `src/.proust/guardrails.yml`

### /simone-prime
**Purpose**: Prime project context for AI interaction
**File**: `src/.proust/commands/simone/prime.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.simone/01_PROJECT_DOCS/ARCHITECTURE.md`

### /simone-project-review
**Purpose**: Comprehensive project health check
**File**: `src/.proust/commands/simone/project_review.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/guardrails.yml`

## Development Commands

### /simone-analyze
**Purpose**: Analyze codebase architecture and patterns
**File**: `src/.proust/commands/simone/analyze_codebase.md`
**Context**:
- `src/.simone/01_PROJECT_DOCS/ARCHITECTURE.md`
- `src/.proust/guardrails.yml`

### /simone-code-review
**Purpose**: Review code against framework standards
**File**: `src/.proust/commands/simone/code_review.md`
**Context**:
- `src/.proust/guardrails.yml`
- `src/.proust/manifesto/manifesto.yml`

### /simone-test
**Purpose**: Execute comprehensive testing workflow
**File**: `src/.proust/commands/simone/test.md`
**Context**:
- `src/.proust/guardrails.yml`
- `src/.simone/00_PROJECT_MANIFEST.md`

### /simone-commit
**Purpose**: Commit changes with narrative context
**File**: `src/.proust/commands/simone/commit.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/brand.yml`

## Task Management Commands

### /simone-create-task
**Purpose**: Create new general task
**File**: `src/.proust/commands/simone/create_general_task.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.simone/99_TEMPLATES/task_template.md`

### /simone-do-task
**Purpose**: Execute specific task with full context
**File**: `src/.proust/commands/simone/do_task.md`
**Context**:
- Task file from `src/.simone/04_GENERAL_TASKS/`
- `src/.proust/guardrails.yml`

### /simone-create-sprint-tasks
**Purpose**: Create sprint tasks from milestone
**File**: `src/.proust/commands/simone/create_sprint_tasks.md`
**Context**:
- Milestone files from `src/.simone/02_REQUIREMENTS/`
- `src/.simone/99_TEMPLATES/task_template.md`

## Sprint Management Commands

### /simone-create-sprints
**Purpose**: Create sprints from milestone
**File**: `src/.proust/commands/simone/create_sprints_from_milestone.md`
**Context**:
- Milestone files from `src/.simone/02_REQUIREMENTS/`
- `src/.simone/99_TEMPLATES/sprint_meta_template.md`

## Quality Assurance Commands

### /simone-consistency-audit
**Purpose**: Audit framework consistency
**File**: `src/.proust/commands/simone/consistency_audit.md`
**Context**:
- All framework files
- `src/.proust/guardrails.yml`

### /simone-testing-review
**Purpose**: Review testing coverage and quality
**File**: `src/.proust/commands/simone/testing_review.md`
**Context**:
- `src/.proust/guardrails.yml`
- `src/.simone/00_PROJECT_MANIFEST.md`

## Creative Commands

### /simone-brainstorm
**Purpose**: Brainstorm solutions with context
**File**: `src/.proust/commands/simone/brainstorm.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/ethos.md`

### /simone-reflect
**Purpose**: Reflect on solution with full context
**File**: `src/.proust/commands/simone/reflect_on_solution.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/ethos.md`

## Integration Commands

### /simone-gh-issues
**Purpose**: Process GitHub issues with context
**File**: `src/.proust/commands/simone/gh_do_issues.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/brand.yml`

### /simone-context-management
**Purpose**: Manage and organize project context
**File**: `src/.proust/commands/simone/context_management.md`
**Context**:
- All `.proust/` and `.simone/` files

## Experimental Commands

### /simone-yolo
**Purpose**: Quick experimental changes
**File**: `src/.proust/commands/simone/yolo.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/guardrails.yml`

### /simone-discuss-review
**Purpose**: Discuss and review with team context
**File**: `src/.proust/commands/simone/discuss_review.md`
**Context**:
- `src/.simone/00_PROJECT_MANIFEST.md`
- `src/.proust/brand.yml`

## Command Implementation

Each slash command should:

1. **Load Context Files**: Read the specified context files before executing
2. **Execute Command Logic**: Follow the TODO steps in the command file
3. **Maintain Memory**: Update relevant state files
4. **Provide Feedback**: Report results and next steps

## Example Usage

```bash
# Check if framework is ready
/proust-status

# Initialize new project
/simone-initialize

# Prime context for development
/simone-prime

# Analyze current codebase
/simone-analyze

# Create new task
/simone-create-task

# Execute specific task
/simone-do-task T001_Setup_Database

# Commit with narrative
/simone-commit
```

## Integration with Claude Code

To integrate these commands with Claude Code:

1. **Add to Settings**: Include command definitions in Claude Code settings
2. **Map to Files**: Each command maps to a specific markdown file
3. **Load Context**: Automatically load required context files
4. **Execute Workflow**: Follow the command's TODO list

This creates a seamless interface between Claude's slash commands and Proust's structured workflows.

---

**Note**: This mapping enables direct access to Proust framework commands through Claude's native slash command interface, maintaining the framework's narrative coherence while providing convenient access patterns.