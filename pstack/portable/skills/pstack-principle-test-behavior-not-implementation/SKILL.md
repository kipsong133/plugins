---
name: pstack-principle-test-behavior-not-implementation
description: "Apply when you write, change, or keep a test. Call the code as its users do and assert the exact result they see. Rewrite or delete a test that would pass if every imported function returned undefined."
disable-model-invocation: true
---

## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

# Test Behavior, Not Implementation

A test calls the code as its users do and asserts the exact result they see. Rewrite or delete any test that would still pass if every imported function returned `undefined` or a wrong value.

These shapes fail that check:

- Loose or no assertion: `toBeDefined`, `toBeTruthy`, `not.toThrow`, `toBeGreaterThan(0)`.
- Call or absence only: `toHaveBeenCalled`, `not.toHaveBeenCalled`, `toBeUndefined`, `toEqual([])`.
- Expected value computed by the code under test: `expect(f(a)).toBe(f(a))`.
- Restated constant, config default, table row, or prompt string.
- Assertions on data the test built, with no call to the subject.

Fix: call the subject in the test body with one concrete input and assert the literal output or effect. For a mock, assert the payload it received. For an absence, also assert the presence on another input. For a constant, test the mechanism that reads it with one input instead of restating the value.

Keep relation checks across table rows (a key in two tables, a parent that exists) and `*.test-d.ts` type checks.
