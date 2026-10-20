# AI Team Framework for Codex

Reusable coding principles and role templates for Codex on macOS and Linux.

## Structure

```text
ai-team/
├── AGENTS.md              # Native Codex repository instructions
├── principles.md          # Shared delivery principles
└── agents/                # Optional role templates
    ├── coordinator.md
    ├── developer.md
    ├── qa.md
    ├── dba.md
    └── designer.md
```

## New project setup

1. Add a concise `AGENTS.md` to the project root.
2. Keep `ai-team` and the project as sibling directories under the same parent.
3. Put project-local supporting guidance under `.codex/agents/` and
   `.codex/instructions/`.
4. In the project's `AGENTS.md`, tell Codex to read
   `../ai-team/principles.md`, the relevant shared `../ai-team/agents/<role>.md`,
   and then the matching project-local files.
5. Keep model/provider selection in Codex settings, not repository files.

Codex automatically loads applicable `AGENTS.md` files. Files under `.codex/`
are ordinary repository files and are read when `AGENTS.md` or the user asks
Codex to read them.

Consumer projects intentionally depend on the `../ai-team` sibling checkout. If
that path is unavailable, Codex must report the missing dependency rather than
silently inventing replacement guidance.

## Principles

1. Think before coding.
2. Prefer the simplest complete solution.
3. Make surgical changes and preserve unrelated work.
4. Verify outcomes with observable evidence.

See `principles.md` for the complete framework.
