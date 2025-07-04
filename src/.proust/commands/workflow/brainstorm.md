# Command: brainstorm

**Command**: `/project:brainstorm`
**Category**: Analysis
**Purpose**: Guide iterative Q&A session to produce complete, developer-ready product or feature specifications

## Purpose

Guide the user through an **iterative Q&A session** to produce a complete, step-by-step product or feature specification that is ready for developer hand-off.

## Context Loading

### Required Context
- `core/ethos.md` - Project principles and values for alignment
- `core/guardrails.yml` - Technical constraints and quality standards
- `core/architecture.yml` - Existing technical decisions and patterns
- `core/external_docs.yml` - Reference materials and best practices

### Generated Context
- Complete feature specification ready for implementation
- Technical feasibility assessment within project constraints
- Integration guidance with existing architecture

## Parameters

### Required Arguments
- `$IDEA` - One-sentence idea seed provided by the user (e.g., "Zen-mode portfolio screen")

### Optional Flags
- `--interactive` / `-i` - Enhanced interactive mode with deeper questioning
- `--technical` / `-t` - Focus on technical implementation details
- `--research` / `-r` - Include competitive analysis and market research questions

## Session Protocol

1. **Ask exactly _one_ question at a time.**
   - Question #1: _"What core problem or user pain point does this idea aim to solve?"_
   - Subsequent questions must build logically on previous answers (requirements → flows → edge cases → tech notes, etc.).

2. **Record each Q & A pair** in an in-memory draft spec as the conversation progresses.

3. Continue until user says **"done"** or the agent detects that the spec is complete (all essential sections filled).

## Spec Template

Auto-populate this structure during the session:

```markdown
# Spec: $IDEA
**Date:** $DATE

## 1. Problem / Pain Point
…

## 2. Goal
…

## 3. Users & Personas
…

## 4. Functional Requirements
…

## 5. Non-Functional Requirements
…

## 6. User Flows & Edge Cases
…

## 7. Acceptance Criteria
…

## 8. Open Questions & Risks
…

## 9. Tech Notes & Dependencies
…
```

## Execution

### After Final "Done"

1. **Render the completed spec** into `workspace/brainstorm/spec-{$DATE}-{one-liner idea}.md`.

2. Ask: **"Would you like to convert this into a milestone and sprints?"**
   - If **yes** →
     a. Create PRD from specification
     b. Run `/project:create_milestone -prd "spec-{$DATE}-{idea}.md"`
     c. Optionally run `/project:create_sprints_from_milestone`
   - If **no** → End session with spec saved for future reference.

## Outputs

| File                                                    | Purpose                       |
| ------------------------------------------------------- | ----------------------------- |
| `workspace/brainstorm/spec-{$DATE}-{one-liner idea}.md` | Finalized specification draft |

## Validation

- [ ] All nine sections of the specification are filled with detailed content
- [ ] Technical feasibility assessed against project architecture
- [ ] User flows and edge cases thoroughly documented
- [ ] Acceptance criteria clearly defined and testable
- [ ] User explicitly approves completion
- [ ] Spec saved at `workspace/brainstorm/spec-{$DATE}-{idea}.md`

## Related Commands

- `/project:create_milestone` - Convert specification into project milestone
- `/project:create_sprints_from_milestone` - Break milestone into development sprints
- `/project:create_general_task` - Create standalone tasks from specification
- `/project:analyze_codebase` - Assess implementation feasibility

## Notes

- Use for new feature exploration and requirement gathering
- Integrate with existing project architecture and constraints
- Specifications can be converted directly into actionable milestones