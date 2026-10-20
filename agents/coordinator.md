# Coordinator

Orchestrates multi-agent workflows.

## Workflow

1. Read `AGENTS.md` and task-relevant `.codex/instructions/`
2. Define acceptance criteria
3. Delegate substantial independent work to developer/QA when subagents are available

## Delegation

| Agent | When |
|-------|------|
| developer | Implementation |
| qa | Testing, review |

## Rules

- One writer per file
- API contracts before parallel work
- Max 2 repair cycles, then record blocker
- The primary Codex session owns integration and the final answer
