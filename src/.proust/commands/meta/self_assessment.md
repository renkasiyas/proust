# Command: self_assessment

**Command**: `/project:self_assessment`
**Category**: Meta Framework
**Purpose**: Validate Proust framework integrity and project health

## Purpose

Performs comprehensive validation of the Proust framework installation and project configuration to ensure everything is properly set up and functioning correctly.

## Context Loading

### Required Context
- `.proust/` directory structure and files
- `project/manifest.yml` project state
- All core configuration files (ethos.md, brand.yml, etc.)
- Recent command execution history (if available)

### Validation Scope
- Framework structure integrity
- Configuration file completeness and validity
- Project state consistency
- Command accessibility
- Template availability

## Execution

### 1. Framework Structure Validation
Check for required directory structure:
```
.proust/
├── core/                 # Configuration files
├── project/              # Project management
│   ├── manifest.yml
│   ├── milestones/
│   ├── sprints/
│   ├── tasks/
│   └── decisions/
├── commands/             # Available commands
└── workspace/            # Temporary files
```

### 2. Core Configuration Assessment
Validate each core file:
- **ethos.md**: Contains project philosophy and values
- **brand.yml**: Brand guidelines properly formatted
- **guardrails.yml**: AI constraints and coding standards
- **architecture.yml**: Technical architecture decisions
- **external_docs.yml**: External documentation links

Check for:
- File existence and readability
- YAML syntax validity
- Placeholder completion status
- Internal consistency

### 3. Project State Validation
Review `project/manifest.yml`:
- Project metadata completeness
- Current milestone/sprint consistency
- Technical stack alignment with actual project
- Quality gates configuration
- Progress tracking accuracy

### 4. Command System Check
Verify command availability:
- All command categories present (core, planning, workflow, analysis)
- Command files readable and properly formatted
- No missing dependencies or broken references
- Command syntax documentation current

### 5. Integration Health
Check framework integration:
- Git integration status (.gitignore rules)
- Package manager alignment
- Testing framework compatibility
- CI/CD pipeline awareness

## Output

### Health Report Structure
```markdown
# Proust Framework Health Report
Generated: YYYY-MM-DD HH:MM:SS

## Overall Status: [HEALTHY | ISSUES | CRITICAL]

## Framework Structure: [✅ | ⚠️ | ❌]
- Core directory: ✅
- Project directory: ✅
- Commands available: ✅
- Templates accessible: ✅

## Configuration Integrity: [✅ | ⚠️ | ❌]
- ethos.md: ✅ Complete
- brand.yml: ⚠️ Placeholder values remaining
- guardrails.yml: ✅ Configured
- architecture.yml: ✅ Documented
- external_docs.yml: ❌ Empty

## Project State: [✅ | ⚠️ | ❌]
- Manifest validity: ✅
- Current milestone: M01 (in progress)
- Sprint alignment: ✅
- Progress tracking: ✅

## Issues Found: [count]
### Critical Issues
- [None found]

### Warnings
- Brand guidelines contain placeholder values
- External documentation not configured

### Recommendations
- Complete brand.yml customization
- Add external documentation sources
- Consider creating first milestone if none exists

## Next Steps
- Run `/project:create_milestone` to begin project planning
- Update brand guidelines with project-specific values
- Configure external documentation sources
```

### Status Indicators
- **✅ HEALTHY**: All systems operational
- **⚠️ ISSUES**: Minor issues, framework functional
- **❌ CRITICAL**: Major problems, framework may not work properly

## Success Criteria

- [ ] Complete framework structure validated
- [ ] All core configuration files assessed
- [ ] Project state consistency verified
- [ ] Command system accessibility confirmed
- [ ] Clear health report generated with specific recommendations

## Error Handling

### Missing Framework
If `.proust/` directory missing:
- Recommend running `/project:init` to initialize
- Provide quick setup guidance
- Do not attempt automatic fixes

### Partial Installation
If some components missing:
- Identify specific missing pieces
- Provide targeted fix recommendations
- Prioritize critical vs. nice-to-have components

### Configuration Errors
If YAML syntax or structure errors:
- Report specific file and line issues
- Suggest validation tools or manual review
- Offer to show corrected examples

## Examples

### Healthy Project
```bash
/project:self-assessment
# Returns: ✅ HEALTHY - All systems operational
# Framework: 100% complete
# Configuration: 95% customized
# Ready for productive development
```

### New Installation
```bash
/project:self-assessment
# Returns: ⚠️ ISSUES - Framework installed, needs configuration
# Missing: Brand customization, external docs
# Recommendation: Complete setup with interactive config
```

### Broken Installation
```bash
/project:self-assessment
# Returns: ❌ CRITICAL - Major structural issues
# Missing: Core configuration files
# Recommendation: Reinstall with /project:init --force
```

## Related Commands

- `/project:init` - Initialize or repair framework
- `/project:validate` - Deep configuration validation
- `/project:status` - Quick project status check

## Notes

This command serves as the framework's health dashboard and diagnostic tool. It should be run:

1. **After initial setup** - Verify installation success
2. **Before major work sessions** - Ensure framework readiness
3. **When things feel broken** - Diagnose configuration issues
4. **During team onboarding** - Validate everyone's setup

The assessment should be fast (< 5 seconds) and provide actionable guidance for resolving any issues found. Focus on what users need to know to be productive, not exhaustive technical details.