# Forking Guide: Build Your Own Living Performance

This repo is designed to be forked. The engine (session management, API integrations, frontend performance) is separated from the content (your eras, your aesthetic DNA, your memory seeds). Replace the content, keep the engine.

---

## What You're Building

A timed generative performance. When a visitor loads the page, the machine pre-generates all content in parallel — poems via Claude, images via gpt-image-1 — then runs through your eras automatically. The viewer watches. The slider is visible. They cannot move it.

---

## Step 1: Define Your Eras

Open `src/prompts/eras.py`. This is where your performance lives.

Each era needs:

```python
"your_era_key": {
    "label": "display name",           # single lowercase word
    "age_range": "when this happened", # e.g. "0–12" or "now"
    "slider_position": 1,              # integer, determines order
    "bio_poem": (                      # fallback poem if Claude API fails
        "line one\n"
        "line two\n"
        "line three\n"
        "line four"
    ),
    "description": "What this era felt like. 2-3 sentences.",
    "developmental_frame": "Psychological theory grounding this era.",
    "emotional_texture": "Keywords describing the feeling of this era.",
    "subjects": [
        # 8-10 subjects per era. EMBED COLOR IN EACH SUBJECT.
        # Each subject is a complete visual description.
        # Vary composition: close-up, wide shot, overhead, interior, exterior.
        # Not every subject needs to include a figure.
        "a detailed description including medium, composition, and specific color palette",
        "another subject with its own embedded color treatment",
    ],
    "moods": [
        "a specific emotional description of the generative register",
        "another mood variant",
        "a third",
        "a fourth",
    ],
    "prompt_template": (
        "Art style and medium description. "
        "What makes this era visually distinct. "
        "Rules for figures, animals, composition. "
        "{subject} "          # DO include this
        "The mood: {mood}. "  # DO include this
        "Emotional resonance: what the image should feel like. "
        "No text anywhere in the image. Square format."
        # DO NOT include {color} — color is embedded in each subject
    ),
}
```

**Tips for subjects:**
- Embed the specific color treatment directly: "warm amber lamplight, deep umber shadows" not a separate color field
- Vary the compositional frame across subjects — overhead, close-up, wide, exterior/interior, macro texture
- Include some subjects without figures (objects, environments, traces of presence)
- Be specific enough that gpt-image-1 has clear visual instructions, not mood words
- 8-10 subjects gives enough variety across sessions that repeat visitors see different images

**Tips for prompt templates:**
- Lead with the medium and art style — this is the most important signal to gpt-image-1
- Include explicit rules about what you never want (text, certain styles, specific elements)
- The `{subject}` and `{mood}` placeholders are assembled by `assembler.py` at runtime
- Do not use a `{color}` placeholder — colors belong in the subjects

---

## Step 2: Write Your Poem Seeds

Open `src/prompts/poem_seeds.py`. This controls what Claude generates for each era.

There are two parts:

**The system prompt** (shared across all eras) defines how Claude speaks. The default voice is fragmented first-person memory. Edit it to match your performance's voice — but keep it specific about format (4 lines, no rhyme, etc.) or Claude will drift.

**Per-era prompts** give Claude the psychological and biographical material to draw from. Each era's prompt should:
- Describe the recurring emotional logic of the era, not a single event
- Include sensory and biographical specifics (the more specific, the better the output)
- End with an instruction like "Write a poem that carries the texture of this entire era — not one afternoon. The whole thing."

```python
ERA_SEEDS = {
    "your_era_key": {
        "era_key": "your_era_key",
        "age_range": "when",
        "prompt": (
            "Generate a 4-line poem from the accumulated experience of [who this person was]. "
            "The recurring emotional logic of this era: [specific memory fragments, "
            "recurring patterns, sensory details, psychological textures]. "
            "Write a poem that carries the texture of this entire era. "
            "Not one [moment/afternoon/night]. The whole [era name]."
        ),
    },
}
```

---

## Step 3: Set Your Baseline

Open `src/prompts/baseline.py`. This is your artistic fingerprint — the DNA that runs under every era.

The baseline prepends every image prompt. It encodes what makes all your art recognizably yours across eras. Think about:

- What medium or style family connects all your work?
- What figures, animals, or motifs appear throughout?
- What do you absolutely never want? (text in the image, certain aesthetics, specific subjects)
- What quality of mark, light, or composition is consistent?

Keep it under 300 words. The baseline should constrain, not dominate. Each era's prompt template and subjects provide the specifics. The baseline provides the through-line.

---

## Step 4: Configure and Deploy

1. Copy `.env.example` to `.env`
2. Add your `OPENAI_API_KEY` (for gpt-image-1 images)
3. Add your `ANTHROPIC_API_KEY` (for Claude poems)
4. Deploy to Render using the included `render.yaml`, or any Python host

**Required environment variables:**
```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

---

## Step 5: Update the Frontend Performance Text

The explainer text, breather sequence, and ending text are in `public/gallery.js` as JavaScript constants at the top of the file. Update them to match your performance's voice and premise.

The slider labels are pulled from the era definitions in `eras.py` — update `label` and `age_range` there.

---

## Cost

**Per visitor session (default config):**
| Item | Model | Cost |
|------|-------|------|
| 6 images | gpt-image-1 medium quality | ~$0.25 |
| 6 poems | Claude Sonnet 4-6 | ~$0.015 |
| **Total** | | **~$0.27/session** |

**Cheaper configuration (~4× savings):**

In `src/api/generate.py`, change:
```python
quality="medium"  →  quality="low"   # $0.042 → $0.011 per image
```

In `src/api/poem_gen.py`, change:
```python
model="claude-sonnet-4-6"  →  model="claude-haiku-4-5-20251001"
```

Combined: ~$0.067/session. Haiku handles 4-line poems well. Low-quality gpt-image-1 still produces the same stylistic output.

---

## Ideas for Your Gallery

The era-slider performance structure works for many autobiographical shapes:

- **Seasons of a relationship** (meeting, honeymoon, settling, crisis, renewal)
- **Career arc** (student, junior, mastery, leadership, legacy)
- **Places you've lived** (each city or home as an era with its own visual DNA)
- **Creative phases** (each body of work as an era)
- **Grief process** (the Kübler-Ross stages as visual eras)
- **Parenthood** (pregnancy through empty nest)
- **A year that changed everything** (each month as an era)

The system doesn't judge your eras. It needs specific visual instructions and specific memory material. The specificity is what makes it feel true.
