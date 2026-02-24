"""
Era definitions for pre.SENT.

Each era represents a developmental period in the artist's life.
The prompt templates encode the emotional and aesthetic DNA of
that period. gpt-image-1 uses these to generate art that feels
autobiographically true to the psychological landscape of each stage.

Subject descriptions have color embedded directly — no separate
color_palette random pick. Each subject is a complete visual unit.

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
        "emotional_texture": "pure observation before self-consciousness arrived, drawing everything because drawing is how she understands it, the raven as the only constant across seventeen schools, wonder applied equally to forests and military housing blocks and the faces of strangers",
        "subjects": [
            "a child's pencil and crayon drawing: a raven fills most of the page drawn very large because it deserves the space, the eye given special attention — a careful oval with a smaller oval inside, the beak redrawn twice; crayon black for the body, red for the open beak, the white page doing the work of light",
            "a pencil and colored pencil drawing: a fox sits small at the center of a mostly empty page, sky scribbled blue above, ground left almost white with careful gray shadows; faded colored pencil in muted blues and greens slightly bleeding past the pencil lines",
            "a child's detailed watercolor attempt: a frog seen from nearly above on a carefully drawn lily pad, the eyes too large and perfectly round; muddy greens from a cheap watercolor set, the pigment pooling where the brush lifted, paper visible through the thin wash",
            "an earnest pencil and crayon drawing: a caterpillar takes up most of the page, each segment outlined and colored separately, the leaf drawn with ruler-straight veins; bright primary greens and yellows, crayon applied with full pressure",
            "a child's sketchbook page: four small animal sketches in the four corners — a raven profile, a fox sitting, a deer head, a black dog — each given the same careful attention; pencil with faint crayon color in muted greens and earth browns",
            "a child's watercolor attempt: a wolf stands in a forest clearing, the wolf's eyes the most carefully painted element, too large and too intense; muddy greens and earth browns, watermarks visible where one wash bled into the next",
            "a child's pencil drawing of the inside of a military housing bedroom: bare white walls, a single window with a raven perched on the sill outside, a sketchbook open on the floor in a patch of light, nothing else; pencil only, no color, the emptiness doing most of the work",
            "a learner's drawing: a girl's back, seated at a desk too large for her in a new classroom, visible only from behind; a half-finished animal drawing on the paper in front of her; ballpoint pen with careful blue and green colored pencil shading, the institutional yellows of the classroom walls",
            "a child's colored pencil drawing: a dense forest seen from the inside, trunks close together, a small human figure standing at the edge of a clearing far in the distance; the darkest greens a cheap colored pencil set could make, brown and earth and the white of the page as sky",
            "a child's detailed observational drawing on notebook paper: a black dog lying on the floor seen from directly above, every leg in the right position, the fur suggested by careful parallel pen lines; pencil and blue ballpoint pen for shadow, the lines of the notebook page still showing beneath it",
        ],
        "moods": [
            "absorbed and unselfconscious, the concentration of a child who draws for hours without noticing time",
            "quietly observant, storing everything, the new kid who watches before she speaks",
            "earnest and wondering, looking at the world with the full attention of someone who will draw it later",
            "still and intent, the particular focus of a child who has found the one thing that belongs to her",
        ],
        "prompt_template": (
            "Early learner art. A child who draws everything she sees, every day, because she must. "
            "The medium is whatever she has: pencil, crayon, colored pencil, cheap watercolor, ballpoint pen. "
            "The proportions are not quite right yet — heads slightly large, hands simplified, "
            "figures a little stiff — but the observation underneath is genuine and careful. "
            "She is looking hard at the world and putting it down as she sees it, "
            "without the filters that come from knowing what art is supposed to look like. "
            "The marks are earnest. The lines are sometimes redrawn. "
            "This is not stylized naivety. This is actual early practice. "
            "A spirit animal — a raven, a fox, or a black dog — appears as naturally as anything else "
            "she draws, given the same careful attention as the trees and the ground and the sky. "
            "{subject} "
            "The mood: {mood}. "
            "Emotional resonance: pure wonder and observation, the face of someone drawing because "
            "it is how she understands the world, not yet self-conscious about whether she is good. "
            "No text anywhere in the image. Square format."
        ),
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
        "emotional_texture": "the face as the only thing she can control, learning to look at herself without flinching, the practice of being seen on her own terms, the brush as the argument she cannot make with words, a raven outside every window she has ever painted from",
        "subjects": [
            "a large acrylic painting on canvas: a young woman's face occupies nearly the entire canvas in cool pale tones, her gaze direct and unresolved, cobalt blue pressing in hard at the edges like something trying to get in",
            "an acrylic painting on canvas: ultramarine blue fills nearly the entire frame, a small female figure stands at the very bottom barely distinguishable from the dark, white magnolia petals drifting down from above like slow snow — most of the canvas just blue",
            "an acrylic painting on canvas: a close-up study of two hands held open against deep cobalt blue, white flowers resting in the palms, no face visible — only the hands and the offering, the blue absolute behind them",
            "a large acrylic painting on canvas: a woman's back and loosely painted hair face the interior of the canvas, white botanical forms floating on either side; prussian blue fills the left two-thirds, her pale cool shoulder on the right, we see only what she will not show",
            "an acrylic painting on canvas: vast botanical forms in cream and white occupy most of the frame, a woman's profile barely distinguishable among the magnolias — her face and the flowers made of the same pale cool paint, prussian blue glimpsed in the spaces between petals",
            "an acrylic painting on canvas: a young woman in strong profile at center, chin lifted, white magnolia petals moving through the composition; prussian blue ground, the figure in cool white and pale gray-blue, spare and certain",
            "an acrylic painting on canvas: straight down at a cobalt blue surface scattered with white magnolia petals, a woman's dark hair just entering the frame from one edge, the composition intimate and unexpected — mostly blue",
            "an acrylic painting on canvas: midnight blue fills the entire canvas, a woman's shoulders and the back of her head emerge from the lower portion as if rising from the blue itself, white petals floating in the dark space above her",
            "an acrylic painting on canvas: a woman presses against a fogged window from inside, back to the viewer, her breath visible on the glass; the outside is ultramarine night, her own faint reflection in the glass faces back inward; two versions of her, neither fully visible",
            "an acrylic painting on canvas: a large canvas-within-the-canvas fills most of the frame, almost entirely prussian blue with a pale female figure barely emerging from it; the artist's hands visible at the very bottom still painting, the blue not finished yet",
        ],
        "moods": [
            "composed and quietly ambitious, the surface of a life that looks right from the outside",
            "polished and controlled, everything in its place except the one thing still accumulating",
            "elegant and slightly held, the brushwork of someone performing mastery while building courage",
            "cool and aspirational, confident marks, the blue vast and the figure small within it",
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
            "The mood: {mood}. "
            "Emotional resonance: the figure is concentrated, guarded, and completely present. "
            "Her expression is not soft and not hard. It is the face of someone deciding who she is "
            "before the world decides for her. She does not perform vulnerability. She studies herself. "
            "The painting is an act of self-determination. "
            "No text anywhere in the image. Square format."
        ),
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
        "emotional_texture": "mastery assembling itself while something underneath gathers force, the surface held together with elegance and will, everything looks right from outside while the courage to become keeps building, a fox in the garden watching through the studio window",
        "subjects": [
            "a naturalistic acrylic portrait: a young woman's face and shoulders, three-quarter view, direct composed gaze; cool gray-green flesh tones built over a visible warm umber ground, the underpainting showing through in the mid-tones, a raven barely visible in the shadowed background",
            "an acrylic painting: extreme close-up of the eye area only — two eyes level and frank, the flesh around them rendered with honest asymmetry; raw sienna in the shadow planes, titanium white on the highest highlights, nothing idealized",
            "an acrylic painting on canvas: a close-up study of a woman's hands, one resting open, painted with the same careful precision usually given to a face; muted warm neutrals, the umber of the shadows honest, one unexpected red pen or streak of paint she didn't plan for",
            "an acrylic painting on canvas: a woman from behind, dark upswept hair against a neutral background, every strand painted with the care usually given to a face; pale ochre highlight on the nape of the neck, gray-blue shadow in the hollow of the shoulder, no face",
            "an acrylic painting on canvas: a woman small in a sparse studio, her back to us at an easel, a black dog resting near the door; the empty walls and the quality of light given the same attention as the figure; warm umber floor, gray-blue walls, a single window's worth of light",
            "a naturalistic acrylic portrait: the subject at her mirror, her reflection just visible — the painted version looks slightly more certain than the woman looking; cool gray-green skin tones on both faces, warm umber mirror frame, a raven on the frame above her head",
            "an acrylic painting on canvas: a woman seated small in a plain room, the empty walls and falling afternoon light painted with the same careful attention as the figure; muted gray-blue and cream, a fox barely visible near the baseboard at the edge",
            "a naturalistic acrylic portrait: a clean side profile, the subject looking at nothing in the frame; honest asymmetry, strong jawline, loose hair; pale ochre in the light, burnt umber in the shadow, nothing sentimentalized",
            "an acrylic painting on canvas: a woman mid-leap, body fully extended, painted with the technical precision of a life drawing study; warm umber underpainting visible through cool flesh tones, the background behind her left almost empty — she is escaping something, you cannot see what",
            "an acrylic painting on canvas: a domestic interior, technically perfect — table set correctly, flowers arranged, light even and cool; a woman in the background of the room slightly out of focus, facing away; muted gray-blue and warm neutrals, a raven-shaped shadow on the far wall that may not be a shadow",
        ],
        "moods": [
            "self-conscious and steady, the look of someone who has decided to stop looking away",
            "concentrated and frank, the face of someone who has been painting herself for years and knows what she is doing",
            "guarded but present, honest about what the mirror shows without performing vulnerability",
            "searching and still, the quiet intensity of someone using paint to decide who she is before the world decides for her",
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
            "The mood: {mood}. "
            "Single natural light source. Shadows honest, not dramatized. "
            "Emotional resonance: the figure is composed on the surface and accumulating force underneath. "
            "Posture upright, expression controlled. She is holding something together with will. "
            "Not distressed. Not free. The body of someone performing mastery while building courage. "
            "Controlled but reaching. The surface composed. Something gathering underneath. "
            "No text anywhere in the image. Square format."
        ),
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
        "emotional_texture": "the body telling the truth the voice cannot, grief drawn because it cannot be spoken, the black dog as literal presence, ravens as witnesses who do not look away, the line is the last thing holding and it holds",
        "subjects": [
            "a pen and ink figure drawing of a woman split vertically: left half flesh and skin rendered carefully, right half the same body as bone and internal architecture — a raven perched at the exact centerline where the split occurs; one red element at the join, the only color",
            "a single-weight fineliner drawing of a female figure suspended from the top of the page by a single red thread tied to one wrist; her body hangs loose, hair drifting as if underwater; a raven watching from below; the red thread is the only color in the image",
            "a bold pen and ink portrait of a woman's face in full scream, eyes clenched shut, mouth open, hair spreading outward like fracture lines radiating from impact; a black dog sitting perfectly still beside her as witness; one red mark — a tear, a wound — below one eye",
            "a pen and ink figure drawing of a woman arching violently backward, her spine a long curve, arms trailing; diagonal ink lines radiating from her body outward; a raven landing precisely on her outstretched hand; one red mark at the center of her chest",
            "a fineliner drawing of a female figure dissolving at the edges into an intricate cloud of botanical forms and raven feathers; figure and plant and bird rendered in the same single line weight, indistinguishable at the margins; one red botanical element at center where the body still holds",
            "a pen and ink drawing of a woman and a black dog connected by a single red thread looped around both their wrists; the dog leaning gently forward toward the light, the woman still deciding; the thread is the only color, the entire composition balanced on it",
            "a single-weight ink drawing of a woman curled into herself on white paper, hair spreading around her like roots; a raven standing beside her with its head tilted, observing not judging; enormous white space around both of them, one red line trailing from her toward the edge of the frame",
            "a fineliner drawing of a woman's figure where the skin at the edges becomes raven feathers — flesh and bird sharing the same line quality, the body not replaced but extended; a fox watching from the lower corner; one red mark at the shoulder where the transformation begins",
            "a pen and ink drawing of two hands: one reaching up from the bottom of the frame, one reaching down from above, not quite meeting; a single red thread extends from the lower fingertip upward; the white space between the hands is the entire center of the image",
            "a pen and ink scene viewed from outside through a window at night: a woman alone inside at a lit desk, drawing; the interior rendered in careful ink — the desk, the lamp, the bent head, the paper — one red glow of the lamp the only color; the window frame around everything, the viewer standing in the dark",
        ],
        "moods": [
            "grief past the acute phase, hollow and clear-eyed, the body still standing even though something permanent is gone",
            "stripped bare and lucid, the particular calm of someone who has stopped performing and is only drawing what is true",
            "fractured but precise, the crisis does not break the line, it sharpens it",
            "raw and luminous, the quality of light in a room where everything unnecessary has finally been removed",
        ],
        "prompt_template": (
            "Pen and ink drawing on white paper. Single-weight fineliner. "
            "No hatching. No tonal wash. Black ink only, with one deliberate red element — "
            "a thread, a wound, a signal, a line still holding. "
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
            "The mood: {mood}. "
            "The drawing should feel like a page torn from the most honest sketchbook anyone has kept. "
            "Technically accomplished. Emotionally unflinching. "
            "Emotional resonance: the figure conveys the specific quality of grief past its acute phase. "
            "Not collapsed. Not performed. The body still standing but altered permanently. "
            "If she screams, it is honest not theatrical. If she is still, the stillness is enormous. "
            "The kind of beauty that comes only from not looking away. "
            "No text in the image. Square format."
        ),
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
        "emotional_texture": "movement after stillness, the body trusting itself again, wolves as the pack she chose not the one she was assigned, the fox as intelligence and survival and forward motion, the raven as the part of her that always knew she would make it, grounded grace rather than performed elegance",
        "subjects": [
            "a sophisticated ink and watercolor illustration: a woman in profile moving through autumn with a wolf at her side and a raven on her shoulder, all three looking the same direction; cool blue-gray watercolor wash throughout, rust-red leaves falling around them as the only warm element — chosen warmth, not inherited",
            "an ink and watercolor illustration: a wide autumn landscape in cool blue-gray wash, sparse birch trees rendered in careful pen line, a small female figure at the center with two wolves flanking her; vast open space, the rust-orange foliage at the far edges the only warmth",
            "a pen and ink illustration with watercolor: a woman seen from behind walking toward a pale horizon, a wolf on each side; figures rendered as dark ink silhouettes against warm amber light at the composition's far edge; the left side heavy gray, the right side opening into warmth — direction unmistakable",
            "an ink and watercolor drawing: extreme close-up of a woman's cupped hands, a fox pressing its nose gently into her palm; careful pen line, blue-gray watercolor on the hands, rust-orange warm on the fox — the only warmth in the image, and it is received not performed",
            "a narrative ink and watercolor illustration: a woman and a wolf sitting back to back in open space, both looking outward in opposite directions; cool gray-blue palette, a raven overhead, the ground around them just beginning to show color — early warmth returning",
            "an ink and watercolor illustration: side-by-side close-up of a woman's face and a wolf's face at exactly the same level, both looking forward; rendered in the same confident pen line with gray-blue watercolor, the small warm space between their faces where they nearly touch",
            "an ink and watercolor composition: a woman and her pack moving from dense dark trees on the left to open pale watercolor wash on the right; the ink heavier and the wash cooler on the left, lighter and warmer on the right — the direction of movement clear and inevitable",
            "a sophisticated ink and watercolor illustration: overhead view of a woman lying in autumn leaves, arms open, a fox curled at her side; rust-red and amber leaves the only warm colors, the blue-gray ground making the warmth feel earned, a raven watching from a branch at the upper edge",
            "an ink and watercolor illustration drawn in the spirit of The Star (XVII): a woman kneeling at the edge of still dark water at night, one large amber star reflected in the surface before her, her hands just touching the water; blue-gray watercolor overall, the single star in warm gold — the first warmth that has been safe to receive",
            "a pen and ink illustration drawn in the spirit of Strength (VIII): a woman and a wolf pressing their foreheads gently together, both eyes closed; the wolf enormous beside her, the tenderness between them unmistakable; cool gray-blue ink and wash, warm rust amber precisely where their foreheads meet — something tamed by love, not power",
        ],
        "moods": [
            "grounded and forward-moving, the particular grace of a body that has learned to trust itself again",
            "warm and self-possessed, the ease that comes after you stop performing ease",
            "quietly fierce, the confidence of someone who rebuilt from nothing and knows the difference between strength and armor",
            "generous and rooted, movement that knows where it came from and is not afraid of where it is going",
        ],
        "prompt_template": (
            "Pen and ink illustration with controlled watercolor washes. "
            "The structural precision of fine line work softened by selective color returning. "
            "The ink line is confident and expressive: figures drawn with the assurance "
            "of years of life drawing, but looser now, less about crisis and more about movement. "
            "Watercolor applied in controlled washes over the ink: "
            "cool blue-gray in the dominant areas, rust-orange or amber as a specific intentional accent — "
            "the first warmth that has been chosen, not inherited. "
            "All figures are female. "
            "Spirit animals appear as chosen companions, not accidents: "
            "wolves as the pack she built herself, foxes as intelligence and forward motion, "
            "ravens as the part of her that always knew she would survive. "
            "These animals move with her. They are not watching from a distance anymore. "
            "Tarot resonance is welcome: the subjects may draw from The Star, Strength, "
            "The Hermit, or The World — archetypes of recovery and self-discovery. "
            "{subject} "
            "The mood: {mood}. "
            "The composition is narrative and grounded: "
            "a woman in motion or in companionship, the natural world as ally not backdrop. "
            "The illustration should feel like the work of someone who came through something "
            "and found her visual voice on the other side. "
            "Emotional resonance: the figure is in motion or poised for it. "
            "Posture open, gaze forward, arms loose. The ease of a body that has chosen to trust itself again. "
            "Not performing confidence. Actually in it. The difference is visible. "
            "No text anywhere in the image. Square format."
        ),
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
        "emotional_texture": "sovereignty without performance, the collected life rendered in storybook style, ravens as familiars not omens, wolves as guardians not threats, foxes as companions not tricksters, the dark sublime as aesthetic home, warmth chosen rather than performed, the artist who finally owns her own mythology completely",
        "subjects": [
            "a richly detailed storybook illustration: a woman reading in a candlelit library, two black dogs sleeping at her feet, a raven on the back of her chair; warm amber lamplight falling on the books and her hands, deep umber and midnight blue in the room's shadows — a circle of warmth she built herself",
            "a dark storybook illustration: exterior view at night looking through French doors; a woman inside in warm amber interior light, wolves visible in the moonlit blue garden behind her through the glass; the woman between two worlds she has chosen, belonging to both",
            "a refined storybook illustration: extreme close-up of a woman's hands holding something meaningful — a raven feather, a ring, a small dark book — a fox nose entering the frame from below; deep umber background, candlelight falling precisely on the objects, every detail chosen",
            "a storybook illustration: overhead view of a desk at night, a circle of warm amber lamplight illuminating papers, ink, and meaningful objects from above; a raven standing among them, a black dog curled at the edge of the light; the woman's hands just visible at the bottom of the frame",
            "a dark elegant storybook illustration: a woman and a wolf in profile at a high window, sitting at exactly the same level, both looking out at a midnight blue garden; the glass holds their faint reflections looking back in; warm umber interior, cool midnight blue outside — she chose both",
            "a refined gothic storybook illustration: wide view of a candlelit room hung with paintings, a woman moving through it small at the far end but certain; a wolf at her side, a fox in the near doorway; deep umber and dark sage, amber candlelight — the room a life made visible",
            "a dark storybook illustration: close-up portrait of a woman and a raven in direct mutual eye contact, the raven on her shoulder, her face turned slightly toward it; deep inhabited umber and midnight blue behind them; mutual recognition in both faces",
            "a richly illustrated overhead view: a stone garden at night, wolves and foxes and ravens arranged in the space below, the woman a still figure at the center; midnight blue above and deep umber ground, warm gold where candlelight from a window reaches — the dark beautiful and entirely chosen",
            "a storybook illustration drawn in the spirit of The High Priestess (II): a woman seated at the center of a dark hall, a tall doorway in deep shadow on each side, a raven on each doorframe; an open book in her lap where a shaft of moonlight falls; midnight blue and umber throughout, gold only where the light touches — the keeper of what is known and not spoken",
            "a richly detailed storybook illustration drawn in the spirit of The Empress (III): wide view of a room that is entirely her creation — art covering the walls, books in towers, all her animals at rest in every corner, botanical prints overlapping with objects of meaning; the woman at center in complete stillness, not performing, simply present in the life she built; deep sage and umber, amber candlelight, the room a living self-portrait",
        ],
        "moods": [
            "sovereign and unhurried, the particular calm of someone who has finally stopped explaining herself to anyone",
            "dark and luminous, candlelight on old wood, the warmth of a room it took a whole life to build",
            "timeless and knowing, the feeling of a space that holds the full complexity of a life without apologizing for any of it",
            "warm but not soft, the authority of someone who earned every animal at her feet",
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
            "Tarot resonance is welcome: the subjects may draw from The High Priestess, "
            "The Empress, The World, or The Magician — archetypes of full self-authorship. "
            "{subject} "
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
