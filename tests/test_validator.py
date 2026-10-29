import unittest,tempfile,shutil
from pathlib import Path
from validate_skill import validate,B
ROOT=Path(__file__).resolve().parents[1]
class Tests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.r=Path(t.name)/'repo';shutil.copytree(ROOT,self.r)
 def change(self,p,a,b):
  q=self.r/p;q.write_text(q.read_text().replace(a,b,1))
 def test_valid(self):self.assertEqual(validate(self.r),[])
 def test_missing_skill(self):
  (self.r/B/'SKILL.md').unlink();self.assertTrue(validate(self.r))
 def test_wrong_name(self):
  self.change(B/'SKILL.md','name: corpo-cena','name: other');self.assertTrue(validate(self.r))
 def test_missing_yaml(self):
  self.change(B/'SKILL.md','---\n','');self.assertTrue(validate(self.r))
 def test_missing_reference(self):
  (self.r/B/'references/preservation.md').unlink();self.assertTrue(validate(self.r))
 def test_missing_english_prompt(self):
  self.change('examples/veranda-complete.md','### Prompt EN 2','### Removed');self.assertTrue(validate(self.r))
 def test_missing_portuguese_prompt(self):
  self.change('examples/veranda-complete.md','### Prompt PT-BR 1','### Removed');self.assertTrue(validate(self.r))
 def test_missing_case(self):
  self.change('tests/acceptance-tests.md','## T18 —','## Removed —');self.assertTrue(validate(self.r))
 def test_missing_source(self):
  (self.r/'docs/SOURCE_SPECIFICATION.md').unlink();self.assertTrue(validate(self.r))
 def test_missing_license(self):
  (self.r/'LICENSE').unlink();self.assertTrue(validate(self.r))
if __name__=='__main__':unittest.main()
