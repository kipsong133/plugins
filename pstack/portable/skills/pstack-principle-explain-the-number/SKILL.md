---
name: pstack-principle-explain-the-number
description: "Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think."
disable-model-invocation: true
---

## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

# Explain the Number

- **Ask "why not double?"** Name the resource or code path that bounds the result, such as a core, a lock, the disk, the network, or the load generator itself. Get it from a profile or from system counters taken during a run, then map it to source. A guess from reading the code is not a limiter. If you cannot say why the number is not twice as good, you do not know what you measured.
- **List what else the number could be measuring, and rule out each one with evidence.** The usual suspects are errors, skipped or cached work, code that never ran, an untuned side (one left on default settings), noise, and a piece too small to matter end to end.
- **Keep the evidence with the number.** Put the run count, the spread, and the limiter in the notes or a linked artifact.

For a performance number, run the full procedure with the [benchmark-checklist](../pstack-benchmark-checklist/SKILL.md) skill. For an eval result, ask the same of the trials: did every run do the task, does the gap hold across trials and models, and does the scenario matter.

You skipped this when the evidence behind a number has no run count, no spread, or no named limiter, or when the time saved is larger than the time the changed piece took.

Distinct from [Prove It Works](../pstack-principle-prove-it-works/SKILL.md), which checks that an output is real.
