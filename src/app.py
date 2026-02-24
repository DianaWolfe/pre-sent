"""
pre.SENT - FastAPI server

Serves the gallery frontend and handles image generation requests.
"""

import os
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv

from api.generate import ImageGenerator
from api.session import start_session, get_era_data
from prompts.assembler import assemble_prompt
from prompts.eras import get_era_list
from gallery.rate_limiter import RateLimiter

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pre_sent")

app = FastAPI(title="pre.SENT", docs_url=None, redoc_url=None)

# Initialize components
generator = ImageGenerator(api_key=os.getenv("OPENAI_API_KEY"))
limiter = RateLimiter(
    min_interval=int(os.getenv("MIN_INTERVAL", "15")),
    max_per_hour=int(os.getenv("MAX_PER_HOUR", "30")),
    global_max_per_hour=int(os.getenv("GLOBAL_MAX_PER_HOUR", "200")),
)

# Serve static files
public_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
app.mount("/static", StaticFiles(directory=public_dir), name="static")


@app.get("/")
async def index():
    """Serve the gallery page."""
    return FileResponse(os.path.join(public_dir, "index.html"))


@app.get("/api/eras")
async def eras():
    """Return the list of available eras for the frontend slider."""
    return JSONResponse(get_era_list())


@app.post("/api/generate")
async def generate(request: Request):
    """
    Generate a new artwork for the given era.

    Expects JSON body: {"era": 1-6}
    Returns JSON: {"image": "data:image/png;base64,...", "era": {...}}
    """
    client_ip = request.client.host
    body = await request.json()
    era_position = body.get("era", 6)

    if not isinstance(era_position, int) or era_position < 1 or era_position > 6:
        raise HTTPException(400, "Era must be an integer 1-6")

    # Rate limit check
    allowed, wait, reason = limiter.check(client_ip)
    if not allowed:
        return JSONResponse(
            {"error": reason, "wait": wait},
            status_code=429,
        )

    # Assemble prompt
    prompt_data = assemble_prompt(era_position)
    logger.info(f"Generating for era '{prompt_data['era_label']}' (client: {client_ip})")

    # Generate image
    result = generator.generate(
        prompt=prompt_data["prompt"],
    )

    if result is None:
        raise HTTPException(500, "Generation failed. Please try again.")

    # Record successful generation
    limiter.record(client_ip)

    return JSONResponse({
        "image": f"data:image/png;base64,{result['image_b64']}",
        "era": {
            "key": prompt_data["era_key"],
            "label": prompt_data["era_label"],
            "description": prompt_data["era_description"],
        },
    })


@app.get("/api/debug")
async def debug_apis():
    """Check both API keys and test the Anthropic connection."""
    import asyncio as _aio
    from concurrent.futures import ThreadPoolExecutor as _TPE

    def _test_anthropic():
        try:
            import anthropic
            key = os.getenv("ANTHROPIC_API_KEY")
            if not key:
                return {"status": "error", "error": "ANTHROPIC_API_KEY not set"}
            client = anthropic.Anthropic(api_key=key)
            resp = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=10,
                messages=[{"role": "user", "content": "say ok"}],
            )
            return {"status": "ok", "response": resp.content[0].text.strip()}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    loop = _aio.get_running_loop()
    with _TPE() as ex:
        anthropic_result = await loop.run_in_executor(ex, _test_anthropic)

    openai_key = os.getenv("OPENAI_API_KEY") or ""
    return JSONResponse({
        "anthropic": anthropic_result,
        "openai_key": "present" if openai_key else "missing",
        "openai_prefix": openai_key[:8] + "..." if openai_key else None,
    })


@app.post("/api/session/start")
async def create_session():
    """Start a new session and kick off parallel generation for all 6 eras."""
    session_id = await start_session()
    return JSONResponse({"session_id": session_id})


@app.get("/api/session/{session_id}/era/{era_key}")
async def get_era(session_id: str, era_key: str):
    """Return pre-generated era content (poem + image) once ready."""
    data = get_era_data(session_id, era_key)
    if data is None:
        return JSONResponse({"ready": False})
    return JSONResponse(data)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
