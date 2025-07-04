# Command: create_milestone

**Command**: `/project:create_milestone`
**Category**: Project Planning
**Purpose**: Create new project milestone from PRD or requirements

## Overview

Analyzes a Product Requirements Document (PRD) or requirements specification and creates a comprehensive milestone with intelligent sprint breakdown suggestions.

## Usage

```bash
# Create milestone from PRD (auto-naming and analysis)
/project:create_milestone -prd "PRD_AppWalletPass.md"

# Interactive milestone creation with discovery
/project:create_milestone -prd "brainstorm_notes.md" --interactive

# Review AI suggestions before creation
/project:create_milestone -prd "PRD_AppWalletPass.md" --review

# Manual milestone creation
/project:create_milestone "Core Authentication System" --manual
```

## Parameters

### Flags
- `-prd` / `--from-prd`: Source PRD file to analyze
- `--interactive` / `-i`: Discovery mode with AI conversation
- `--review` / `-r`: Show analysis and suggestions before creating
- `--manual` / `-m`: Skip AI analysis, manual definition
- `--force`: Overwrite existing milestone with same ID

### Arguments
- `milestone_name`: Manual milestone name (when not using -prd)

## Behavior

### Auto Mode (Default)
1. **PRD Analysis**
   ```
   Input: "PRD: AppWalletPass"
   Output: M01_AppWalletPass
   ```
   - Parse PRD title for milestone name
   - Analyze Purpose section for milestone description
   - Extract Goals for success criteria
   - Map User Stories to feature breakdown
   - Parse Functional Requirements for sprint suggestions
   - Review Technical Considerations for task complexity

2. **Milestone Creation**
   - Generate milestone ID (M01, M02, etc. based on existing)
   - Create comprehensive milestone file with:
     - Requirements analysis from PRD
     - Suggested sprint breakdown
     - Technical considerations
     - Success criteria and definition of done

3. **Sprint Suggestions**
   ```
   PRD Analysis → Sprint Breakdown:
   - Backend API requirements → M01_S01_BackendAPI
   - Mobile integration needs → M01_S02_MobileIntegration
   - QR/Branding requirements → M01_S03_QRBranding
   - Testing considerations → M01_S04_Testing
   ```

### Interactive Mode
1. **PRD Understanding**
   ```
   AI: "I see this PRD covers wallet pass functionality.
        Should this be one milestone or split into phases?"

   Human: "One milestone, but I'm not sure about sprint breakdown"

   AI: "The PRD mentions QR codes, mobile integration, and branding.
        Should backend API come first, or do you prefer parallel development?"

   Human: "Sequential: backend → mobile → branding → testing"

   AI: "Got it! I'll suggest 4 sprints in that order."
   ```

2. **Iterative Refinement**
   - AI asks clarifying questions about requirements
   - Human provides context and preferences
   - AI adapts suggestions based on conversation
   - Final milestone reflects collaborative understanding

### Review Mode
1. **Analysis Display**
   ```
   AI Analysis of "PRD: AppWalletPass":

   Detected Requirements:
   ✓ QR code generation with logo overlay
   ✓ Apple Wallet (PKPass) integration
   ✓ Google Wallet compliance
   ✓ Mobile app integration
   ✓ Brand consistency requirements

   Suggested Milestone: M01_AppWalletPass

   Proposed Sprint Breakdown:
   • M01_S01_BackendAPI (QR generation, pass creation)
   • M01_S02_MobileIntegration (PKPass, Google Wallet)
   • M01_S03_QRBranding (logo overlay, brand compliance)
   • M01_S04_Testing (device testing, QA validation)

   Continue with this structure? (y/n/modify)
   ```

2. **Human Review**
   - Show complete analysis and reasoning
   - Allow modification of suggestions
   - Confirm before creation
   - Option to iterate or start over

## Context Loading

### Required Context
- `core/ethos.md` - Project philosophy and decision framework
- `core/architecture.yml` - Technical patterns and constraints
- `project/manifest.yml` - Current project state and existing milestones
- Specified PRD file - Requirements to analyze

