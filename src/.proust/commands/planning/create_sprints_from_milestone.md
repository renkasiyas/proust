# Command: create_sprints_from_milestone

**Command**: `/project:create_sprints_from_milestone`
**Category**: Project Planning
**Purpose**: Transform milestone requirements into logical sprint structure with clear deliverables

## Purpose

Analyze an existing milestone and create a comprehensive sprint breakdown that organizes work into logical, independent deliverables while considering technical dependencies and project constraints.

## Context Loading

### Required Context
- `project/manifest.yml` - Current project state
- `project/milestones/M##_*.md` - Target milestone requirements
- `core/architecture.yml` - Technical constraints and patterns
- `core/ethos.md` - Project values and decision framework
- `project/decisions/` - Relevant architectural decisions

### Generated Context
- Sprint structure and dependencies
- Deliverable breakdown and timeline
- Updated project manifest state

## Parameters

### Required Arguments
- `-m MILESTONE_ID` - Target milestone ID (e.g., M01, M02)

### Optional Flags
- `--interactive` / `-i` - Interactive sprint planning with AI guidance
- `--review` / `-r` - Show sprint breakdown before creation
- `--append` / `-a` - Add sprints to existing milestone sprints
- `--force` - Overwrite existing sprint files

## Execution

### 1. Milestone Analysis
Load and analyze target milestone:
- Read milestone requirements and goals
- Identify key deliverables and features
- Parse success criteria and constraints
- Review any existing sprint structure

**Output current milestone state:**
```
Analyzing Milestone: M01_AppWalletPass
Goals: 3 primary objectives identified
Deliverables: 8 major features mapped
Existing sprints: 1 completed, 2 in progress
```

### 2. Sprint Boundary Analysis
Determine logical sprint boundaries:
- **Dependency mapping**: Identify technical prerequisites
- **Value delivery**: Group features for independent releases
- **Complexity assessment**: Balance sprint size and scope
- **Integration points**: Consider testing and deployment needs

**Sprint patterns detected:**
- **Foundation → Features → Integration**: Backend APIs → Frontend → Testing
- **Layer-by-layer**: Data → Business Logic → UI → Polish
- **Feature-complete**: End-to-end feature delivery per sprint

### 3. Sprint Structure Generation
Create sprint breakdown with intelligent naming:

**Sprint naming convention**: `M##_S##_SprintFocus`
- `M01_S01_BackendFoundation`
- `M01_S02_CoreFeatures`
- `M01_S03_IntegrationTesting`

**For each sprint:**
- **Primary goal**: Clear objective and focus
- **Key deliverables**: 3-5 specific outcomes
- **Dependencies**: Prerequisites from other sprints
- **Definition of done**: Completion criteria

### 4. Sprint File Creation
Generate comprehensive sprint files:

**File structure**: `project/sprints/M##_S##_SprintName.md`

**Content includes:**
```yaml
---
id: "M01_S01"
type: "sprint"
title: "Backend Foundation"
status: "planned"
parent_id: "M01"
milestone_id: "M01"
sprint_number: 1
goal: "Establish core backend infrastructure and APIs"
created: "2024-12-27T15:30:00Z"
updated: "2024-12-27T15:30:00Z"
priority: "high"
---
```

**Sprint content:**
- Sprint overview and context
- Primary goal and objectives
- Key deliverables breakdown
- Technical considerations and constraints
- Definition of done criteria
- Risk assessment and mitigation

### 5. Dependency Validation
Verify sprint dependencies and order:
- **Sequential dependencies**: Sprint B requires Sprint A completion
- **Parallel opportunities**: Sprints that can run concurrently
- **Integration points**: Cross-sprint coordination needs
- **Resource conflicts**: Team capacity and skill requirements

### 6. Project Manifest Update
Update `project/manifest.yml` with new sprint structure:
- Add new sprints to planned array
- Update current milestone sprint count
- Refresh project timeline and estimates
- Record sprint creation metadata

## Output

### Sprint Structure Summary
```
✅ Sprint breakdown created for M01_AppWalletPass

Sprint Structure:
├── M01_S01_BackendFoundation (2 weeks)
│   ├── API framework setup
│   ├── Database schema design
│   ├── Authentication system
│   └── Core QR generation logic
├── M01_S02_WalletIntegration (2 weeks)
│   ├── Apple Wallet pass creation
│   ├── Google Pay integration
│   ├── Pass distribution system
│   └── Mobile app connectivity
└── M01_S03_TestingDeployment (1 week)
    ├── End-to-end testing
    ├── Performance optimization
    ├── Security audit
    └── Production deployment

Dependencies:
- S02 requires S01 API completion
- S03 requires S01 + S02 integration

Next Steps:
1. Review sprint breakdown: project/sprints/
2. Create sprint tasks: /project:create_sprint_tasks -s M01_S01
3. Begin development: /project:do_task
```

## Success Criteria

- [ ] Milestone thoroughly analyzed for deliverables
- [ ] Sprint boundaries logically defined
- [ ] Sprint files created with comprehensive content
- [ ] Dependencies identified and validated
- [ ] Project manifest updated with sprint structure
- [ ] Clear next steps provided

## Error Handling

### Milestone Issues
- **Milestone not found**: Validate milestone ID and suggest existing milestones
- **Incomplete milestone**: Prompt to complete milestone requirements first
- **Already has sprints**: Offer append mode or sprint replacement options

### Sprint Planning Issues
- **Complex dependencies**: Break down into smaller, manageable sprints
- **Unclear requirements**: Interactive mode to clarify deliverables
- **Resource constraints**: Adjust sprint scope based on team capacity

### Integration Problems
- **Manifest conflicts**: Resolve project state inconsistencies
- **File system errors**: Handle permission and storage issues
- **Template errors**: Fall back to manual sprint creation

## Examples

### Web Application
```bash
/project:create_sprints_from_milestone -m M01
# Creates: M01_S01_BackendAPI, M01_S02_Frontend, M01_S03_Integration
# Focus: API → UI → Testing pattern
```

### Mobile App
```bash
/project:create_sprints_from_milestone -m M02 --interactive
# Creates: M02_S01_CoreScreens, M02_S02_DataSync, M02_S03_Publishing
# Focus: User experience → Backend → Distribution
```

### API Service
```bash
/project:create_sprints_from_milestone -m M03 --review
# Creates: M03_S01_Authentication, M03_S02_BusinessLogic, M03_S03_Performance
# Focus: Security → Features → Optimization
```

## Related Commands

- `/project:create_milestone` - Create the source milestone
- `/project:create_sprint_tasks` - Break sprints into specific tasks
- `/project:do_task` - Execute individual sprint tasks
- `/project:project_review` - Assess sprint planning effectiveness

## Notes

This command is critical for transforming high-level requirements into actionable development work. The sprint structure it creates directly impacts development velocity and project success.

**Key principles:**
1. **Independent value**: Each sprint should deliver standalone value
2. **Logical progression**: Sprint order should follow technical dependencies
3. **Balanced scope**: Sprints should be completable in 1-3 weeks
4. **Clear boundaries**: Sprint goals should be unambiguous and measurable

Success here sets up the entire development workflow for the milestone.