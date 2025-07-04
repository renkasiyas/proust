# Command: context_management

**Command**: `/project:context_management`
**Category**: Core Framework
**Purpose**: Manage AI context and memory for optimal project understanding

## Purpose

Provide comprehensive context management for the Proust framework, ensuring AI maintains accurate and up-to-date understanding of project state, architecture, and development patterns.

## Sub-Commands

| Sub-Command | Description |
|-------------|-------------|
| `refresh` | Update AI context with recent project changes |
| `analyze` | Assess current context quality and completeness |
| `optimize` | Improve context efficiency and relevance |
| `export` | Generate comprehensive context documentation |

## Context Loading

### Required Context
- All core configuration files
- Project manifest and current state
- Recent development activity
- Command execution history
- Current codebase structure

### Context Scope
- Project architecture and patterns
- Development conventions and standards
- Team workflow and processes
- Technical decisions and rationale
- Current project phase and goals

## Execution

### Sub-Command: `refresh`

**Usage**: `/project:context_management refresh`

**Purpose**: Update AI context with recent changes

**Steps**:
1. **Scan for changes** since last context update
2. **Analyze impact** of changes on project understanding
3. **Update context files** with new information
4. **Validate consistency** across all context sources
5. **Generate summary** of context updates

**Output**:
```
Context refresh completed for TaskFlow project

Changes detected:
- New milestone M02 created
- Architecture updated (microservices → monolith)
- 3 new dependencies added
- Testing framework changed (Jest → Vitest)

Context updates:
✅ core/architecture.yml updated
✅ project/manifest.yml refreshed
✅ Dependencies synchronized
⚠️  Brand guidelines need attention

Next: Run /project:self-assessment to validate changes
```

### Sub-Command: `analyze`

**Usage**: `/project:context_management analyze`

**Purpose**: Assess context quality and identify gaps

**Steps**:
1. **Evaluate completeness** of each context source
2. **Check consistency** across configuration files
3. **Identify outdated** or conflicting information
4. **Assess relevance** to current project phase
5. **Calculate context health score**

**Output**:
```
Context Analysis Report - TaskFlow Project

Context Health Score: 85/100

Completeness Assessment:
✅ Project ethos: 100% (comprehensive)
✅ Architecture: 95% (minor gaps in deployment)
⚠️  Brand guidelines: 60% (placeholder values)
❌ External docs: 20% (mostly empty)

Consistency Check:
✅ Technical stack alignment
✅ Quality gates configuration
⚠️  Version numbers mismatch (manifest vs package.json)

Recommendations:
1. Complete brand guidelines customization
2. Add external documentation sources
3. Sync version numbers across files
4. Document recent architecture decisions
```

### Sub-Command: `optimize`

**Usage**: `/project:context_management optimize`

**Purpose**: Improve context efficiency and remove redundancy

**Steps**:
1. **Identify redundant** context information
2. **Consolidate overlapping** configuration
3. **Streamline context loading** patterns
4. **Remove outdated** references
5. **Optimize file organization**

**Output**:
```
Context optimization completed

Improvements made:
- Consolidated 3 duplicate architecture references
- Removed 5 outdated external documentation links
- Streamlined manifest.yml structure
- Organized workspace files by relevance

Performance gains:
- Context loading: 40% faster
- Memory usage: 25% reduction
- Information density: 15% improvement

Files modified:
- core/architecture.yml (consolidated)
- core/external_docs.yml (cleaned)
- project/manifest.yml (restructured)
```

### Sub-Command: `export`

**Usage**: `/project:context_management export [--format markdown|json|yaml]`

**Purpose**: Generate comprehensive context documentation

**Steps**:
1. **Aggregate all context** sources
2. **Generate unified documentation**
3. **Create visual representations** (if applicable)
4. **Export in requested format**
5. **Save to workspace** for review

**Output**:
```
Context export completed

Generated files:
- workspace/context/project_context_2024-12-27.md (15KB)
- workspace/context/architecture_diagram.svg
- workspace/context/context_summary.json

Export includes:
✅ Complete project overview
✅ Technical architecture details
✅ Team conventions and standards
✅ Development workflow patterns
✅ Current project state and goals

Use for: team onboarding, documentation, external review
```

## Command Usage Examples

### Daily Context Refresh
```bash
# Update context before starting development
/project:context_management refresh
```

### Weekly Context Health Check
```bash
# Assess context quality and identify maintenance needs
/project:context_management analyze
```

### Performance Optimization
```bash
# Improve context efficiency and organization
/project:context_management optimize
```

### Team Onboarding
```bash
# Generate comprehensive context documentation
/project:context_management export --format markdown
```

### Problem Diagnosis
```bash
# When AI seems to misunderstand project
/project:context_management analyze
/project:context_management refresh
```

## Success Criteria

- [ ] Context accurately reflects current project state
- [ ] All configuration files are consistent
- [ ] Context loading is efficient and comprehensive
- [ ] AI demonstrates updated project understanding
- [ ] Context health score > 90%

## Error Handling

### Context Corruption
- **Inconsistent files**: Identify conflicts and suggest resolutions
- **Missing context**: Regenerate from available sources
- **Outdated information**: Prompt for manual review and updates

### Performance Issues
- **Slow context loading**: Optimize file organization and content
- **Memory usage high**: Remove redundancy and consolidate information
- **Context bloat**: Archive old information to workspace

### Integration Problems
- **Command failures**: Validate context dependencies
- **AI confusion**: Simplify and clarify context sources
- **Workflow disruption**: Prioritize critical context elements

## Integration

### With Other Commands
- **Automatic refresh** after major project changes
- **Context validation** before complex command execution
- **Performance monitoring** during development workflows

### With Development Workflow
- **Pre-commit context checks** to maintain accuracy
- **Milestone context updates** to reflect project evolution
- **Sprint planning context** to guide AI understanding

## Related Commands

- `/project:self-assessment` - Validate framework integrity
- `/project:analyze_codebase` - Deep project analysis
- `/project:project_review` - High-level project assessment

## Notes

Context management is critical for maintaining AI effectiveness throughout project lifecycle. This command should be used:

1. **Regularly** - Daily or before major work sessions
2. **Reactively** - When AI seems confused or outdated
3. **Proactively** - Before team presentations or reviews
4. **Systematically** - As part of maintenance routines

Good context management ensures AI partners remain intelligent and helpful throughout the entire development process.