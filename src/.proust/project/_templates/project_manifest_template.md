---
project_name: {{PROJECT_NAME}}
current_milestone_id: {{CURRENT_MILESTONE_ID}}
highest_sprint_in_milestone: {{HIGHEST_SPRINT_IN_MILESTONE}}
current_sprint_id: {{CURRENT_SPRINT_ID}}
status: active
last_updated: YYYY-MM-DDTHH:MM:SSZ
---

# Project Manifest: {{PROJECT_NAME}}

This manifest serves as the central reference point for the project. It tracks the current focus and links to key documentation.

## 1. Project Vision & Overview

{{PROJECT_VISION}}

This project follows a milestone-based development approach.

## 2. Current Focus

- **Milestone:** {{CURRENT_MILESTONE_ID}} - {{CURRENT_MILESTONE_NAME}}
- **Sprint:** {{CURRENT_SPRINT_ID}} - {{CURRENT_SPRINT_NAME}}

## 3. Sprints in Current Milestone

{{SPRINT_LIST}}

## 4. Key Documentation

- [Project Architecture](../core/architecture.yml)
- [Current Milestone](./milestones/{{CURRENT_MILESTONE_ID}}_*.md)
- [All Tasks](./tasks/)

## 5. Quick Links

- **Current Sprint:** [{{CURRENT_SPRINT_ID}} Sprint](./sprints/{{CURRENT_SPRINT_ID}}_*.md)
- **Active Tasks:** [Sprint Tasks](./tasks/) filtered by {{CURRENT_SPRINT_ID}}
- **Decisions:** [Architecture Decisions](./decisions/)
