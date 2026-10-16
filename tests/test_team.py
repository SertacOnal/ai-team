import importlib.util,tempfile,subprocess,unittest,json
from pathlib import Path
spec=importlib.util.spec_from_file_location('team',Path(__file__).parents[1]/'scripts/team.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Team(unittest.TestCase):
 def repo(self,t):
  p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);return p
 def test_framework_has_no_roles(self):m.validate();self.assertFalse(list((m.ROOT/'.codex/agents').glob('*.toml')))
 def test_preserves_project_roles_config_and_handoff(self):
  with tempfile.TemporaryDirectory() as t:
   p=self.repo(t);(p/'.codex/agents').mkdir(parents=True);role=p/'.codex/agents/developer.toml';role.write_text('project role');(p/'.codex/config.toml').write_text('model="local"');(p/'AGENTS.md').write_text('project rules')
   m.install(p);self.assertFalse((p/'.ai-framework').exists());m.install(p,True);(p/'.ai/handoff.md').write_text('my work');m.install(p,True)
   self.assertEqual(role.read_text(),'project role');self.assertEqual((p/'.ai/handoff.md').read_text(),'my work');self.assertTrue((p/'AGENTS.md').read_text().startswith('project rules'));self.assertEqual((p/'AGENTS.md').read_text().count(m.START),1)
 def test_legacy_owned_roles_retired(self):
  with tempfile.TemporaryDirectory() as t:
   p=self.repo(t);(p/'.ai-team').mkdir();(p/'.codex/agents').mkdir(parents=True);role=p/'.codex/agents/team_developer.toml';role.write_text('old');(p/'.ai-team/install.json').write_text(json.dumps({'files':{'.codex/agents/team_developer.toml':m.digest(b'old')}}))
   m.install(p);self.assertTrue(role.exists());m.install(p,True);self.assertFalse(role.exists());self.assertFalse((p/'.ai-team/install.json').exists())
 def test_edited_legacy_blocks_before_mutation(self):
  with tempfile.TemporaryDirectory() as t:
   p=self.repo(t);(p/'.ai-team').mkdir();(p/'.codex/agents').mkdir(parents=True);role=p/'.codex/agents/team_qa.toml';role.write_text('user edits');(p/'.ai-team/install.json').write_text(json.dumps({'files':{'.codex/agents/team_qa.toml':m.digest(b'old')}}))
   with self.assertRaises(ValueError):m.install(p,True)
   self.assertEqual(role.read_text(),'user edits');self.assertFalse((p/'.ai-framework').exists())
 def test_malformed_markers_preserved(self):
  with tempfile.TemporaryDirectory() as t:
   p=self.repo(t);text=m.END+'\nUser rules\n'+m.START;(p/'AGENTS.md').write_text(text)
   with self.assertRaises(ValueError):m.install(p,True)
   self.assertEqual((p/'AGENTS.md').read_text(),text)
