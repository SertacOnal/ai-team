# AI Team Framework

Generic agent templates + Karpathy principles.

## Structure

```
ai-team/
├── principles.md              # Core principles, caveman talk, model selection
└── opencode/
    ├── opencode.jsonc         # Base config
    └── agents/                # Base templates
        ├── developer.md
        ├── qa.md
        ├── coordinator.md
        └── designer.md
```

## Base Agents

| Agent | Purpose |
|-------|---------|
| `developer` | Implementation, testing |
| `qa` | Independent review |
| `coordinator` | Orchestration |
| `designer` | UI/UX design (optional) |

## Usage

### New Project

1. Copy `opencode/agents/` to `your-project/.opencode/agents/`
2. Add project-specific details (stack, commands, rules)
3. Add `../ai-team/principles.md` to instructions

### Inheritance

```
principles.md        → Caveman, model selection, self-maintenance
base agents          → Common workflow, constraints
project agents       → Stack, commands, project rules
project instructions → Knowledge base (schema, api, etc.)
```

## What Goes Where

| Content | Location |
|---------|----------|
| Caveman talk | principles.md |
| Model selection | principles.md |
| Self-maintenance | principles.md |
| Common workflow | base agents |
| Stack/commands | project agents |
| Schema/API docs | project instructions |
