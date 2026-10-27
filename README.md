# AI Team Framework

Karpathy-inspired coding principles + OpenCode agent templates.

## Structure

```
ai-team/
├── principles.md           # Core principles, caveman talk, model selection
└── opencode/
    └── agents/             # Base agent templates
        ├── coordinator.md
        ├── developer.md
        ├── qa.md
        └── designer.md
```

## Usage

### New Project Setup

1. Create `.opencode/agents/` in your project
2. Create agent files referencing ai-team:

```yaml
# your-project/.opencode/agents/developer.md
---
description: Your project developer
mode: all
instructions:
  - ../ai-team/principles.md
  - ../ai-team/opencode/agents/developer.md
---

# Developer — Your Project

## Stack
...

## Commands
...
```

3. Add project-specific details (stack, commands, rules)

## Four Principles

1. **Think Before Coding** — Analyze, then implement
2. **Simplicity First** — Existing conventions over new abstractions
3. **Surgical Changes** — Touch only relevant files
4. **Goal-Driven** — Observable evidence, not assumptions

## Features

- **Caveman Talk** — Brief responses, save tokens
- **Model Selection** — Auto-switch between tiers (HIGH/MID/LOW)
- **Self-Maintenance** — Update knowledge base when code changes

See `principles.md` for details.

## References

- [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)
- [OpenCode Docs](https://opencode.ai/v2/docs/)
