# pre.SENT

AI performance art trained on the visual DNA of a real artist. A living gallery that traces one woman's life through six psychological eras, from the cartoonish sarcasm of childhood through the confessional line work of crisis to the refined storybook sovereignty of now. Every image generated in real time. Nothing saved. The AI does not invent. It inherits.

**Live:** [pre-sent.onrender.com](https://pre-sent.onrender.com)

---

## What Is This

pre.SENT is a web-based generative art installation. Visitors arrive at a minimal gallery and use a slider to move through six psychological eras of one woman's life. The system generates original artwork on the spot using DALL-E 3, guided by the actual aesthetic fingerprint of each period: the medium she used, the mark quality, the subjects she returned to, the emotional register of the work.

The gallery auto-advances through the eras. You can take over at any time by moving the slider yourself.

The art is ephemeral. Nothing is stored. When you leave, every image disappears. The gallery exists only in the present tense. That is the point.

---

## The Eras

The slider maps to six stages of a real artistic life. Each era carries its own visual language built from actual practice: medium, mark quality, color palette, compositional instincts, and the spirit animals that ran alongside each period.

| # | Era | Life Stage | Visual Language |
|---|-----|-----------|----------------|
| 1 | **Wonder** | Childhood. Army brat. Always moving. Art as the only room she kept. | Cartoon figures with deadpan expressions in front of loose impressionist environments. Clashing primaries. The humor of a child who has seen too much. A raven follows her. |
| 2 | **Becoming** | Adolescence. The self-portrait as act of self-determination. | Naturalistic acrylic on canvas, painted from the mirror. Cool gray-green flesh tones. Honest asymmetry. The face as the only thing she could control. |
| 3 | **Proving Years** | Early adulthood. A marriage too easy. Everything looks perfect from the outside. | Large-scale acrylic: deep cobalt blue ground, white magnolias floating through it, a female figure emerging. The paintings got ambitious while she stayed composed. |
| 4 | **Unraveling** | Crisis. The brush went down. The fineliner came up. | Single-weight pen and ink on white paper. No hatching. No wash. One red element per image: a thread, a wound, a signal. Black dogs as grief. Ravens as witnesses. |
| 5 | **Reconstruction** | Rebuilding. Color returned, but chosen this time. | Pen and ink with controlled watercolor washes. Cool blue-gray dominant. Wolves and foxes as chosen companions. The body moving forward on purpose. |
| 6 | **Reclamation** | Now. The artist at full power. | Refined dark storybook aesthetic. Rich, deep, warm from within. Ravens at the shoulder. Wolves at the feet. Every element earned. |

**Consistent across all eras:** cool palette only, generous negative space, female figures exclusively, spirit animals as presences not decoration.

---

## Architecture

```
VISITOR
  │
  ▼
Slider (1–6) ──► POST /api/generate
                        │
                        ▼
              era-specific prompt template
                   + baseline aesthetic DNA
                   + randomized subject/mood
                        │
                        ▼
                   DALL-E 3 API
                        │
                        ▼
              base64 image → browser
              (NOT stored anywhere)
                        │
                        ▼
              2.5s opacity fade-in on canvas
```

---

## How It Works

1. Visitor opens the gallery. Era 1 begins generating immediately.
2. After each image appears, the gallery auto-advances to the next era after 12 seconds.
3. Moving the slider pauses auto-advance and generates for the selected era.
4. Each generation pulls from era-specific prompt templates + a shared aesthetic baseline.
5. Randomized subject and mood ensure no two generations are identical.
6. Images appear via opacity transition. Nothing is saved to disk or database.

---

## Fork Your Own Gallery

This repo is designed to be forked. To build your own living gallery:

1. **Define your eras** in `src/prompts/eras.py`. Each era needs a label, prompt template, subjects, moods, and color palette. The system handles the rest.
2. **Set your baseline** in `src/prompts/baseline.py`. This is your consistent aesthetic DNA — the fingerprint that runs under every era. Include your medium preferences, compositional instincts, any absolute rules.
3. **Add your key** — copy `.env.example` to `.env` and add your `OPENAI_API_KEY`.
4. **Deploy** — see deployment instructions below.

See `docs/FORKING_GUIDE.md` for a full walkthrough.

---

## Running Locally

```bash
git clone https://github.com/DianaWolfe/pre-sent.git
cd pre-sent
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
cd src && uvicorn app:app --reload --port 8000
# Open http://localhost:8000
```

---

## Deploying to Render

The repo includes a `render.yaml`. On Render:

1. New → Web Service → connect this repo
2. Render detects `render.yaml` and pre-fills all config
3. Add `OPENAI_API_KEY` in the Environment tab
4. Deploy

---

## Cost

DALL-E 3 at standard quality costs $0.04 per image. The rate limiter defaults to one generation per 15 seconds per visitor. At typical browsing pace a 10-minute visit generates roughly 5–8 images ($0.20–0.32). The global hourly cap is configurable in `render.yaml`.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vanilla HTML / CSS / JS |
| Backend | Python, FastAPI |
| Image Generation | DALL-E 3 via OpenAI API |
| Hosting | Render (included `render.yaml`) |

---

## Project Structure

```
pre-sent/
├── README.md
├── render.yaml              # One-click Render deployment config
├── requirements.txt
├── .env.example
├── src/
│   ├── app.py               # FastAPI server, static file serving
│   ├── api/generate.py      # DALL-E 3 integration
│   ├── prompts/
│   │   ├── eras.py          # Era definitions, prompt templates, subjects, moods
│   │   ├── baseline.py      # Consistent aesthetic DNA (palette, composition rules)
│   │   └── assembler.py     # Combines era + baseline into final prompt
│   └── gallery/
│       └── rate_limiter.py  # Per-visitor and global API cost control
├── public/
│   ├── index.html           # Gallery frontend
│   ├── style.css
│   └── gallery.js           # Slider, auto-advance, generation, fade-in
└── docs/
    ├── CONCEPT.md
    └── FORKING_GUIDE.md
```

---

## Research Context

pre.SENT sits within a broader research program on identity, AI collaboration, and what it means to have a creative practice that exists outside your own hands. The gallery asks whether a generative system, given precise psychological and aesthetic constraints built from real artistic history, can produce work that feels genuinely autobiographical — even though the system has no autobiography.

It also asks: what is a self-portrait when it is different every time you look? What is a style when it is inherited rather than made?

---

*Built by [Diana Wolfe, PhD](https://dianawolfe.com)*
