import importlib.util,tempfile,subprocess,unittest,json
from pathlib import Path
spec=importlib.util.spec_from_file_location('team',Path(__file__).parents[1]/'scripts/team.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Team(unittest.TestCase):
 def test_roles(self):self.assertEqual(len(m.validate()),3)
 def test_install_preserves_and_updates(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);(p/'AGENTS.md').write_text('Project rules\n');(p/'.codex').mkdir();(p/'.codex/config.toml').write_text('model = "existing"\n')
   m.install(p);self.assertFalse((p/'.ai').exists());m.install(p,True)
   self.assertTrue((p/'AGENTS.md').read_text().startswith('Project rules'));self.assertIn('existing',(p/'.codex/config.toml').read_text())
   (p/'.ai/handoff.md').write_text('user handoff');m.install(p,True);self.assertEqual((p/'.ai/handoff.md').read_text(),'user handoff');self.assertEqual((p/'AGENTS.md').read_text().count(m.START),1)
 def test_conflicting_role_not_overwritten(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);m.install(p,True);role=p/'.codex/agents/team_qa.toml';role.write_text('local changes')
   with self.assertRaises(ValueError):m.install(p,True)
   self.assertEqual(role.read_text(),'local changes')

 def test_reversed_markers_preserved(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);text=m.END+'\nUser rules\n'+m.START;(p/'AGENTS.md').write_text(text)
   with self.assertRaises(ValueError):m.install(p,True)
   self.assertEqual((p/'AGENTS.md').read_text(),text)

 def test_upgrade_removes_only_owned_unchanged_retired_roles(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);m.install(p,True)
   role=p/'.codex/agents/team_backend.toml';role.write_text('old owned role');custom=p/'.codex/agents/custom.toml';custom.write_text('keep')
   manifest=p/'.ai-team/install.json';d=json.loads(manifest.read_text());d['files']['.codex/agents/team_backend.toml']=m.digest(role.read_bytes());manifest.write_text(json.dumps(d))
   m.install(p);self.assertTrue(role.exists());m.install(p,True)
   self.assertFalse(role.exists());self.assertTrue(custom.exists());self.assertNotIn('.codex/agents/team_backend.toml',json.loads(manifest.read_text())['files'])

 def test_edited_retired_role_blocks_before_writes(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);subprocess.run(['git','init',t],check=True,capture_output=True);m.install(p,True)
   role=p/'.codex/agents/team_po.toml';role.write_text('user changes');manifest=p/'.ai-team/install.json';d=json.loads(manifest.read_text());d['files']['.codex/agents/team_po.toml']=m.digest(b'original');manifest.write_text(json.dumps(d));before=(p/'AGENTS.md').read_bytes()
   with self.assertRaises(ValueError):m.install(p,True)
   self.assertEqual(role.read_text(),'user changes');self.assertEqual((p/'AGENTS.md').read_bytes(),before)
