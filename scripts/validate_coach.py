#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for label,text in [('SKILL.md',skill),('README.md',readme)]:
    if '0.3.2' not in text: errors.append(f'{label}: version 0.3.2 missing')
for stale in ['experiment/self-attack','audit/consistency-check','audit/final-audit','models/qN.md','runs/final/qN.json']:
    if stale in skill: errors.append(f'SKILL.md: stale contract {stale}')
if 'SkillHub `registry.yaml`' not in skill and 'SkillHub 的 `registry.yaml`' not in skill:
    errors.append('SKILL.md: registry routing authority missing')
if not (ROOT/'templates/competition-repo/DEPRECATED.md').exists():
    errors.append('embedded competition template not visibly deprecated')
legacy=[p for p in (ROOT/'templates/competition-repo').rglob('*') if p.is_file() and p.name!='DEPRECATED.md']
if legacy: errors.append('obsolete embedded template files remain: '+', '.join(str(p.relative_to(ROOT)) for p in legacy[:5]))
for p in (ROOT/'playbooks').glob('*.md'):
    if '情景策略参考，不是执行阶段' not in p.read_text(encoding='utf-8'):
        errors.append(f'{p.relative_to(ROOT)} missing non-stage guardrail')
if errors:
    print('COACH_VALIDATION_FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('COACH_VALIDATION_PASS: state-first + registry routing + single template authority')