### Optional Context
- `core/brand.yml` - Design guidelines for UI/UX requirements
- `core/guardrails.yml` - Technical constraints and standards
- Existing milestone files - Pattern consistency

## PRD Analysis Engine

### Supported PRD Sections
1. **Purpose/Overview** → Milestone description and scope
2. **Goals/Objectives** → Success criteria and key results
3. **User Stories** → Feature breakdown and user value
4. **Functional Requirements** → Sprint organization logic
5. **Technical Considerations** → Implementation complexity
6. **Non-Functional Requirements** → Quality gates and constraints

### Sprint Logic Patterns
- **Backend → Frontend**: API-first development
- **Core → Extensions**: Essential features first
- **Infrastructure → Features**: Foundation-first approach
- **Design → Implementation**: UX-first development

### Complexity Assessment
- **Low**: Simple CRUD operations, UI updates
- **Medium**: Integration work, complex business logic
- **High**: New architecture, external dependencies

## Output

### Created Files
```
project/milestones/M01_AppWalletPass.md
```

### File Structure
```yaml
---
id: "M01"
type: "milestone"
title: "AppWalletPass"
status: "open"
created: "2024-12-27T16:00:00Z"
updated: "2024-12-27T16:00:00Z"
priority: "high"
---

## Milestone Overview
[AI-generated from PRD Purpose section]

## Requirements Analysis
[Structured breakdown of PRD requirements]

## Sprint Breakdown
[AI-suggested sprint organization]

## Success Criteria
[Extracted from PRD Goals and acceptance criteria]

## Technical Considerations
[Architecture and implementation notes]

## Definition of Done
[Completion criteria and quality gates]
```

### Project Manifest Update
```yaml
current_state:
  milestone: "M01"
  milestone_name: "AppWalletPass"

milestones:
  planned: ["M01"]
```

## Success Criteria

- [ ] Milestone ID assigned correctly (M01, M02, etc.)
- [ ] PRD requirements mapped to milestone scope
- [ ] Sprint breakdown suggestions are logical
- [ ] Success criteria are measurable
- [ ] Technical considerations address implementation
- [ ] Project manifest updated with new milestone

## Error Handling

### PRD Analysis Failures
- **Unrecognized format**: Request clarification or manual mode
- **Missing sections**: Use available information, flag gaps
- **Ambiguous requirements**: Trigger interactive mode
- **Complex dependencies**: Suggest milestone splitting

### File System Issues
- **PRD file not found**: Clear error with file path verification
- **Existing milestone conflict**: Offer merge or rename options
- **Permission errors**: Guidance on file access resolution

## Examples

### Comprehensive PRD
```bash
/project:create_milestone -prd "PRD_AppWalletPass.md"

# AI reads 10-section PRD, creates:
# M01_AppWalletPass with 4 logical sprints
# Comprehensive requirements analysis
# Clear success criteria and technical notes
```

### Minimal Requirements
```bash
/project:create_milestone -prd "feature_idea.md" --interactive

# AI: "This looks like a simple feature. One sprint or multiple?"
# Human: "Multiple - I want design exploration first"
# AI: "I'll suggest design → implementation → testing"
```

### Manual Creation
```bash
/project:create_milestone "User Authentication System" --manual

# Creates milestone with basic structure
# Human fills in requirements and breakdown
# AI can suggest sprints later with /project:create_sprints_from_milestone
```

## Related Commands

- `/project:create_sprints_from_milestone -m M01` - Generate sprints for milestone
- `/project:modify_milestone M01` - Edit milestone after creation
- `/project:delete_milestone M01` - Remove milestone safely


## Notes

This command implements the core PRD-to-Milestone transformation that enables the entire Proust workflow. The AI must:

1. **Parse intelligently** - Extract meaningful structure from varied PRD formats
2. **Suggest logically** - Sprint breakdown based on dependency analysis and patterns
3. **Enable collaboration** - Interactive mode for human-AI milestone refinement
4. **Maintain context** - Integration with existing project structure and constraints

The goal is transforming static requirements documents into executable project structures that guide development from conception to completion.