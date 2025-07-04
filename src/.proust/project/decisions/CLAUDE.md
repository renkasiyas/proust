# CLAUDE.md - Decisions Folder Guide

## Overview
This folder contains Architectural Decision Records (ADRs) that document important technical and design decisions made during project development. ADRs provide context for future developers and maintain a history of why decisions were made.

## What Qualifies as an ADR

### Document These Decisions:
- **Technology choices** (frameworks, libraries, databases)
- **Architectural patterns** (MVC, microservices, event-driven)
- **Data modeling decisions** (schema design, relationships)
- **Security approaches** (authentication, authorization)
- **Performance strategies** (caching, optimization)
- **Integration patterns** (APIs, third-party services)
- **Development workflow** (testing, deployment, CI/CD)
- **Code organization** (folder structure, naming conventions)

### Don't Document These:
- **Trivial decisions** (variable names, minor styling)
- **Temporary workarounds** (unless they become permanent)
- **Individual bug fixes** (use task documentation instead)
- **Regular feature implementations** (document in milestones/sprints)

## Naming Convention
**CRITICAL**: ADR files MUST follow this exact pattern:
```
ADR###_Decision_Title.md
```

- `ADR` - Fixed prefix for Architectural Decision Record
- `###` - Three-digit sequential number (001, 002, etc.)
- `_` - Single underscore separators
- `Decision_Title` - Descriptive title using underscores for spaces

### Examples:
- ✅ `ADR001_Database_Choice.md`
- ✅ `ADR002_Authentication_Strategy.md`
- ✅ `ADR003_API_Design_Pattern.md`
- ❌ `ADR1_Database.md` (missing leading zeros)
- ❌ `ADR001-Database-Choice.md` (wrong separators)
- ❌ `Database_Choice_ADR.md` (wrong prefix position)

## ADR Structure
Each ADR file MUST contain:

### 1. YAML Frontmatter (REQUIRED)
```yaml
---
id: "ADR###"
type: "decision"
title: "Decision Title"
status: "proposed | accepted | deprecated | superseded"
created: "YYYY-MM-DDTHH:MM:SSZ"
updated: "YYYY-MM-DDTHH:MM:SSZ"
context: "What prompted this decision"
decision: "What was decided"
consequences: "What are the implications"
---
```

### 2. Standard ADR Sections

#### Status
- **Proposed**: Under consideration
- **Accepted**: Decision made and implemented
- **Deprecated**: No longer recommended but not forbidden
- **Superseded**: Replaced by a newer decision (reference the new ADR)

#### Context
- What is the issue that we're seeing that is motivating this decision?
- What factors are driving the need for a decision?
- What constraints exist that limit our options?

#### Decision
- What is the change that we're proposing or have agreed to implement?
- Why did we choose this option over alternatives?
- What are the key principles guiding this decision?

#### Consequences
- What becomes easier or more difficult as a result of this change?
- What are the positive outcomes we expect?
- What are the risks or negative implications?
- How does this affect other parts of the system?

## Creating New ADRs

### Step 1: Use Template
Copy from ` _templates/adr_template.md` and customize:
```bash
cp  _templates/adr_template.md decisions/ADR###_Your_Decision.md
```

### Step 2: Sequential Numbering
Use the next available ADR number (check existing files for highest number).

### Step 3: Complete All Sections
- Provide clear context for the decision
- Document the chosen solution
- Explain why alternatives were rejected
- Outline expected consequences

### Step 4: Link Related Decisions
- Reference related ADRs
- Note if this supersedes previous decisions
- Mention affected milestones or sprints

## ADR Lifecycle

### 1. Proposed
- Decision is under consideration
- Gathering input and evaluating options
- May have multiple competing proposals

### 2. Accepted
- Decision has been made
- Implementation can proceed
- Becomes part of project standards

### 3. Deprecated
- No longer recommended approach
- Existing implementations remain but discourage new use
- Often a transitional state

### 4. Superseded
- Replaced by newer decision
- Reference the superseding ADR
- Keep for historical context

## Decision Categories

### Technical Architecture
- Framework and library choices
- Database and storage decisions
- API design patterns
- Security implementations

### Process & Workflow
- Development methodologies
- Testing strategies
- Deployment procedures
- Code review processes

### Design & UX
- Design system choices
- User interface patterns
- Accessibility approaches
- Performance standards

## Important Notes for AI

1. **Context preservation** - ADRs maintain institutional memory
2. **Decision rationale** - Explain why, not just what
3. **Alternative consideration** - Document options that were rejected
4. **Impact assessment** - Consider consequences across the system
5. **Future reference** - Write for developers who join the project later

## Integration with Project
ADRs inform and guide:
- **Architecture decisions** in core/architecture.yml
- **Guardrails** for AI behavior
- **Code review** criteria
- **New feature** implementation approaches

## Common Mistakes to Avoid
- Documenting every minor decision (focus on significant ones)
- Not explaining the context that led to the decision
- Failing to consider and document consequences
- Not updating status when decisions change
- Writing for current team only (think future developers)
- Not linking related decisions

## Best Practices
- **Write promptly** - Document decisions when they're made, not months later
- **Be specific** - Provide concrete details, not vague statements
- **Include alternatives** - Show what options were considered
- **Update status** - Keep ADR status current as project evolves
- **Cross-reference** - Link to related milestones, sprints, and other ADRs

## Review and Maintenance
- **Regular review** - Periodically assess if decisions still make sense
- **Status updates** - Mark deprecated or superseded decisions
- **New ADRs** - Create new ADRs when revisiting old decisions
- **Documentation sync** - Ensure core architecture files reflect current ADRs

This folder preserves the reasoning behind important project decisions for current and future team members.