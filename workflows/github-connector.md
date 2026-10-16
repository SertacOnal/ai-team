# GitHub connector delivery

Own the request as a single coordinator: PO scope and observable acceptance,
Lead refinement and dependencies in the main session, developer for
implementation, qa for independent acceptance and optional designer
for substantive visual work. Do not start separate PO/Lead/researcher agents. Stakeholder
review is the final product checkpoint, not an approval for every role handoff.

Use the runner's trusted target/workspace assignment. Read existing-project rules and delegate using the project-owned .codex/agents roles.
For connector assignments, legacy pnl_*, lab_* and team_* roles are superseded by project roles;
legacy project knowledge remains context only. For new work,
use appropriate general specialists without imposing Pnlcal financial rules.
Research returns source-backed findings. Plan-only requests do not edit products.

Write `progress.json` in the assigned workspace as work advances. It contains
`phase` (analysis/design/refinement/development/qa/review/blocked), `summary`, and
`tasks` with `id`, `title`, `role`, `status` (todo/doing/review/done/blocked),
`acceptance`, `dependencies` and `evidence`. Keep task IDs stable across updates.
Do not include tokens, private user data or raw command output in this file.
The runner mirrors safe progress to the parent issue and child work items.

Actual tasks and dependencies determine work breakdown, not a fixed agent count.
Assign exclusive writable paths and one owner for common files. QA failure returns
to the developer; never weaken tests to produce success. Runtime limits govern
parallel work. No delegation means sequential role passes and disclosed self-review.

If a material product question blocks work, return blocked and put the question in
the summary. Continue independent work when possible. On `/agent continue`, read
the saved work, latest request and stakeholder response before continuing.

Finish with status `review` when delivery and required checks are complete, or
`blocked` with the concrete missing decision/environment. Include safe acceptance
evidence. The stakeholder decides final acceptance. Keep code local unless the
current request explicitly authorizes publishing changes; never deploy by default.

## Runner browser QA handoff
For implemented Pnlcal frontend work, finish implementation and test authoring,
first write current progress.json, stop all delegated writers, then atomically write
`browser-qa-request.json` containing exactly
`{"suite":"pnlcal-frontend"}`. Return phase blocked with QA pending immediately. Never poll or wait for the
result in this turn: the runner stops the producer at the handoff and resumes a
separate QA review after tests finish. The trusted
runner runs npm ci, Chromium install, E2E typecheck and the configured Playwright
suite outside the Codex sandbox, then resumes you with browser-qa-result.json.
Do not repeatedly launch Chromium inside macOS workspace-write. Read actual
results and inspect failure artifacts. Runner PASS is test-suite evidence only;
independent QA still decides acceptance. If you change source/tests afterward,
request a fresh run and leave browser acceptance blocked. Plan-only tasks never
request this handoff. Logs stay local and must not be posted raw to GitHub.
