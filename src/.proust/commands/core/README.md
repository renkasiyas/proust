# Core Commands Guide

The core commands provide framework management and setup functionality. These commands establish and maintain the Proust framework foundation, ensuring proper configuration and AI context management.

## Command Overview

| Command                  | Purpose                   | Use Case                                    |
| ------------------------ | ------------------------- | ------------------------------------------- |
| `init`                   | Quick framework setup     | Add Proust to existing project (automated)  |
| `initialize`             | Interactive guided setup  | Add Proust to existing project (customized) |
| `initialize_new_project` | Complete project creation | Start new project from scratch              |
| `context_management`     | AI context & memory       | Maintain AI project understanding           |

## Command Details

### 1. `/project:init` - Quick Framework Setup

**Purpose**: Fast, automated framework initialization for existing projects

**When to use**: When you want to add Proust to an existing project with minimal interaction

**What it does**:
- Automatically detects project type (React, Python, etc.)
- Creates unified `.proust/` structure
- Populates core files with intelligent defaults
- Sets up project manifest based on detected characteristics
- Minimal user interaction required

**Example flow**:
```bash
/project:init
# Detected: React + TypeScript project named "TaskFlow"
# Creates: webapp-optimized configuration with frontend-focused guardrails
# Ready in ~30 seconds
```

**Output**: Complete framework setup with smart defaults, ready for immediate use

---

### 2. `/project:initialize` - Interactive Guided Setup

**Purpose**: Comprehensive, interactive framework setup with user guidance

**When to use**: When you want control over configuration and learning about framework features

**What it does**:
- Interactive project discovery and confirmation
- Guided configuration of ethos, architecture, and standards
- User can customize all aspects of setup
- Creates first milestone based on project analysis
- Educational experience showing framework capabilities

**Example flow**:
```bash
/project:initialize
# "I found a React/TypeScript project named 'TaskFlow'. Proceed? (yes/no)"
# Guides through ethos definition, coding standards setup
# Creates customized M01_Code_Quality_Foundation milestone
# Takes ~5-10 minutes with user input
```

**Output**: Fully customized framework configuration reflecting user preferences

---

### 3. `/project:initialize_new_project` - Complete Project Creation

**Purpose**: Create entirely new project from scratch with full ecosystem

**When to use**: Starting a completely new project and want everything set up perfectly

**What it does**:
- Technology stack selection and configuration
- Complete project structure creation (src/, tests/, docs/)
- Development environment setup (package.json, build tools, etc.)
- Git repository initialization
- First milestone creation for project foundation
- Production-ready setup out of the box

**Example flow**:
```bash
/project:initialize_new_project
# Guides through: TypeScript + Next.js + PostgreSQL selection
# Creates: Complete project structure + dev environment
# Includes: Testing setup, CI/CD templates, documentation
# Results: Ready-to-develop project in ~2-3 minutes
```

**Output**: Complete, production-ready project with development environment

---

### 4. `/project:context_management` - AI Context & Memory

**Purpose**: Manage AI understanding and context for optimal project intelligence

**When to use**:
- Daily before major work sessions
- When AI seems confused about project state
- After significant project changes
- For team onboarding documentation

**Sub-commands**:

#### `refresh` - Update AI Context
```bash
/project:context_management refresh
# Scans for recent changes, updates AI understanding
# Syncs manifest with actual project state
```

#### `analyze` - Context Quality Assessment
```bash
/project:context_management analyze
# Context Health Score: 85/100
# Identifies gaps, inconsistencies, outdated info
# Provides specific improvement recommendations
```

#### `optimize` - Performance Improvement
```bash
/project:context_management optimize
# Removes redundancy, consolidates information
# 40% faster context loading, 25% memory reduction
```

#### `export` - Generate Documentation
```bash
/project:context_management export --format markdown
# Creates comprehensive project documentation
# Perfect for team onboarding or external review
```

## How They Work Together

### Setup Progression

1. **New Project**: `initialize_new_project` → Complete ecosystem
2. **Existing Project**: `init` (quick) or `initialize` (guided) → Framework addition
3. **Validation**: Framework ready for use
4. **Maintenance**: `context_management` → Keep AI intelligent

### Daily Workflow Integration

```bash
# Start of work session
/project:context_management refresh
# Framework is ready for use

# During development
# (use planning, workflow, analysis commands)

# Maintenance
/project:context_management analyze  # weekly
/project:context_management optimize # monthly
```

### Command Relationship

- **init/initialize** → Setup foundation
- **initialize_new_project** → Complete project creation
- **Framework monitoring** → Use meta commands for health checks
- **context_management** → AI intelligence maintenance

All core commands focus on framework integrity and AI context management, providing the foundation for the planning, workflow, and analysis commands that handle day-to-day development tasks.

## Quick Reference

### First Time Setup
```bash
# Existing project (quick)
/project:init

# Existing project (guided)
/project:initialize

# New project from scratch
/project:initialize_new_project
```

### Health & Maintenance
```bash
# Check framework health
# Use meta commands for framework health
/project:self_assessment

# Update AI context
/project:context_management refresh

# Analyze context quality
/project:context_management analyze
```

### Troubleshooting
```bash
# When things feel broken
# Use meta commands for framework health
/project:self_assessment
/project:context_management analyze

# When AI seems confused
/project:context_management refresh
```

These core commands establish the foundation for productive AI-assisted development with the Proust framework.