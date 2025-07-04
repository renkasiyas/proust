# Proust Framework Templates

This directory contains reference templates and examples to help users understand how to structure their Proust-enabled projects.

## Directory Structure

```
templates/
├── examples/               # Filled examples for reference
│   ├── webapp_project/     # Simple webapp example (existing)
│   └── fake_project/       # Enterprise example with "ACME Corp"
└── starters/               # Starting templates for new projects
    ├── minimal/            # Bare bones (existing)
    └── standard/           # Common project structure
```

## Usage

### For New Projects

**Minimal Starter**: Copy from `starters/minimal/` for a bare-bones setup:
```bash
cp -r templates/starters/minimal/* ./.proust/
```

**Standard Starter**: Copy from `starters/standard/` for a typical project:
```bash
cp -r templates/starters/standard/* ./.proust/
```

### For Learning

**Simple Example**: Review `examples/webapp_project/` for basic structure

**Enterprise Example**: Study `examples/fake_project/` to see how a complex enterprise project might be organized:
- Professional brand guidelines (`core/brand.yml`)
- Mature project ethos (`core/ethos.md`)
- Advanced project state (`project/manifest.yml`)

## Template Philosophy

### Examples
- **Complete**: Show realistic, filled-in content
- **Diverse**: Cover different project types and scales
- **Educational**: Demonstrate best practices and patterns

### Starters
- **Practical**: Ready to customize for real projects
- **Guided**: Include helpful comments and placeholder text
- **Scalable**: Structure that grows with project complexity

## Customization Guide

After copying a starter template:

1. **Core Configuration**: Update `core/` files with your project's identity
2. **Project State**: Modify `project/manifest.yml` with current information
3. **Remove Placeholders**: Replace all `{{PLACEHOLDER}}` values
4. **Delete Instructions**: Remove TODO comments and example text

## Template Maintenance

- Examples should demonstrate realistic, production-quality content
- Starters should balance guidance with simplicity
- All templates must follow the unified Proust architecture
- Templates are versioned with the framework and updated as needed

These templates help users quickly understand Proust patterns and get productive faster.