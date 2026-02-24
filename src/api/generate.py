"""
DALL-E 3 API integration for pre.SENT.

Handles image generation calls to OpenAI's API.
Returns base64-encoded image data (not URLs) so images
are truly ephemeral and not stored on OpenAI's servers
longer than necessary.
"""

import logging
from openai import OpenAI

logger = logging.getLogger(__name__)


class ImageGenerator:
    """Generates images via DALL-E 3 API."""

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt, style="natural", size="1024x1024", quality="standard"):
        """
        Generate a single image from a prompt.

        Args:
            prompt: The assembled prompt string
            style: 'natural' or 'vivid'
            size: '1024x1024', '1792x1024', or '1024x1792'
            quality: 'standard' ($0.04) or 'hd' ($0.08)

        Returns:
            Dict with 'image_b64' (base64 string) and 'revised_prompt'
            or None on failure
        """
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                style=style,
                n=1,
                response_format="b64_json",
            )

            image_data = response.data[0]

            return {
                "image_b64": image_data.b64_json,
                "revised_prompt": image_data.revised_prompt,
            }

        except Exception as e:
            logger.error(f"DALL-E 3 generation failed: {e}")
            return None
