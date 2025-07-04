# Workflow Commands Guide

The workflow commands handle daily development operations including task execution, version control, testing, and code quality. These commands implement the practical workflows that transform planned work into completed features.

## Command Overview

| Command         | Purpose                                  | Use Case                                           |
| --------------- | ---------------------------------------- | -------------------------------------------------- |
| `prime`         | Quick context loading                   | Start of work session for AI context               |
| `do_task`       | End-to-end task execution              | Process tasks from selection to completion         |
| `test`          | Run test suite with auto-fixes         | Continuous testing during development              |
| `code_review`   | Deep code quality validation           | Ensure changes meet project standards              |
| `commit`        | Smart Git commit management            | Create logical, well-messaged commits              |
| `brainstorm`    | Interactive feature development        | Explore and specify new features                   |
| `gh_do_issues`  | GitHub issue implementation            | Contribute fixes with automated PR workflow        |
| `yolo`          | Autonomous task execution              | Batch process all open work with safety            |

## Workflow Patterns

### Daily Development Workflow
```
Start of Session
    ↓ /project:prime
Context Loaded
    ↓ /project:do_task
Task Implementation
    ↓ /project:test
Quality Validation
    ↓ /project:code_review
Change Approval
    ↓ /project:commit
Version Control
```

### Feature Development Workflow
```
New Feature Idea
    ↓ /project:brainstorm
Feature Specification
    ↓ /project:create_milestone -prd "spec.md"
Implementation Planning
    ↓ /project:do_task
Feature Development
```

### Quality Assurance Workflow
```
Code Changes
    ↓ /project:test
Infrastructure Fixes
    ↓ /project:code_review
Security & Architecture Validation
    ↓ /project:commit
Tracked Changes
```

## Command Details

### 1. `/project:prime` - Quick Context Loading

**Purpose**: Rapidly establish AI context with project overview

**Key Features**:
- **Instant context**: Load architecture, manifest, and ethos
- **Status summary**: Current milestone, sprint, and task count
- **Lightweight**: No file modifications, just context loading
- **Session starter**: Essential before task work in new sessions

**Usage Examples**:
```bash
# Start work session
/project:prime

# Output example:
# 🛠  Project: MyApp  |  Stack: React, Node.js, PostgreSQL
# 🚩 Milestone: M01  |  Active Sprint: M01_S02  |  Tasks Open: 5
# 📋 Principle: Ship working software frequently
```

---

### 2. `/project:do_task` - End-to-End Task Execution

**Purpose**: Complete workflow from task selection through implementation to completion

**Key Features**:
- **Smart selection**: Auto-select next open task or specify ID
- **Status tracking**: Updates task from open → in_progress → completed
- **Integrated review**: Automatic code review before completion
- **Output logging**: Timestamped progress documentation

**Usage Examples**:
```bash
# Work on next available task
/project:do_task

# Work on specific task
/project:do_task M01_S02_T03

# Work on general task
/project:do_task T042
```

