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

# Atmospheric seed phrases — one is injected per generation to push
# variety even when the same subject/color/mood combination is drawn.
ATMOSPHERE = [
    "late afternoon light filtering through",
    "early morning, before anyone is awake",
    "deep winter stillness",
    "the moment just after",
    "the moment just before",
    "suspended mid-breath",
    "overcast and diffuse light",
    "a single strong light source from one side",
    "lit from below",
    "viewed from very close",
    "viewed from a distance",
    "the subject barely visible in shadow",
    "harsh midday light, no softness",
    "fog or haze at the edges",
    "the quality of light after rain",
    "candlelight from off-frame",
    "the composition weighted to the left",
    "the composition weighted to the right",
    "the subject in the lower third only",
    "vast empty space above the subject",
    "the subject pressed to one edge",
    "dense and layered, no empty space",
    "sparse — more white than anything else",
    "the subject partially cut off by the frame",
    "two elements in tension with each other",
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
    atmosphere = random.choice(ATMOSPHERE)

    era_prompt = era["prompt_template"].format(
        subject=subject,
        color=color,
        mood=mood,
    )

    # Prepend baseline aesthetic DNA; append atmospheric seed for variety
    full_prompt = f"{BASELINE} {era_prompt} Atmospheric quality: {atmosphere}."

    # DALL-E 3 has a prompt length limit (~4000 chars)
    if len(full_prompt) > 3900:
        full_prompt = full_prompt[:3900]

    return {
        "prompt": full_prompt,
        "era_key": era_key,
        "era_label": era["label"],
        "era_description": era["description"],
    }
