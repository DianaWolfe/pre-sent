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
        "label": "wonder",
        "age_range": "0–12",
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
            "crayon primaries used without mixing: red next to blue next to green, the palette of someone using what is there",
            "pencil and colored pencil on lined notebook paper, the colors bleeding slightly past the lines",
            "muddy greens and earth browns from a cheap watercolor set, pigment pooling where the brush lifted",
            "faded colored pencil over pencil sketch, the lines showing through, layered without technique",
            "ballpoint pen marks with colored pencil filled in, the blue of a cheap pen and the green of a school crayon"
        ],
        "art_references": [
            "a child's earnest pencil and crayon drawing, proportions slightly off but the observation genuine",
            "early learner figure drawing in colored pencil, the head a little too big, the hands simplified",
            "a child's sketchbook page, pencil lines repeated where she was not sure, working it out on the paper",
            "naive observational drawing with the unselfconscious marks of someone who has not yet learned what art is supposed to look like",
            "early watercolor attempt with pencil underdrawing visible, pigment puddled in the low spots, the sky overworked"
        ],
        "emotional_texture": "pure observation before self-consciousness arrived, drawing everything because drawing is how she understands it, the raven as the only constant across seventeen schools, wonder applied equally to forests and military housing blocks and the faces of strangers",
        "subjects": [
            "a child's pencil and crayon drawing: a raven fills most of the page, drawn very large because it deserves the space, the eye given special attention — a careful oval with a smaller oval inside, the beak redrawn twice to get it right",
            "a pencil and colored pencil drawing: a fox sits small at the center of a mostly empty page, sky scribbled blue above, ground white with careful gray shadows, the whole scene observed quietly from a distance",
            "a child's detailed pencil drawing: a frog seen from nearly above, sitting in the center of a carefully drawn lily pad, the eyes too large and perfectly round, wavy lines radiating outward to the page edges",
            "an earnest pencil and crayon drawing: a caterpillar takes up most of the page, each segment carefully outlined and colored, the leaf drawn with ruler-straight veins, the whole composition filling the paper edge to edge",
            "a child's sketchbook page: four small animal sketches in different corners — a raven profile, a fox sitting, a deer head, a black dog — each drawn with the same careful attention, the page full of looking",
            "a child's watercolor: a wolf stands in a forest clearing, trees surrounding it on three sides creating a natural frame, the wolf's eyes the most carefully painted thing on the page, too large and too intense",
            "a learner's colored pencil drawing: a deer half in the trees and half in open meadow, the line between forest and clearing a visible seam in the drawing, every detail on both sides given equal serious attention",
            "a child's pencil drawing: a raven in flight, wings spread wide from one side of the paper to the other, the primary feathers carefully counted and drawn, pencil lines visible where the wingspan was restarted to get it right"
        ],
        "prompt_template": (
            "Early learner art. A child who draws everything she sees, every day, because she must. "
            "The medium is whatever she has: pencil, crayon, colored pencil, cheap watercolor, ballpoint pen. "
            "The proportions are not quite right yet — heads slightly large, hands simplified, "
            "figures a little stiff — but the observation underneath is genuine and careful. "
            "She is looking hard at the world and putting it down as she sees it, "
            "without the filters that come from knowing what art is supposed to look like. "
            "The marks are earnest. The lines are sometimes redrawn. The colors don't always mix right. "
            "This is not stylized naivety. This is actual early practice. "
            "A spirit animal — a raven, a fox, or a black dog — appears as naturally as anything else "
            "she draws, given the same careful attention as the trees and the ground and the sky. "
            "{subject} "
            "Color palette: {color}. "
            "The mood: {mood}. "
            "Emotional resonance: pure wonder and observation, the face of someone drawing because "
            "it is how she understands the world, not yet self-conscious about whether she is good. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "absorbed and unselfconscious, the concentration of a child who draws for hours without noticing time",
            "quietly observant, storing everything, the new kid who watches before she speaks",
            "earnest and wondering, looking at the world with the full attention of someone who will draw it later",
            "still and intent, the particular focus of a child who has found the one thing that belongs to her"
        ],
    },

    "becoming": {
        "label": "becoming",
        "age_range": "13–17",
        "slider_position": 2,
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
        "emotional_texture": "the face as the only thing she can control, learning to look at herself without flinching, the practice of being seen on her own terms, the brush as the argument she cannot make with words, a raven outside every window she has ever painted from",
        "subjects": [
            "a large acrylic painting on canvas: a young woman's face occupies nearly the entire canvas in cool pale tones, her gaze direct and unresolved, cobalt blue pressing in at the very edges",
            "an acrylic painting on canvas: ultramarine blue fills nearly the entire frame, a small female figure stands at the very bottom barely distinguishable from the dark, white magnolia petals drifting down from above like slow snow",
            "an acrylic painting on canvas: a close-up study of two hands held open against deep cobalt blue, white flowers resting in the palms, no face visible — only the hands and the offering",
            "a large acrylic painting on canvas: a woman's back and loosely painted hair face the blue interior of the canvas, white botanical forms floating on either side of her, we see only what she will not show",
            "an acrylic painting on canvas: vast botanical forms in cream and white occupy most of the frame, a woman's profile barely distinguishable among the magnolias — her face and the flowers made of the same pale paint",
            "an acrylic painting on canvas: prussian blue fills the background, a young woman in strong profile at center, chin lifted, white magnolia petals moving through the composition, the painting spare and certain",
            "an acrylic painting on canvas: the view is straight down at white magnolia petals scattered across a cobalt blue surface, a woman's dark hair just entering the frame from one edge, the angle intimate and unexpected",
            "an acrylic painting on canvas: midnight blue fills the entire canvas, a woman's shoulders and the back of her head emerge from the lower portion as if rising from the blue itself, white petals floating in the space above"
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
            "All figures are female. All figures are fully clothed. "
            "{subject} "
            "Color: {color}. "
            "The mood: {mood}. "
            "Emotional resonance: the figure is concentrated, guarded, and completely present. "
            "Her expression is not soft and not hard. It is the face of someone deciding who she is "
            "before the world decides for her. She does not perform vulnerability. She studies herself. "
            "The painting is an act of self-determination. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "composed and quietly ambitious, the surface of a life that looks right from the outside",
            "polished and controlled, everything in its place except the one thing still accumulating",
            "elegant and slightly held, the brushwork of someone performing mastery while building courage",
            "cool and aspirational, confident marks, the blue vast and the figure small within it"
        ],
    },

    "proving": {
        "label": "proving",
        "age_range": "18–29",
        "slider_position": 3,
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
        "emotional_texture": "mastery assembling itself while something underneath gathers force, the surface held together with elegance and will, everything looks right from outside while the courage to become keeps building, a fox in the garden watching through the studio window",
        "subjects": [
            "a naturalistic acrylic portrait: a young woman's face and shoulders, three-quarter view, direct composed gaze, skin tones built in careful cool layers over a warm ground, a raven barely visible in the shadowed background",
            "an acrylic painting: an extreme close-up of the eye area only — two eyes level and frank, the flesh around them painted with honest asymmetry, the rest of the face outside the frame, only what matters most",
            "an acrylic painting on canvas: a close-up study of a woman's hands, one resting open, painted with the same observational precision usually given to a face, the palette muted and honest, nothing decorative",
            "an acrylic painting on canvas: a woman from behind, her dark hair against a neutral background, every strand of the upswept hair painted with the careful attention usually applied to a face, the nape of the neck, the line of shoulder",
            "an acrylic painting on canvas: a woman in profile at an easel in a spare studio, small within the room, her back to the viewer, a black dog resting near the door, the room given as much care as she is",
            "a naturalistic acrylic portrait: the subject sits facing her mirror, her reflection visible in it — the painted version of her looks slightly more certain than the woman looking, a raven perched on the mirror frame",
            "an acrylic painting on canvas: a woman seated in a plain room, figure rendered small within the composition, the empty walls and light of the room painted with the same careful attention as the figure, a fox barely visible at the edge",
            "a naturalistic acrylic portrait: a close profile, the subject looking at nothing in the frame, painted with unflinching observational focus, the strong jawline and loose hair, honest asymmetry, nothing idealized"
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
            "Emotional resonance: the figure is composed on the surface and accumulating force underneath. "
            "Posture upright, expression controlled. She is holding something together with will. "
            "Not distressed. Not free. The body of someone performing mastery while building courage. "
            "Controlled but reaching. The surface composed. Something gathering underneath. "
            "No text anywhere in the image. Square format."
        ),
        "moods": [
            "self-conscious and steady, the look of someone who has decided to stop looking away",
            "concentrated and frank, the face of someone who has been painting herself for years and knows what she is doing",
            "guarded but present, honest about what the mirror shows without performing vulnerability",
            "searching and still, the quiet intensity of someone using paint to decide who she is before the world decides for her"
        ],
    },

    "unraveling": {
        "label": "unraveling",
        "age_range": "~30",
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
        "label": "reconstruction",
        "age_range": "31–37",
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
            "a sophisticated ink and watercolor illustration: a woman in profile, a wolf at her side and a raven on her shoulder, all three moving in the same direction through autumn, blue-gray wash and rust-red leaf accents",
            "an ink and watercolor illustration: a wide autumn landscape in cool blue-gray wash, sparse birch trees, a small female figure at the center with two wolves beside her, the space vast and welcoming, not threatening",
            "a pen and ink illustration with watercolor: a woman seen from behind walking toward open light, a wolf on each side, figures rendered as silhouettes against the warm pale edge of the composition, the direction unmistakable",
            "an ink and watercolor drawing: an extreme close-up of a woman's hands, a fox pressing its nose against her palm, rendered in careful pen line with gray-blue wash and warm rust on the fox, nothing else in the frame",
            "a narrative ink and watercolor illustration: a woman and a wolf sitting back to back, both looking outward in opposite directions, the composition square and still, cool gray palette, a raven overhead",
            "an ink and watercolor illustration: side-by-side close-up of a woman's face and a wolf's face at the same level, both looking in the same direction, rendered in the same confident line quality with gray-blue watercolor",
            "an ink and watercolor composition: a woman and her pack emerging from dark forest into open space, the composition moving from heavy ink-dark trees on the left to pale wash on the right, movement and arrival unmistakable",
            "a sophisticated ink and watercolor illustration: overhead view of a woman and a fox at her feet, autumn leaves scattered around them on the ground, the figure seen from above, the rust-red of the fox and the leaves the only warmth"
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

    "sovereign": {
        "label": "sovereign",
        "age_range": "now",
        "slider_position": 6,
        "bio_poem": (
            "You built the table. You chose who sits there.\n"
            "The dogs at your feet, the ring on your hand, the work that is yours.\n"
            "Some nights the table feels too large.\n"
            "Sovereignty is quiet. It does not perform."
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
            "a richly detailed storybook illustration: a woman in a candlelit library surrounded by books and objects of power, two black dogs sleeping at her feet, a raven on the back of her chair, warm amber light from one lamp",
            "a dark storybook illustration: a woman standing in a doorway at night, wolves visible in the moonlit garden behind her, the view is from outside looking in, warm interior light against cool night air, a raven on the door frame above",
            "a refined storybook illustration: extreme close-up of a woman's hands holding a meaningful object — a raven feather, a ring, a small dark book — a fox nose just entering the frame from below, the dark warm background out of focus",
            "a storybook illustration: overhead view of a woman's desk at night, lamplight illuminating papers and objects from above, a raven standing among them, a black dog curled at the edge, the woman herself barely visible at the bottom of the frame",
            "a dark elegant storybook illustration: a woman in profile at a high window at night, a wolf sitting beside her at the same level, both looking out at the same dark garden, the glass reflecting both their faces faintly back",
            "a refined gothic storybook illustration: wide view of a candlelit room hung with paintings, a woman small at the far end moving through it, a wolf at her side, a fox in the near doorway, the room itself the main character",
            "a dark storybook illustration: a close-up portrait of a woman and a raven in direct eye contact, her face turned slightly toward it, the raven on her shoulder, the background dark and inhabited, mutual recognition in both faces",
            "a richly illustrated storybook scene: a stone garden at night seen from above, wolves and foxes and ravens arranged in the space below, the woman a still figure at the center, the dark beautiful and entirely chosen"
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
    return "sovereign", ERAS["sovereign"]


def get_era_list():
    """Return eras in slider order for the frontend."""
    return sorted(
        [{"key": k, **{f: v[f] for f in ["label", "age_range", "slider_position", "description", "bio_poem"]}}
         for k, v in ERAS.items()],
        key=lambda x: x["slider_position"]
    )
