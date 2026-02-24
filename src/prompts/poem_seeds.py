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
- Never use anyone's name. Refer to people only by their relationship to the memory: the teacher, the husband, the machine, the child, the dog, the one who left. The viewer is the only witness here."""

ERA_SEEDS = {
    "wonder": {
        "era_key": "wonder",
        "age_range": "0–12",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a neurodivergent child "
            "(age 4-12) who sees patterns the adults don't want seen. An army brat, always "
            "moving, always the new kid who watches too carefully. She memorizes the rules "
            "and then watches everyone break them. She draws because paper doesn't lie. "
            "Memory fragments: new school every two years, drawing as the only honest "
            "language, adults whose smiles didn't match their words, rules that only applied "
            "to her, forests as the only honest place, dogs as the only consistent love, "
            "the art teacher whose words matched her face, saying the thing everyone "
            "pretended not to see and being punished for it, building worlds on paper because "
            "the real one had broken rules. The child doesn't have adult language for what "
            "she sees. She just knows something is wrong and no one will say it. Pick ONE "
            "specific sensory memory and let it unspool into exactly 4 lines."
        ),
    },
    "becoming": {
        "era_key": "becoming",
        "age_range": "13–17",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a neurodivergent teenager "
            "(13-17) whose pattern recognition has become conscious. She can now NAME what was "
            "wrong. She watches her parents, her teachers, her peers perform rules they don't "
            "follow. She paints with fury because she's been told her accuracy is a personality "
            "flaw. Memory fragments: anger had somewhere to go but her brain never stopped "
            "cataloging, performing versions to survive systems she'd decoded, patterns in fake "
            "smiles as a fluent language by fifteen, rage on canvas because a quiet girl with "
            "insights was dangerous, the guidance counselor who'd given up on her own life, "
            "they failed to protect her and told her to trust the system that failed, the "
            "intensity wasn't a disorder it was accuracy and nobody wanted accuracy. She's a "
            "teenager so the emotions are huge and the language is becoming sharp but not yet "
            "refined. Pick ONE specific sensory memory and let it unspool into exactly 4 lines."
        ),
    },
    "proving": {
        "era_key": "proving",
        "age_range": "18–29",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a woman in her twenties "
            "with a perfect-looking life that isn't hers. Memory fragments: raising siblings "
            "while building a career, a marriage easy the way giving up is easy, self-portraits "
            "with the eyes right but not the truth, the specific boredom of a safe marriage, "
            "performing gratitude for a life you didn't choose, paintings technically perfect "
            "and emotionally empty, stable until stable feels like slow death, the most talented "
            "person in every room and the least free. Pick ONE specific sensory memory and let "
            "it unspool into exactly 4 lines."
        ),
    },
    "unraveling": {
        "era_key": "unraveling",
        "age_range": "~30",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a woman going through "
            "divorce at 30 whose art breaks open into raw black ink with red as the only color. "
            "Memory fragments: divorce papers and the light was wrong, drew yourself split in "
            "half, silence of an apartment meant for two, red ink the only color that made "
            "sense, drawings got honest when everything fell apart, drawing at 3am because "
            "sleep felt like giving up, bodies connected by red thread pulling apart, the shame "
            "wasn't the failure it was how long you pretended, hands shook for a month and the "
            "drawings got better, panic came in waves and you drew between them. Pick ONE "
            "specific sensory memory and let it unspool into exactly 4 lines."
        ),
    },
    "reconstruction": {
        "era_key": "reconstruction",
        "age_range": "31–37",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a woman rebuilding after "
            "collapse. Mind heart body aligning for the first time. Memory fragments: first "
            "morning you didn't reach for someone who wasn't there, body in the gym as first "
            "thing that was yours again, wolves started appearing in every painting, hot yoga "
            "at 6am the sweat and the silence, the doctorate felt like a dare, the palette "
            "went quiet grays blues rust gold, adopted a shepherd and remembered loyalty, the "
            "first painting without anger and it was better, discipline wasn't punishment "
            "anymore it was architecture. Pick ONE specific sensory memory and let it unspool "
            "into exactly 4 lines."
        ),
    },
    "sovereign": {
        "era_key": "sovereign",
        "age_range": "now",
        "prompt": (
            "Generate a 4-line poem from the fragmented memories of a woman who has arrived "
            "but knows arrival is a construction. Memory fragments: Tudor house with art on "
            "walls and dogs on couches, someone asleep while you sketch at midnight, building "
            "a robot in the garage, paintings dark and elegant and unexplained, you built the "
            "table and chose who sits there, sovereignty is quiet it does not perform, some "
            "nights the table feels too large, you chose all of this and could un-choose it "
            "and that is the vertigo, the loneliness of knowing meaning is constructed and "
            "you built it. Pick ONE specific sensory memory and let it unspool into exactly "
            "4 lines."
        ),
    },
}
