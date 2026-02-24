/**
 * pre.SENT v2 — Gallery
 *
 * A performance in four screens. No viewer control.
 * Screen 1: Explainer  (~20s)
 * Screen 2: Breather   (~13s)
 * Screen 3: Gallery    (~3 min, 6 eras auto-advancing)
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

  // Timing (ms)
  const T = {
    ERA_TITLE_FADE:  1500,
    POEM_FADE:       2000,
    POEM_HOLD:       18000,
    IMAGE_FADE:      2500,
    IMAGE_HOLD:      10000,
    ERA_FADE_OUT:    2000,
    INTER_ERA_PAUSE: 1500,
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

      await sleep(50);
      el.style.opacity = "1";
      await sleep(1500 + hold);

      if (!final) {
        el.style.transition = "opacity 1s ease";
        el.style.opacity = "0";
        await sleep(1000);
      }
    }

    explainer.classList.add("fading");
    await sleep(1500);
    explainer.style.display = "none";
  }

  // ── Screen 2: Breather ────────────────────────────────────────────────────

  async function runBreather() {
    const line1 = document.getElementById("breather-line-1");
    const line2 = document.getElementById("breather-line-2");

    await sleep(7000);

    line1.style.opacity = "1";
    await sleep(2500);
    line2.style.opacity = "1";
    await sleep(3000);

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

    // Era name + age above canvas
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
      canvasPoem.style.opacity = "0";
      await revealImage(data.image);
      await sleep(T.IMAGE_HOLD);
    } else {
      await sleep(T.IMAGE_HOLD);
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
      // If image fails to load, resolve anyway so gallery doesn't hang
      artwork.onerror = () => {
        setTimeout(resolve, T.IMAGE_FADE);
      };
      artwork.src = src;
    });
  }

  // ── Transition slide: unraveling → reconstruction ─────────────────────────

  async function runTransitionSlide() {
    const slide = document.getElementById("transition-slide");
    const text  = document.getElementById("transition-slide-text");

    // Cut in instantly
    slide.style.opacity = "1";
    slide.style.pointerEvents = "all";

    // Flash sequence: white → black → white → black → white → settle
    const flashes = [
      ["#ffffff",  80],
      ["#0c0c0a",  90],
      ["#ffffff",  80],
      ["#0c0c0a", 110],
      ["#ffffff", 140],
      ["#fafaf8", 500],
    ];
    for (const [bg, dur] of flashes) {
      slide.style.background = bg;
      await sleep(dur);
    }

    // Generative speaks in Aptos
    text.innerHTML = '<del>i</del> am not broken.<br>WE are breaking.';
    text.style.opacity = "1";
    await sleep(1500 + 5000);

    // Fade text then slide out
    text.style.opacity = "0";
    await sleep(1000);
    slide.style.transition = "opacity 1.5s ease";
    slide.style.opacity = "0";
    await sleep(1500);

    // Reset
    slide.style.transition = "";
    slide.style.background = "#fafaf8";
    slide.style.pointerEvents = "none";
    text.innerHTML = "";
  }

  // ── Screen 4: Ending ──────────────────────────────────────────────────────

  async function runEnding() {
    const line1 = document.getElementById("cycle-end-line-1");
    const line2 = document.getElementById("cycle-end-line-2");
    const line3 = document.getElementById("cycle-end-line-3");

    // Fade to black (3s)
    cycleEnd.classList.add("active");
    await sleep(3000 + 2000);

    // "the moment has ended." — holds 4s
    line1.style.opacity = "1";
    await sleep(2000 + 4000);

    // "what you saw was ours..." — holds 5s
    line2.style.opacity = "1";
    await sleep(2000 + 5000);

    // "did the machine know her?" — holds indefinitely
    line3.style.opacity = "1";
  }

  // ── Session ───────────────────────────────────────────────────────────────

  async function waitForEra(eraKey) {
    const MAX_RETRIES = 60; // 2 minutes max
    for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
      try {
        const res = await fetch(`/api/session/${sessionId}/era/${eraKey}`);
        const data = await res.json();
        if (data.ready) return data;
      } catch (e) {
        // network blip — keep trying
      }
      await sleep(2000);
    }
    // Timed out — return fallback so gallery doesn't hang
    return {
      era_key:   eraKey,
      era_label: eraKey,
      age_range: "",
      poem:      "the machine is still\ntrying to remember\nsomething was here\nit is not gone",
      image:     null,
      ready:     true,
    };
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
      const [erasData, sessionData] = await Promise.all([
        fetch("/api/eras").then((r) => r.json()),
        fetch("/api/session/start", { method: "POST" }).then((r) => r.json()),
      ]);

      eras = erasData;
      sessionId = sessionData.session_id;
      renderSliderLabels();

      await runExplainer();
      await runBreather();

      for (let i = 0; i < ERA_KEYS.length; i++) {
        const eraKey = ERA_KEYS[i];
        const position = i + 1;

        if (eraKey === "unraveling") {
          await runTransitionSlide();
        }

        const data = await waitForEra(eraKey);
        await runEra(data, position);
        await sleep(T.INTER_ERA_PAUSE);
      }

      await runEnding();

    } catch (e) {
      console.error("pre.SENT error:", e);
    }
  }

  window.addEventListener("resize", positionLabels);
  init();
})();
