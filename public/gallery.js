/**
 * pre.SENT v2 — Gallery
 *
 * A performance in four screens. No viewer control.
 * Screen 1: Explainer  (~15s)
 * Screen 2: Breather   (~13s)
 * Screen 3: Gallery    (~2.5 min, 6 eras auto-advancing)
 * Screen 4: Ending     (black, sequential text, holds indefinitely)
 */

(function () {
  // ── Elements ──────────────────────────────────────────────────────────────

  const slider        = document.getElementById("era-slider");
  const artwork       = document.getElementById("artwork");
  const cycleEnd      = document.getElementById("cycle-end");
  const explainer     = document.getElementById("explainer");
  const explainerBody = document.getElementById("explainer-body");
  const eraDisplay    = document.getElementById("era-display");
  const eraName       = document.getElementById("era-display-name");
  const eraAge        = document.getElementById("era-display-age");
  const canvasPoem    = document.getElementById("canvas-poem");
  const canvasPoemText= document.getElementById("canvas-poem-text");
  const breather      = document.getElementById("breather");
  const sliderLabels  = document.getElementById("slider-labels");

  // ── State ─────────────────────────────────────────────────────────────────

  let eras = [];
  let sessionId = null;

  const ERA_KEYS = [
    "wonder", "becoming", "proving",
    "unraveling", "reconstruction", "sovereign",
  ];

  // Timing (ms) — mirrors performance_text.py GALLERY_TIMING
  const T = {
    ERA_TITLE_FADE:   1500,
    POEM_FADE:        2000,
    POEM_HOLD:        10000,
    IMAGE_FADE:       2500,
    IMAGE_HOLD:       10000,
    ERA_FADE_OUT:     2000,
    INTER_ERA_PAUSE:  1500,
    UNRAVELING_PAUSE: 4000,  // white silence before reconstruction
  };

  // ── Utilities ─────────────────────────────────────────────────────────────

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  // ── Screen 1: Explainer ───────────────────────────────────────────────────

  const EXPLAINER_GROUPS = [
    { text: "you are about to watch a machine remember someone's life.", hold: 3500 },
    {
      text: "an artist left everything here.\nher paintings. her pain. her patterns.\ndecades of color and loss and recovery\ntranslated into instructions a machine can follow.",
      hold: 5000,
    },
    {
      text: "the machine has never seen her work.\nit inherits. it interprets. it may betray.\nthat uncertainty is the art.",
      hold: 4500,
    },
    {
      text: "what happens next will not repeat.\nnot the same poem. not the same image.\nnot the same rendering.\nyou cannot pause it. you cannot keep it.",
      hold: 4500,
    },
    { text: "nothing is saved.", hold: 2500, final: true },
  ];

  async function runExplainer() {
    for (let i = 0; i < EXPLAINER_GROUPS.length; i++) {
      const { text, hold, final } = EXPLAINER_GROUPS[i];

      const el = document.createElement("p");
      el.className = "explainer__group" + (final ? " explainer__group--final" : "");
      el.innerHTML = text.replace(/\n/g, "<br>");
      el.style.opacity = "0";
      explainerBody.innerHTML = "";
      explainerBody.appendChild(el);

      // Trigger fade in
      await sleep(50);
      el.style.opacity = "1";
      await sleep(1500 + hold);

      // Fade out (except final group — whole explainer fades)
      if (!final) {
        el.style.transition = "opacity 1s ease";
        el.style.opacity = "0";
        await sleep(1000);
      }
    }

    // Fade entire explainer out
    explainer.classList.add("fading");
    await sleep(1500);
    explainer.style.display = "none";
  }

  // ── Screen 2: Breather ────────────────────────────────────────────────────

  async function runBreather() {
    // Breather is visible from HTML load; voice lines start hidden (opacity 0 in CSS)
    const line1 = document.getElementById("breather-line-1");
    const line2 = document.getElementById("breather-line-2");

    // Let breathing animation play for ~7s before machine speaks
    await sleep(7000);

    // The generative speaks (roman type — tonal shift)
    line1.style.opacity = "1";
    await sleep(2500);
    line2.style.opacity = "1";
    await sleep(3000);

    // Fade out breather
    breather.style.opacity = "0";
    await sleep(1500);
    breather.classList.add("hidden");
  }

  // ── Poem formatter ────────────────────────────────────────────────────────
  // Every standalone "i" becomes ~~i~~ WE — the machine is confused about
  // whether it is self, other, memory, or machine.

  function formatPoem(raw) {
    return raw
      .replace(/\bi\b/g, '<del>i</del><span class="we">WE</span>')
      .replace(/\n/g, "<br>");
  }

  // ── Screen 3: Gallery — per-era sequence ──────────────────────────────────

  async function runEra(data, position) {
    setSlider(position);

    // Reset
    artwork.classList.remove("visible");
    artwork.style.opacity = "";
    canvasPoem.style.opacity = "0";
    canvasPoemText.innerHTML = "";

    // Fade in era name + age above canvas
    eraName.textContent = data.era_label;
    eraAge.textContent = data.age_range;
    eraDisplay.style.opacity = "1";
    await sleep(T.ERA_TITLE_FADE);

    // Poem fades in inside the canvas
    canvasPoemText.innerHTML = formatPoem(data.poem);
    canvasPoem.style.opacity = "1";
    await sleep(T.POEM_FADE + T.POEM_HOLD);

    // Crossfade: poem out, image in — or hold poem if no image
    if (data.image) {
      canvasPoem.style.opacity = "0";   // poem fades out
      await revealImage(data.image);    // image fades in simultaneously
      await sleep(T.IMAGE_HOLD);
    } else {
      await sleep(T.IMAGE_HOLD);        // poem holds in canvas for full image window
    }

    // Fade out everything together
    eraDisplay.style.transition = `opacity ${T.ERA_FADE_OUT}ms ease`;
    eraDisplay.style.opacity = "0";
    artwork.style.transition = `opacity ${T.ERA_FADE_OUT}ms ease`;
    artwork.style.opacity = "0";
    canvasPoem.style.opacity = "0";
    await sleep(T.ERA_FADE_OUT);

    // Reset for next era
    artwork.classList.remove("visible");
    artwork.style.transition = "";
    artwork.style.opacity = "";
    eraDisplay.style.transition = "";
  }

  function revealImage(src) {
    return new Promise((resolve) => {
      artwork.onload = () => {
        artwork.classList.add("visible");
        setTimeout(resolve, T.IMAGE_FADE);
      };
      artwork.src = src;
    });
  }

  // ── Screen 4: Ending ──────────────────────────────────────────────────────

  async function runEnding() {
    const line1 = document.getElementById("cycle-end-line-1");
    const line2 = document.getElementById("cycle-end-line-2");
    const line3 = document.getElementById("cycle-end-line-3");

    // Fade to black (3s transition)
    cycleEnd.classList.add("active");
    await sleep(3000 + 2000); // fade + 2s black silence

    // "the moment has ended." — holds 4s
    line1.style.opacity = "1";
    await sleep(2000 + 4000);

    // "what you saw was hers..." — holds 5s
    line2.style.opacity = "1";
    await sleep(2000 + 5000);

    // "did the machine know her?" — holds indefinitely
    line3.style.opacity = "1";
  }

  // ── Session ───────────────────────────────────────────────────────────────

  async function startSession() {
    const res = await fetch("/api/session/start", { method: "POST" });
    const data = await res.json();
    return data.session_id;
  }

  async function waitForEra(eraKey) {
    while (true) {
      const res = await fetch(`/api/session/${sessionId}/era/${eraKey}`);
      const data = await res.json();
      if (data.ready) return data;
      await sleep(2000);
    }
  }

  // ── Slider helpers ────────────────────────────────────────────────────────

  function setSlider(position) {
    slider.value = position;
    document.querySelectorAll(".slider-label-wrapper").forEach((el) => {
      el.classList.toggle("active", parseInt(el.dataset.position) === position);
    });
  }

  function renderSliderLabels() {
    sliderLabels.innerHTML = "";
    eras.forEach((era) => {
      const wrapper = document.createElement("div");
      wrapper.className = "slider-label-wrapper";
      wrapper.dataset.position = era.slider_position;

      const name = document.createElement("span");
      name.className = "slider-label";
      name.textContent = era.label;

      const age = document.createElement("span");
      age.className = "slider-label-age";
      age.textContent = era.age_range;

      wrapper.appendChild(name);
      wrapper.appendChild(age);
      sliderLabels.appendChild(wrapper);
    });
    setSlider(1);
    requestAnimationFrame(positionLabels);
  }

  function positionLabels() {
    const thumbWidth = 16;
    const min = parseInt(slider.min);
    const max = parseInt(slider.max);
    const range = max - min;
    const trackWidth = slider.offsetWidth - thumbWidth;
    document.querySelectorAll(".slider-label-wrapper").forEach((wrapper) => {
      const value = parseInt(wrapper.dataset.position);
      const left = thumbWidth / 2 + ((value - min) / range) * trackWidth;
      wrapper.style.left = left + "px";
    });
  }

  // ── Init ──────────────────────────────────────────────────────────────────

  async function init() {
    try {
      // Start session + load era labels in parallel (maximise generation buffer)
      const [erasData, sessionData] = await Promise.all([
        fetch("/api/eras").then((r) => r.json()),
        fetch("/api/session/start", { method: "POST" }).then((r) => r.json()),
      ]);

      eras = erasData;
      sessionId = sessionData.session_id;
      renderSliderLabels();

      // Screen 1: Explainer (~15s, generation runs in background)
      await runExplainer();

      // Screen 2: Breather (~13s, more buffer)
      await runBreather();

      // Screen 3: Gallery
      for (let i = 0; i < ERA_KEYS.length; i++) {
        const eraKey = ERA_KEYS[i];
        const position = i + 1;

        // 4-second white silence before reconstruction (the most important moment)
        if (eraKey === "reconstruction") {
          await sleep(T.UNRAVELING_PAUSE);
        }

        // Retrieve pre-generated content (should be ready by now)
        const data = await waitForEra(eraKey);
        await runEra(data, position);
        await sleep(T.INTER_ERA_PAUSE);
      }

      // Screen 4: Ending
      await runEnding();

    } catch (e) {
      console.error("pre.SENT error:", e);
    }
  }

  window.addEventListener("resize", positionLabels);
  init();
})();
