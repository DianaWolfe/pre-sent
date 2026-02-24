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


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
