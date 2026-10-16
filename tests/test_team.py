import importlib.util,tempfile,subprocess,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('team',Path(__file__).parents[1]/'scripts/team.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Team(unittest.TestCase):
 def test_roles(self):self.assertEqual(len(m.validate()),9)
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
