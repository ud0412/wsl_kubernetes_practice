from pathlib import Path
import re
import sys
import yaml
root=Path(__file__).resolve().parents[1]
errors=[]
for file in [root / "README.md", * (root / "Guide").rglob("*.md")]:
    text=file.read_text(encoding="utf-8")
    if len(re.findall(r"^```", text, re.M)) % 2: errors.append(str(file)+": fence")
    for target in re.findall(r"\]\(([^)]+)\)",text):
        if target.startswith(("https:","http:","#")): continue
        if not (file.parent / target.split("#")[0]).exists(): errors.append(str(file)+": "+target)
for file in (root / "infrastructure").rglob("*.yaml"): list(yaml.safe_load_all(file.read_text()))
assert ".github_key" in (root / ".gitignore").read_text()
assert "Plan.md" in (root / ".gitignore").read_text()
if errors: sys.exit("\n".join(errors))
print("Foundation source and guide checks passed")
