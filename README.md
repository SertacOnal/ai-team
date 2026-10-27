# AI Team Framework

Karpathy-inspired coding principles and reusable Codex role guidance.

## Structure

```text
ai-team/
├── AGENTS.md
├── model-policy.md
├── principles.md
└── agents/
    ├── coordinator.md
    ├── spec-writer.md
    ├── developer.md
    ├── qa.md
    ├── dba.md
    ├── financial-reviewer.md
    └── designer.md
```

## Project setup

Keep this repository beside the consuming project. Put persistent project rules
in the project's `AGENTS.md`, project role details in `.codex/agents/`, and
on-demand knowledge in `.codex/instructions/`.

Add explicit reading instructions to the project's `AGENTS.md`, for example:

```markdown
Before project work, read `../ai-team/principles.md`,
`../ai-team/agents/coordinator.md`, and `.codex/agents/coordinator.md`.
For implementation, also read `../ai-team/agents/developer.md` and
`.codex/agents/developer.md`.
Apply shared guidance first, followed by project-specific rules.
If the sibling repository is missing, report the missing dependency.
```

`AGENTS.md` is the Codex entry point. The other Markdown files are explicitly
read context; placing them in `agents/` does not install runtime agent types or
select models. When delegation is available and permitted, include the relevant
shared and project role paths in each assignment. Otherwise apply the roles
sequentially and identify self-review honestly.

Task closure follows the self-evaluation in `principles.md`: developers propose
lessons, QA checks the evidence, and the coordinator curates reusable project
knowledge. No new lesson means no extra knowledge file.

See [principles.md](principles.md) for coding and delivery rules and
[model-policy.md](model-policy.md) for the shared model policy. All roles inherit
the coordinator model; routine work defaults to Sol/high, with Astra/high
recommended for critical financial, architectural, security, or data work.

## References

- [Codex workflow conventions](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)
- [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)
