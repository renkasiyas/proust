# Proust Framework Commands

This directory contains executable workflow commands organized by function. Commands are invoked using `/project:command_name` syntax in Claude Code.

## Directory Structure

```
commands/
├── core/                  # Framework management and setup
├── planning/             # Project planning and milestone workflows
├── workflow/             # Daily development workflows
├── analysis/             # Intelligence and analysis commands
└── README.md            # This documentation
```

## Command Categories

### core/ - Framework Management (5 commands)
Commands for framework setup and maintenance:

- **`init.md`** - Initialize Proust framework in existing project
- **`initialize.md`** - Set up new Proust-enabled project structure
- **`initialize_new_project.md`** - Complete new project initialization
- **`context_management.md`** - Manage AI context and memory
- **`self-assessment.md`** - Framework health and integrity checks

**Usage Example:**
```bash
/project:init                    # Initialize framework
/project:self-assessment         # Check framework status
```

### planning/ - Project Planning (4 commands)
Commands for milestone and sprint planning workflows:

- **`create_milestone.md`** - Create new project milestones with requirements
- **`create_sprints_from_milestone.md`** - Break milestones into sprint structure
- **`create_sprint_tasks.md`** - Generate tasks from sprint definitions
- **`create_general_task.md`** - Create standalone tasks outside sprints

**Usage Example:**
```bash
/project:create_milestone -n "User Authentication"
/project:create_sprints_from_milestone -m M01
/project:create_sprint_tasks -s M01_S01
```

### workflow/ - Daily Development (7 commands)
Commands for day-to-day development activities:

- **`do_task.md`** - Execute specific tasks with full context loading
- **`commit.md`** - Intelligent commit workflow with context awareness
- **`code_review.md`** - Structured code review with project context
- **`test.md`** - Testing workflows and test generation
- **`gh_do_issues.md`** - GitHub issue management and automation
- **`prime.md`** - Prepare development environment and context
- **`yolo.md`** - Quick development actions and rapid prototyping

**Usage Example:**
```bash
/project:do_task -t M01_S01_T01  # Execute specific task
/project:commit -m "feature"     # Smart commit with context
/project:code_review -f src/     # Review code changes
```

### analysis/ - Intelligence Commands (7 commands)
Commands for project analysis and insights:

- **`analyze_codebase.md`** - Comprehensive codebase analysis and architecture review
- **`brainstorm.md`** - Generate ideas and solutions for project challenges
- **`project_review.md`** - High-level project assessment and recommendations
- **`testing_review.md`** - Analyze testing coverage and strategy
- **`consistency_audit.md`** - Check project consistency and standards compliance
- **`reflect_on_solution.md`** - Reflect on implemented solutions and improvements
- **`discuss_review.md`** - Facilitate review discussions and decision-making

**Usage Example:**
```bash
/project:analyze_codebase        # Full codebase analysis
/project:project_review          # Project health assessment
/project:consistency_audit       # Check standards compliance
```

## Command Execution

### Invocation Syntax
Commands use the unified `/project:command_name` syntax:
```bash
/project:command_name [arguments]
```

### Context Loading
All commands automatically load relevant context:
- Project manifest and current state
- Milestone and sprint information
- Architecture and technical configuration
- Team conventions and standards

### Argument Patterns
Common argument patterns across commands:
- `-t TASK_ID` - Target specific task (e.g., M01_S01_T01)
- `-s SPRINT_ID` - Target specific sprint (e.g., M01_S01)
- `-m MILESTONE_ID` - Target specific milestone (e.g., M01)
- `-f PATH` - Target specific file or directory
- `-n NAME` - Specify name for new entities

## Command Development

### Command Structure
Each command file follows this structure:
```markdown
# Command: command_name

## Purpose
Brief description of what this command accomplishes.

## Context Loading
List of context files and data sources the command requires.

## Execution
Detailed step-by-step execution instructions for AI.

## Output
Description of expected outputs and side effects.

## Examples
Usage examples with different argument combinations.
```

### Best Practices
1. **Context-Aware**: All commands load relevant project context
2. **Idempotent**: Commands can be safely re-run
3. **Atomic**: Each command accomplishes one clear objective
4. **Discoverable**: Clear naming and documentation
5. **Consistent**: Follow established patterns and conventions

## Integration

### With Project Structure
Commands integrate with the unified Proust architecture:
- Read from `core/` configuration
- Update `project/` state and files
- Generate output in `workspace/` when appropriate
- Reference `templates/` for examples

### With Development Workflow
Commands support the complete development lifecycle:
1. **Planning**: milestone → sprint → task creation
2. **Development**: task execution → code review → commit
3. **Analysis**: codebase review → project assessment → improvements

This command system provides powerful, context-aware workflows for AI-assisted development while maintaining project consistency and quality standards.