#!/usr/bin/env python3
"""Install portable instructions into a project without touching product code."""
import argparse,hashlib,json,subprocess,sys,tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START='<!-- ai-team:start -->';END='<!-- ai-team:end -->'
BLOCK=START+'\nRead [.ai-team/AGENTS.md](.ai-team/AGENTS.md) and use relevant team_* roles.\n'+END

def digest(b):return hashlib.sha256(b).hexdigest()
def validate():
    roles=list((ROOT/'.codex/agents').glob('team_*.toml'))
    if len(roles)!=9:raise ValueError('Expected nine team roles')
    for p in roles:
        d=tomllib.loads(p.read_text())
        if d.get('name')!=p.stem or d.get('model')!='gpt-6-luna' or d.get('model_reasoning_effort')!='low' or not d.get('developer_instructions'):raise ValueError('Invalid role '+p.name)
    tomllib.loads((ROOT/'.codex/config.toml').read_text());json.loads((ROOT/'templates/project.json').read_text())
    return roles

def install(target,apply=False):
    target=Path(target).resolve()
    top=subprocess.run(['git','-C',str(target),'rev-parse','--show-toplevel'],check=True,capture_output=True,text=True).stdout.strip()
    if Path(top).resolve()!=target:raise ValueError('Target must be the Git repository root')
    config=target/'.codex/config.toml'
    if config.exists() and tomllib.loads(config.read_text()).get('agents',{}).get('enabled') is False:
        raise ValueError('Target disables agents; preserve config and resolve explicitly')
    files={'.ai-team/AGENTS.md':(ROOT/'AGENTS.md').read_bytes(), '.ai-team/workflows/github-connector.md':(ROOT/'workflows/github-connector.md').read_bytes()}
    for p in validate():files['.codex/agents/'+p.name]=p.read_bytes()
    if not (target/'.codex/config.toml').exists():files['.codex/config.toml']=(ROOT/'.codex/config.toml').read_bytes()
    for name in ('project.json','handoff.md'):
        if not (target/'.ai'/name).exists():files['.ai/'+name]=(ROOT/'templates'/name).read_bytes()
    state=target/'.ai-team/install.json'
    if state.is_symlink():raise ValueError('Symlink state refused')
    previous=json.loads(state.read_text()).get('files',{}) if state.exists() else {}
    for rel,data in files.items():
        p=target/rel
        if any(x.is_symlink() for x in [p,*p.parents] if x!=target.parent):raise ValueError('Symlink destination refused')
        if p.exists() and p.read_bytes()!=data and digest(p.read_bytes())!=previous.get(rel):raise ValueError('Preserve local edits; reconcile '+rel)
    agents=target/'AGENTS.md'
    if agents.is_symlink():raise ValueError('Symlink AGENTS refused')
    text=agents.read_text() if agents.exists() else ''
    if text.count(START)!=text.count(END) or text.count(START)>1 or (START in text and text.index(END)<text.index(START)):raise ValueError('Malformed managed block')
    if START in text:
        a=text.index(START);b=text.index(END)+len(END);text=text[:a]+BLOCK+text[b:]
    else:text=text.rstrip()+'\n\n'+BLOCK+'\n'
    print(('APPLY' if apply else 'DRY RUN')+f': {len(files)} files in {target}; existing project config/environment/handoff preserved')
    if not apply:return
    for rel,data in files.items():
        p=target/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    agents.write_text(text)
    owned={**previous,**{r:digest(b) for r,b in files.items()}}
    state.write_text(json.dumps({'version':1,'files':owned},indent=2)+'\n')

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True);sub.add_parser('validate');i=sub.add_parser('install');i.add_argument('--target',required=True);i.add_argument('--apply',action='store_true');a=p.parse_args()
    if a.command=='validate':validate();print('PASS: nine roles, config and environment template')
    else:install(a.target,a.apply)
if __name__=='__main__':
    try:main()
    except (ValueError,OSError,subprocess.CalledProcessError) as e:print('ERROR: '+str(e),file=sys.stderr);sys.exit(1)
