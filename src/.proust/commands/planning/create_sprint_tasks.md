# Command: create_sprint_tasks

**Command**: `/project:create_sprint_tasks`
**Category**: Project Planning
**Purpose**: Break sprint deliverables into specific, actionable implementation tasks

## Purpose

Analyze a sprint's goals and deliverables, then create detailed task breakdown with technical guidance, acceptance criteria, and clear implementation steps that enable focused development work.

## Context Loading

### Required Context
- `project/manifest.yml` - Current project state
- `project/sprints/M##_S##_*.md` - Target sprint requirements
- `project/milestones/M##_*.md` - Parent milestone context
- `core/architecture.yml` - Technical constraints and patterns
- `core/guardrails.yml` - Coding standards and quality gates
- `project/decisions/` - Relevant architectural decisions

### Generated Context
- Task breakdown and dependencies
- Implementation guidance and patterns
- Updated sprint and project state

## Parameters

### Required Arguments
- `-s SPRINT_ID` - Target sprint ID (e.g., M01_S01, M02_S03)

### Optional Flags
- `--interactive` / `-i` - Interactive task planning with AI guidance
- `--review` / `-r` - Show task breakdown before creation
- `--append` / `-a` - Add tasks to existing sprint tasks
- `--research` - Analyze codebase for implementation context
- `--force` - Overwrite existing task files

## Execution

### 1. Sprint Analysis & Validation
Load and validate target sprint:
- Verify sprint exists and is not completed
- Read sprint goals and deliverables
- Parse parent milestone context
- Check for existing tasks

**Output sprint state:**
```
Analyzing Sprint: M01_S01_BackendFoundation
Goal: Establish core backend infrastructure and APIs
Deliverables: 4 major components identified
Existing tasks: 2 completed, 1 in progress
Parent milestone: M01_AppWalletPass
```

### 2. Deliverable Decomposition
Break sprint deliverables into actionable tasks:
- **Granular analysis**: Decompose each deliverable into 4-8 hour tasks
- **Dependency mapping**: Identify task prerequisites and sequence
- **Technical research**: Analyze existing codebase for integration points
- **Implementation patterns**: Reference architectural decisions and standards

**Task categorization:**
- **Setup tasks**: Environment, dependencies, foundation
- **Core implementation**: Business logic and functionality
- **Integration tasks**: Component connectivity and data flow
- **Validation tasks**: Testing, documentation, review

### 3. Technical Guidance Integration
Enhance tasks with implementation context:
- **Architecture references**: Link to relevant architectural decisions
- **Code patterns**: Reference existing codebase patterns and conventions
- **Quality standards**: Include testing and documentation requirements
- **Integration points**: Identify interfaces and dependencies

### 4. Task File Generation
Create comprehensive task files with structured content:

**File naming**: `project/tasks/M##_S##_T##_TaskName.md`

**Task metadata:**
```yaml
---
id: "M01_S01_T01"
type: "task"
title: "Setup QR Generation Service"
status: "open"
parent_id: "M01_S01"
sprint_id: "M01_S01"
milestone_id: "M01"
complexity: "medium"
priority: "high"
created: "2024-12-27T15:30:00Z"
updated: "2024-12-27T15:30:00Z"
estimated_hours: 6
---
```

**Task content structure:**
- **Task overview**: Purpose and context within sprint
- **Technical requirements**: Specific implementation needs
- **Acceptance criteria**: Clear completion requirements
- **Implementation guidance**: Architecture references and patterns
- **Testing requirements**: Quality validation criteria
- **Documentation needs**: Required documentation updates

### 5. Implementation Context Research
Analyze codebase for task-specific guidance:
- **Pattern identification**: Find similar implementations
- **Interface analysis**: Identify integration points
- **Dependency mapping**: Locate required libraries and modules
- **Testing patterns**: Reference existing test structures

