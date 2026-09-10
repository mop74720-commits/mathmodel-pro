#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for label,text in [('SKILL.md',skill),('README.md',readme)]:
    if '0.4.1' not in text: errors.append(f'{label}: version 0.4.1 missing')
for phrase in ['OFFICIAL_RULES_NEEDED','RULE_PROFILE.json','PENDING_OFFICIAL_RULES_VERIFICATION','不得**给出 `SUBMISSION_READY`']:
    if phrase not in skill: errors.append('official-rules closure missing '+phrase)
for phrase in ['Selection Workspace','cheap probe','flip condition','不得自动把 Selection']:
    if phrase not in skill: errors.append('selection contract missing '+phrase)
for phrase in ['Outcome first','REPRODUCIBLE','COMPETITIVE_ENOUGH','incumbent challenge','系统闭环度']:
    if phrase not in skill: errors.append('quality/competitiveness invariant missing '+phrase)
for phrase in ['Historical Experience Memory','experience/index.yaml','历史经验只能作为 prior','deciding evidence 必须来自当前题面']:
    if phrase not in skill: errors.append('historical-experience integration missing '+phrase)
for rel in ['references/selection-route-decision.md','THIRD_PARTY_NOTICES.md','docs/v0.4.0-changelog.md','docs/v0.4.1-changelog.md','experience/README.md','experience/index.yaml','experience/patterns.yaml','experience/failures.yaml','scripts/validate_experience.py']:
    if not (ROOT/rel).exists(): errors.append('missing '+rel)
if 'SkillHub `registry.yaml`' not in skill and 'SkillHub 的 `registry.yaml`' not in skill: errors.append('registry routing authority missing')
if not (ROOT/'templates/competition-repo/DEPRECATED.md').exists(): errors.append('embedded template not deprecated')
legacy=[p for p in (ROOT/'templates/competition-repo').rglob('*') if p.is_file() and p.name!='DEPRECATED.md']
if legacy: errors.append('obsolete embedded template files remain')
for p in (ROOT/'playbooks').glob('*.md'):
    if '情景策略参考，不是执行阶段' not in p.read_text(encoding='utf-8'): errors.append(str(p.relative_to(ROOT))+' missing non-stage guardrail')
if errors:
    print('COACH_VALIDATION_FAIL'); [print('-',e) for e in errors]; sys.exit(1)
print('COACH_VALIDATION_PASS: state-first + outcome-first + historical-prior retrieval + evidence-driven incumbent challenge + selection workspace')