**Workflow**:
1. Select or identify task
2. Validate dependencies and requirements
3. Set status to in_progress
4. Execute implementation
5. Run code review
6. Update status to completed
7. Rename file (T### → TX### for general tasks)

---

### 3. `/project:test` - Smart Test Execution

**Purpose**: Run tests with automatic infrastructure fixes

**Key Features**:
- **Framework detection**: Auto-detect test runner (pytest, jest, etc.)
- **Auto-fixes**: Create missing `__init__.py`, install dependencies
- **Smart reporting**: Pass rate, execution time, actionable issues
- **Non-invasive**: Only fixes infrastructure, not business logic

**Usage Examples**:
```bash
# Run test suite
/project:test

# Output example:
# Test Results:
# - Total: 156
# - Passed: 151 (96.8%)
# - Failed: 3
# - Skipped: 2
# - Time: 12.4s
#
# Issues Fixed:
# - Created missing __init__.py in tests/utils/
# - Installed missing dev dependency: pytest-mock
#
# Status: FAILING (3 tests need attention)
```

---

### 4. `/project:code_review` - Zero-Tolerance Quality Check

**Purpose**: Deep validation of code changes against project standards

**Key Features**:
- **Architecture compliance**: Validate against guardrails and patterns
- **Security scanning**: Check for vulnerabilities and bad practices
- **Severity ranking**: Issues rated 1-10 for prioritization
- **Persistent logging**: Reviews saved to task/sprint files

**Usage Examples**:
```bash
# Review latest changes
/project:code_review

# Review specific commit
/project:code_review abc123

# Review specific files
/project:code_review src/api/auth.js src/api/users.js
```

**Review Categories**:
- Architecture alignment
- Security vulnerabilities
- Code quality standards
- Test coverage
- Documentation completeness

---

### 5. `/project:commit` - Intelligent Version Control

**Purpose**: Create logical, well-structured commits with proper messages

**Key Features**:
- **Smart grouping**: Logical commit sets based on changes
- **Context awareness**: Links commits to tasks/sprints
- **YOLO mode**: Skip approval for autonomous workflows
- **Pre-commit compliance**: Handles hooks without bypassing

**Usage Examples**:
```bash
# Interactive commit workflow
/project:commit

# Commit with task context
/project:commit M01_S02_T03

# Autonomous mode (no approval)
/project:commit T042 YOLO

# Commit entire sprint
/project:commit M01_S02
```

---

### 6. `/project:brainstorm` - Interactive Feature Development

**Purpose**: Guide iterative Q&A to create complete feature specifications

**Key Features**:
- **Structured questioning**: One question at a time progression
- **Nine-section specs**: Problem → Goal → Requirements → Tech notes
- **Milestone ready**: Specs can convert directly to milestones
- **Context aware**: Integrates with project architecture

**Usage Examples**:
```bash
# Start brainstorming session
/project:brainstorm "Real-time notifications"

# Technical focus mode
/project:brainstorm "API versioning strategy" --technical

# Research mode
/project:brainstorm "Mobile offline sync" --research
```

**Output**: `workspace/brainstorm/spec-{$DATE}-{idea}.md`

---

### 7. `/project:gh_do_issues` - GitHub Issue Workflow

**Purpose**: Select, implement, and submit PRs for GitHub issues

**Key Features**:
- **Issue selection**: Prioritize "good first issue" labels
- **Branch management**: Proper naming and linking
- **PR automation**: Create PR with issue linking
- **Test integration**: Ensure all tests pass before PR

**Usage Examples**:
```bash
# Auto-select appropriate issue
/project:gh_do_issues

# Target specific issue
/project:gh_do_issues https://github.com/org/repo/issues/42
```

**Workflow**:
1. Select small, implementable issue
2. Comment implementation plan
3. Create feature branch
4. Implement with tests
5. Open PR with proper linking
6. Monitor CI and address feedback

---

### 8. `/project:yolo` - Autonomous Task Processing

**Purpose**: Execute all available tasks without user interaction

**Key Features**:
- **Safety guidelines**: Protects critical files and configs
- **Mode selection**: Sprint-specific or general processing
- **Auto-recovery**: Handles test failures and conflicts
- **Comprehensive reporting**: Full summary of all actions

**Usage Examples**:
```bash
# Process all available work
/project:yolo

# Focus on specific sprint
/project:yolo M01_S02

# General tasks only
/project:yolo --general-only
```

**Safety Rules**:
- No critical file modifications (.env, migrations, prod configs)
- Stop on database schema changes
- Stop on >5 file deletions
- Stop on persistent test failures

## Integration Patterns

### With Core Commands
- **Context setup**: Use `/project:prime` after `/project:initialize`
- **Memory management**: `/project:context_management` between sessions

### With Planning Commands
- **Task source**: Workflow commands execute tasks created by planning
- **Specification flow**: `/project:brainstorm` → `/project:create_milestone`
- **Progress tracking**: Task completion updates manifest automatically

### With Analysis Commands
- **Quality gates**: `/project:code_review` validates implementation
- **Health monitoring**: `/project:test` results feed into analysis
- **Decision support**: Review findings guide development choices

### With Meta Commands
- **Framework health**: Use `/project:self_assessment` if commands fail
- **Response quality**: `/project:reflect_on_solution` for complex work

## File Structure Integration

Workflow commands operate on and update files throughout the Proust structure:

```
.proust/
├── workspace/
│   ├── brainstorm/           # Feature specifications
│   │   └── spec-DATE-idea.md
│   └── scratch/              # Temporary workflow files
└── project/
    ├── manifest.yml          # Updated with task progress
    ├── tasks/                # Task status and logs
    │   ├── M01_S01_T01_*.md # Sprint tasks
    │   └── T###_*.md         # General tasks
    └── sprints/              # Sprint progress tracking
```

## Best Practices

### Task Execution
1. **Start with context**: Always `/project:prime` in new sessions
2. **Review before complete**: Let code_review validate changes
3. **Document progress**: Task logs help future understanding

### Quality Assurance
1. **Test frequently**: Run `/project:test` after significant changes
2. **Review severity**: Address high-severity issues immediately
3. **Commit logically**: Group related changes, clear messages

### Autonomous Workflows
1. **Monitor YOLO**: Review summary after autonomous execution
2. **Set boundaries**: Configure safety rules appropriately
3. **Incremental adoption**: Start with single sprints before full YOLO

### Collaboration
1. **PR workflow**: Use `/project:gh_do_issues` for contributions
2. **Clear commits**: Help team understand change purpose
3. **Test coverage**: Ensure changes don't break existing functionality

## Quick Reference

### Daily Development
```bash
# Morning startup
/project:prime
/project:do_task

# After implementation
/project:test
/project:code_review
/project:commit
```

### Feature Development
```bash
# New feature workflow
/project:brainstorm "feature idea"
/project:create_milestone -prd "spec-DATE.md"
/project:create_sprints_from_milestone -m M##
/project:do_task
```

### Quality Check
```bash
# Comprehensive validation
/project:test
/project:code_review
/project:project_review
```

### Autonomous Execution
```bash
# Let AI handle everything
/project:yolo M01_S02  # Sprint-specific
/project:yolo          # All available work
```

These workflow commands provide the practical implementation layer that transforms planned work into shipped features while maintaining quality, security, and project coherence throughout the development lifecycle.