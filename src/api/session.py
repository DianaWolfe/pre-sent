"""
Session-based pre-generation for pre.SENT v2.

When a visitor loads the page, a session is created and all 6 eras
are generated in parallel (images + poems). By the time the gallery
starts (~27s of explainer + breather), content is ready.

Sessions expire after 10 minutes and are cleaned up lazily.
"""

import asyncio
import logging
import os
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

logger = logging.getLogger("pre_sent")

sessions: Dict[str, Any] = {}
_executor = ThreadPoolExecutor(max_workers=12)  # 6 images + 6 poems


async def start_session() -> str:
    """Create a session and kick off parallel generation for all 6 eras."""
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "created_at": datetime.now(),
        "data": {},
    }
    asyncio.create_task(_generate_all(session_id))
    return session_id


def get_era_data(session_id: str, era_key: str) -> Optional[dict]:
    """Return era data if ready, None if session doesn't exist."""
    session = sessions.get(session_id)
    if not session:
        return None
    return session["data"].get(era_key)


async def _generate_all(session_id: str) -> None:
    from prompts.eras import ERAS

    tasks = [_generate_era(session_id, era_key) for era_key in ERAS]
    await asyncio.gather(*tasks, return_exceptions=True)
    _cleanup_sessions()


async def _generate_era(session_id: str, era_key: str) -> None:
    from prompts.eras import ERAS

    era = ERAS[era_key]
    era_position = era["slider_position"]
    loop = asyncio.get_event_loop()

    # Stagger image requests: era 1 at 0s, era 2 at 5s, ... era 6 at 25s.
    # Poems all start immediately (fast); images stagger to avoid rate limits.
    image_delay = (era_position - 1) * 5

    try:
        poem_future = loop.run_in_executor(_executor, _gen_poem, era_key)
        await asyncio.sleep(image_delay)
        image_future = loop.run_in_executor(_executor, _gen_image, era_position)

        # return_exceptions=True so a failed image doesn't discard a good poem
        poem_result, image_result = await asyncio.gather(
            poem_future, image_future, return_exceptions=True
        )

        if isinstance(poem_result, Exception):
            logger.error(f"Session {session_id[:8]} '{era_key}' poem failed: {poem_result}", exc_info=poem_result)
            poem = era.get("bio_poem", "the memory held\nbut the words came out wrong\nsomething was here\nand now it isn't")
        else:
            poem = poem_result

        if isinstance(image_result, Exception):
            logger.error(f"Session {session_id[:8]} '{era_key}' image failed: {image_result}", exc_info=image_result)
            image = None
        else:
            image = image_result

    except Exception as exc:
        logger.error(f"Session {session_id[:8]} '{era_key}' setup failed: {exc}", exc_info=True)
        poem = era.get("bio_poem", "the memory held\nbut the words came out wrong\nsomething was here\nand now it isn't")
        image = None

    if session_id in sessions:
        sessions[session_id]["data"][era_key] = {
            "era_key": era_key,
            "era_label": era["label"],
            "age_range": era["age_range"],
            "poem": poem,
            "image": image,
            "ready": True,
        }
        logger.info(f"Session {session_id[:8]} '{era_key}' ready (image={'yes' if image else 'no'})")


def _gen_poem(era_key: str) -> str:
    from api.poem_gen import generate_poem
    return generate_poem(era_key)


def _gen_image(era_position: int) -> Optional[str]:
    from api.generate import ImageGenerator
    from prompts.assembler import assemble_prompt

    api_key = os.getenv("OPENAI_API_KEY")
    generator = ImageGenerator(api_key=api_key)
    prompt_data = assemble_prompt(era_position)
    result = generator.generate(prompt=prompt_data["prompt"])
    if result and result.get("image_b64"):
        return f"data:image/png;base64,{result['image_b64']}"
    return None


def _cleanup_sessions() -> None:
    cutoff = datetime.now() - timedelta(minutes=10)
    expired = [k for k, v in sessions.items() if v["created_at"] < cutoff]
    for k in expired:
        del sessions[k]
    if expired:
        logger.info(f"Cleaned up {len(expired)} expired session(s)")
