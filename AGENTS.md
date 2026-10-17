# AI Team Framework

Generic AI agent framework with Karpathy-inspired coding principles.

## Purpose

This repository provides:
- **Coding principles** (`principles.md`) — Discipline for AI-assisted development
- **Generic agents** (`opencode/agents/`) — Reusable OpenCode agent templates
- **Project templates** (`templates/`) — Handoff and project configuration

## Usage

This is a **reference repository**. It defines no project-specific agents.

### For New Projects

1. Create `.opencode/` in your project root
2. Copy or adapt agents from `ai-team/opencode/agents/`
3. Add project-specific agents as needed
4. Reference `principles.md` in your instructions

### For Existing Projects

Reference this framework in your project's `opencode.jsonc`:

```jsonc
{
  "instructions": ["../ai-team/principles.md"]
}
```

Or copy `principles.md` to your project's `.opencode/` or docs.

## Available Agents

| Agent | Mode | Purpose |
|-------|------|---------|
| `coordinator` | primary | Project orchestration and delegation |
| `developer` | all | Generic software development |
| `qa` | subagent | Independent testing and review |
| `designer` | subagent | UI/UX design (optional) |

## Principles Summary

1. **Think before coding** — Analyze, then implement
2. **Simplicity first** — Existing conventions over new abstractions  
3. **Surgical changes** — Touch only relevant files
4. **Goal-driven** — Observable success criteria

See `principles.md` for the complete framework.

## Constraints

- No automatic commit/push/deploy
- No credentials in outputs
- Synthetic fixtures only (no production data)
- One writer per file
- User authorization required for releases

## Related

- [OpenCode Documentation](https://opencode.ai/v2/docs/)
- [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)
