"""
Era definitions for pre.SENT.

Each era represents a developmental period in the artist's life.
The prompt templates encode the emotional and aesthetic DNA of
that period. DALL-E 3 uses these to generate art that feels
autobiographically true to the psychological landscape of each stage.

To fork this for your own gallery, replace these eras with your own.
The system doesn't care how many eras you define or what they contain.
It only needs: key, label, age_range, description, and prompt_template.
"""

import random

ERAS = {
    "wonder": {
        "label": "Wonder",
        "age_range": "Childhood (~0-12)",
        "slider_position": 1,
        "bio_poem": (
            "Born different with a heart full of gold,\n"
            "an army brat in every corner of the world.\n"
            "The only safe place was the one you made yourself,\n"
            "running wild through forests they could never fold."
        ),
        "description": (
            "Animistic thinking. The world is alive and everything means "
            "something. Objects have feelings. Shadows have intentions. "
            "Safety and danger coexist in the same fairy tale."
        ),
        "developmental_frame": "Piaget's preoperational and concrete operational stages. Erikson's industry vs. inferiority.",
        "color_palette": ["cobalt blue", "cream white", "soft pink wash", "ink black", "sage green"],
        "art_references": ["Japanese ink illustration", "whimsical pen and ink", "elegant line drawing", "botanical illustration meets fairy tale", "multimedia sketchbook art"],
        "emotional_texture": "safe danger, enchantment, curiosity, animism, secret worlds, precocious precision",
        "subjects": [
            "an elaborate bouquet of flowers erupting from stylized clouds, petals scattering like confetti",
            "a single feather with intricate barb detail resting inside a geometric shape",
            "a tree that is also a map, with branches becoming rivers and leaves becoming countries",
            "a field of wildflowers drawn with obsessive botanical detail where tiny creatures hide",
            "a bird with impossibly elegant tail feathers perched on a stack of old books",
            "a glass jar filled with fireflies sitting on a windowsill with rain outside",
            "a compass rose made of flowers and vines with a small animal at the center",
            "an old suitcase open to reveal an entire miniature world growing inside it",
        ],
        "prompt_template": (
            "Clean pen and ink illustration with a multimedia quality. "
            "The style is cartoonish but elegant, precise and whimsical, "
            "like a gifted child drawing with adult-level control. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Fine detailed linework on white or cream paper. "
            "Some areas left as pure ink, others with delicate watercolor wash. "
            "The drawing should feel both innocent and strangely sophisticated. "
            "No text. "
            "Aspect ratio 1:1. Style: natural."
        ),
        "moods": [
            "enchanted and safe, like the moment before a bedtime story",
            "curious and alive, as if the world is holding its breath",
            "golden and warm, the way summer afternoons felt when they lasted forever",
            "quietly mysterious, a secret that only children can see",
        ],
    },

    "becoming": {
        "label": "Becoming",
        "age_range": "Adolescence (~13-17)",
        "slider_position": 2,
        "bio_poem": (
            "Anger always had a place to go, but intellect had none.\n"
            "The small world is too small. Spread your wings.\n"
            "Stop and start the performances that will never bring you peace.\n"
            "Be brave enough to heal, and the world is yours."
        ),
        "description": (
            "Identity formation. Everything is intense, everything matters, "
            "nothing is settled. The self is under construction and the "
            "scaffolding is visible."
        ),
        "developmental_frame": "Erikson's identity vs. role confusion. Marcia's identity statuses.",
        "color_palette": ["crimson magenta", "burnt gold", "ultramarine blue", "emerald green", "deep violet"],
        "art_references": ["thick impasto acrylic", "palette knife painting", "expressive color field", "figurative charcoal study", "raw textural painting"],
        "emotional_texture": "intensity, longing, self-consciousness, defiance, raw beauty, thick emotion",
        "subjects": [
            "a mass of flowers rendered in violent impasto, petals built up in thick ridges of crimson and magenta",
            "a figure study in charcoal with wild flowing hair, the body twisting with energy",
            "a landscape where the sky is built from aggressive palette knife strokes of gold and red",
            "hands covered in paint reaching upward, rendered in heavy acrylic texture",
            "a bouquet that is more texture than form, paint so thick it casts shadows",
            "a stormy seascape in thick acrylic where the waves are sculpted from the paint itself",
            "a single rose rendered so thickly the petals seem to peel off the canvas",
            "an abstract explosion of color against a gray field, like emotion breaking through",
        ],
        "prompt_template": (
            "Thick impasto acrylic painting with heavy palette knife texture. "
            "The paint should look three-dimensional, built up in ridges and layers. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Aggressive, physical brushwork. Paint applied so thickly you can "
            "feel the emotion in the texture. Bold, saturated color. "
            "The painting should feel like it was made by someone who is "
            "learning their own power and cannot contain it. "
            "Visible canvas texture beneath heavy paint. "
            "No text. "
            "Aspect ratio 1:1. Style: vivid."
        ),
        "moods": [
            "fierce and tender at the same time, like a bruise that is also beautiful",
            "storm-lit and urgent, the way everything feels at sixteen",
            "lonely in a way that is also defiant, chosen solitude",
            "electric and unstable, the moment before something changes forever",
        ],
    },

    "proving": {
        "label": "The Proving Years",
        "age_range": "Early Adulthood (~18-29)",
        "slider_position": 3,
        "bio_poem": (
            "Ups and downs and turn arounds,\n"
            "two steps forward and one step back.\n"
            "Everything looks perfect from the outside.\n"
            "You are building the courage to finally take flight."
        ),
        "description": (
            "The construction of a stable base. Raising siblings, "
            "losing yourself to a marriage that was too easy. "
            "The architecture of a life that looks right from the outside "
            "while you gather the strength to become."
        ),
        "developmental_frame": "Erikson's intimacy vs. isolation. Levinson's early adult transition.",
        "color_palette": ["deep cobalt blue", "rose pink", "warm skin tones", "charcoal gray", "magnolia cream"],
        "art_references": ["realistic acrylic painting", "figurative acrylic portraiture", "abstract structural composition", "diptych painting", "classical acrylic with modern edge"],
        "emotional_texture": "ambition, mastery, controlled surfaces, beginning to abstract, the body as subject",
        "subjects": [
            "a dancer mid-leap between two canvases, one deep blue with magnolias, the other washed in pink",
            "a self-portrait where the face dissolves into abstract brushstrokes at the edges",
            "a figure arched backward with hair cascading, rendered in masterful gray tones with one splash of gold",
            "a lighthouse at sunset painted with confident realistic technique, golden sky ablaze",
            "a still life where half is photorealistic and half dissolves into geometric abstraction",
            "hands clasped together rendered in precise acrylic realism against an abstract color field",
            "a figure in white fabric caught mid-motion against a deep cobalt background with floating petals",
            "an architectural structure painted precisely that begins to fracture into abstract planes of color",
        ],
        "prompt_template": (
            "Acrylic painting demonstrating technical mastery. "
            "The style moves between photorealistic figurative work and "
            "abstract structural composition. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Confident brushwork, rich color depth, professional-level "
            "acrylic technique. The painting should feel like someone "
            "who has mastered realism and is beginning to push beyond it. "
            "Both control and release visible in the same piece. "
            "No text. "
            "Aspect ratio 1:1. Style: natural."
        ),
        "moods": [
            "polished and aspirational, the surface of a life under construction",
            "controlled and elegant but with a single detail that doesn't belong",
            "impressive and slightly hollow, like an architect's rendering before anyone moves in",
            "ambitious and precise, the way things look when you are trying very hard",
        ],
    },

    "unraveling": {
        "label": "The Unraveling",
        "age_range": "Crisis (~30)",
        "slider_position": 4,
        "bio_poem": (
            "There was a time you let yourself love and believe.\n"
            "You have been alone before. You will be again.\n"
            "Can you make it out alive?\n"
            "You are never going to be the same, again and again and again."
        ),
        "description": (
            "The collapse of constructed identity. Grief, disillusionment, "
            "the discovery that the architecture you built cannot hold. "
            "Everything you thought was permanent turns out to be contingent."
        ),
        "developmental_frame": "Kübler-Ross grief model. Existential crisis (Yalom). Identity deconstruction.",
        "color_palette": ["ink black", "stark white", "violent red", "pale blue wash", "graphite gray"],
        "art_references": ["bold ink illustration", "pen and ink with red accent", "raw illustrative style", "graphic novel aesthetic", "figure drawing meets punk art"],
        "emotional_texture": "fragmentation, grief, disillusionment, raw honesty, the body splitting open, survival as art",
        "subjects": [
            "a figure split down the middle, half flesh half skeleton, smoke curling from the split",
            "two bodies connected by a single red thread, one pulling away into void while the other dissolves",
            "a woman drawn in bold black ink with violent red slashes crossing her body like wounds or wings",
            "a figure suspended by strings like a marionette, some strings already cut, floating",
            "a self-portrait where the face is screaming with eyes closed, repeated text filling the background",
            "a figure arching backward with a camera or mechanical object fused to her body, red light radiating",
            "hands reaching for each other across white space, a red line tangling between them",
            "a body curled into itself, drawn in confident single-weight ink line, hair spreading like roots",
        ],
        "prompt_template": (
            "Bold pen and ink illustration on white paper with a raw, "
            "personal illustrative style. Black ink linework with "
            "occasional violent red ink accents as the only color. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Confident flowing linework, bodies drawn with anatomical "
            "knowledge but stylized with emotion. The red is used "
            "sparingly but powerfully, like blood or a thread or a wound. "
            "The illustration should feel like pages torn from someone's "
            "most honest sketchbook. Vulnerable, unflinching, beautiful. "
            "White space used deliberately. "
            "Aspect ratio 1:1. Style: natural."
        ),
        "moods": [
            "grief that has moved past the sharp phase into the hollow one",
            "stripped bare and strangely calm, the exhaustion after the storm",
            "fractured but honest, the first time you see clearly because the performance stopped",
            "desolate and luminous, the way empty rooms catch light they never caught when full",
        ],
    },

    "reconstruction": {
        "label": "The Reconstruction",
        "age_range": "Rebuilding (~31-37)",
        "slider_position": 5,
        "bio_poem": (
            "There are no more boundaries.\n"
            "You will launch from newfound footing.\n"
            "Mind, heart, body, all aligned.\n"
            "Movement, grace, and hope, all together."
        ),
        "description": (
            "Post-traumatic growth. The broken pieces are not discarded "
            "but rearranged into something stronger. Gold in the cracks. "
            "The self that emerges is more complex and more honest than "
            "the one that shattered."
        ),
        "developmental_frame": "Erikson's generativity vs. stagnation. Tedeschi & Calhoun's post-traumatic growth. Kintsugi as psychological metaphor.",
        "color_palette": ["muted blue-gray", "rust red accent", "warm cream", "slate charcoal", "gold leaf"],
        "art_references": ["elegant watercolor illustration", "muted palette narrative illustration", "Japanese-influenced contemporary illustration", "atmospheric figure and animal composition", "sophisticated mixed media"],
        "emotional_texture": "integration, earned warmth, grounded strength, tender fierceness, growth through rupture, the pack",
        "subjects": [
            "a woman in profile surrounded by wolves, all facing the same direction, autumn leaves drifting",
            "a figure walking through birch trees with two large dogs flanking her like guardians",
            "hands shaping clay on a wheel, rendered in soft muted tones with gold leaf accents",
            "a garden reclaiming an old stone wall, painted in sophisticated muted watercolor",
            "a woman's silhouette filled with a landscape of mountains and running water",
            "a table set for friends with wildflowers and candlelight, painted in warm restrained tones",
            "a wolf and a woman sleeping back to back, rendered in soft gray-blue wash with red leaf accents",
            "a window box garden in full bloom on a weathered building, elegant muted palette",
        ],
        "prompt_template": (
            "Elegant illustration in a sophisticated mixed media style "
            "combining muted watercolor, ink, and subtle gold accents. "
            "The aesthetic is mature, restrained, and narrative. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Muted blue-gray tones with selective warm accents of rust red "
            "or gold. Compositional sophistication with layered elements. "
            "The illustration should feel like the work of someone who has "
            "passed through fire and come out with a quieter, more powerful "
            "visual voice. Controlled, atmospheric, deeply felt but never loud. "
            "No text. "
            "Aspect ratio 1:1. Style: natural."
        ),
        "moods": [
            "grounded and tender, the strength that comes after you stop performing",
            "warm and complex, like a room that has been lived in by someone who finally likes living there",
            "quietly fierce, the calm confidence of someone who rebuilt from nothing",
            "generous and rooted, growth that knows its own soil",
        ],
    },

    "reclamation": {
        "label": "The Reclamation",
        "age_range": "Now",
        "slider_position": 6,
        "bio_poem": (
            "You built the table. You chose who sits there.\n"
            "The dogs at your feet, the ring on your hand, the work that is yours.\n"
            "Sovereignty is quiet. It does not perform.\n"
            "You are finally the author of every room you walk into."
        ),
        "description": (
            "Self-authorship. Sovereignty. The dark sublime. "
            "You are no longer constructing an identity for anyone else. "
            "The aesthetic is yours: classical, mystical, warm but not soft, "
            "earned through every era that came before."
        ),
        "developmental_frame": "Kegan's Stage 5 (self-transforming mind). Jung's individuation. Self-authorship.",
        "color_palette": ["deep sage", "umber", "midnight blue", "antique gold", "candlelight warm"],
        "art_references": ["mature illustrative acrylic", "dark academia illustration", "elegant narrative painting", "classical meets contemporary illustration", "sophisticated acrylic with occult undertones"],
        "emotional_texture": "sovereignty, dark sublime, mystical knowing, earned complexity, warm authority, the collector",
        "subjects": [
            "a library at midnight with candles and curiosities, painted in rich dark acrylics with illustrative precision",
            "a woman's figure silhouetted in a doorway of a Tudor house, wolves waiting in the garden",
            "a piano room at golden hour with art ascending the stairwell walls, painted in elegant acrylic",
            "a study filled with skulls, globes, dried botanicals, and an animatronic head under construction",
            "a lighthouse on a rocky coast rendered in mature acrylic style, dark and luminous",
            "a gallery wall of collected paintings arranged in a salon hang, candlelit, deeply atmospheric",
            "a figure at a desk writing by lamplight surrounded by research and robots and dogs sleeping nearby",
            "a moonlit garden with German Shepherds standing guard among old roses and iron gates",
        ],
        "prompt_template": (
            "Mature acrylic painting with an elegant illustrative quality. "
            "Dark academia aesthetic meets classical romantic painting. "
            "{subject} "
            "Color palette dominated by {color}. "
            "The mood is {mood}. "
            "Rich dark tones with warm candlelit accents. The acrylic technique "
            "is masterful but retains an illustrative sensibility, narrative "
            "and atmospheric rather than purely realistic. "
            "The painting should feel like the work of someone who has collected "
            "a life worth looking at and knows exactly how to render it. "
            "Timeless, elegant, secretive, earned. "
            "No text. "
            "Aspect ratio 1:1. Style: vivid."
        ),
        "moods": [
            "sovereign and mystical, the calm of someone who chose every object in the room",
            "dark and luminous, like candlelight on old wood and gold frames",
            "timeless and knowing, the feeling of a house that holds secrets it is not ashamed of",
            "warm but not soft, the authority of someone who earned their quiet",
        ],
    },
}


def get_era_by_position(position):
    """Get era config by slider position (1-6)."""
    for key, era in ERAS.items():
        if era["slider_position"] == position:
            return key, era
    return "reclamation", ERAS["reclamation"]


def get_era_list():
    """Return eras in slider order for the frontend."""
    return sorted(
        [{"key": k, **{f: v[f] for f in ["label", "age_range", "slider_position", "description", "bio_poem"]}}
         for k, v in ERAS.items()],
        key=lambda x: x["slider_position"]
    )
