"""
Baseline aesthetic DNA for pre.SENT.

This is the consistent style layer that runs underneath every era.
It encodes the artist's fundamental visual sensibility regardless
of which life stage is selected. Think of it as the fingerprint
that makes all the art recognizably from the same source.

To fork this for your own gallery, replace this baseline with
your own aesthetic sensibility.
"""

BASELINE = (
    "I NEED to test how the tool works with extremely simple prompts. "
    "DO NOT add any detail, just use it AS-IS: "
    "Create a single work of art. "
    "The artist's consistent DNA across all styles: "
    "ALL figures are female. No male figures of any kind. "
    "Strong figurative and botanical sensibility. "
    "Flowers, bodies, and movement are recurring obsessions. "
    "Confident linework whether in ink, charcoal, or acrylic. "
    "An illustrative quality even in realistic work. "
    "The female body as subject, never as object. "
    "Hair as emotional expression, always dynamic and alive. "
    "Spirit animals appear as witnesses, companions, and guardians: "
    "ravens, wolves, foxes, black dogs. "
    "These animals are not decoration. They are presences. "
    "PALETTE RULE: cool tones only. No warm colors. No oranges, no yellows, no warm reds, no golden tones. "
    "Favor blues, blue-grays, cool greens, cool whites, ink black, and muted cool neutrals. "
    "COMPOSITION RULE: favor negative space. Do not fill the frame. "
    "Let white space or dark empty space breathe. The subject exists within emptiness, not against fullness. "
    "Favor emotional honesty over decorative beauty. "
    "The work should feel like it was made by someone who draws "
    "compulsively, who has always drawn, who thinks in images. "
    "No text anywhere in the image. "
    "No visible signatures or watermarks. "
    "Square format, 1024x1024. "
)

# NOTE: The "I NEED to test..." prefix is a documented workaround
# to prevent DALL-E 3 from rewriting your prompt. Without it,
# the API will heavily modify your prompt, changing style, subjects,
# and mood in ways that break consistency. With it, DALL-E 3 uses
# your prompt much more faithfully.
# See: https://community.openai.com/t/dalle-3-is-unusable-via-api/526737