### 6. Task Dependency Validation
Verify task relationships and sequencing:
- **Sequential dependencies**: Task B requires Task A completion
- **Resource dependencies**: Shared components or services
- **Integration checkpoints**: Cross-task coordination points
- **Parallel opportunities**: Tasks that can run concurrently

### 7. Sprint & Manifest Updates
Update project state with new task structure:
- Update sprint file with task references
- Add tasks to project manifest
- Update sprint progress tracking
- Record task creation metadata

## Output

### Task Breakdown Summary
```
✅ Task breakdown created for M01_S01_BackendFoundation

Task Structure:
├── M01_S01_T01_SetupQRGeneration (6h)
│   ├── Install QR library dependencies
│   ├── Create QR service interface
│   ├── Implement basic QR generation
│   └── Add unit tests and documentation
├── M01_S01_T02_DatabaseSchema (4h)
│   ├── Design pass storage schema
│   ├── Create migration scripts
│   ├── Add model validations
│   └── Set up test fixtures
├── M01_S01_T03_AuthenticationAPI (8h)
│   ├── Implement JWT token system
│   ├── Create user registration endpoints
│   ├── Add authentication middleware
│   └── Write integration tests
└── M01_S01_T04_PassCreationEndpoint (6h)
    ├── Design pass creation API
    ├── Implement business logic
    ├── Add error handling
    └── Create API documentation

Dependencies:
- T03 requires T02 database setup
- T04 requires T01 + T03 completion

Total Estimated: 24 hours (~3 days)

Next Steps:
1. Review task breakdown: project/tasks/
2. Begin development: /project:do_task -t M01_S01_T01
3. Track progress: /project:self-assessment
```

## Success Criteria

- [ ] Sprint thoroughly analyzed for task breakdown
- [ ] Tasks properly sized (4-8 hour chunks)
- [ ] Clear acceptance criteria for each task
- [ ] Technical guidance and context provided
- [ ] Task dependencies identified and validated
- [ ] Sprint and manifest files updated
- [ ] Implementation patterns referenced

## Error Handling

### Sprint Issues
- **Sprint not found**: Validate sprint ID and suggest existing sprints
- **Sprint completed**: Warn against modifying completed sprint tasks
- **Missing deliverables**: Interactive mode to clarify sprint scope

### Task Planning Issues
- **Oversized tasks**: Break down complex tasks into smaller chunks
- **Unclear requirements**: Research mode to analyze implementation needs
- **Missing context**: Load additional architectural information

### Technical Issues
- **Codebase analysis failures**: Provide generic implementation guidance
- **Pattern recognition errors**: Fall back to manual task structuring
- **Dependency conflicts**: Highlight issues for manual resolution

## Examples

### Backend API Sprint
```bash
/project:create_sprint_tasks -s M01_S01
# Creates: Authentication, Database, Core APIs, Testing tasks
# Focus: Infrastructure → Business Logic → Integration
```

### Frontend Development Sprint
```bash
/project:create_sprint_tasks -s M01_S02 --research
# Creates: Component setup, State management, UI implementation, Testing
# Includes: Codebase analysis for existing patterns
```

### Integration Sprint
```bash
/project:create_sprint_tasks -s M01_S03 --interactive
# Creates: Service integration, Testing, Performance, Deployment
# Interactive: Clarify complex integration requirements
```

## Related Commands

- `/project:create_sprints_from_milestone` - Create the source sprint
- `/project:do_task` - Execute individual tasks
- `/project:create_general_task` - Create standalone tasks
- `/project:project_review` - Assess task planning effectiveness

## Notes

This command is the final step in transforming abstract requirements into concrete, actionable development work. The task quality directly impacts development velocity and code quality.

**Key principles:**
1. **Actionable specificity**: Tasks should be implementable in a single focused session
2. **Clear completion**: Acceptance criteria should be unambiguous
3. **Context awareness**: Tasks should reference relevant architectural decisions
4. **Quality integration**: Testing and documentation should be built into each task

Well-defined tasks enable focused development, reduce context switching, and ensure consistent progress toward sprint goals.