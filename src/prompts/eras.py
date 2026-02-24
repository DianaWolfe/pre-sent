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
            "Cartoonish, impressionist, and sarcastic before she had words "
            "for any of it. Drawing was the world she controlled. "
            "The humor was armor. The art was the only room with a lock."
        ),
        "developmental_frame": "Piaget's preoperational and concrete operational stages. Erikson's industry vs. inferiority.",
        "color_palette": ["clashing primaries red, yellow, electric blue", "muddy forest greens and dirty browns", "faded crayola palette gone slightly wrong", "loud orange against crayon-box purple", "cadmium yellow and cobalt blue fighting each other"],
        "art_references": ["precocious child drawing with impressionist color thrown in the background", "naive art that knows what it is doing", "flat cartoon figures in front of loosely gestural impressionist environments", "outsider art energy with interior intelligence", "wobbly confident lines over loose paint blobs"],
        "emotional_texture": "sarcasm housed in a too-small body, wry observation of adults who think she is not watching, cartoon logic applied to genuinely strange circumstances, humor as private language, the child who already knows the joke",
        "subjects": [
            "a flat cartoon girl with an oversized head and a deadpan expression standing alone in a loosely impressionist forest, trees rendered in quick dabs of green and shadow around her flat outlined form",
            "a child's cartoon self-portrait with exaggerated eyes and a knowing smirk, the background a loose impressionist smear of a military base housing block in grays and browns",
            "a cartoon rendering of a moving van loaded with furniture, the child figure sitting on top of it looking unbothered, background impressionistically blurred into highway and sky",
            "a flat cartoonish girl reading a giant book in the middle of impressionist chaos adults rendered as smeared color blobs arguing in the background",
            "a small cartoon figure standing in an impressionistically painted forest, light coming through the trees in loose dabs of gold and green, the child's expression entirely self-contained",
            "a child's cartoon drawing of a classroom where every figure is forward-facing and identical except one, turned away, the background loosely painted in institutional yellow-green",
            "a naive cartoon drawing of a small girl and a very large dog, the dog painted impressionistically in warm ochre strokes, the girl flat and outlined with a deadpan face",
            "a cartoonish figure sitting on a packed suitcase in an airport, surrounding crowds painted in swift impressionist strokes of movement and color, the child perfectly still and unimpressed",
        ],
        "prompt_template": (
            "A hybrid of child's cartoon drawing and impressionist painting. "
            "The figures are drawn with flat, simplified outlines wobbly and confident at once, "
            "the line quality of someone who draws compulsively and has strong opinions. "
            "Faces have a deadpan, knowing quality: slightly too-adult expressions in a child's body. "
            "The backgrounds and environments are handled in loose impressionist paint "
            "quick dabs, gestural strokes, no clean edges, light broken into color. "
            "The tension between the flat cartoon figure and the painterly world around it "
            "is the structural point of the image. "
            "{subject} "
            "Color palette: {color}. Colors don't quite harmonize that dissonance is intentional. "
            "The mood: {mood}. "
            "Cartoon logic governs the figures. Impressionist instinct governs everything else. "
            "The image should feel like a precocious kid who has been to too many places "
            "and learned to observe everything from a slight ironic distance. "
            "No text anywhere in the image. Square format. Style: natural."
        ),
        "moods": [
            "deadpan and privately amused, the expression of a child who has already figured out the adults in the room",
            "wry and watchful, humor used as a portable shelter you carry from base to base",
            "sarcastic but not mean the kind of funny that comes from being the new kid seventeen times",
            "irreverent and self-contained, a small person with an enormous interior life and a straight face",
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
            "She picked up a brush and pointed it at her own face. "
            "The self-portrait as act of self-determination. "
            "Naturalistic, observational, unsparing. The canvas was where "
            "she got to decide what she looked like."
        ),
        "developmental_frame": "Erikson's identity vs. role confusion. Marcia's identity statuses.",
        "color_palette": ["cool gray-green flesh tones over a warm umber underpainting", "raw sienna shadows and titanium white highlights", "deep burnt umber in the darks, pale yellow ochre in the lights", "muted warm neutrals with one saturated note breaking through", "gray-blue in the shadows, cream in the high planes of the face"],
        "art_references": ["naturalistic acrylic portrait painted from the mirror", "observational life painting in acrylic on canvas", "careful realist self-portraiture with visible brushwork", "academic portrait study made personal", "acrylic on canvas with layered skin tones and honest asymmetry"],
        "emotional_texture": "the face as first serious subject, learning to look at yourself without flinching, the practice of being seen on your own terms, quiet intensity in the act of making your own image, controlled mastery over something the world cannot take away",
        "subjects": [
            "a naturalistic acrylic self-portrait of a young woman, three-quarter view, direct gaze that holds the viewer without aggression, skin tones built in cool gray-green layers over a warm ground",
            "a close-up acrylic portrait study of a teenage girl, face occupying most of the canvas, hair painted in long dark sweeping strokes, the face slightly asymmetrical and honest",
            "a self-portrait lit from a single window source one side of the face in warm highlight, the other in cool gray shadow, painted with quiet observational precision in acrylic",
            "an acrylic portrait in profile, strong jawline, hair loose, the sitter looking away, painted with the kind of control that comes from drawing the same face hundreds of times",
            "a naturalistic acrylic figure study from the waist up, one hand resting near the chin, the posture of someone sitting for their own portrait with careful attention",
            "a self-portrait where the eyes are looking slightly downward, painted in careful acrylic layers, skin tones mixing warm and cool in the way real skin does, nothing dramatized",
            "an acrylic portrait where the subject looks directly back at the viewer, expressionless in the way of serious self-study, dark hair against a neutral warm-gray background",
            "a mirror reflection self-portrait in acrylic the figure slightly different from the expected reflection, painted with naturalistic light and honest attention to what looking at yourself actually shows",
        ],
        "prompt_template": (
            "Naturalistic acrylic portrait on canvas, painted from direct observation "
            "from the mirror, from life, from the kind of looking that is also a form of argument. "
            "The technique is careful and layered: a warm umber ground visible in places, "
            "cool gray-green flesh tones built over it, highlights in pale ochre or cream. "
            "Brushwork is visible but controlled the marks show the work of looking, "
            "not expressive abandon. The paint is opaque where it needs to be, "
            "thinner and more transparent in the shadows. "
            "Canvas texture shows through in the mid-tones. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "Single natural light source. Shadows honest, not dramatized. "
            "The painting is an act of self-study the artist using the canvas "
            "to negotiate with her own image, to decide what she looks like. "
            "Nothing idealized, nothing distorted. The face holds its own gaze. "
            "No text anywhere in the image. Square format. Style: natural."
        ),
        "moods": [
            "self-conscious and steady at the same time the look of someone who has decided to stop looking away",
            "concentrated and frank, the face of a teenager who has been painting herself for years and knows exactly what she is doing",
            "guarded but present, honest about what the mirror shows without performing vulnerability",
            "searching and still the quiet intensity of someone using paint to figure out who she is before the world decides for her",
        ],
    },

    "proving": {
        "label": "Proving Years",
        "age_range": "Early Adulthood (~18-29)",
        "slider_position": 3,
        "bio_poem": (
            "Ups and downs and turn arounds,\n"
            "two steps forward and one step back.\n"
            "Everything looks perfect from the outside.\n"
            "You are building the courage to finally take flight."
        ),
        "description": (
            "The paintings get bigger. The palette gets more ambitious. "
            "Figures and botanicals share the canvas the self and the natural world "
            "in conversation. Everything looks composed from the outside. "
            "Inside, the courage to become is still accumulating."
        ),
        "developmental_frame": "Erikson's intimacy vs. isolation. Levinson's early adult transition.",
        "color_palette": ["deep ultramarine and cobalt blue dominating the canvas", "white and cream magnolia petals against the blue", "warm rose and flesh tones emerging from the lower composition", "rich cool blue with one warm figure breaking the field", "prussian blue background with soft botanical whites floating through it"],
        "art_references": ["ambitious acrylic on canvas combining figurative and botanical elements", "large-scale acrylic with confident broad strokes and floating botanical forms", "figurative painting where the figure and flowers share equal weight", "acrylic technique showing mastery of color field and form simultaneously", "bold compositional acrylic where the background is as important as the subject"],
        "emotional_texture": "mastery being assembled, the surface held together while something underneath gathers force, ambition worn as elegance, the woman who looks composed because she has practiced it, botanical and figurative in conversation as if the self and the natural world are the same question",
        "subjects": [
            "a large acrylic painting on canvas with a deep cobalt blue background and large white magnolia blossoms floating through the composition, a female figure emerging in the lower half in warm rose and flesh tones",
            "an acrylic painting where ultramarine blue fills the canvas and pale botanical forms magnolias or peonies drift through the field, a figure's face or hands barely visible beneath the flowers",
            "a confident acrylic composition where a woman's form in warm skin tones rises against an intensely blue painted ground, white flower petals scattered across both figure and background",
            "an acrylic figure and floral painting where deep cobalt blue occupies most of the canvas, loose white botanical shapes moving through it, and a female face looking up from below",
            "a large-format acrylic painting combining a figurative element face or torso in warm flesh tones with large loosely rendered white flowers against a dominant blue ground",
            "an acrylic painting with the deep blue of a night garden and cream-white magnolia blooms, a figure barely visible underneath, the botanicals and the body overlapping",
            "a technically confident acrylic where a woman in warm pinks stands within a swirling composition of cobalt blue and white botanical forms, the brushwork broad and sure",
            "an acrylic painting where the palette is entirely blue and white except for the warm flesh tones of a figure, the flowers and the woman inhabiting the same compositional space with equal weight",
        ],
        "prompt_template": (
            "A large-scale acrylic painting on canvas ambitious in composition, "
            "technically accomplished, the work of someone who has been painting for years "
            "and is now reaching for something bigger. "
            "The technique is confident: broad, decisive strokes for the background, "
            "more deliberate layering for the figurative elements. "
            "Paint applied with full brushes no timid marks, no overworking. "
            "The surface has depth: thin glazes in the botanical forms, "
            "opaque buildup where the figure emerges. "
            "{subject} "
            "Color palette: {color}. The blue is the foundation and the atmosphere. "
            "The mood: {mood}. "
            "The composition holds two things at once the figure and the botanical "
            "as if the painter has decided that the self and the natural world "
            "are the same question asked two ways. "
            "Controlled but reaching. Masterful but not finished becoming. "
            "No text anywhere in the image. Square format. Style: natural."
        ),
        "moods": [
            "composed and quietly ambitious, the surface of a life that looks right from the outside",
            "polished and aspirational, the way things look when you are building something and not yet sure what",
            "elegant and slightly held everything in its place except the one thing that is still accumulating",
            "confident and reaching, the brushwork of someone who knows what she can do and suspects she can do more",
        ],
    },

    "unraveling": {
        "label": "Unraveling",
        "age_range": "Crisis (~30)",
        "slider_position": 4,
        "bio_poem": (
            "There was a time you let yourself love and believe.\n"
            "You have been alone before. You will be again.\n"
            "Can you make it out alive?\n"
            "You are never going to be the same, again and again and again."
        ),
        "description": (
            "The brush put down. The fineliner picked up. "
            "Everything stripped to line and white space. "
            "The body became the subject its fractures, its anatomy, "
            "what it looks like when it is coming apart and still standing."
        ),
        "developmental_frame": "Kübler-Ross grief model. Existential crisis (Yalom). Identity deconstruction.",
        "color_palette": ["dense black fineliner ink on stark white", "black ink only, no color wash", "pure black line on white paper with a single red accent one thread, one mark, one line", "black and white with one element in cadmium red used once, used finally", "ink black against white with red used like punctuation a wound, a thread, a signal"],
        "art_references": ["single-weight fineliner pen and ink on smooth white paper or Bristol board", "confident unbroken line drawing with zero hatching or tonal shading", "confessional figure drawing in pure pen and ink", "the anatomy of crisis drawn in decisive black line", "raw illustrative pen work where the white space is as active as the line"],
        "emotional_texture": "the body telling the truth the voice cannot, anatomy made visible through skin, grief drawn rather than spoken, the line as the last thing holding, white space as breath, red as the only remaining heat",
        "subjects": [
            "a pen and ink figure drawing of a woman split vertically one half flesh and skin, the other half bones and internal structure fully rendered, the two halves meeting at a clean center line, one red element at the split",
            "a single-weight fineliner drawing of a female figure suspended by a thin red thread from the top of the page, her body loose and falling, the thread the only color in the image",
            "a bold pen and ink self-portrait of a screaming face eyes clenched, mouth open, hair spreading outward like fracture lines, the face taking up most of the page, white space around it enormous",
            "a pen and ink figure drawing of a woman arching violently backward, diagonal radiating lines emanating from her body like energy or breaking, one red mark at the center of the chest",
            "a fineliner drawing of a female figure emerging from or dissolving into an intricate cloud of pen-drawn botanical forms flowers and vines drawn with the same line as the body, figure and plant indistinguishable at the edges",
            "a pen and ink drawing of two figures connected by a single red thread that runs between them, one figure pulling away, the other staying, the thread the only color in the image",
            "a single-weight ink drawing of a woman curled into herself on white paper, hair spreading out around her like roots, the composition intimate and minimal, enormous white space surrounding the figure",
            "a fineliner pen drawing of a woman's face and torso where the skin dissolves at the edges into pen-drawn text words written so small they read as texture, a face emerging from language",
        ],
        "prompt_template": (
            "Pen and ink drawing on white paper single-weight fineliner, "
            "no hatching, no tonal wash, no color except one deliberate red element. "
            "The line is confident and unbroken: this is not tentative mark-making "
            "but the drawing of someone who has practiced figure work for years "
            "and is now using that skill to make something urgent and true. "
            "Anatomical knowledge is present but the figures are not clinical "
            "they are emotionally live, bodies in states of fracture or suspension or emergence. "
            "The white space is compositional: more white than black on the page, "
            "the empty areas as active as the drawn ones. "
            "Hair is drawn as an emotional element it moves, spreads, radiates, curls "
            "in ways that match the internal state of the figure. "
            "{subject} "
            "Color: black ink on white. {color}. "
            "The red element when it appears is used once, decisively: "
            "a thread, a line, a wound, a signal. It means something. "
            "The mood: {mood}. "
            "The drawing should feel like a page torn from the most honest sketchbook "
            "anyone has ever kept technically accomplished, emotionally unflinching, "
            "the kind of beauty that comes from not looking away. "
            "No text in the image. Square format. Style: natural."
        ),
        "moods": [
            "grief past the acute phase hollow, clear-eyed, the body still standing even though something is gone",
            "stripped bare and lucid, the particular calm of someone who has stopped performing and is just drawing what is true",
            "fractured but precise the crisis doesn't break the line, it sharpens it",
            "raw and luminous, the quality of light in a room where everything unnecessary has been removed",
        ],
    },

    "reconstruction": {
        "label": "Reconstruction",
        "age_range": "Rebuilding (~31-37)",
        "slider_position": 5,
        "bio_poem": (
            "There are no more boundaries.\n"
            "You will launch from newfound footing.\n"
            "Mind, heart, body, all aligned.\n"
            "Movement, grace, and hope, all together."
        ),
        "description": (
            "The line softened. Color came back but chosen this time, not default. "
            "Ink and watercolor together: the structure of the pen years "
            "with warmth returning through the wash. "
            "Wolves. Movement. The body in full stride."
        ),
        "developmental_frame": "Erikson's generativity vs. stagnation. Tedeschi & Calhoun's post-traumatic growth. Kintsugi as psychological metaphor.",
        "color_palette": ["cool blue-gray as the dominant tone with rust-red or burnt orange as one warm accent", "muted slate and ash-blue with a single autumn-red element a leaf, a thread, a mark", "gray-blue watercolor washes over confident ink line, warm ochre used sparingly", "cool white hair and cool blue environment with one warm accent in red-orange", "blue-gray and cream with rust as the single note of heat"],
        "art_references": ["sophisticated pen and ink illustration with controlled watercolor washes", "narrative illustration combining confident ink outline with muted color", "ink and watercolor figure and animal composition", "mature illustrative style emerging from raw pen work into considered color", "editorial illustration with emotional depth ink armature, watercolor atmosphere"],
        "emotional_texture": "movement after stillness, the body trusting itself again, animal companionship as earned loyalty, grounded grace rather than performed elegance, the kind of strength that does not need to announce itself",
        "subjects": [
            "a sophisticated ink and watercolor illustration of a white-haired woman in profile, a wolf at her side, both moving in the same direction through autumn, rendered in cool blue-gray with rust-red leaf accents",
            "an ink and watercolor illustration of a woman in motion striding, arms loose with one or two large dogs flanking her as companions, cool gray-blue palette with warm autumn color in the leaves around them",
            "an ink and watercolor drawing of a female figure standing in birch trees, the trees rendered in loose gray-blue washes around a confident ink outline, red-orange leaves falling through the composition",
            "a narrative illustration in pen and ink with watercolor of a woman and a wolf facing the same direction, her hand resting on its back, both still, the palette cool and restrained with one warm accent",
            "an ink and watercolor illustration of a figure in full stride, dogs running alongside, the movement fluid and confident, blue-gray tones with warm rust accents in the ground and leaves",
            "a pen and ink illustration with watercolor wash of a woman in profile, strong jaw, loose hair, looking ahead with quiet certainty, a wolf visible in the background, cool palette with one warm element",
            "an ink and watercolor composition of a woman emerging from a birch forest into open space, the trees loosely painted behind her, her form in confident ink line, the palette moving from cool shadow to warm light",
            "a sophisticated narrative illustration in ink and watercolor a woman and her dogs in autumn light, everything rendered in muted blue and cream except for the rust-red leaves and one warm accent element",
        ],
        "prompt_template": (
            "Pen and ink illustration with controlled watercolor washes "
            "the structural precision of fine line work softened by selective color. "
            "The ink line is confident and expressive: figures drawn with "
            "the assurance of years of life drawing, but looser now, "
            "less about crisis and more about movement. "
            "Watercolor is applied in controlled washes over the ink "
            "not loose and wet but considered: cool blue-gray tones in the dominant areas, "
            "one warm accent color (rust, ochre, burnt orange) used for specific elements. "
            "The palette is muted and sophisticated nothing oversaturated, "
            "color used for atmosphere rather than expression. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "The composition is narrative and grounded: "
            "figures in motion or in companionship, the natural world as context not backdrop. "
            "The illustration should feel like the work of someone "
            "who came through something and found their visual voice on the other side "
            "more controlled, more chosen, quieter but not quieted. "
            "No text anywhere in the image. Square format. Style: natural."
        ),
        "moods": [
            "grounded and forward-moving, the particular grace of a body that has learned to trust itself again",
            "warm and self-possessed, the ease that comes after you stop performing ease",
            "quietly fierce the confidence of someone who rebuilt from nothing and knows the difference between strength and armor",
            "generous and rooted, movement that knows where it came from and is not afraid of where it is going",
        ],
    },

    "reclamation": {
        "label": "Reclamation",
        "age_range": "Now",
        "slider_position": 6,
        "bio_poem": (
            "You built the table. You chose who sits there.\n"
            "The dogs at your feet, the ring on your hand, the work that is yours.\n"
            "Sovereignty is quiet. It does not perform.\n"
            "You are finally the author of every room you walk into."
        ),
        "description": (
            "The dark sublime. The collected life. "
            "A visual vocabulary built from everything that came before "
            "cartoon observation, portrait discipline, botanical ambition, "
            "confessional line, reconstructed color and now fully owned. "
            "The rooms are hers. The wolves are at her feet."
        ),
        "developmental_frame": "Kegan's Stage 5 (self-transforming mind). Jung's individuation. Self-authorship.",
        "color_palette": ["deep sage and umber with antique gold accents", "midnight blue and candlelight warm the palette of a room at night with one lamp on", "rich dark tones forest green, deep brown, near-black lit by warm amber", "deep cool darks with warm light sources: candle, lamp, firelight", "umber and prussian blue with gold leaf and candlelight warm as the only lights"],
        "art_references": ["mature illustrative acrylic painting with dark academic palette", "rich dark-toned acrylic with illustrative precision and narrative depth", "classical interior painting with contemporary illustrative sensibility", "the visual language of someone who has been collecting and making for thirty years", "acrylic on canvas combining portraiture, interior, animal, and botanical all earned"],
        "emotional_texture": "sovereignty without performance, the dark sublime as aesthetic home, warmth that has been chosen not defaulted into, the collector and the maker occupying the same room, authority that does not need to be announced",
        "subjects": [
            "a richly painted acrylic interior at midnight a library or study with candles burning, shelves of books and objects, two German Shepherds sleeping in the foreground, deep sage and umber tones lit by warm candlelight",
            "an acrylic painting of a woman's figure silhouetted in a doorway of a dark house at night, wolves in the garden behind her visible in the darkness, the light from within warm against the deep blue outside",
            "a mature acrylic interior scene a piano room in the golden hour, paintings covering a stairwell wall salon-style, the room lit from within, everything chosen and placed with intention",
            "an acrylic painting of a researcher's desk by lamplight papers, a skull, dried botanicals, a robot or mechanical object in progress, two dogs asleep nearby, the room dark and warm and full",
            "a richly painted acrylic moonlit garden scene old roses and iron gates, German Shepherds standing among the plants, the blue of night sky against warm stone, everything rendered with illustrative precision",
            "a mature acrylic painting of a woman at a desk writing by lamplight, surrounded by books and research and objects collected over years, dogs asleep at her feet, the room dark and deeply inhabited",
            "an acrylic painting of a candlelit interior a salon of collected paintings on a dark wall, objects on every surface, a figure moving through the space with complete ownership of it",
            "a dark, richly painted acrylic of a woman standing in her own library at night holding a glass, not performing for anyone, wolves at her feet, the room behind her entirely hers",
        ],
        "prompt_template": (
            "Mature acrylic painting on canvas rich, dark, illustratively precise. "
            "The technique has the depth of someone who has been painting for thirty years: "
            "multiple glazed layers in the darks, confident opaque work in the lights and mid-tones, "
            "the surface alive with subtle variation. "
            "The palette is deep and intentional: sage, umber, midnight blue, near-black, "
            "warmed by specific light sources candles, lamps, firelight, moon. "
            "The painting style is illustrative in the best sense: "
            "narrative, atmospheric, every element chosen, nothing accidental. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "The composition conveys sovereignty: this is a room that belongs to someone, "
            "an image made by someone who has earned the right to their own aesthetic. "
            "The dark is not threatening it is chosen. The warmth is not performed it is real. "
            "Every element (the dogs, the books, the objects, the light) "
            "should feel like it was placed by someone who knows exactly what they are doing. "
            "No text anywhere in the image. Square format. Style: vivid."
        ),
        "moods": [
            "sovereign and unhurried, the particular calm of someone who has finally stopped explaining herself",
            "dark and luminous candlelight on old wood, the warmth of a room that took decades to build",
            "timeless and knowing, the feeling of a space that holds the full complexity of a life without apologizing for any of it",
            "warm but not soft authority that came from everything that preceded it, worn quietly",
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
