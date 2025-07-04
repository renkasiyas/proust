# Command: initialize

**Command**: `/project:initialize`
**Category**: Core Framework
**Purpose**: Set up Proust Framework in existing project with interactive guidance

## Purpose

Interactively initialize the Proust Framework for an existing project—detect project characteristics, guide configuration setup, create baseline structure, and establish the first milestone.

## Context Loading

### Required Context
- Current directory structure and files
- Git repository status (if present)
- Existing package management files (`package.json`, `pyproject.toml`, etc.)
- Project documentation (`README.md`, etc.)

### Generated Context
- Project metadata and characteristics
- Framework configuration preferences
- Initial project state in `manifest.yml`

## Execution

### 1. Project Discovery
Scan and analyze the existing project:
- Detect language/tooling from package files
- Identify project name from README or directory
- Determine project type (webapp, api, mobile, cli, library)
- Check if `.proust/` already exists
- Assess current development stage

**Output brief findings:**
```
Detected: TypeScript React project named "TaskFlow"
Package manager: npm
Framework: Next.js
Git repository: Yes (main branch)
```

### 2. Interactive Confirmation
Present findings to user for confirmation:
```
I found a React/TypeScript project named "TaskFlow".
Project type appears to be: webapp
Proceed with Proust setup? (yes/no)
```

If user wants to override, allow customization of:
- Project name and description
- Project type and technical stack
- Team size and methodology
- Development approach

### 3. Check Existing Configuration
If `.proust/` directory exists:
- List existing configuration files
- Show current project state
- Ask whether to:
  - **Extend**: Add missing components
  - **Refresh**: Update existing configuration
  - **Replace**: Start completely fresh
  - **Cancel**: Exit without changes

### 4. Core Configuration Setup
Create unified Proust structure:
```
.proust/
├── core/
│   ├── ethos.md              # Project philosophy (interactive)
│   ├── brand.yml             # Design guidelines (templated)
│   ├── guardrails.yml        # Coding standards (detected)
│   ├── architecture.yml      # Technical decisions (analyzed)
│   └── external_docs.yml     # Documentation links (empty)
├── project/
│   ├── manifest.yml          # Project state (generated)
│   ├── milestones/           # (empty, ready)
│   ├── sprints/              # (empty, ready)
│   ├── tasks/                # (empty, ready)
│   └── decisions/            # (empty, ready)
├── commands/                 # (framework commands)
└── workspace/                # (temporary directories)
```

### 5. Interactive Configuration
Guide user through key configuration:

**Project Ethos** (ethos.md):
- Ask for project philosophy and core values
- Identify decision-making criteria
- Define quality standards
- Establish team working principles

**Architecture Analysis** (architecture.yml):
- Analyze existing codebase patterns
- Document detected architecture type
- Identify key components and technologies
- Record technical constraints

**Coding Standards** (guardrails.yml):
- Detect existing linting/formatting tools
- Identify testing frameworks
- Set up AI behavioral constraints
- Configure quality gates

### 6. First Milestone Creation
Suggest and create initial milestone:
- Analyze project state to suggest milestone focus
- Interactively confirm milestone name and scope
- Create milestone directory structure
- Generate initial milestone metadata

**Example:**
```
Based on your codebase, I suggest starting with:
Milestone: "M01_Code_Quality_Foundation"
Focus: Establish testing, documentation, and CI/CD

Create this milestone? (yes/no/customize)
```

### 7. Project Manifest Generation
Create `project/manifest.yml` with:
- Project metadata (name, description, version, type)
- Current state (milestone, sprint, status)
- Technical information (detected stack)
- Team context (size, methodology, timezone)
- Quality gates and dependencies
- Initial goals and success criteria

### 8. Integration Setup
Configure project integration:
- Update `.gitignore` to exclude workspace/
- Add Proust documentation to README
- Set up package.json scripts if applicable
- Configure IDE/editor integration hints

## Output

### Success Summary
```
✅ Proust Framework initialized for "TaskFlow"

Created Structure:
- Core configuration (5 files)
- Project management directories
- First milestone: M01_Code_Quality_Foundation
- Framework commands available

Configuration Status:
- Project ethos: ✅ Defined
- Architecture: ✅ Documented
- Guardrails: ✅ Configured
- Brand guidelines: ⚠️ Template (customize later)

Next Steps:
1. Review: .proust/core/ethos.md
2. Create first tasks: /project:create_sprint_tasks -m M01
3. Begin development: /project:do_task
4. Health check: /project:self-assessment
```

## Success Criteria

- [ ] Unified directory structure created
- [ ] Core configuration files populated with project-specific content
- [ ] Project manifest reflects actual project characteristics
- [ ] First milestone created and configured
- [ ] Framework integration completed
- [ ] User understands next steps

## Error Handling

### Project Detection Failures
- **Unknown project type**: Use generic template with manual customization
- **No package files**: Prompt for manual project information
- **Multiple frameworks detected**: Ask user to choose primary

### Permission Issues
- **Read-only filesystem**: Clear error with resolution steps
- **Existing files conflict**: Offer backup/merge strategies
- **Git conflicts**: Guide through resolution process

### Configuration Errors
- **Invalid user input**: Re-prompt with validation
- **YAML syntax errors**: Auto-correct or show examples
- **Missing dependencies**: Suggest installation steps

## Examples

### Web Application
```bash
/project:initialize
# Detected: React + TypeScript + Next.js
# Creates: webapp-optimized configuration
# Milestone: "M01_User_Interface_Foundation"
# Focus: Component library and design system
```

### API Service
```bash
/project:initialize
# Detected: Python + FastAPI + PostgreSQL
# Creates: api-focused configuration
# Milestone: "M01_API_Core_Endpoints"
# Focus: Authentication and core business logic
```

### Mobile App
```bash
/project:initialize
# Detected: Flutter + Dart
# Creates: mobile-optimized configuration
# Milestone: "M01_App_Foundation"
# Focus: Navigation and core screens
```

## Related Commands

- `/project:init` - Quick setup without interaction
- `/project:self-assessment` - Validate setup
- `/project:create_milestone` - Add more milestones
- `/project:status` - Check current project state

## Notes

This command provides the complete guided onboarding experience for the Proust Framework. It should:

1. **Feel intelligent** - AI understands the project without excessive questions
2. **Be educational** - Show users what they're getting and why
3. **Stay flexible** - Allow customization for unique project needs
4. **Ensure success** - Verify everything works before completion

The interactive experience is critical for user adoption - it must demonstrate the framework's value while being efficient and helpful.