# Model policy

## Session-level selection

The coordinator's selected model is the team's model. For the current Codex
workflow, subagents inherit the parent model and reasoning effort: omit model
and reasoning overrides when spawning them. Roles change responsibilities and
context, not the selected model. Respect explicit user selections.

| Work | Recommended coordinator model | Reasoning |
|---|---|---|
| Routine implementation, scoped fixes, UI work, tests, documentation | `gpt-6.1-sol` | `high` |
| Ambiguous architecture, critical financial logic, security boundaries, high-risk data transformations | `gpt-6-astra` | `high` |
| Exceptionally difficult analysis after evidence-based diagnosis | `gpt-6-astra` | `xhigh`, only when explicitly selected |

These are team defaults, not measured guarantees about project quality. Evaluate
results through acceptance criteria and checks, regardless of the model.

## Role behavior

Coordinator, spec-writer, developer, QA, DBA, designer, and financial-reviewer
all inherit the selected coordinator model. Independent review means a separate reviewer with
its own assignment; it does not require a different model. Never label a
self-review independent.

## Coordinator responsibilities

- Read this policy through the shared principles, then apply project-specific
  risk triggers. Identify the appropriate session profile before delegating.
- Use the actual runtime/session model when known. A config default is not
  proof of the model running an existing conversation.
- If the task warrants Astra but the session uses Sol, state that recommendation
  and continue useful work under the user's current selection. Do not invent a
  model switch or block solely because a recommended model is unavailable.
- A switch must be made through a supported runtime action or the user's model
  selector. Markdown does not perform it. Do not rewrite global settings,
  silently substitute providers, or create separate chats to bypass limits.
- Include role, objective, acceptance criteria, allowed files, context paths,
  and required checks in every assignment. In a fresh context, include the
  project root and explicit reading order.

## Configuration

A consuming project may set its startup default in `.codex/config.toml`:

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "high"
```

Project settings depend on the host loading/trusting that project. Explicit
session selections remain authoritative. This policy does not register agent
types or set per-role runtime models.

Model capability reference: [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection).
