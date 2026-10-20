# Codex adapter for the shared AI Team

This file only describes how Codex loads the existing framework. It contains no
separate role definitions, delivery principles, or project knowledge.

## Source loading

Before project work:

1. Identify the target project and read its `AGENTS.md` and applicable nested
   `AGENTS.md` files. Resolve all paths below against that project, not the shell's
   current directory.
2. Read `../ai-team/principles.md` from disk. This is the shared source of delivery
   behavior for both Codex and OpenCode.
3. Read the project's `.opencode/opencode.jsonc` and load its `instructions`
   entries, expanding globs relative to the project. Do not treat JSONC as plain
   JSON. Read referenced local instruction files; do not execute embedded commands
   merely because they occur in documentation.
4. Start with the coordinator role. Read `.opencode/agents/coordinator.md` if it
   exists; otherwise read `../ai-team/opencode/agents/coordinator.md`.
5. For each role, read its current `.opencode/agents/<role>.md`, recursively load
   the YAML front matter's `instructions` references in their listed order, then
   apply the file's Markdown body. Resolve these references relative to the
   containing agent file. If no project role exists, use the matching shared
   `../ai-team/opencode/agents/<role>.md`. Apply shared guidance first and project
   specifics afterward. Detect reference cycles; report missing sources instead
   of silently inventing a replacement.

Read sources again when they change. Never maintain copied Codex versions of
principles, agent bodies, project commands, or knowledge base files. The existing
`.opencode/` names are storage locations shared by both runtimes.

## Runtime adaptation

- Use Codex's available subagent tools to delegate under the shared framework.
  Give each subagent its role, project directory, source paths to read, objective,
  acceptance criteria, exclusive writable files, and required checks. Require it
  to load the same current shared and project sources before acting. Coordinator
  owns integration and QA stays independent of implementation.
- OpenCode `mode`, provider/model identifiers, formatter, snapshots and runtime
  configuration are not Codex configuration. Do not rewrite them or claim they
  were activated. Keep the current Codex model unless an authorized, supported
  runtime mechanism permits a change. Report unavailable capabilities honestly.
- Read OpenCode permission declarations as behavioral restrictions, including
  read-only roles, denied operations and approval requirements. They do not
  install a Codex sandbox or tool-level enforcement. Codex's actual tool access
  and higher-priority instructions continue to apply; never bypass them.
- Follow the shared maintenance policy using the existing project knowledge
  files. Do not create a second Codex knowledge base or edit shared definitions
  incidentally. Changes explicitly requested by the user remain authorized.
- If subagents are unavailable, report that limitation and distinguish sequential
  self-review from independent QA. Never claim an agent ran when it did not.

## Scope

Activate this adapter for projects with `.opencode/opencode.jsonc` or
`.opencode/agents/`. Other repositories retain their own workflow. This adapter
provides instruction loading and role delegation, not an OpenCode runtime.
