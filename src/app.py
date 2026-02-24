"""
pre.SENT v2 — FastAPI server

Serves the gallery frontend and the session-based generation API.
"""

import os
import logging
import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv

from api.session import start_session, get_era_data
from prompts.eras import get_era_list

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pre_sent")

app = FastAPI(title="pre.SENT", docs_url=None, redoc_url=None)

public_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
app.mount("/static", StaticFiles(directory=public_dir), name="static")


@app.get("/")
async def index():
    return FileResponse(os.path.join(public_dir, "index.html"))


@app.get("/api/eras")
async def eras():
    return JSONResponse(get_era_list())


@app.get("/api/debug")
async def debug_apis():
    """Live check of both API keys. Remove or restrict before public launch."""
    def _test_anthropic():
        try:
            import anthropic
            key = os.getenv("ANTHROPIC_API_KEY")
            if not key:
                return {"status": "error", "error": "ANTHROPIC_API_KEY not set"}
            client = anthropic.Anthropic(api_key=key)
            resp = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=10,
                messages=[{"role": "user", "content": "say ok"}],
            )
            return {"status": "ok", "response": resp.content[0].text.strip()}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as ex:
        anthropic_result = await loop.run_in_executor(ex, _test_anthropic)

    openai_key = os.getenv("OPENAI_API_KEY") or ""
    return JSONResponse({
        "anthropic": anthropic_result,
        "openai_key": "present" if openai_key else "missing",
        "openai_prefix": openai_key[:8] + "..." if openai_key else None,
    })


@app.post("/api/session/start")
async def create_session():
    session_id = await start_session()
    return JSONResponse({"session_id": session_id})


@app.get("/api/session/{session_id}/era/{era_key}")
async def get_era(session_id: str, era_key: str):
    data = get_era_data(session_id, era_key)
    if data is None:
        return JSONResponse({"ready": False})
    return JSONResponse(data)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
