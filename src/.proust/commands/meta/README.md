# Meta Commands Guide

The meta commands provide framework introspection, validation, and AI optimization capabilities for the Proust Framework itself. These commands operate on the framework structure, templates, and AI behavior rather than project deliverables.

## Command Overview

| Command              | Purpose                                    | Use Case                                                 |
| -------------------- | ------------------------------------------ | -------------------------------------------------------- |
| `self_assessment`    | Validate framework health and integrity   | Regular framework health monitoring and troubleshooting   |
| `consistency_audit`  | Hunt contradictions across all documents  | Quality assurance and documentation integrity validation  |
| `reflect_on_solution`| Optimize AI responses iteratively        | Response quality improvement and reasoning refinement     |

## Meta Command Categories

### Framework Validation
Commands that assess the health and integrity of the Proust Framework itself:

- **`self_assessment`**: Validates core framework files, directory structure, and configuration integrity
- **`consistency_audit`**: Deep analysis hunting contradictions across all framework documents and templates

### AI Optimization
Commands that improve AI behavior and response quality:

- **`reflect_on_solution`**: Iterative self-review and optimization of AI responses until no issues remain

## Command Details

### 1. `/project:self_assessment` - Framework Health Validation

**Purpose**: Comprehensive validation of Proust Framework installation and health

**Key Features**:
- **Structure validation**: Verify all required directories and files exist
- **Configuration integrity**: Check core files (ethos, architecture, guardrails) for completeness
- **Template consistency**: Validate template placeholders and format consistency
- **Command availability**: Verify all command files are properly structured

**Usage Examples**:
```bash
# Complete framework health check
/project:self_assessment

# Focus on specific component
/project:self_assessment --component core

# Validation with auto-repair
/project:self_assessment --repair
```

**Output**: Framework health report with specific issues and recommendations

---

### 2. `/project:consistency_audit` - Deep Contradiction Analysis

**Purpose**: Hunt contradictions and inconsistencies across all project documents and templates

**Key Features**:
- **Contradiction detection**: Cross-compare rules, permissions, and statements
- **Authority conflicts**: Identify overlapping sources of truth
- **Broken references**: Find dead links, missing files, and invalid paths
- **Hierarchy alignment**: Validate principle cascading across framework layers

**Usage Examples**:
```bash
# Full framework consistency audit
/project:consistency_audit

# Focus on specific document types
/project:consistency_audit --scope "core,templates"

# Critical issues only
/project:consistency_audit --severity critical
```

**Output**: `workspace/assessments/$DATE_consistency_audit.md` with detailed findings

---

### 3. `/project:reflect_on_solution` - AI Response Optimization

**Purpose**: Iteratively self-review and optimize AI responses until no issues remain

**Key Features**:
- **Issue identification**: Detect mistakes, inconsistencies, and gaps in responses
- **Solution generation**: Provide multiple candidate solutions for each issue
- **Efficiency analysis**: Compare solutions by time, impact, and success probability
- **Iterative refinement**: Continue optimization until no further improvements possible

**Usage Examples**:
```bash
# Optimize previous response
/project:reflect_on_solution "${PREVIOUS_RESPONSE}" 1

# Multi-response optimization
/project:reflect_on_solution "${CONVERSATION_HISTORY}" 3

# Focus on specific aspects
/project:reflect_on_solution "${RESPONSE}" 1 --focus accuracy
```

**Output**: Refined responses or optimization confirmation with improvement rationale

## Integration Patterns

### Framework Maintenance Workflow
```
Framework Installation
    ↓ /project:self_assessment
Health Validation
    ↓ /project:consistency_audit
Integrity Verification
    ↓ Regular monitoring cycle
```

### Quality Assurance Workflow
```
Template Development
    ↓ /project:consistency_audit
Document Integrity Check
    ↓ /project:self_assessment
Framework Health Verification
```

### AI Optimization Workflow
```
Complex Response Generation
    ↓ /project:reflect_on_solution
Response Quality Improvement
    ↓ Iterative refinement cycle
```

## Meta vs Project Commands

### Meta Commands (Framework-focused):
- Operate on Proust Framework structure itself
- Validate templates, configurations, and AI behavior
- Ensure framework integrity and consistency
- Improve AI response quality and reasoning

### Project Commands (Deliverable-focused):
- **Core**: Project setup and initialization
- **Planning**: Requirements to implementation workflow
- **Analysis**: Project health and progress assessment
- **Workflow**: Development task execution

## Best Practices

### Regular Framework Health Monitoring
1. **Installation validation**: Run `/project:self_assessment` after framework updates
2. **Template integrity**: Use `/project:consistency_audit` before distributing templates
3. **Continuous validation**: Include meta commands in CI/CD pipelines

### Quality Assurance Integration
1. **Pre-release**: Full consistency audit before framework releases
2. **Documentation updates**: Self_assessment after major template changes
3. **Response quality**: Use reflection for complex or critical responses

### Troubleshooting Workflow
1. **Framework issues**: Start with `/project:self_assessment`
2. **Documentation conflicts**: Run `/project:consistency_audit`
3. **AI behavior**: Use `/project:reflect_on_solution` for response improvement

## File Structure Integration

Meta commands operate on the entire Proust Framework structure:

```
.proust/
├── commands/
│   ├── core/              # Meta commands validate structure
│   ├── planning/          # Meta commands check consistency
│   ├── analysis/          # Meta commands ensure integrity
│   ├── workflow/          # Meta commands verify completeness
│   └── meta/              # Self-referential validation
├── core/                  # Primary validation target
├── project/               # Template consistency checks
├── workspace/             # Assessment output location
└── templates/             # Template integrity validation
```

## Quick Reference

### Framework Health Check
```bash
# Complete framework validation
/project:self_assessment && /project:consistency_audit
```

### Template Quality Assurance
```bash
# Validate template integrity
/project:consistency_audit --scope templates
/project:self_assessment --component templates
```

### AI Response Optimization
```bash
# Improve response quality
/project:reflect_on_solution "${RESPONSE}" 1
```

### Troubleshooting Commands
```bash
# Diagnose framework issues
/project:self_assessment --verbose
/project:consistency_audit --critical-only
```

These meta commands ensure the Proust Framework maintains high quality, consistency, and optimal AI behavior while providing comprehensive introspection capabilities for framework maintenance and improvement.