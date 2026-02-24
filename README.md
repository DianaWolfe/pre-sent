# pre.SENT

A living art gallery that generates ephemeral artwork in real time based on the psychological eras of a human life. Every visit produces art that has never existed before and will never exist again.

## What Is This

pre.SENT is a web-based generative art installation. Visitors arrive at a minimal gallery page and use a slider to select a life era: from the magical thinking of childhood through the fractures of crisis to the sovereignty of reclamation. The system generates original artwork on the spot using DALL-E 3, filtered through the emotional and aesthetic DNA of each developmental period.

The art is ephemeral. Nothing is saved. When you leave, the images are gone. The gallery exists only in the present tense. That is the point.

## The Eras

The slider maps to six psychological stages of a life. Each era carries its own visual language: color palette, art movement references, emotional texture, subject matter tendencies, and compositional rules.

| Era | Label | Developmental Frame | Visual Language |
|-----|-------|--------------------|----|
| 1 | **Wonder** | Childhood (~0-12). Animistic thinking, magical realism. Piaget's preoperational and concrete stages. The world is alive and everything means something. | Bright saturated color, fairy tale imagery, golden light, picture book illustration, hidden creatures, enchanted landscapes |
| 2 | **Becoming** | Adolescence (~13-17). Identity formation (Erikson). Everything is intense, everything matters, nothing is settled. | High contrast, dramatic lighting, portraiture with obscured faces, storm imagery, chiaroscuro, Pre-Raphaelite influence |
| 3 | **The Proving Years** | Early adulthood (~18-27). Intimacy vs. isolation. Performance, ambition, the construction of a self for public consumption. | Sharp geometric composition, architectural subjects, clean lines, muted professional palette with flashes of aspiration, Art Deco influence |
| 4 | **The Unraveling** | Crisis/Divorce. Disillusionment, grief, the collapse of constructed identity. Kübler-Ross meets existential psychology. | Fragmentation, torn textures, desaturated color with isolated moments of vivid warmth, abstract expressionist influence, empty rooms, broken symmetry |
| 5 | **The Reconstruction** | Rebuilding (~30s-40s). Post-traumatic growth. Generativity (Erikson). Integration of the broken pieces into something stronger. | Kintsugi aesthetic, warm earth tones returning, botanical imagery, gold veining through dark surfaces, wabi-sabi imperfection, layered mixed media |
| 6 | **The Reclamation** | Now. Self-authorship (Kegan Stage 5). Sovereignty, earned complexity, the dark sublime. | Deep moody palette (sage, umber, midnight), classical romantic painting, mystical and occult imagery, lighthouses, veiled figures, candlelit interiors, old world with modern edge |

## Architecture

```
┌──────────────────────────────────────────────┐
│              VISITOR BROWSER                  │
│                                               │
│  ┌─────────────────────────────────────────┐  │
│  │         ERA SLIDER (1-6)                │  │
│  │  Wonder ──────────── Reclamation        │  │
│  └──────────────┬──────────────────────────┘  │
│                 │                              │
│  ┌──────────────▼──────────────────────────┐  │
│  │         GALLERY CANVAS                  │  │
│  │    (generated art appears here)         │  │
│  │                                         │  │
│  │    [loading state: slow painterly       │  │
│  │     reveal as image generates]          │  │
│  │                                         │  │
│  └─────────────────────────────────────────┘  │
│                                               │
│  ┌─────────────────────────────────────────┐  │
│  │  ERA LABEL + BRIEF PSYCHOLOGICAL NOTE   │  │
│  └─────────────────────────────────────────┘  │
└──────────────┬───────────────────────────────┘
               │ API call
               ▼
┌──────────────────────────────────────────────┐
│              SERVER                           │
│                                               │
│  1. Receive era selection                     │
│  2. Select prompt template for era            │
│  3. Inject randomized elements (subject,      │
│     composition, time of day, weather)        │
│  4. Call DALL-E 3 API                         │
│  5. Return image to client                    │
│  6. Image is NOT stored anywhere              │
│                                               │
└──────────────────────────────────────────────┘
```

## How It Works

1. Visitor opens the gallery page
2. A default era is selected and art begins generating
3. Visitor moves the slider to explore different life stages
4. Each slider position triggers a new generation using era-specific prompt templates
5. The prompt template includes fixed aesthetic DNA (palette, style, mood) plus randomized elements (specific subject, composition, lighting) so no two generations are identical
6. Images appear with a slow painterly reveal (opacity fade simulating a painting emerging)
7. When the visitor leaves, everything disappears

## For Builders: Fork Your Own Gallery

This repo is designed to be forked. To create your own living gallery:

1. **Define your eras** in `src/prompts/eras.py`. Each era needs a label, description, and prompt template with visual DNA.
2. **Set your aesthetic baseline** in `src/prompts/baseline.py`. This is the consistent style layer that runs underneath all eras (your personal artistic sensibility).
3. **Add your API key** to `.env`
4. **Deploy** to Vercel, Railway, or any Node/Python host

The system separates *your* content (era definitions, aesthetic DNA) from the *engine* (prompt assembly, API calls, gallery frontend). Fork the engine, replace the content.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML/CSS/JS (vanilla, no framework needed) |
| Backend | Python (FastAPI) |
| Image Generation | DALL-E 3 (OpenAI API) |
| Hosting | Vercel / Railway / any Python host |

## Project Structure

```
pre-sent/
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
├── src/
│   ├── app.py                   # FastAPI server
│   ├── api/
│   │   ├── __init__.py
│   │   └── generate.py          # DALL-E 3 API integration
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── eras.py              # Era definitions and prompt templates
│   │   ├── baseline.py          # Your aesthetic DNA (consistent style layer)
│   │   └── assembler.py         # Combines era + baseline + randomization
│   └── gallery/
│       ├── __init__.py
│       └── rate_limiter.py      # Prevent runaway API costs
├── public/
│   ├── index.html               # Gallery frontend
│   ├── style.css                # Gallery styling
│   └── gallery.js               # Slider interaction + image display
└── docs/
    ├── CONCEPT.md               # Artistic and psychological framing
    └── FORKING_GUIDE.md         # How to build your own gallery
```

## Running Locally

```bash
git clone https://github.com/yourusername/pre-sent.git
cd pre-sent
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
python src/app.py
# Open http://localhost:8000
```

## Cost

Each DALL-E 3 generation costs $0.04-0.08 depending on size and quality. The rate limiter defaults to one generation per 15 seconds to prevent runaway costs. At typical browsing pace, a 10-minute visit generates roughly 5-8 images ($0.20-0.64).

## Research Context

pre.SENT sits within a broader research program on identity, AI collaboration, and what it means to have a creative practice that exists outside your own hands. The gallery explores whether a generative system, given the right psychological and aesthetic constraints, can produce art that feels genuinely autobiographical, even though the system has no autobiography.

It also asks: what is an art gallery when nothing in it persists? What is a self-portrait when it's different every time you look?

## License

MIT. See [LICENSE](LICENSE).

---

*Built by [Diana Wolfe, PhD](https://dianawolfe.com) as part of the Experiments series on applied AI research.*
