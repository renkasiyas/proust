# Starter Templates

This directory contains ready-to-use templates for starting new Proust-enabled projects. Copy these as a foundation and customize for your specific needs.

## Available Starters

### minimal/
Bare-bones configuration for quick project setup:
- Essential files only (`core/ethos.md`)
- Minimal configuration
- Perfect for experimentation or simple projects
- Copy and customize placeholder content

### standard/
Complete starter template for typical projects:
- Full core/ configuration (ethos, brand guidelines, etc.)
- Comprehensive project/ setup (manifest, milestones, etc.)
- Realistic defaults and examples
- Suitable for most production projects

## Quick Start

### 1. Choose Your Starter
```bash
# For simple projects
cp -r src/.proust/templates/starters/minimal/* ./.proust/

# For full-featured projects
cp -r src/.proust/templates/starters/standard/* ./.proust/
```

### 2. Customize Configuration
- Update `core/ethos.md` with your project philosophy
- Modify `project/manifest.yml` with your project details
- Replace placeholders with actual values
- Add additional configuration files as needed

### 3. Initialize Project Structure
```bash
# Create initial milestone and sprint
mkdir -p ./.proust/project/{milestones,sprints,tasks,decisions}
```

## Customization Guide

### Core Configuration
- **ethos.md**: Define project values and working principles
- **brand.yml**: Brand guidelines and visual identity (standard template)
- **architecture.yml**: Technical architecture decisions (standard template)
- **guardrails.yml**: AI behavior constraints (standard template)

### Project Management
- **manifest.yml**: Central project state and metadata
- **milestones/**: Major project phases
- **sprints/**: Development iterations
- **tasks/**: Individual work items
- **decisions/**: Architectural decision records

### Best Practices
1. **Start simple**: Begin with minimal, add complexity as needed
2. **Be specific**: Replace generic placeholders with project-specific content
3. **Maintain consistency**: Keep configuration aligned with actual project state
4. **Document decisions**: Use decision records for important choices

## Template Evolution

Starter templates are:
- **Opinionated**: Reflect Proust best practices
- **Flexible**: Easy to adapt for different project types
- **Current**: Updated with framework improvements
- **Tested**: Validated with real project usage

Choose the starter that best matches your project's complexity and customize from there.