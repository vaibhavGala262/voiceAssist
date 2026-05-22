import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Sanskar Voice Bot")
HERE = Path(__file__).parent

@app.get("/", response_class=HTMLResponse)
def index():
    html_path = HERE / "voicebot.html"
    if not html_path.exists():
        return HTMLResponse("<h1>voicebot.html not found</h1>", status_code=404)
    return HTMLResponse(html_path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"\n  >>> Open http://localhost:{port} in Chrome <<<\n")
    uvicorn.run(app, host="127.0.0.1", port=port)
