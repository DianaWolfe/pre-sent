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
            "She was always moving. New bases, new schools, new faces "
            "who would never quite stick. Art was the only room she kept. "
            "Cartoonish, impressionist, sarcastic before she had words for it. "
            "A raven followed her. She drew everything she saw."
        ),
        "developmental_frame": "Piaget's preoperational and concrete operational stages. Erikson's industry vs. inferiority.",
        "color_palette": [
            "clashing primaries: red, yellow, electric blue that fights with itself",
            "muddy forest greens and dirty earth browns, the colors of hiding",
            "faded crayon palette gone slightly wrong, like a coloring book left in the sun",
            "loud orange against crayon-box purple, a child who refuses to match",
            "cadmium yellow and cobalt blue in open conflict"
        ],
        "art_references": [
            "child's cartoon drawing with impressionist paint thrown in the background",
            "naive art that knows exactly what it is doing",
            "flat cartoon female figure in front of loose gestural impressionist forest",
            "outsider art energy with interior intelligence, wry and watchful",
            "wobbly confident lines over loose paint blobs, a girl who draws everything"
        ],
        "emotional_texture": "sarcasm too old for the body, wry observation of adults who think she is not watching, cartoon logic applied to genuinely strange circumstances, the raven as the only constant, humor as the portable shelter you carry from base to base",
        "subjects": [
            "a flat cartoon girl with an oversized head and a deadpan expression standing in a loosely impressionist forest, a raven perched on her shoulder looking equally unimpressed, trees rendered in quick dabs of green shadow around her flat outlined form",
            "a child's cartoon self-portrait with exaggerated eyes and a knowing smirk, a black dog sitting beside her with the same expression, the background an impressionist smear of a military base housing block",
            "a cartoon girl sitting on top of a packed moving van looking completely unbothered, a fox visible in the impressionistically blurred roadside watching her go",
            "a flat cartoonish girl reading a giant book alone in an impressionist forest, a raven reading over her shoulder, adults rendered as smeared color blobs in the distant background",
            "a small cartoon female figure standing in an impressionistically painted forest clearing, a black dog at her heels, light through the trees in loose dabs of gold and green, her expression entirely self-contained",
            "a child's cartoon drawing of a classroom full of identical forward-facing figures except one girl turned away toward the window where a raven sits on the sill",
            "a naive cartoon drawing of a girl and a very large fox, the fox impressionistically painted in warm ochre strokes, the girl flat and outlined holding its tail like a leash",
            "a cartoonish girl sitting on a packed suitcase in an airport, a raven on her luggage, surrounding crowds painted in swift impressionist strokes of movement, the girl perfectly still and unimpressed"
        ],
        "prompt_template": (
            "A hybrid of child's cartoon drawing and impressionist painting. "
            "The central figure is a girl drawn with flat simplified outlines, "
            "wobbly and confident at once, the line quality of someone who draws compulsively. "
            "Her face has a deadpan knowing quality: slightly too-adult expression in a child's body. "
            "She is never afraid. She is watching everything. "
            "Emotional resonance: private amusement at a world she has already figured out. "
            "The figure does not perform joy or distress. She observes. Her stillness is the joke. "
            "A spirit animal accompanies her: a raven, a fox, or a black dog. "
            "The animal is drawn with the same cartoon flatness as the girl. "
            "The animal is not cute. It is a companion with opinions. "
            "The backgrounds and environments are handled in loose impressionist paint: "
            "quick dabs, gestural strokes, no clean edges, light broken into color. "
            "The tension between the flat cartoon figures and the painterly world around them "
            "is the structural point of the image. "
            "{subject} "
            "Color palette: {color}. Colors don't quite harmonize. That dissonance is intentional. "
            "The mood: {mood}. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "deadpan and privately amused, the expression of a child who has already figured out the adults in the room",
            "wry and watchful, humor used as a portable shelter carried from base to base",
            "sarcastic but not mean, the kind of funny that comes from being the new kid seventeen times",
            "irreverent and self-contained, a small person with an enormous interior life and a straight face"
        ],
    },

    "becoming": {
        "label": "Becoming",
        "age_range": "Adolescence (~13-17)",
        "slider_position": 3,
        "bio_poem": (
            "Anger always had a place to go, but intellect had none.\n"
            "The small world is too small. Spread your wings.\n"
            "Stop and start the performances that will never bring you peace.\n"
            "Be brave enough to heal, and the world is yours."
        ),
        "description": (
            "She picked up a brush and pointed it at her own face. "
            "The mirror was the only fixed point in a world that kept moving. "
            "The self-portrait as act of self-determination. "
            "The raven watched from outside the window. "
            "She painted herself until she knew what she looked like."
        ),
        "developmental_frame": "Erikson's identity vs. role confusion. Marcia's identity statuses.",
        "color_palette": [
            "cool gray-green flesh tones over a warm umber underpainting, the skin of someone learning their own face",
            "raw sienna shadows and titanium white highlights, honest about the asymmetry",
            "deep burnt umber in the darks, pale yellow ochre in the light planes of the face",
            "muted warm neutrals with one saturated color breaking through like something she couldn't contain",
            "gray-blue shadow against cream highlight, the palette of a single window in a new room"
        ],
        "art_references": [
            "naturalistic acrylic self-portrait painted from the mirror, careful and unflinching",
            "observational life painting in acrylic on canvas, the face as first serious subject",
            "realist portrait study with visible brushwork, someone learning to look without flinching",
            "academic portrait approach made personal and urgent",
            "acrylic on canvas with layered skin tones, honest asymmetry, nothing idealized"
        ],
        "emotional_texture": "the face as the only thing she can control, learning to look at herself without flinching, the practice of being seen on her own terms, the brush as the argument she cannot make with words, a raven outside every window she has ever painted from",
        "subjects": [
            "a naturalistic acrylic self-portrait of a teenage girl, three-quarter view, direct gaze that holds the viewer without aggression, skin tones built in cool layers over a warm ground, a raven barely visible in the dark background",
            "a close-up acrylic portrait study of a young woman, face occupying most of the canvas, hair painted in long dark sweeping strokes, the face slightly asymmetrical and completely honest",
            "a self-portrait lit from a single window source, one side of the face in warm highlight the other in cool gray shadow, painted with quiet observational precision in acrylic, a fox reflected faintly in the mirror behind her",
            "an acrylic portrait in profile, strong jawline, hair loose, the sitter looking away from the viewer toward something outside the frame, a black dog sitting at the edge of the composition",
            "a naturalistic acrylic figure study from the waist up, one hand resting near the chin, the posture of someone sitting for her own portrait with complete seriousness",
            "a self-portrait where the eyes look slightly downward in concentration, painted in careful acrylic layers, skin tones mixing warm and cool the way real skin does, nothing dramatized",
            "an acrylic portrait where the subject looks directly back at the viewer with the expressionless focus of serious self-study, dark hair against a neutral background, a raven's wing just visible at the edge of the canvas",
            "a mirror self-portrait in acrylic where the reflection is slightly more certain than the painter, as if the canvas version of her knows something she is still working out"
        ],
        "prompt_template": (
            "Naturalistic acrylic portrait on canvas, painted from direct observation. "
            "From the mirror, from life, from the kind of looking that is also a form of argument. "
            "The technique is careful and layered: warm umber ground visible in places, "
            "cool gray-green flesh tones built over it, highlights in pale ochre or cream. "
            "Brushwork visible but controlled. The marks show the work of looking, not expressive abandon. "
            "Canvas texture shows through in the mid-tones. "
            "The subject is always female. Always the artist herself, or someone who is her. "
            "A spirit animal, a raven or fox or black dog, may appear at the edge of the composition "
            "as a witness. It does not demand attention. It is simply there. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "Single natural light source. Shadows honest, not dramatized. "
            "Emotional resonance: the figure is concentrated, guarded, and completely present. "
            "Her expression is not soft and not hard. It is the face of someone deciding who she is "
            "before the world decides for her. She does not perform vulnerability. She studies herself. "
            "The painting is an act of self-determination. "
            "The face holds its own gaze. Nothing idealized. Nothing flinched from. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "self-conscious and steady, the look of someone who has decided to stop looking away",
            "concentrated and frank, the face of a teenager who has been painting herself for years and knows what she is doing",
            "guarded but present, honest about what the mirror shows without performing vulnerability",
            "searching and still, the quiet intensity of someone using paint to decide who she is before the world decides for her"
        ],
    },

    "proving": {
        "label": "Proving Years",
        "age_range": "Early Adulthood (~18-29)",
        "slider_position": 2,
        "bio_poem": (
            "Ups and downs and turn arounds,\n"
            "two steps forward and one step back.\n"
            "Everything looks perfect from the outside.\n"
            "You are building the courage to finally take flight."
        ),
        "description": (
            "The paintings got bigger. The palette got more ambitious. "
            "She raised her siblings and lost herself to a marriage that was too easy. "
            "Botanical and figurative, cobalt blue and white magnolias. "
            "Everything looked composed from the outside. "
            "A fox watched from the garden. She kept painting."
        ),
        "developmental_frame": "Erikson's intimacy vs. isolation. Levinson's early adult transition.",
        "color_palette": [
            "deep ultramarine and cobalt blue dominating three-quarters of the canvas, cool and absolute",
            "prussian blue background with cream-white botanical forms floating through it",
            "deep cool blue field with pale gray-white magnolia petals and cool-toned flesh",
            "cobalt blue ground with white flowers and cool blue-gray figure emerging from beneath them",
            "midnight blue and cool white only, no warm tones anywhere in the image"
        ],
        "art_references": [
            "large-scale acrylic painting on canvas, blue ground with figurative and botanical elements",
            "ambitious acrylic where deep blue occupies most of the canvas and botanical forms drift through it",
            "figurative acrylic painting, a woman and white flowers against a dominant cobalt blue ground",
            "acrylic on canvas with confident broad strokes, botanical and figure sharing a cool blue field",
            "painterly acrylic composition, cool blue atmosphere, white magnolias, female figure emerging"
        ],
        "emotional_texture": "mastery assembling itself while something underneath gathers force, the surface held together with elegance and will, everything looks right from outside while the courage to become keeps building, a fox in the garden watching through the studio window",
        "subjects": [
            "a large acrylic painting on canvas: deep cobalt blue fills the background, large white magnolia blossoms float through the composition, a female figure's face or shoulders emerge from the lower portion in cool pale tones, a fox barely visible in the dark lower corner",
            "an acrylic painting on canvas: ultramarine blue ground, pale cream-white botanical forms drifting across the surface, a woman's hands reaching upward through the flowers, negative space above",
            "a large acrylic painting on canvas: cool dark blue background with white magnolia petals scattered across it like something released, a female figure's profile visible at the left edge looking inward",
            "an acrylic painting on canvas: prussian blue fills the frame, white and pale gray botanical forms in the upper two-thirds, a woman's face upturned in the lower third as if surfacing from deep water",
            "a large acrylic painting on canvas: deep blue ground, a female figure standing within it in cool pale tones, white flowers surrounding her, the composition spare and the blue vast around everything",
            "an acrylic painting on canvas: midnight blue background, a single large magnolia blossom in cool white at center, a woman's silhouette in the lower portion, most of the canvas empty blue",
            "a large acrylic painting on canvas: cobalt blue ground with loose white botanical brushstrokes moving through it, a female face barely distinguishable from the flowers, dissolved into the composition",
            "an acrylic painting on canvas: deep blue fills most of the frame, white petals in the upper portion, a woman's figure in cool blue-gray at the bottom, the painting spare and the silence enormous"
        ],
        "prompt_template": (
            "THIS IS A LARGE-SCALE ACRYLIC PAINTING ON CANVAS. "
            "Not a cartoon. Not an illustration. Not a sketch. "
            "An acrylic painting with broad confident brushstrokes on canvas. "
            "The background is deep cobalt or ultramarine blue, painted with full brushes, "
            "occupying most of the canvas. "
            "White or cream-white botanical forms, magnolias or large petals, "
            "float through the blue field. "
            "A female figure emerges within or beneath the botanical forms, "
            "painted in cool pale tones that do not compete with the blue. "
            "NO warm colors. NO cartoon elements. NO illustration style. "
            "Cool palette only: blues, cool whites, pale gray-blue flesh tones. "
            "Generous negative space. The blue breathes. The composition does not crowd itself. "
            "All figures are female. "
            "{subject} "
            "Color: {color}. "
            "The mood: {mood}. "
            "Emotional resonance: the figure is composed on the surface and accumulating force underneath. "
            "Posture upright, expression controlled. She is holding something together with will. "
            "Not distressed. Not free. The body of someone performing mastery while building courage. "
            "Controlled but reaching. The surface composed. Something gathering underneath. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "composed and quietly ambitious, the surface of a life that looks right from the outside",
            "polished and controlled, everything in its place except the one thing still accumulating",
            "elegant and slightly held, the brushwork of someone performing mastery while building courage",
            "cool and aspirational, confident marks, the blue vast and the figure small within it"
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
            "The brush went down. The fineliner came up. "
            "Everything stripped to line and white space and the truth of the body. "
            "The black dog arrived and stayed. Ravens circled. "
            "She drew the anatomy of what was happening to her "
            "because there was no other language for it."
        ),
        "developmental_frame": "Kubler-Ross grief model. Existential crisis (Yalom). Identity deconstruction.",
        "color_palette": [
            "dense black fineliner ink on stark white, nothing else, nowhere to hide",
            "black ink only with one single red element used like a wound or a signal or a thread still holding",
            "pure black line on white paper, the red appears once and only once, decisive",
            "black and white with one cadmium red accent used finally, the only remaining heat in the image",
            "ink black against white, the red used like punctuation at the end of something"
        ],
        "art_references": [
            "single-weight fineliner pen and ink on smooth white paper, zero hatching, pure line",
            "confessional figure drawing in pen and ink, the anatomy of grief made visible",
            "bold ink illustration where white space is as active as the drawn line",
            "raw illustrative pen work, bodies in states of fracture or suspension or emergence",
            "pen and ink drawing with one red element, a thread or a wound or a line still connecting"
        ],
        "emotional_texture": "the body telling the truth the voice cannot, grief drawn because it cannot be spoken, the black dog as literal presence, ravens as witnesses who do not look away, voodoo logic where the body split open is also the body becoming, the line is the last thing holding and it holds",
        "subjects": [
            "a pen and ink figure drawing of a woman split vertically, one half flesh and skin the other half bones and internal structure fully rendered, a raven perched at the center line where the split occurs, one red element at the join",
            "a single-weight fineliner drawing of a female figure suspended by a thin red thread from the top of the page, her body loose and falling, a raven watching from below, the thread the only color in the image",
            "a bold pen and ink portrait of a woman's screaming face, eyes clenched and mouth open, hair spreading outward like fracture lines, a black dog sitting quietly beside her as witness",
            "a pen and ink figure drawing of a woman arching violently backward, diagonal lines radiating from her body like breaking, a raven landing on her outstretched hand, one red mark at the center of the chest",
            "a fineliner drawing of a female figure dissolving into an intricate cloud of pen-drawn botanical forms and raven feathers, figure and plant and bird indistinguishable at the edges",
            "a pen and ink drawing of a woman and her black dog connected by a single red thread, the dog pulling gently toward the light, the woman still deciding, the thread the only color",
            "a single-weight ink drawing of a woman curled into herself on white paper, a raven standing nearby with its head tilted, hair spreading around her like roots, enormous white space surrounding both of them",
            "a fineliner drawing of a woman's figure where the skin at the edges becomes raven feathers, flesh and bird sharing the same line quality, a fox watching from the lower corner"
        ],
        "prompt_template": (
            "Pen and ink drawing on white paper. Single-weight fineliner. "
            "No hatching. No tonal wash. No color except one deliberate red element. "
            "The line is confident and unbroken: the drawing of someone who has practiced "
            "figure work for years and is now using that skill to make something urgent and true. "
            "All figures are female. "
            "Spirit animals appear as active presences, not decoration: "
            "a black dog as the body of grief itself, ravens as witnesses who do not look away, "
            "a fox as the part of her that is already planning the escape. "
            "These animals share the same line quality as the figure. They belong to the same world. "
            "Anatomical knowledge present in the figures but not clinical. "
            "Bodies in states of fracture, suspension, emergence, or dissolution. "
            "The white space is compositional. More white than black on the page. "
            "Hair drawn as an emotional element: it moves, spreads, radiates, becomes feathers. "
            "{subject} "
            "Color: black ink on white. {color}. "
            "The red element appears once, decisively: a thread, a wound, a signal, a line still holding. "
            "The mood: {mood}. "
            "The drawing should feel like a page torn from the most honest sketchbook anyone has kept. "
            "Technically accomplished. Emotionally unflinching. "
            "Emotional resonance: the figure conveys the specific quality of grief past its acute phase. "
            "Not collapsed. Not performed. The body still standing but altered permanently. "
            "If she screams, it is honest not theatrical. If she is still, the stillness is enormous. "
            "The kind of beauty that comes only from not looking away. "
            "No text in the image. Square format."
        ),
        "moods": [
            "grief past the acute phase, hollow and clear-eyed, the body still standing even though something permanent is gone",
            "stripped bare and lucid, the particular calm of someone who has stopped performing and is only drawing what is true",
            "fractured but precise, the crisis does not break the line, it sharpens it",
            "raw and luminous, the quality of light in a room where everything unnecessary has finally been removed"
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
            "The line softened. Color came back, but chosen this time. "
            "Ink and watercolor together: the structure she built in the dark years "
            "with warmth returning through the wash. "
            "The wolves found her. The fox had been waiting. "
            "She learned what it meant to move forward on purpose."
        ),
        "developmental_frame": "Erikson's generativity vs. stagnation. Tedeschi and Calhoun's post-traumatic growth. Kintsugi as psychological metaphor.",
        "color_palette": [
            "cool blue-gray as the dominant tone with rust-red or burnt orange as one warm accent",
            "muted slate and ash-blue with a single autumn-red element, a leaf, a fox, a mark of warmth",
            "gray-blue watercolor washes over confident ink line, ochre used sparingly and with intention",
            "cool blue environment with one warm accent in rust-orange, the first warmth in a long time",
            "blue-gray and cream with rust as the single note of heat, chosen rather than inherited"
        ],
        "art_references": [
            "sophisticated pen and ink illustration with controlled watercolor washes, the structure of the pen years softened by color",
            "narrative illustration combining confident ink line with muted watercolor, figures in motion",
            "ink and watercolor composition of a woman and her animal companions, earned loyalty",
            "mature illustrative style where the rawness of the pen work is still present but color has returned",
            "editorial illustration with emotional depth, ink gives structure, watercolor gives warmth"
        ],
        "emotional_texture": "movement after stillness, the body trusting itself again, wolves as the pack she chose not the one she was assigned, the fox as intelligence and survival and forward motion, the raven as the part of her that always knew she would make it, grounded grace rather than performed elegance",
        "subjects": [
            "a sophisticated ink and watercolor illustration of a woman in profile, a wolf at her side and a raven on her shoulder, all three moving in the same direction through autumn, rendered in cool blue-gray with rust-red leaf accents",
            "an ink and watercolor illustration of a woman in full stride with two wolves flanking her as chosen companions, a fox running ahead, cool gray-blue palette with warm autumn color in the leaves",
            "an ink and watercolor drawing of a woman standing in birch trees, wolves in the trees around her, rendered in loose gray-blue washes around a confident ink outline, red-orange leaves falling",
            "a narrative illustration in pen and ink with watercolor of a woman and a wolf sitting back to back, both looking outward, the palette cool and restrained, a raven overhead",
            "an ink and watercolor illustration of a woman in motion, arms loose and confident, a fox running alongside her, the movement fluid and sure, blue-gray tones with warm rust accents",
            "a pen and ink illustration with watercolor wash of a woman in profile, strong jaw, hair loose, looking ahead with quiet certainty, a wolf behind her and a raven above, cool palette with one warm element",
            "an ink and watercolor composition of a woman and her pack, two wolves and a fox, emerging from a forest into open space, her form in confident ink line, the palette moving from cool shadow to first warm light",
            "a sophisticated ink and watercolor illustration of a woman with a raven on one arm and a fox at her feet, autumn light around her, everything rendered in muted blue and cream except for the rust-red of the fox and the leaves"
        ],
        "prompt_template": (
            "Pen and ink illustration with controlled watercolor washes. "
            "The structural precision of fine line work softened by selective color returning. "
            "The ink line is confident and expressive: figures drawn with the assurance "
            "of years of life drawing, but looser now, less about crisis and more about movement. "
            "Watercolor applied in controlled washes over the ink: "
            "cool blue-gray in the dominant areas, one warm accent color for specific elements. "
            "All figures are female. "
            "Spirit animals appear as chosen companions, not accidents: "
            "wolves as the pack she built herself, foxes as intelligence and forward motion, "
            "ravens as the part of her that always knew she would survive. "
            "These animals move with her. They are not watching from a distance anymore. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "The composition is narrative and grounded: "
            "a woman in motion or in companionship, the natural world as ally not backdrop. "
            "The illustration should feel like the work of someone who came through something "
            "and found her visual voice on the other side. "
            "Emotional resonance: the figure is in motion or poised for it. "
            "Posture open, gaze forward, arms loose. The ease of a body that has chosen to trust itself again. "
            "Not performing confidence. Actually in it. The difference is visible. "
            "More controlled, more chosen, quieter but not diminished. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "grounded and forward-moving, the particular grace of a body that has learned to trust itself again",
            "warm and self-possessed, the ease that comes after you stop performing ease",
            "quietly fierce, the confidence of someone who rebuilt from nothing and knows the difference between strength and armor",
            "generous and rooted, movement that knows where it came from and is not afraid of where it is going"
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
            "A refined storybook aesthetic, dark and warm and entirely hers. "
            "The ravens at her shoulder. The wolves at her feet. "
            "The rooms she built from everything she survived. "
            "Every element chosen. Nothing accidental. "
            "The artist at full power, in full possession of her own mythology."
        ),
        "developmental_frame": "Kegan's Stage 5 (self-transforming mind). Jung's individuation. Self-authorship.",
        "color_palette": [
            "deep sage and warm umber with antique gold as the light source, a room she built herself",
            "midnight blue and candlelight warm, the palette of a library at night with one lamp on",
            "rich dark tones, forest green and deep brown and near-black, lit by warm amber from within",
            "deep cool darks warmed by specific intimate light sources, candle, lamp, firelight, fox eyes in the dark",
            "umber and prussian blue with gold leaf and one warm candlelit interior, the dark as home not threat"
        ],
        "art_references": [
            "refined storybook illustration with a dark and elegant sensibility, Arthur Rackham meets Shaun Tan",
            "dark fairytale illustration style, sophisticated and warm, every detail meaningful",
            "narrative storybook art with occult undertones and emotional depth, animals as characters not props",
            "mature illustrative style combining botanical, animal, and interior elements with painterly warmth",
            "gothic storybook aesthetic, rich and intimate, the kind of illustration that holds its own secrets"
        ],
        "emotional_texture": "sovereignty without performance, the collected life rendered in storybook style, ravens as familiars not omens, wolves as guardians not threats, foxes as companions not tricksters, the dark sublime as aesthetic home, warmth chosen rather than performed, the artist who finally owns her own mythology completely",
        "subjects": [
            "a richly detailed storybook illustration of a woman in a candlelit library surrounded by books and botanical specimens and objects of power, two black dogs sleeping at her feet, a raven on the back of her chair, rendered in dark warm illustrative style",
            "a dark storybook illustration of a woman standing in a doorway of a candlelit stone house at night, wolves in the moonlit garden behind her, a raven on her shoulder, the light from within warm against the cool night",
            "a refined narrative illustration of a woman at a long table she built herself, objects arranged with intention around her, a fox curled at one end, a raven on her arm, the room dark and deeply inhabited",
            "a storybook illustration of a woman in a garden at dusk, old roses and iron gates, two wolves standing guard among the plants, a raven in the rose canes above her, rendered in rich dark illustrative style with warm candlelit accents",
            "a dark elegant storybook illustration of a woman at a desk by lamplight, papers and research and objects collected over years spread around her, a black dog at her feet and a raven on the lamp, the room hers completely",
            "a refined gothic storybook illustration of a woman moving through a candlelit room hung with her own paintings, a wolf at her side, a fox in the doorway, a raven overhead, everything chosen and in its place",
            "a dark and warm storybook illustration of a woman with a raven on one shoulder and a wolf pressing against her leg, standing in a moonlit room full of objects she has collected over a lifetime, sovereign and unhurried",
            "a richly illustrated storybook scene of a woman in a stone garden at night, sitting among the wolves and foxes and ravens she has gathered, not performing peace but actually in it, the dark beautiful and chosen"
        ],
        "prompt_template": (
            "Refined storybook illustration style, dark and warm and deeply narrative. "
            "Think gothic fairy tale art with emotional intelligence: "
            "rich detailed environments, every object placed with intention, "
            "animals as characters with their own presence and dignity. "
            "The line work is illustrative and confident. "
            "The color is deep and warm: dark sage, umber, near-black, "
            "lit from within by candles and lamps and firelight. "
            "All figures are female. "
            "Spirit animals appear as familiars and chosen companions: "
            "ravens at the shoulder, wolves at the feet, foxes in the doorways, "
            "black dogs as loyal and ancient presences. "
            "These animals are not decoration. They are part of her court. "
            "They have been with her through every era. Here they are finally home. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "The composition conveys sovereignty: "
            "a woman in full possession of her own aesthetic and mythology. "
            "The dark is not threatening. It is chosen. "
            "The warmth is not performed. It is real. "
            "Emotional resonance: the figure is sovereign and unhurried. "
            "She is not performing for anyone in the image. Posture still, expression complete. "
            "She is not arriving anywhere. She is already there. "
            "The animals at her feet and shoulder are not props. They are her court. She earned them. "
            "Every element should feel earned. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "sovereign and unhurried, the particular calm of someone who has finally stopped explaining herself to anyone",
            "dark and luminous, candlelight on old wood, the warmth of a room it took a whole life to build",
            "timeless and knowing, the feeling of a space that holds the full complexity of a life without apologizing for any of it",
            "warm but not soft, the authority of someone who earned every animal at her feet"
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
