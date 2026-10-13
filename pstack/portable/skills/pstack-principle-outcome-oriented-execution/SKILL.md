---
name: pstack-principle-outcome-oriented-execution
description: "Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code."
disable-model-invocation: true
---

## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

# Outcome-Oriented Execution

Optimize for the intended, verifiable end state rather than preserving smooth intermediate states.

**Why:** Keeping every intermediate step fully stable often creates temporary compatibility code that becomes long-lived debt. Converge on the target architecture and prove correctness at explicit verification boundaries.

**Core rule:**
- Prioritize end-state integrity over transitional stability
- Intermediate breakage is acceptable when it is planned, scoped, and reversible

**Guardrails:**
- Use this for planned rewrites and migrations with explicit phase boundaries
- Declare where temporary breakage is acceptable
- Keep high-signal checks for actively touched areas while migrating
- Require full static and runtime verification at plan completion
