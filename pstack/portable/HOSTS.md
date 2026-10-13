# Local host mappings

These mappings take precedence over upstream Cursor-specific instructions. The upstream workflows remain in the original `pstack/skills` directory for comparison.

## Models and roles

Read `~/.config/pstack/models.json` when a workflow delegates. Default every role to `inherit-parent`; omit an explicit model and reasoning override. A configured model is usable only if the current host exposes it and host instructions permit the override. If distinct model families are unavailable, report that the reviews used the same family. Do not claim a multi-model review. Upstream Grok and Claude Cursor slugs are not portable identifiers.

## Tools and delegation

On Codex use exposed collaboration tools for subtasks, subject to session instructions. On Claude Code use its available Agent/Task mechanism. Custom Cursor agent types are not automatically registered. Read the matching Markdown brief under `../../agents/` relative to the skill folder, and give that brief to a supported generic agent. Never pretend to dispatch a cloud agent. Use local isolated worktrees when the host supports them. When delegation is unavailable or disallowed, perform sequential passes and report that independence was not verified.

Use the host's planning and question tools when available. Cursor's custom mode persistence and keyboard shortcuts do not apply. Invoke the main skill again in a later conversation when needed. Scheduling requires a host-supported scheduler and the user's request; a process running now is not a future wakeup. Cursor `/loop` is not installed by this package.

## Verification and external integrations

Use available browser, native UI, simulator, or terminal tools for the actual target. `cursor-team-kit`, `deslop`, Bugbot, Cursor cloud APIs, Grok Bot, and third-party MCP services are not bundled. Inspect available equivalents and report missing capabilities. A diff review can replace a prose cleanup step, but cannot prove live behavior. Project-required verification still applies.

## History and storage

Use the active host's authorized history tools and current task artifacts. Cursor transcript locations and agent stores are not host-independent paths. Limit history access to the task scope; use `~/.local/share/pstack/runs/<task-id>/` for local decision trails when the host supplies no task storage. Resolve bundled scripts relative to the skill's absolute directory.

## Authorization

A skill describes workflow, not permission to message people, deploy, merge, delete data, alter credentials, or expand task scope. Follow current user authorization and host rules. Installing the package does not activate its autonomous workflows or recurring jobs.

## Runtime

The bundled TypeScript helpers require Bun. The install process links instructions and supporting resources; it does not start a watcher or automation. Run package installation in `pstack-poteto-mode/scripts` before using its helpers if `node_modules` is absent.
