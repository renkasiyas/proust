# Command: initialize_new_project

**Command**: `/project:initialize_new_project`
**Category**: Core Framework
**Purpose**: Complete project initialization from scratch with full Proust ecosystem setup

## Purpose

Initialize a completely new project with the full Proust Framework ecosystem. This command scaffolds the entire project structure, seeds core documentation, and prepares the first milestone for immediate development.

## Context Loading

### Required Context
- Current directory (should be empty or minimal)
- Git repository status
- Available starter templates
- Framework best practices

### Generated Context
- Complete project configuration
- Initial architecture documentation
- First milestone structure
- Development environment setup

## Execution

### 1. Project Discovery & Confirmation
Detect and confirm project basics:
- Analyze any existing files (`package.json`, `README.md`, etc.)
- Identify project type and primary technology stack
- Determine project name from directory or user input
- Confirm project metadata with user

**Interactive Prompt:**
```
Creating new project in: /path/to/project
Detected name: "my-app"
Project type: webapp (React/TypeScript detected)
Is this correct? (yes/no/customize)
```

### 2. Technology Stack Selection
Guide technology stack configuration:
- **Language**: TypeScript, Python, Go, Rust, etc.
- **Framework**: React, Next.js, FastAPI, Express, etc.
- **Architecture**: SPA, SSR, Microservices, Monolith
- **Database**: PostgreSQL, MongoDB, SQLite, etc.
- **Deployment**: Vercel, AWS, Docker, Heroku

### 3. Scaffold Complete Project Structure
Create full project structure:

```
project-root/
├── .proust/
│   ├── core/
│   │   ├── ethos.md              # Project philosophy
│   │   ├── brand.yml             # Design guidelines
│   │   ├── guardrails.yml        # Coding standards
│   │   ├── architecture.yml      # Technical decisions
│   │   └── external_docs.yml     # Documentation links
│   ├── project/
│   │   ├── manifest.yml          # Project state
│   │   ├── milestones/           # Project phases
│   │   ├── sprints/              # Development iterations
│   │   ├── tasks/                # Individual work items
│   │   └── decisions/            # Architecture decisions
│   ├── commands/                 # Framework commands
│   └── workspace/                # Temporary files
├── src/                          # Source code (framework-specific)
├── tests/                        # Test files
├── docs/                         # Project documentation
├── .gitignore                    # Version control exclusions
├── README.md                     # Project overview
└── [framework-specific files]    # package.json, pyproject.toml, etc.
```

### 4. Generate Core Configuration
Create comprehensive core files:

**Project Ethos** (`core/ethos.md`):
- Interactive definition of project values
- Decision-making framework
- Quality standards
- Team working principles

**Architecture Documentation** (`core/architecture.yml`):
- Technology stack rationale
- System design patterns
- Component relationships
- Technical constraints

**Coding Standards** (`core/guardrails.yml`):
- Language-specific conventions
- Testing requirements
- Security considerations
- Performance guidelines

**Brand Guidelines** (`core/brand.yml`):
- Visual identity (if applicable)
- Design system foundations
- UI/UX principles
- Accessibility standards

### 5. Initialize Development Environment
Set up development tooling:
- Package manager configuration
- Development dependencies
- Build and test scripts
- Code formatting and linting
- Pre-commit hooks
- CI/CD pipeline templates

### 6. Create Foundation Milestone
Generate first milestone structure:
```
.proust/project/milestones/M01_Project_Foundation.md
```

**Milestone content:**
- Project setup and tooling
- Core architecture implementation
- Testing framework establishment
- Documentation foundation
- CI/CD pipeline setup

### 7. Generate Project Manifest
Create comprehensive `project/manifest.yml`:
- Project metadata and description
- Technical stack configuration
- Team context and methodology
- Quality gates and standards
- Initial milestone and sprint planning
- Success criteria and metrics

### 8. Initialize Version Control
Set up Git repository:
- Initialize repository if not exists
- Create `.gitignore` with framework exclusions
- Stage initial files
- Create first commit with project scaffold
- Set up branch protection rules (guidance)

### 9. Development Environment Validation
Verify setup completeness:
- All configuration files valid
- Development dependencies installed
- Build/test commands functional
- Linting and formatting operational
- Framework commands accessible

## Output

### Project Creation Summary
```
🎉 New project "TaskFlow" created successfully!

Project Structure:
├── ✅ Core configuration (5 files)
├── ✅ Development environment setup
├── ✅ Testing framework configured
├── ✅ Git repository initialized
└── ✅ First milestone: M01_Project_Foundation

Technology Stack:
- Language: TypeScript
- Framework: Next.js 14
- Database: PostgreSQL
- Deployment: Vercel
- Testing: Jest + Cypress

Next Steps:
1. Review project ethos: .proust/core/ethos.md
2. Customize brand guidelines: .proust/core/brand.yml
3. Create first sprint: /project:create_sprints_from_milestone -m M01
4. Begin development: /project:do_task
5. Validate setup: /project:self-assessment

Commands available:
- /project:create_milestone     # Plan project phases
- /project:create_sprint_tasks  # Break down work
- /project:analyze_codebase     # Analyze architecture
- /project:do_task             # Execute development tasks
```

## Success Criteria

- [ ] Complete project structure created
- [ ] All core configuration files populated
- [ ] Development environment functional
- [ ] First milestone defined and structured
- [ ] Version control initialized
- [ ] Framework commands operational
- [ ] Clear next steps provided

## Error Handling

### Directory Conflicts
- **Non-empty directory**: Confirm before proceeding or suggest different location
- **Permission issues**: Clear guidance on resolving access problems
- **Existing project detected**: Offer to use `/project:initialize` instead

### Technology Stack Issues
- **Unsupported framework**: Provide generic template with customization guidance
- **Dependency conflicts**: Suggest resolution strategies
- **Version incompatibilities**: Recommend compatible versions

### Configuration Errors
- **Invalid user input**: Re-prompt with validation and examples
- **Template processing failures**: Fall back to manual configuration
- **Missing prerequisites**: Guide through installation process

## Examples

### Full-Stack Web Application
```bash
/project:initialize_new_project
# Creates: React + TypeScript + Node.js + PostgreSQL
# Milestone: M01_MVP_Foundation
# Includes: Authentication, database setup, core UI components
```

### API Microservice
```bash
/project:initialize_new_project
# Creates: Python + FastAPI + PostgreSQL + Docker
# Milestone: M01_API_Core
# Includes: Authentication, database models, API documentation
```

### Mobile Application
```bash
/project:initialize_new_project
# Creates: Flutter + Dart + Firebase
# Milestone: M01_App_Foundation
# Includes: Navigation, state management, core screens
```

## Related Commands

- `/project:initialize` - Set up framework in existing project
- `/project:create_milestone` - Add additional milestones
- `/project:self-assessment` - Validate framework setup
- `/project:analyze_codebase` - Understand project structure

## Notes

This command provides the complete "project from scratch" experience. It should:

1. **Be opinionated but flexible** - Smart defaults with customization options
2. **Create production-ready foundation** - Not just scaffolding, but quality setup
3. **Educate while building** - Show users best practices through choices
4. **Ensure immediate productivity** - Everything should work after completion

The goal is to go from empty directory to productive development environment in minutes, with all the Proust Framework benefits immediately available.