# Simone Command Execution Model

This document explains how Simone framework commands are designed to work with Claude Code.

## Command Syntax

Simone commands follow this pattern:
```
/project:simone:command_name [arguments]
```

**Examples:**
- `/project:simone:initialize` - Set up new project
- `/project:simone:do_task T01_S01` - Execute specific task
- `/project:simone:commit YOLO` - Auto-commit changes

## Execution Environment

### Required Context
Commands expect this directory structure:
```
project_root/
├── src/
│   ├── .proust/            # Framework configuration
│   │   ├── universal_claude.md
│   │   ├── guardrails.yml
│   │   └── commands/simone/  # Command definitions
│   └── .simone/            # Project management structure
│       ├── 00_PROJECT_MANIFEST.md
│       ├── 01_PROJECT_DOCS/
│       ├── 02_REQUIREMENTS/
│       └── 03_SPRINTS/
```

### Variable Resolution
Commands use variables that are resolved as follows:

| Variable        | Source                          | Example                                          |
| --------------- | ------------------------------- | ------------------------------------------------ |
| `$DATE`         | Current UTC timestamp           | `2025-01-03T14:30:00Z`                           |
| `$ARGUMENTS`    | Text following command name     | `T01_S01` from `/project:simone:do_task T01_S01` |
| `$MILESTONE_ID` | Current milestone from manifest | `M01`                                            |
| `$SPRINT_ID`    | Current sprint from manifest    | `S01`                                            |

### File Loading Mechanism
Each command specifies "Context Files to Load":

1. Claude Code reads the command file (e.g., `do_task.md`)
2. Loads specified context files into working memory
3. Executes the command steps with full context available

## Command Types and Usage

### 1. Project Setup Commands

#### `/project:simone:initialize`
**Purpose:** Set up Simone framework for new project
**Prerequisites:** None (creates structure)
**Outputs:** Complete `.simone/` directory structure

```bash
# Interactive setup
/project:simone:initialize

# The command will:
# 1. Analyze current project structure
# 2. Ask for confirmation
# 3. Create framework directories
# 4. Generate initial documentation
```

### 2. Task Management Commands

#### `/project:simone:do_task [task_id]`
**Purpose:** Execute a specific task end-to-end
**Prerequisites:** Task file exists, dependencies complete
**Outputs:** Completed task with status updates

```bash
# Execute specific task
/project:simone:do_task T01_S01

# Execute next available task
/project:simone:do_task
```

#### `/project:simone:create_general_task`
**Purpose:** Create new task outside sprint structure
**Prerequisites:** Framework initialized
**Outputs:** New task file in `04_GENERAL_TASKS/`

### 3. Review and Quality Commands

#### `/project:simone:code_review [scope]`
**Purpose:** Review code changes against requirements
**Prerequisites:** Git repository with changes
**Outputs:** PASS/FAIL verdict with detailed findings

```bash
# Review latest commit
/project:simone:code_review

# Review specific files
/project:simone:code_review src/components/TaskCard.tsx

# Review commit range
/project:simone:code_review HEAD~3..HEAD
```

#### `/project:simone:project_review [scope]`
**Purpose:** Comprehensive project health assessment
**Prerequisites:** Framework structure exists
**Outputs:** Timestamped report in `10_STATE_OF_PROJECT/`

### 4. Version Control Commands

#### `/project:simone:commit [context] [YOLO]`
**Purpose:** Intelligent Git commit with context awareness
**Prerequisites:** Git repository with changes
**Outputs:** Logical commits with conventional messages

```bash
# Interactive commit (asks for approval)
/project:simone:commit T01_S01

# Auto-commit without approval
/project:simone:commit T01_S01 YOLO

# Commit all unrelated changes
/project:simone:commit
```

## Error Handling

### Common Failures and Recovery

**Command not found:**
```
Error: Command file not found at src/.proust/commands/simone/do_task.md
```
→ Verify framework installation and file structure

**Missing context files:**
```
Error: Cannot load src/.simone/00_PROJECT_MANIFEST.md
```
→ Run `/project:simone:initialize` first

**Invalid task state:**
```
Error: Task T01_S01 has status 'completed' - cannot execute
```
→ Check task status, may need new task

**Git repository issues:**
```
Error: Not a git repository
```
→ Initialize git: `git init`

### Rollback Procedures

**Failed task execution:**
1. Task status remains `in_progress`
2. Check Output Log for error details
3. Fix issues and re-run command
4. Or manually set status to `failed`

**Failed commits:**
1. Changes remain staged/unstaged
2. Fix pre-commit hook failures
3. Re-run commit command
4. Or manually commit with `git commit`

## Integration with Claude Code

### How Commands are Processed

1. **Parse command:** Extract command name and arguments
2. **Load command definition:** Read from `src/.proust/commands/simone/`
3. **Load context files:** As specified in command definition  
4. **Execute steps:** Follow command's TODO list sequentially
5. **Update state:** Modify project files as needed
6. **Report results:** Summary and next steps

### Variable Injection

Claude Code provides these variables to command execution:
- Current timestamp for `$DATE`
- Command arguments for `$ARGUMENTS`
- Project state from manifest parsing

### File Path Resolution

All paths in commands are relative to project root:
- `src/.proust/universal_claude.md` resolves to project working directory
- Commands can read/write any file in project
- Git operations work in project root context

## Best Practices

### Command Usage Patterns

**Start new project:**
```bash
/project:simone:initialize
# → Review generated structure
# → Customize templates
# → Create first milestone
```

**Daily development workflow:**
```bash
/project:simone:do_task
# → Work on assigned task
/project:simone:code_review
# → Verify quality standards
/project:simone:commit T01_S01
# → Commit with context
```

**Project health monitoring:**
```bash
/project:simone:project_review
# → Generate comprehensive report
# → Address any critical findings
```

### Command Chaining

Commands can suggest follow-up actions:
```
✅ Task T01_S01 completed successfully
⏭️ Next steps: /project:simone:commit T01_S01
```

This enables natural workflow progression.

## Troubleshooting

### Debug Command Execution

1. **Verify file structure** - Check all referenced paths exist
2. **Check command syntax** - Ensure proper argument format
3. **Review context files** - Validate referenced files are readable
4. **Test with simpler commands** - Start with `/project:simone:initialize`

### Performance Considerations

- Commands load multiple context files - may take 10-30 seconds
- Large projects with many tasks may slow command execution
- Git operations can be time-consuming with large repositories

### Compatibility

**Supported environments:**
- Claude Code with file system access
- Git repositories (required for commit/review commands)
- Any operating system with standard file operations

**Not supported:**
- Read-only file systems
- Projects without Git initialization
- Environments without command execution capabilities

---

_This execution model enables structured, AI-assisted project management through standardized command interfaces._