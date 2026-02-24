# Forking Guide: Build Your Own Living Gallery

This repo is designed to be forked. The engine (API integration, frontend, rate limiting) is separated from the content (your eras, your aesthetic DNA). Replace the content, keep the engine.

## Step 1: Define Your Eras

Open `src/prompts/eras.py`. This is where your gallery lives.

Each era needs:

```python
"your_era_key": {
    "label": "Display Name",
    "age_range": "When this happened",
    "slider_position": 1,  # Integer, determines slider order
    "description": "What this era felt like. 2-3 sentences.",
    "color_palette": ["color1", "color2", "color3"],
    "art_references": ["art movement or artist influence"],
    "emotional_texture": "keywords describing the feeling",
    "subjects": [
        "a specific scene DALL-E can paint",
        "another specific scene",
        # Add 6-10 subjects per era for variety
    ],
    "prompt_template": "The DALL-E prompt with {subject}, {color}, {mood} placeholders",
    "moods": [
        "a specific emotional description",
        # Add 3-5 moods per era
    ],
}
```

You can have any number of eras (update the slider max in `public/index.html`).

**Tips for good prompt templates:**
- Start with the art style/medium ("Oil painting in the style of...")
- Include the `{subject}`, `{color}`, and `{mood}` placeholders
- End with "No text. No people's faces shown directly."
- Specify "Style: natural" or "Style: vivid" (vivid is more dramatic)

**Tips for good subjects:**
- Be specific and visual ("a window seat during a rainstorm with a book left open")
- Avoid abstract concepts ("sadness") in favor of concrete scenes that evoke them
- Include environmental details (lighting, time of day, weather)
- Each subject should be different enough to produce visually distinct results

## Step 2: Set Your Baseline

Open `src/prompts/baseline.py`. This is your artistic fingerprint.

The baseline prompt runs underneath every era. It encodes what makes all your art recognizably yours. Think about:

- What medium do you gravitate toward? (oil painting, watercolor, photography, digital)
- What quality makes something feel like *your* taste?
- What do you never want in the image? (text, specific faces, certain styles)

## Step 3: Configure and Deploy

1. Get an OpenAI API key at https://platform.openai.com
2. Copy `.env.example` to `.env`, add your key
3. Adjust rate limits in `.env` to match your budget
4. Deploy to Vercel, Railway, Render, or any Python host

## Cost Estimation

| Browsing Pattern | Images/Visit | Cost/Visit |
|-----------------|-------------|-----------|
| Quick look (2 min) | 2-3 | $0.08-0.12 |
| Exploratory (10 min) | 5-8 | $0.20-0.32 |
| Deep engagement (30 min) | 15-20 | $0.60-0.80 |

At $0.04/image (standard quality), budget roughly $1-5/day for a personal gallery with light traffic.

## Ideas for Your Gallery

The era-slider concept works for many autobiographical structures:

- **Seasons of a relationship** (meeting, honeymoon, settling, crisis, renewal)
- **Career arc** (student, junior, mastery, leadership, legacy)
- **Places you've lived** (each city/home as an era with its own visual DNA)
- **Creative phases** (each body of work as an era)
- **Grief process** (denial, anger, bargaining, depression, acceptance, as visual)
- **Parenthood** (pregnancy, newborn, toddler, school age, teenager, empty nest)

The system doesn't judge your eras. It just needs specific visual instructions for each one.
