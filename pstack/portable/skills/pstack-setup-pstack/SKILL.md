---
name: pstack-setup-pstack
description: Configure pstack role models for local Codex and Claude Code sessions.
---

# Configure pstack

Read [host mappings](../../HOSTS.md). Load `~/.config/pstack/models.json` if present. Ask which host and role preferences to change. Inherit the current parent model for unspecified roles. Offer explicit models only when the active host confirms they are available; keep model identifiers and reasoning effort as separate fields. Show the proposed configuration, then save the agreed values to `~/.config/pstack/models.json` without editing Codex or Claude global instruction files. Return the written path and roles. Each installed pstack skill reads this configuration through its compatibility section. Model settings never authorize additional actions.
