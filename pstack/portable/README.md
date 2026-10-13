# pstack for local Codex and Claude Code

52 skills, adapted from Cursor pstack 0.15.21. The original skills and MIT license are retained in the parent directory. Installed names use `pstack-` to preserve existing skills.

## Use

Codex: `$pstack-poteto-mode`, `$pstack-how`, `$pstack-interrogate`.
Claude Code: `/pstack-poteto-mode`, `/pstack-how`, `/pstack-interrogate`.
Help: `pstack-poteto-help`. Configure role models: `pstack-setup-pstack`.
Start a new session after installation to refresh discovery. Cursor custom-mode persistence is not installed.

## Install again

Run `python3 pstack/portable/install.py` from the repository root. It builds adapted copies and links them into `~/.agents/skills` and `~/.claude/skills`. It refuses to replace unrelated existing entries. It preserves upstream explicit-only policies; Codex receives equivalent `agents/openai.yaml` policies.

The script rebuilds generated skill directories. Keep personal edits in the original skills or the builder, rather than in generated copies. After rebuilding, run `bun install --frozen-lockfile` in `pstack/portable/skills/pstack-poteto-mode/scripts` before using TypeScript helpers.

## Update

The checkout has `origin` pointing to the personal fork and `upstream` pointing to Cursor. Fetch upstream, review and integrate changes on the compatibility branch, then run the installer again. Automatic updates are not enabled.

## Verification

52 entrypoints and 104 global symlinks verified. Bundled helper suite: 63 tests passed; TypeScript checking passed with Bun 1.4.3. Reinstall was verified. End-to-end workflows involving cloud agents, distinct model families, external services, or future wakeups require host-supported equivalents. See [HOSTS.md](HOSTS.md).
