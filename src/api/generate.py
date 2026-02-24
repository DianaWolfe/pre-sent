"""
gpt-image-1 API integration for pre.SENT.

Handles image generation calls to OpenAI's API.
Returns base64-encoded image data (not URLs) so images
are truly ephemeral and not stored on OpenAI's servers
longer than necessary.
"""

import logging
from openai import OpenAI

logger = logging.getLogger(__name__)


class ImageGenerator:
    """Generates images via gpt-image-1 API."""

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt, size="1024x1024", quality="medium"):
        """
        Generate a single image from a prompt.

        Args:
            prompt: The assembled prompt string
            size: '1024x1024', '1792x1024', or '1024x1792'
            quality: 'low', 'medium', or 'high'

        Returns:
            Dict with 'image_b64' (base64 string) and 'revised_prompt'
            or None on failure
        """
        try:
            response = self.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size=size,
                quality=quality,
                n=1,
            )

            image_data = response.data[0]

            return {
                "image_b64": image_data.b64_json,
                "revised_prompt": None,
            }

        except Exception as e:
            logger.error(f"gpt-image-1 generation failed: {e}")
            return None
