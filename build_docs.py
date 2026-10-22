import json
from pathlib import Path

from fastapi.openapi.docs import get_redoc_html

from main import app

site = Path("site")
site.mkdir(exist_ok=True)
(site / "openapi.json").write_text(json.dumps(app.openapi(), indent=2),
                                   encoding="utf-8")
(site / "index.html").write_bytes(get_redoc_html(openapi_url="openapi.json",
                                                 title=app.title).body)
print("API docs written to site/")