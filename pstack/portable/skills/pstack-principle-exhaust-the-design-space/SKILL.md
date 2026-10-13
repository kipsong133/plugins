---
name: pstack-principle-exhaust-the-design-space
description: "Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing."
disable-model-invocation: true
---

## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

# Exhaust the Design Space

It also applies to product design decisions where user experience depends on feel, not logic.
