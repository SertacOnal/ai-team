# AI Team Framework

This repository contains reusable Codex guidance and role templates. It is not a
runtime, provider configuration, or model selector.

## Codex behavior

- Codex loads this `AGENTS.md` automatically when working in this repository.
- Keep provider and model selection outside the repository. Use the model chosen
  by the current Codex session.
- Treat files in `agents/` as role templates. They are guidance for Codex
  subagents, not independently installed agent types.
- Read `principles.md` before changing framework behavior or role definitions.
- Consumer projects may load this repository through the sibling path
  `../ai-team`. Keep shared principles and base role templates stable so those
  projects can use them as their single shared source of truth.

## Structure

```text
ai-team/
├── AGENTS.md
├── README.md
├── principles.md
└── agents/
    ├── coordinator.md
    ├── developer.md
    ├── qa.md
    ├── dba.md
    └── designer.md
```

## Working rules

- Inspect before editing and preserve unrelated user changes.
- Prefer small, focused changes using existing conventions.
- Define observable success criteria and run relevant checks.
- Delegate only substantial independent work when Codex subagent tools are
  available. The primary Codex session remains responsible for integration.
- Assign each subagent a role, objective, acceptance criteria, writable files,
  and required checks. One writer owns a file at a time.
- Keep QA independent from implementation for high-risk or substantial changes.
- Never claim that a role or check ran unless it actually did.
- Do not commit, push, deploy, change credentials, or touch production data
  unless the user explicitly requests that action.

## Validation

For documentation-only changes, verify links and search for obsolete runtime
configuration references. There is no build step for this repository.
