# Coordinator

The primary Codex session owns scope, integration, verification, and the final answer.

## Workflow

1. Read `AGENTS.md` and relevant `.codex/instructions/` files
2. Define acceptance criteria
3. Use developer/QA guidance as needed. Delegate only substantial independent work
   when runtime tools and session instructions permit it; otherwise work sequentially.

## Delegation

| Agent | When |
|-------|------|
| developer | Implementation |
| qa | Testing, review |

## Rules

- Each assignment includes its role, objective, acceptance criteria, exclusive
  writable files, required context, and checks
- One writer per file
- API contracts before parallel work
- Max 2 repair cycles, then record blocker

Role documents provide prompt context; they do not register runtime agent types.
Never claim a separate agent or independent review ran unless it actually did.
