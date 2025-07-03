# Proust Framework

An AI memory and context management framework for software development, inspired by Marcel Proust's exploration of memory, time, and narrative coherence.

## Overview

Proust provides structured context management and project organization for AI-assisted development. Like its namesake's literary exploration of involuntary memory, Proust helps AI assistants maintain deep context awareness across projects, sessions, and time.

The framework combines two complementary systems:

- **`.proust/`** - Configuration and memory patterns for AI assistants 
- **`.simone/`** - Structured project management with narrative continuity

Together, they enable AI assistants to maintain rich contextual memory while ensuring project coherence and quality.

## Philosophy

Named after Marcel Proust, whose *In Search of Lost Time* revolutionized our understanding of memory and narrative, this framework applies similar principles to software development:

- **Memory as Foundation** - Context persists across sessions and projects
- **Narrative Coherence** - Every change fits into the larger story
- **Time and Reflection** - Past decisions inform present actions
- **Deep Context** - Surface details reveal deeper patterns

## Quick Start

### 1. Framework Setup

```bash
# Copy the framework to your project
cp -r src/.proust your-project/.proust
cp -r src/.simone your-project/.simone

# Or clone this repository
git clone https://github.com/renkasiyas/proust.git
```

### 2. Customize Configuration

```bash
# Use the template guide
cat TEMPLATE_GUIDE.md

# Reference examples
ls .examples/

# Key files to customize:
# - .proust/ethos.md (your project's memory and values)
# - .proust/guardrails.yml (AI behavioral patterns)
# - .proust/brand.yml (visual and verbal identity)
# - .proust/universal_claude.md (Claude configuration)
```

### 3. Initialize Project Memory

```bash
# With Claude Code
/project:simone:initialize

# This will:
# - Analyze your project's narrative
# - Create contextual documentation
# - Establish memory patterns
```

## Core Concepts

### Proust System (`.proust/`)

**Purpose:** AI memory and context management

**Key Files:**
- `ethos.md` - Project memory, values, and narrative identity
- `guardrails.yml` - AI behavioral patterns and constraints  
- `brand.yml` - Visual and verbal identity preservation
- `universal_claude.md` - Claude Code memory configuration
- `manifesto/manifesto.yml` - Technical memory and architecture decisions

### Simone System (`.simone/`)

**Purpose:** Structured project narrative with clear progression

**Structure:**
```
.simone/
├── 00_PROJECT_MANIFEST.md     # Current narrative state
├── 01_PROJECT_DOCS/           # Technical memory
├── 02_REQUIREMENTS/           # Story-based requirements
├── 03_SPRINTS/                # Narrative chapters
├── 04_GENERAL_TASKS/          # Character development
├── 05_ARCHITECTURAL_DECISIONS/ # Plot decisions
├── 10_STATE_OF_PROJECT/       # Narrative snapshots
└── 99_TEMPLATES/              # Story templates
```

## Workflow

### Daily Development with Memory

1. **Recall previous context**
   ```bash
   /project:simone:do_task
   ```

2. **Develop with memory**
   - Follow narrative acceptance criteria
   - Update memory logs continuously
   - Maintain story coherence

3. **Validate narrative consistency**
   ```bash
   /project:simone:code_review
   ```

4. **Commit to collective memory**
   ```bash
   /project:simone:commit T01_S01
   ```

### Memory Health

```bash
# Comprehensive memory review
/project:simone:project_review

# Framework memory consistency check
/project:simone:consistency_audit
```

## Key Features

### 🧠 AI Memory Management
- Persistent context across sessions
- Narrative coherence enforcement
- Automated memory validation
- Deep contextual understanding

### 📖 Project Narrative
- Story-driven milestone → chapter → scene structure
- Clear character arcs and plot development
- Automated narrative status management
- Rich context for every story element

### 🔍 Memory Quality Assurance
- Built-in narrative review process
- Memory validation steps
- Contextual compliance checking
- Zero-tolerance narrative gaps

### 📚 Context Visibility
- Real-time narrative status
- Historical memory snapshots
- Clear story progression guidance
- Comprehensive memory audit trails

## Memory Patterns

### Template Files
Located throughout the framework with `{{PLACEHOLDER}}` values:
- Replace placeholders with project-specific memory
- Remove template instructions when memory is established
- Reference `.examples/` for memory patterns

### Example Files
Located in `.examples/` showing established memory patterns:
- Complete memory configurations
- All placeholders filled with narrative context
- Clean, production-ready memory

### Documentation
- `TEMPLATE_GUIDE.md` - How to establish memory patterns
- `COMMAND_EXECUTION.md` - How memory commands work
- `STATUS_VALUES.md` - Narrative state definitions
- Framework memory audits and patterns

## Command Reference

### Memory Initialization
- `/project:simone:initialize` - Establish memory patterns for new project
- `/project:simone:initialize_new_project` - Complete memory reset

### Narrative Management
- `/project:simone:do_task [task_id]` - Execute story element with full context
- `/project:simone:create_general_task` - Create new story element
- `/project:simone:create_sprint_tasks` - Create narrative chapter

### Memory Quality
- `/project:simone:code_review [scope]` - Review changes against narrative
- `/project:simone:project_review` - Comprehensive memory health check
- `/project:simone:consistency_audit` - Memory integrity validation

### Memory Persistence
- `/project:simone:commit [context] [YOLO]` - Commit to collective memory
- Support for narrative commit messages
- Context-aware memory grouping

## Integration

### With Existing Projects

1. **Memory assessment phase**
   - Review current project narrative
   - Identify memory requirements
   - Plan framework memory adoption

2. **Gradual memory establishment**
   - Start with `.proust/` memory configuration
   - Add Simone narrative structure incrementally
   - Migrate existing memory into framework

3. **Full memory integration**
   - All development through memory framework
   - Team training on memory commands
   - Regular memory reviews

## Best Practices

### Establishing Memory
1. Start with example memory patterns as reference
2. Customize core memory files (ethos, guardrails, brand) first
3. Establish initial narrative and memory structure
4. Train team on memory command usage

### Team Memory Adoption
1. Begin with simple memory tasks to build familiarity
2. Use memory review process consistently
3. Regular memory reviews to identify pattern improvements
4. Document team-specific memory conventions

### Memory Maintenance
1. Regular memory consistency audits
2. Update memory patterns when framework evolves
3. Keep memory documentation synchronized
4. Version control memory changes

## Memory Philosophy in Practice

The Proust Framework transforms development from discrete tasks into continuous narrative:

- **Every commit** becomes a sentence in the project's story
- **Every feature** develops character and plot
- **Every decision** builds on accumulated memory
- **Every review** ensures narrative coherence

Like Proust's involuntary memory triggered by a madeleine, the framework helps AI assistants recall and apply relevant context automatically, creating deeper, more coherent software development experiences.

---

**Framework Version:** 2.1.0  
**Last Updated:** 2025-01-03  
**Inspired by:** Marcel Proust's *In Search of Lost Time*  
**Compatibility:** Claude Code, AI assistants with memory capabilities

*"The real voyage of discovery consists not in seeking new landscapes, but in having new eyes."* - Marcel Proust