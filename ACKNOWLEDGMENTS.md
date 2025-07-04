# Acknowledgments

## Simone Framework

The Simone project management system integrated within the Proust Framework is based on the original work by **Helmi**.

- **Original Repository:** https://github.com/Helmi/claude-simone
- **Author:** Helmi (@Helmi on GitHub, @helmi on Anthropic Discord)
- **License:** MIT License
- **Copyright:** Copyright (c) 2024 Helmi

### About the Original Simone

Simone is a directory-based project management system specifically designed to work with Claude Code's strengths and limitations. It provides structure for breaking down software projects into manageable, context-aware tasks organized as:

- **Milestones** (M01, M02...) - Major project phases
- **Sprints** (S01, S02...) - Focused work periods within milestones
- **Tasks** (T01, T02...) - Atomic units of work

The core innovation of Simone is its approach to AI context management: starting fresh for each task while providing rich, relevant surrounding context.

### Integration in Proust Framework

We have integrated and extended Helmi's original Simone framework within the broader Proust Framework ecosystem. While maintaining the core concepts and workflow, we have:

- Integrated Simone with the Proust AI memory system
- Added new commands and documentation specific to our use case
- Extended the framework with `.proust/` configuration for broader AI context management
- Packaged it as part of the `proust-framework` Python package

### Attribution

This integration complies with the MIT License terms of the original work. We are grateful to Helmi for creating and open-sourcing this innovative approach to AI-assisted project management.

### Links

- Original Simone: https://github.com/Helmi/claude-simone
- Installation: `npx hello-simone`
- Proust Framework: https://github.com/renkasiyas/proust

## Other Acknowledgments

- Marcel Proust - for the philosophical inspiration behind AI memory and context management
- The Claude Code team at Anthropic - for creating the platform that makes this framework possible