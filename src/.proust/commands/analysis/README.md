# Analysis Commands Guide

The analysis commands provide comprehensive evaluation and assessment capabilities for projects using the Proust Framework. These commands focus on project health monitoring, quality assessment, and facilitating technical discussions to maintain high standards throughout development.

## Command Overview

| Command              | Purpose                                    | Use Case                                                 |
| -------------------- | ------------------------------------------ | -------------------------------------------------------- |
| `analyze_codebase`   | Generate comprehensive health reports      | Deployment readiness assessment and architecture compliance |
| `project_review`     | Comprehensive project state evaluation     | Regular project health monitoring and milestone assessment |
| `testing_review`     | Test suite alignment assessment            | Testing strategy validation and coverage analysis        |
| `discuss_review`     | Technical discussion facilitation          | Code review follow-up and decision documentation         |

## Analysis Workflow Patterns

### Health Assessment Workflow
```
Regular Development Cycle
    ↓ /project:analyze_codebase
Deployment Readiness Report
    ↓ /project:project_review
Comprehensive State Assessment
```

### Quality Assurance Workflow
```
Development Milestone
    ↓ /project:testing_review
Test Suite Assessment
    ↓ /project:discuss_review
Technical Discussion & Decisions
```

### Continuous Monitoring Workflow
```
Sprint Completion
    ↓ /project:project_review
Progress Evaluation
    ↓ /project:analyze_codebase
Technical Debt Assessment
```

## Command Details

### 1. `/project:analyze_codebase` - Comprehensive Health Analysis

**Purpose**: Generate single-session health reports for deployment readiness assessment

**Key Features**:
- **Architecture compliance**: Validate against `core/architecture.yml` patterns
- **Guardrail scanning**: Check code quality standards from `core/guardrails.yml`
- **Feature coverage**: Map implementation against planned milestones
- **Deployment readiness**: GO/NO-GO assessment with blocking issues

**Usage Examples**:
```bash
# Generate comprehensive health report
/project:analyze_codebase

# Compare against previous assessment
/project:analyze_codebase --compare "2025-06-20_assessment"

# Focus on specific milestone
/project:analyze_codebase --milestone M01
```

**Output**: `workspace/assessments/$DATE/` with comprehensive reports including:
- `overall_project_status.md`
- `feature_checklist.md`
- `identified_issues.md`
- `deployment_readiness.md`

---

### 2. `/project:project_review` - Comprehensive State Evaluation

**Purpose**: Conduct high-level review of entire project state with John Carmack-style analysis

**Key Features**:
- **Test infrastructure assessment**: Health scoring and blocking analysis
- **Documentation alignment**: Reality vs. documented architecture
- **Progress evaluation**: Sprint and milestone completion analysis
- **Carmack critique**: Blunt observations on simplicity and maintainability

**Usage Examples**:
```bash
# Full project review
/project:project_review

# Focus on specific milestone
/project:project_review M01

# Sprint-focused review
/project:project_review S02
```

**Output**: `workspace/assessments/YYYY-MM-DD-HH-MM-<judgment-slug>.md` with:
- Executive summary and sentiment
- Test infrastructure assessment
- Architecture and progress analysis
- Critical findings and recommendations

---

### 3. `/project:testing_review` - Test Strategy Alignment

**Purpose**: Assess test suite alignment with strategy and identify coverage gaps

**Key Features**:
- **Strategy alignment**: Compare tests against documented testing strategy
- **Coverage analysis**: Identify gaps in critical functionality
- **Test quality**: Flag over-engineered, fragile, or unnecessary tests
- **Actionable recommendations**: Specific modification suggestions

**Usage Examples**:
```bash
# Complete test suite review
/project:testing_review

# Strategy creation mode
/project:testing_review --create-strategy

# Focus on specific test category
/project:testing_review --category integration
```

**Output**: `workspace/assessments/YYYY-MM-DD-HH-MM-test-alignment.md` with:
- Alignment summary
- Tests requiring modification
- Coverage gap analysis
- Test health indicators

---

### 4. `/project:discuss_review` - Technical Discussion Facilitation

**Purpose**: Facilitate John Carmack-style technical discussions around review findings

**Key Features**:
- **Review-driven discussion**: Load findings from specific task reviews
- **One-question flow**: Focused, practical questioning
- **Decision documentation**: Log outcomes with timestamps
- **Action tracking**: Generate follow-up tasks from decisions

**Usage Examples**:
```bash
# Discuss specific task review
/project:discuss_review --task T07_S02

# General technical discussion
/project:discuss_review "Severity 8 log injection"

# Architecture decision discussion
/project:discuss_review --focus architecture
```

**Output**: Decision logs appended to task outputs or discussion logs with:
- Key discussion points
- Decisions made
- Next actions identified

## Integration Patterns

### With Core Commands
- **Framework setup**: Use after `/project:initialize` to establish baseline health
- **Context awareness**: Analysis results inform `/project:context_management`

### With Planning Commands
- **Milestone gates**: Use analysis commands as quality checkpoints
- **Implementation readiness**: `/project:analyze_codebase` before starting sprints
- **Progress tracking**: `/project:project_review` after sprint completion

### With Workflow Commands
- **Pre-deployment**: `/project:analyze_codebase` before production releases
- **Post-implementation**: `/project:project_review` after major features
- **Decision support**: `/project:discuss_review` for technical choices

### With Meta Commands
- **Framework health**: Use `/project:self_assessment` for Proust validation
- **Document integrity**: Use `/project:consistency_audit` for contradiction hunting
- **Response quality**: Use `/project:reflect_on_solution` for analysis optimization

## File Structure Integration

Analysis commands create and manage assessment files in the unified Proust structure:

```
.proust/
├── workspace/
│   └── assessments/          # All analysis outputs
│       ├── YYYY-MM-DD/       # Daily health reports
│       ├── project-reviews/  # Comprehensive reviews
│       └── test-alignments/  # Testing assessments
└── project/
    ├── manifest.yml          # Updated with analysis insights
    └── decisions/            # ADRs influenced by discussions
```

## Best Practices

### Regular Health Monitoring
1. **Weekly assessments**: Run `/project:analyze_codebase` before releases
2. **Milestone reviews**: Use `/project:project_review` at major checkpoints
3. **Trend analysis**: Compare assessments over time for improvement tracking

### Quality Integration
1. **Test alignment**: Regular `/project:testing_review` cycles
2. **Decision tracking**: Document all `/project:discuss_review` outcomes
3. **Architecture compliance**: Use analysis to validate design decisions

### Actionable Insights
1. **Issue prioritization**: Focus on high-severity findings first
2. **Task creation**: Convert findings into actionable work items
3. **Continuous improvement**: Use insights to update standards

## Quick Reference

### Pre-Release Assessment
```bash
# Full deployment readiness check
/project:analyze_codebase
/project:testing_review
/project:project_review
```

### Sprint Retrospective
```bash
# Sprint completion analysis
/project:project_review M01_S02
/project:discuss_review --sprint M01_S02
```

### Quality Deep Dive
```bash
# Comprehensive quality assessment
/project:testing_review
/project:analyze_codebase --focus quality
/project:discuss_review "quality findings"
```

### Technical Decision
```bash
# Architecture decision discussion
/project:discuss_review "proposed architecture change"
# Document decision in project/decisions/
```

These analysis commands provide focused project assessment capabilities that complement the workflow commands (for implementation), planning commands (for organization), and meta commands (for framework health), ensuring comprehensive project quality management throughout the development lifecycle.