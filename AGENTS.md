# AI Team Framework

Shared coding principles and role guidance for Codex. This repository contains
Markdown instructions, not executable agent registrations.

## Context

Before editing this framework, read `principles.md` and `agents/coordinator.md`.
Read the other role documents only when relevant. Inspect Git state first and
preserve unrelated changes.

## Structure

- `principles.md`: coding discipline, delivery, task self-evaluation, runtime limits,
  and evidence-based knowledge upkeep.
- `model-policy.md`: coordinator model recommendations inherited by all roles.
- `agents/financial-reviewer.md`: independent financial correctness review.
- `agents/coordinator.md`: scope, integration, and delegation guidance.
- `agents/spec-writer.md`: requirements, contracts, and testable acceptance criteria.
- `agents/developer.md`: implementation and verification.
- `agents/qa.md`: independent review and acceptance evidence.
- `agents/dba.md`: schema, data, and cache review.
- `agents/designer.md`: optional substantive UI/UX design.

## Maintenance

- Keep roles as plain Markdown without provider-specific frontmatter.
- Keep generic rules here and stack/commands in project-local guidance.
- Project `AGENTS.md` must explicitly tell Codex which shared files to read.
- Role documents are context for the current session or an explicitly assigned
  subagent; they do not configure models, tools, or permissions.
- Use available runtime browser tools for UI verification. Keep project E2E
  commands in project guidance rather than installing browser integrations here.

## Verification

For documentation changes, check relative paths, role references, the integrated
Git diff, and whitespace. No application build is needed for prose-only edits.
