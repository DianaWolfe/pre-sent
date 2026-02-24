"""
Prompt assembler for pre.SENT.

Combines era-specific prompt templates with randomized elements
to ensure every generation is unique while staying within the
aesthetic boundaries of each life stage.

The assembly process:
1. Select the era's prompt template
2. Choose a random subject from the era's subject pool
3. Choose a random color emphasis from the era's palette
4. Choose a random mood from the era's mood pool
5. Prepend the baseline aesthetic layer
6. Return the assembled prompt for gpt-image-1
"""

import random
from .eras import ERAS, get_era_by_position
from .baseline import BASELINE

COMPOSITION_MODIFIERS = [
    "Close-up detail, cropped tight.",
    "Wide shot, full scene with negative space.",
    "Overhead view, looking down.",
    "Side profile composition, strong diagonal.",
    "Centered symmetrical composition.",
    "Off-center subject, rule of thirds.",
    "Extreme close-up on texture and surface.",
    "Medium distance, environmental context visible.",
]


def assemble_prompt(era_position):
    """
    Build a complete DALL-E 3 prompt for a given era.

    Args:
        era_position: Integer 1-6 from the slider

    Returns:
        Dict with 'prompt', 'era_key', 'era_label' for the API call
    """
    era_key, era = get_era_by_position(era_position)

    subject = random.choice(era["subjects"])
    color = random.choice(era["color_palette"])
    mood = random.choice(era["moods"])
    composition = random.choice(COMPOSITION_MODIFIERS)

    era_prompt = era["prompt_template"].format(
        subject=subject,
        color=color,
        mood=mood,
    )

    # Prepend baseline aesthetic DNA; append composition modifier for variety
    full_prompt = f"{BASELINE} {era_prompt} {composition}"

    # DALL-E 3 has a prompt length limit (~4000 chars)
    if len(full_prompt) > 3900:
        full_prompt = full_prompt[:3900]

    return {
        "prompt": full_prompt,
        "era_key": era_key,
        "era_label": era["label"],
        "era_description": era["description"],
    }
