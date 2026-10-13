---
name: pstack-principle-subtract-before-you-add
description: "Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base."
disable-model-invocation: true
---

## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

# Subtract Before You Add

When evolving a system, remove complexity first, then build. Default to subtraction.

Make simplification a continual investment. Leave the design slightly simpler and more capable behind the same or smaller surface than you found it.

- Sequence removal before construction
- Cut before you polish (get to the minimum before investing in quality)
- Design for observed usage, not speculative edge cases
- No speculative validators, parsers, or guards beyond what the spec demands
- Simplify prompts (remove redundant instructions, excessive templates)
- When a reference has no novel content, delete it rather than leaving a stub
