# Initialize Project

**Command**: `/project:init`
**Category**: Core Framework
**Purpose**: Set up Proust Framework in existing project

## Overview

Initializes the Proust Framework in the current project, creating the unified directory structure and setting up essential configuration files with intelligent defaults.

## Usage

```bash
# Basic initialization
/project:init

# Interactive setup with guided configuration
/project:init --interactive

# Initialize with specific project type
/project:init --type webapp

# Initialize from existing configuration
/project:init --from-template minimal
```

## Parameters

### Flags
- `--interactive` / `-i`: Step-by-step guided setup with questions
- `--type` / `-t`: Project type (webapp, api, mobile, cli, library)
- `--from-template`: Use predefined template (minimal, standard, comprehensive)
- `--force`: Overwrite existing Proust configuration

### Arguments
- `project_name`: Optional project name (defaults to directory name)

## Behavior

### Default Mode (Auto)
1. **Detect project characteristics**
   - Scan for `package.json`, `pyproject.toml`, `pom.xml`, etc.
   - Identify primary language and framework
   - Extract project name from existing files

2. **Create unified structure**
   - Generate `.proust/` directory with core/, project/, commands/, workspace/
   - Copy appropriate starter templates based on detected project type
   - Create initial manifest.yml with project metadata

3. **Initialize core files**
   - Generate ethos.md with project-appropriate values
   - Create brand.yml with sensible defaults
   - Set up guardrails.yml based on detected language/framework
   - Configure architecture.yml with identified patterns
   - Populate external_docs.yml with relevant documentation links

### Interactive Mode
1. **Project discovery**
   - Ask user to confirm detected project characteristics
   - Allow override of language, framework, and project type
   - Gather additional context (team size, methodology, goals)

2. **Configuration customization**
   - Guide through ethos definition
   - Customize brand colors and guidelines
   - Set up coding standards and guardrails
   - Define quality gates and requirements

3. **Template selection**
   - Choose from available project templates
   - Customize directory structure if needed
   - Select initial milestone and sprint structure

## Context Loading

### Required Context
- Current directory structure and files
- Git repository status (if present)
- Existing package management files
- Project documentation (README, etc.)

### Generated Context
- Project metadata and characteristics
- Framework configuration preferences
- Initial project state in manifest.yml

## Output

### Created Structure
```
.proust/
├── core/
│   ├── ethos.md              # Project philosophy
│   ├── brand.yml             # Design guidelines
│   ├── guardrails.yml        # Coding standards
│   ├── architecture.yml      # Technical decisions
│   └── external_docs.yml     # Documentation links
├── project/
│   ├── manifest.yml          # Project state
│   ├── milestones/           # (empty, ready for content)
│   ├── sprints/              # (empty, ready for content)
│   ├── tasks/                # (empty, ready for content)
│   └── decisions/            # (empty, ready for content)
├── commands/                 # (framework commands)
└── workspace/                # (temporary directories)
```

### Generated Files
- **manifest.yml**: Project metadata and current state
- **core/ files**: Customized for detected project type
- **README additions**: Instructions for using framework
- **.gitignore updates**: Exclude workspace/ from version control

## Success Criteria

- [ ] Unified directory structure created successfully
- [ ] Core files populated with project-specific content
- [ ] Project manifest reflects actual project characteristics
- [ ] No conflicts with existing project structure
- [ ] Framework validation passes (`/project:status`)

## Error Handling

### Common Issues
- **Existing .proust/ directory**: Prompt for --force or backup
- **Insufficient permissions**: Clear error message with resolution
- **Unknown project type**: Fall back to generic template with warning
- **Git conflicts**: Guidance on resolving version control issues

### Recovery
- **Partial initialization**: Clean up incomplete structure
- **Failed detection**: Manual specification options
- **Template errors**: Fall back to minimal configuration

## Examples

### Web Application
```bash
# Detected: React + TypeScript project
/project:init
# Creates webapp-optimized configuration with:
# - Frontend-focused guardrails
# - Component architecture patterns
# - Testing and build integration
```

### API Service
```bash
# Detected: Python FastAPI project
/project:init --interactive
# Guides through:
# - API design standards
# - Database architecture decisions
# - Deployment considerations
```

### Mobile App
```bash
# Flutter project with custom branding
/project:init --type mobile
# Sets up:
# - Mobile-specific workflows
# - Platform deployment patterns
# - UI/UX focused guardrails
```

## Related Commands

- `/project:status` - Validate framework setup
- `/project:validate` - Check configuration integrity
- `/project:create_milestone` - Begin project planning

## Notes

This command is the entry point to the Proust Framework experience. Success here determines whether users adopt the framework or abandon it, so the experience must be:

1. **Fast for obvious cases** - Don't ask questions AI can answer
2. **Helpful for complex cases** - Interactive mode for custom needs
3. **Safe for existing projects** - Never break what's already working
4. **Educational** - Show users what they're getting

The initialization process should feel magical - AI understands the project and sets up intelligent defaults, but humans retain full control over the final configuration.