#!/usr/bin/env python3
"""Install shared framework only; project-owned agents are never generated."""
import argparse,hashlib,json,subprocess,sys,tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START='<!-- ai-team:start -->';END='<!-- ai-team:end -->'
BLOCK=START+'\nRead [.ai-framework/principles.md](.ai-framework/principles.md). The main session coordinates; use relevant project-owned roles in `.codex/agents/` when present.\n'+END

def digest(b):return hashlib.sha256(b).hexdigest()
def validate():
    if list((ROOT/'.codex/agents').glob('*.toml')):raise ValueError('Shared framework must not define agents')
    for p in ('principles.md','workflows/github-connector.md'):
        if not (ROOT/p).read_text().strip():raise ValueError('Empty framework file')
    tomllib.loads((ROOT/'runtime.toml').read_text());json.loads((ROOT/'templates/project.json').read_text())

def install(target,apply=False):
    validate();target=Path(target).resolve()
    top=subprocess.run(['git','-C',str(target),'rev-parse','--show-toplevel'],check=True,capture_output=True,text=True).stdout.strip()
    if Path(top).resolve()!=target:raise ValueError('Target must be the Git repository root')
    def path(rel):
        p=target/rel
        if any(x.is_symlink() for x in [p,*p.parents] if x!=target.parent):raise ValueError('Symlink destination refused')
        return p
    state=path('.ai-framework/install.json');legacy=path('.ai-team/install.json')
    previous=json.loads((state if state.exists() else legacy).read_text()).get('files',{}) if state.exists() or legacy.exists() else {}
    files={'.ai-framework/principles.md':(ROOT/'principles.md').read_bytes(),'.ai-framework/workflows/github-connector.md':(ROOT/'workflows/github-connector.md').read_bytes()}
    for name in ('project.json','handoff.md'):
        if not path('.ai/'+name).exists():files['.ai/'+name]=(ROOT/'templates'/name).read_bytes()
    retired={'.codex/agents/team_'+n+'.toml' for n in ('po','lead','developer','qa','designer','frontend','backend','infrastructure','researcher')}
    retired.update(('.ai-team/AGENTS.md','.ai-team/workflows/github-connector.md'))
    stale=set(previous)&retired
    for rel,data in files.items():
        p=path(rel)
        if p.exists() and p.read_bytes()!=data and digest(p.read_bytes())!=previous.get(rel):raise ValueError('Preserve local edits; reconcile '+rel)
    for rel in stale:
        p=path(rel)
        if p.exists() and digest(p.read_bytes())!=previous[rel]:raise ValueError('Preserve edited retired file; reconcile '+rel)
    agents=path('AGENTS.md');text=agents.read_text() if agents.exists() else ''
    if text.count(START)!=text.count(END) or text.count(START)>1 or (START in text and text.index(END)<text.index(START)):raise ValueError('Malformed managed block')
    if START in text:
        a=text.index(START);b=text.index(END)+len(END);text=text[:a]+BLOCK+text[b:]
    else:text=text.rstrip()+'\n\n'+BLOCK+'\n'
    print(('APPLY' if apply else 'DRY RUN')+f': {len(files)} framework/template files, {len(stale)} retired files; project agents preserved')
    if not apply:return
    for rel,data in files.items():
        p=path(rel);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    for rel in stale:path(rel).unlink(missing_ok=True)
    agents.write_text(text)
    owned={**{r:h for r,h in previous.items() if r not in stale},**{r:digest(b) for r,b in files.items()}}
    state.write_text(json.dumps({'version':2,'files':owned},indent=2)+'\n')
    if legacy.exists():legacy.unlink()

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True);sub.add_parser('validate');i=sub.add_parser('install');i.add_argument('--target',required=True);i.add_argument('--apply',action='store_true');a=p.parse_args()
    if a.command=='validate':validate();print('PASS: framework, runtime and templates; no shared roles')
    else:install(a.target,a.apply)
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,subprocess.CalledProcessError) as e:print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
