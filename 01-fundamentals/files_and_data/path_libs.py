import json
from pathlib import Path

path = Path("data") / "resuts.json"
path.parent.mkdir(exist_ok=True)

path.write_text(json.dumps({"model": "claude", "tokens": 512}, indent=2), encoding="utf-8" )

data = json.loads(path.read_text(encoding="utf-8"))
print (data["tokens"])
