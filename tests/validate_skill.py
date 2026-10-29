from pathlib import Path
import re,sys,yaml
B=Path('.agents/skills/corpo-cena')
def validate(root):
 root=Path(root);errors=[]
 for p in ('README.md','LICENSE','CHANGELOG.md','docs/SOURCE_SPECIFICATION.md','docs/AUDIT.md','tests/acceptance-tests.md','examples/veranda-complete.md','.github/workflows/validate.yml',str(B/'SKILL.md')):
  if not (root/p).is_file() or not (root/p).read_text().strip():errors.append('missing '+p)
 if errors:return errors
 text=(root/B/'SKILL.md').read_text()
 try:
  assert text.startswith('---\n');d=yaml.safe_load(text.split('---',2)[1]);assert d['name']=='corpo-cena' and isinstance(d['description'],str) and len(d['description'])>40
 except Exception:errors.append('invalid metadata')
 for t in ('seis prompts','não inserir automaticamente','Não gere imagens diretamente'):
  # Original source has a different imperative casing for this rule.
  if t.lower() not in text.lower():errors.append('missing rule '+t)
 for p in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' not in link and not link.startswith('#'):
    target=(p.parent/link.split('#')[0]).resolve()
    if not target.is_relative_to(root.resolve()) or not target.exists():errors.append('bad link '+link)
 example=(root/'examples/veranda-complete.md').read_text()
 for lang in ('PT-BR','EN'):
  blocks=re.findall(r'### Prompt '+lang+r' ([123])\n(.+?)(?=\n##|\Z)',example,re.S)
  if [n for n,t in blocks]!=['1','2','3']:errors.append('missing complete prompt '+lang)
  for n,t in blocks:
   if len(t.strip())<500 or ('Preserve' not in t):errors.append('incomplete preservation prompt')
 for i in range(1,19):
  if f'## T{i:02d} —' not in (root/'tests/acceptance-tests.md').read_text():errors.append('missing case')
 return errors
if __name__=='__main__':
 e=validate(Path(__file__).resolve().parents[1]);print('\n'.join(e) if e else 'PASS: package, YAML, links and six complete example prompts');sys.exit(bool(e))
