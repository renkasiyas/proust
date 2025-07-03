# Framework Template Guide

This guide explains how to properly customize the framework templates for your project.

## Quick Start

1. **Copy the framework structure** to your project
2. **Replace placeholders** throughout template files
3. **Remove template instructions** when customization is complete
4. **Reference examples** in `src/.examples/` for guidance

## Template Customization Process

### Step 1: Understand Placeholder Syntax

All templates use this placeholder format:
```
{{PLACEHOLDER_NAME}}
```

**Examples:**
- `{{PROJECT_NAME}}` → Replace with your actual project name
- `{{YYYY-MM-DD}}` → Replace with current date in ISO format
- `{{HEX_PRIMARY}}` → Replace with your primary brand color

### Step 2: Systematic Replacement

Work through templates in this order:

1. **Project Identity Files**
   - `src/.proust/ethos.md` - Mission, vision, principles
   - `src/.proust/manifesto/manifesto.yml` - Technical architecture

2. **Configuration Files**
   - `src/.proust/universal_claude.md` - Claude Code settings
   - `src/.proust/guardrails.yml` - AI coding standards
   - `src/.context/brand.yml` - Design system

3. **Simone Project Structure**
   - `src/.simone/00_PROJECT_MANIFEST.md` - Project status
   - Templates in `src/.simone/99_TEMPLATES/`

### Step 3: Remove Template Instructions

After filling placeholders, delete these sections:
- Instruction blocks at top of files (usually commented)
- Lines starting with "# HOW TO USE THIS TEMPLATE"
- Any remaining `{{PLACEHOLDER}}` references
- Helper comments explaining what to fill in

### Step 4: Validate Configuration

Check that your customization:
- ✅ Has no remaining `{{PLACEHOLDER}}` text
- ✅ Uses consistent project naming throughout
- ✅ Follows the patterns shown in examples
- ✅ Has working file references and paths

## File-Specific Guidance

### ethos.md
**Purpose:** Define why your project exists and how team should work

**Key sections to customize:**
- Mission statement (1-2 sentences)
- Vision paragraph (future state)
- Core principles table (3-7 principles max)
- Product personality (tone, voice, metaphor)

### guardrails.yml
**Purpose:** AI coding standards and automated checks

**Key sections to customize:**
- `always` rules - what AI should always do
- `never` rules - what AI must never do
- `architecture_layers` - your project's folder structure
- `enforcement` - lint rules and pre-commit checks

### brand.yml
**Purpose:** Visual design system and brand guidelines

**Key sections to customize:**
- Color palette (primary, secondary, neutral scale)
- Typography (font families and sizing scale)
- Logo usage rules
- Voice and tone guidelines

### universal_claude.md
**Purpose:** Claude Code configuration for your project

**Key sections to customize:**
- Project identity table
- Testing strategy requirements
- Shell and tooling preferences
- Prohibited practices list

### manifesto.yml
**Purpose:** Technical architecture and development standards

**Key sections to customize:**
- Technology stack details
- Architecture layer definitions
- Deployment target configurations
- Monitoring and performance tools

## Common Mistakes to Avoid

### ❌ Leaving Template Instructions
```markdown
<!-- DELETE THIS BEFORE USING -->
Replace {{PROJECT_NAME}} with your project name
```

### ✅ Clean Final File
```markdown
# TaskFlow Project Architecture
```

### ❌ Inconsistent Naming
- Some files say "TaskFlow"
- Others say "My Project"
- Commands reference "task-flow"

### ✅ Consistent Throughout
- All references use same project name
- Consistent capitalization and spacing
- Matching technical identifiers

### ❌ Generic Placeholder Values
```yaml
primary: "#FF0000"  # Generic red
tagline: "A great app"  # Meaningless
```

### ✅ Meaningful Project Values
```yaml
primary: "#2563eb"  # TaskFlow brand blue
tagline: "Structured Project Management for Development Teams"
```

## Validation Checklist

Before considering templates complete:

- [ ] Search entire project for `{{` - should return zero results
- [ ] All file paths and references work correctly
- [ ] Project name is consistent across all files
- [ ] Dates use ISO 8601 format (YYYY-MM-DD)
- [ ] Colors use hex format (#RRGGBB)
- [ ] Technical stack info is accurate and current
- [ ] Testing requirements match your project needs
- [ ] All instruction comments removed

## Getting Help

**Reference materials:**
- `src/.examples/` - Filled example files
- Framework audit report - Identifies common issues
- Individual template files - Include specific guidance

**Common issues:**
- File path references not working → Check `src/` prefix usage
- Commands failing → Verify directory structure matches templates
- Inconsistent configuration → Use examples as reference patterns

---

_This guide helps ensure framework templates are properly customized for production use._