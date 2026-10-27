# AI Team Framework

Generic agent templates + Karpathy principles for OpenCode.

## Structure

```
ai-team/
├── principles.md              # Core principles, caveman talk, model selection
└── opencode/
    ├── agents/                # Base templates
    │   ├── developer.md
    │   ├── qa.md
    │   ├── coordinator.md
    │   └── designer.md
    ├── config/                # Shared configurations
    │   └── playwright.jsonc   # Browser automation config
    ├── scripts/               # Utility scripts
    │   └── chrome-debug.sh    # Chrome remote debugging launcher
    └── docs/                  # Documentation
        └── browser-automation.md
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

1. Create `.opencode/agents/` in your project
2. Create agent files with instructions referencing ai-team:
   ```yaml
   instructions:
     - ../ai-team/principles.md
     - ../ai-team/opencode/agents/developer.md
   ```
3. Add project-specific details (stack, commands, rules)

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

## Browser Automation

Agents can control Chrome via Playwright MCP using existing login sessions.

### Quick Start

```bash
# 1. Start Chrome with remote debugging
~/Repos/ai-team/opencode/scripts/chrome-debug.sh

# 2. Add to project opencode.json (or copy opencode/config/playwright.jsonc)
{
  "mcp": {
    "servers": {
      "playwright": {
        "type": "local",
        "command": ["npx", "-y", "@playwright/mcp", "--cdp-endpoint", "http://127.0.0.1:9222"]
      }
    }
  }
}
```

See `opencode/docs/browser-automation.md` for full documentation.
