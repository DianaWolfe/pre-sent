"""
Claude API poem generation for pre.SENT v2.

Generates a unique 4-line memory poem for each era using the
Anthropic Claude API. Every call produces a different poem.
"""

import os
import anthropic
from prompts.poem_seeds import ERA_SEEDS, POEM_SYSTEM_PROMPT


def generate_poem(era_key: str) -> str:
    """
    Generate a 4-line memory poem for the given era.

    Args:
        era_key: Era identifier (wonder, becoming, proving, etc.)

    Returns:
        4-line poem as a newline-separated string.
    """
    seed = ERA_SEEDS.get(era_key)
    if not seed:
        return "the memory failed\nsomething that was\ncouldn't hold its shape\nbut the feeling remained"

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=150,
        temperature=1.0,
        system=POEM_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": seed["prompt"]}],
    )

    return response.content[0].text.strip()
