#!/usr/bin/env python3
"""Build and link the shared Codex / Claude Code edition from this checkout."""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'skills'
SKILLS = ROOT / 'skills'
NAMES = {p.name: 'pstack-' + p.name for p in SOURCE.iterdir() if (p / 'SKILL.md').exists()}
COMPAT = '''## Codex / Claude Code compatibility

Apply this section before the upstream workflow. Read [host mappings](../../HOSTS.md) when using model configuration, delegation, history, automation, or Cursor-specific tools. Resolve bundled skills by their original directory name using [the skill map](../../skill-map.json); their installed names have a `pstack-` prefix. Resolve all scripts relative to this skill directory.

Use the current host's tools and inherit the parent model by default. Cursor model slugs, cloud agents, `Task` parameters, custom modes, and `/loop` are examples of upstream capabilities, not tools to assume exist here. Preserve host instructions and the user's authorization scope for every action.

'''
for old, new in sorted(NAMES.items()):
    assert len(new) <= 64, new
    for base in (Path.home()/'.agents/skills', Path.home()/'.claude/skills'):
        link = base/new
        if link.exists() or link.is_symlink():
            if not link.is_symlink() or link.resolve() != (SKILLS/new).resolve():
                raise SystemExit(f'Existing installation preserved: {link}')
for old, new in sorted(NAMES.items()):
    initial = SKILLS/old
    if initial.exists():
        shutil.rmtree(initial)
    target = SKILLS/new
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SOURCE/old, target)
    shutil.copy2(ROOT.parent/'LICENSE', target/'LICENSE')
    for file in target.rglob('*.md'):
        data = file.read_text()
        for sibling, installed in sorted(NAMES.items(), key=lambda item: -len(item[0])):
            data = re.sub(r'(?<=\.\./)' + re.escape(sibling) + r'(?=/)', installed, data)
            data = re.sub(r'/' + re.escape(sibling) + r'(?![\w-])', '/' + installed, data)
        file.write_text(data)
    entry = target/'SKILL.md'
    data = entry.read_text()
    front, body = data[4:].split('\n---', 1)
    front = re.sub(r'^name:.*$', 'name: '+new, front, flags=re.M)
    front = re.sub(r'^(mode|icon|color|reminder):.*\n?', '', front, flags=re.M)
    data = data.replace('../../README.md', '../../README.upstream.md')
    entry.write_text('---\n'+front+'\n---\n\n'+COMPAT+body.lstrip())
    if 'disable-model-invocation: true' in front:
        (target/'agents').mkdir(exist_ok=True)
        (target/'agents/openai.yaml').write_text('policy:\n  allow_implicit_invocation: false\n')
    if old == 'setup-pstack':
        entry.write_text('''---
name: pstack-setup-pstack
description: Configure pstack role models for local Codex and Claude Code sessions.
---

# Configure pstack

Read [host mappings](../../HOSTS.md). Load `~/.config/pstack/models.json` if present. Ask which host and role preferences to change. Inherit the current parent model for unspecified roles. Offer explicit models only when the active host confirms they are available; keep model identifiers and reasoning effort as separate fields. Show the proposed configuration, then save the agreed values to `~/.config/pstack/models.json` without editing Codex or Claude global instruction files. Return the written path and roles. Each installed pstack skill reads this configuration through its compatibility section. Model settings never authorize additional actions.
''')
    for base in (Path.home()/'.agents/skills', Path.home()/'.claude/skills'):
        base.mkdir(parents=True, exist_ok=True)
        link = base/new
        if not link.is_symlink():
            link.symlink_to(target, target_is_directory=True)
for directory in ('agents', 'docs'):
    shutil.copytree(ROOT.parent/directory, ROOT/directory, dirs_exist_ok=True)
shutil.copy2(ROOT.parent/'README.md', ROOT/'README.upstream.md')
for shared in [ROOT/'README.upstream.md', *(ROOT/'docs').rglob('*.md')]:
    text = shared.read_text()
    for old, new in NAMES.items():
        text = text.replace('/skills/'+old+'/', '/skills/'+new+'/')
    shared.write_text(text)
(ROOT/'skill-map.json').write_text(json.dumps(NAMES, indent=2)+'\n')
print(f'Installed {len(NAMES)} skills for Codex and Claude Code.')
