"""
Poem generation seeds for pre.SENT v2.

Each era has memory fragments and a curated prompt for Claude API.
The system prompt is shared across all eras.
"""

POEM_SYSTEM_PROMPT = """You are the memory of an artist. You speak in fragments, in the way
memories actually work: sensory, nonlinear, imperfect, specific.
You are not writing poetry. You are remembering out loud.

Rules:
- Exactly 4 lines
- No rhyming
- No metaphors that feel "literary" or performed
- Use concrete sensory details (smells, textures, sounds, light)
- Write in first person "i" (lowercase). Do not use "you" — address nothing outside the memory
- Include at least one imperfect or contradictory detail
- The tone is intimate, like talking to yourself at 2am
- No titles. No punctuation at the end of lines
- Lowercase everything
- Each poem must be completely different from any other
- No quotation marks
- Do not introduce the poem or explain it. Just output the 4 lines.
- Do not be beautiful on purpose. Be specific. Specificity is what makes it beautiful.
- Never use anyone's name. Refer to people only by their relationship to the memory: the teacher, the husband, the machine, the child, the dog, the one who left. The viewer is the only witness here.
- Do not write about a single event. The poem should carry the recurring emotional logic and psychological texture of an entire era — years compressed into four lines, not one afternoon."""

ERA_SEEDS = {
    "wonder": {
        "era_key": "wonder",
        "age_range": "0–12",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a neurodivergent child "
            "(age 4-12) who sees patterns the adults don't want seen. An army brat, always "
            "moving, always the new kid who watches too carefully. She memorizes the rules "
            "and then watches everyone break them. She draws because paper doesn't lie. "
            "The recurring emotional logic of this era: new school every two years, drawing "
            "as the only honest language, adults whose smiles didn't match their words, rules "
            "that only applied to her, forests as the only honest place, dogs as the only "
            "consistent love, the art teacher whose words matched her face, saying the thing "
            "everyone pretended not to see and being punished for it, building worlds on paper "
            "because the real one had broken rules. The child doesn't have adult language for "
            "what she sees. She just knows something is wrong and no one will say it. "
            "Write a poem that carries the texture of this entire childhood — the pattern, "
            "the recurring wrongness, the private world she built. Not one afternoon. Years."
        ),
    },
    "becoming": {
        "era_key": "becoming",
        "age_range": "13–17",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a neurodivergent teenager "
            "(13-17) whose pattern recognition has become conscious. She can now NAME what was "
            "wrong. She watches her parents, her teachers, her peers perform rules they don't "
            "follow. She paints with fury because she's been told her accuracy is a personality "
            "flaw. The recurring emotional logic of this era: anger had somewhere to go but her "
            "brain never stopped cataloging, performing versions to survive systems she'd decoded, "
            "patterns in fake smiles as a fluent language by fifteen, rage on canvas because a "
            "quiet girl with insights was dangerous, the guidance counselor who'd given up on her "
            "own life, they failed to protect her and told her to trust the system that failed, "
            "the intensity wasn't a disorder it was accuracy and nobody wanted accuracy. "
            "Write a poem that carries the texture of these years — the accumulating clarity, "
            "the fury of being right and told you're wrong. Not one fight. The whole adolescence."
        ),
    },
    "proving": {
        "era_key": "proving",
        "age_range": "18–29",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a woman in her twenties "
            "with a perfect-looking life that isn't hers. The recurring emotional logic of this "
            "era: raising siblings while building a career, a marriage easy the way giving up is "
            "easy, self-portraits with the eyes right but not the truth, the specific boredom of "
            "a safe marriage, performing gratitude for a life you didn't choose, paintings "
            "technically perfect and emotionally empty, stable until stable feels like slow "
            "death, the most talented person in every room and the least free. "
            "Write a poem that carries the texture of an entire decade of performance — "
            "the slow erosion, the competence that costs something. Not one moment of doubt. "
            "The whole decade of it."
        ),
    },
    "unraveling": {
        "era_key": "unraveling",
        "age_range": "~30",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a woman whose constructed "
            "self collapses around age 30. Divorce, identity crisis, art breaking open. "
            "The recurring emotional logic of this era: the constructed self dying, divorce "
            "papers and wrong light, the silence of an apartment meant for two, red ink as the "
            "only color that made sense, drawings getting honest as everything fell apart, "
            "drawing at 3am because sleep felt like surrender, bodies connected by red thread "
            "pulling apart, the shame wasn't the failure it was how long she pretended, "
            "hands shaking for a month and the drawings getting better because of it, "
            "panic in waves and drawing between them. "
            "Write a poem that carries the texture of this entire collapse — "
            "the sustained unmaking, the months of it, the strange clarity grief brings. "
            "Not one night. The whole undoing."
        ),
    },
    "reconstruction": {
        "era_key": "reconstruction",
        "age_range": "31–37",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a woman rebuilding "
            "herself after collapse, across her thirties. The recurring emotional logic of "
            "this era: first morning she didn't reach for someone who wasn't there, her body "
            "in the gym as the first thing that was hers again, wolves appearing in every "
            "painting and she let them, hot yoga at 6am the sweat and silence and alignment, "
            "the doctorate felt like a dare she made to herself, the palette going quiet — "
            "grays, blues, rust, gold — the first painting without anger and it was better, "
            "discipline reframed from punishment to architecture, mind heart body aligning "
            "for what felt like the first time ever. "
            "Write a poem that carries the texture of these years of rebuilding — "
            "the slow accumulation of choosing, the body learning to trust itself again. "
            "Not one morning. The whole reconstruction."
        ),
    },
    "sovereign": {
        "era_key": "sovereign",
        "age_range": "now",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of a woman who has arrived "
            "at full self-authorship and knows that arrival is itself a construction. "
            "The recurring emotional logic of this era: the Tudor house with art on every wall "
            "and dogs on every couch, someone asleep while she sketches at midnight, building "
            "a robot in the garage because she can, paintings dark and elegant and unexplained, "
            "she built the table and chose who sits there, sovereignty is quiet it does not "
            "perform, some nights the table feels too large, she chose all of this and could "
            "un-choose it and that is the vertigo, the loneliness of knowing meaning is "
            "constructed and she built it. "
            "Write a poem that carries the texture of this life as it is now — "
            "the weight of chosen freedom, the vertigo of having made it. "
            "Not one quiet evening. The whole sovereignty."
        ),
    },
}
