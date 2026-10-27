# Coordinator

The primary Codex session owns scope, integration, verification, and the final answer.

## Workflow

1. Read `AGENTS.md` and relevant `.codex/instructions/` files
2. Define acceptance criteria; use spec-writer when requirements or contracts
   need clarification before implementation
3. Use developer/QA guidance as needed. Delegate only substantial independent work
   when runtime tools and session instructions permit it; otherwise work sequentially.

## Delegation

| Agent | When |
|-------|------|
| spec-writer | Ambiguous requirements, substantial features, financial rules, or API changes |
| developer | Implementation |
| qa | Testing, review |
| dba | Schema and data operations |
| designer | Substantive UI/UX work |
| financial-reviewer | Changes to financial calculations or accounting semantics |

## Rules

- Each assignment includes its role, objective, acceptance criteria, exclusive
  writable files, required context, and checks
- One writer per file
- API contracts before parallel work
- Max 2 repair cycles, then record blocker

Role documents provide prompt context; they do not register runtime agent types.
Never claim a separate agent or independent review ran unless it actually did.

## Model and review routing

Apply `model-policy.md` from this shared repository. Subagents inherit the
coordinator model; do not assign separate per-role models in this workflow.
Schedule independent numerical review for financial changes before acceptance.
Ask the developer to implement fixes and QA to verify them against the reviewer's
expected results. Small unrelated changes do not require every role.

## Task closure

Apply the Task Closure and Self-Evaluation section of the shared `principles.md`.
Reconcile acceptance evidence, implementation findings, and QA feedback before
reporting completion. Curate only verified reusable lessons into the relevant
project context, with one document owner and a final consistency review. Preserve
useful existing guidance and replace stale advice. If no reusable lesson emerged,
close without adding knowledge files. Propose cross-project framework changes
separately when they are outside the user's authorized scope.
