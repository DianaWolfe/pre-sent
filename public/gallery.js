/**
 * pre.SENT - Gallery
 *
 * A performance. Six eras. One cycle.
 * Begins with a breathing exercise. Moves through an artist's life.
 * Ends in white. Requires a refresh to re-enter.
 */

(function () {
  const slider = document.getElementById("era-slider");
  const artwork = document.getElementById("artwork");
  const loading = document.getElementById("loading");
  const empty = document.getElementById("empty");
  const eraLabel = document.getElementById("era-label");
  const eraAge = document.getElementById("era-age");
  const sliderLabels = document.getElementById("slider-labels");
  const cycleEnd = document.getElementById("cycle-end");

  let eras = [];
  let firstLoad = true;

  const DISPLAY_DURATION = 20000;   // 20s per image
  const POEM_MIN_DURATION = 7000;   // poem card shows for at least 7s
  const PREFETCH_DELAY = 9000;      // start prefetch 9s after image appears
  const RATE_LIMIT_RETRY = 10000;   // wait 10s if rate limited

  // Single prefetch slot
  let prefetch = { era: null, data: null, promise: null };

  // ── Init ─────────────────────────────────────────────────────────────────

  async function init() {
    try {
      const res = await fetch("/api/eras");
      eras = await res.json();
      renderSliderLabels();

      // Populate era 1 poem in entrance card
      const era1 = eras.find((e) => e.slider_position === 1);
      if (era1) {
        const poemEl = document.getElementById("entrance-poem");
        if (poemEl) poemEl.innerHTML = era1.bio_poem.replace(/\n/g, "<br>");
      }

      loop(1);
    } catch (e) {
      console.error("Failed to load eras:", e);
    }
  }

  // ── Main loop ─────────────────────────────────────────────────────────────

  async function loop(era) {
    setSlider(era);
    setEraInfo(era);
    showLoading(era);

    // Enforce minimum poem card display time (except first load — entrance card handles that)
    const imagePromise = getImage(era);
    const timerPromise = firstLoad ? Promise.resolve() : sleep(POEM_MIN_DURATION);
    const [data] = await Promise.all([imagePromise, timerPromise]);

    await revealImage(data.image);

    // Prefetch next era in background
    const next = era < 6 ? era + 1 : null;
    if (next) {
      setTimeout(() => startPrefetch(next), PREFETCH_DELAY);
    }

    await sleep(DISPLAY_DURATION);

    if (era >= 6) {
      endCycle();
      return;
    }

    loop(next);
  }

  // ── Image retrieval ───────────────────────────────────────────────────────

  async function getImage(era) {
    if (prefetch.era === era && prefetch.data) {
      const data = prefetch.data;
      prefetch = { era: null, data: null, promise: null };
      return data;
    }

    if (prefetch.era === era && prefetch.promise) {
      await prefetch.promise;
      if (prefetch.data) {
        const data = prefetch.data;
        prefetch = { era: null, data: null, promise: null };
        return data;
      }
    }

    return await fetchWithRetry(era);
  }

  async function fetchWithRetry(era) {
    while (true) {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ era }),
      });

      if (res.status === 429) {
        const body = await res.json();
        const wait = body.wait ? body.wait * 1000 : RATE_LIMIT_RETRY;
        await sleep(wait + 500);
        continue;
      }

      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    }
  }

  function startPrefetch(era) {
    if (prefetch.era === era) return;
    prefetch = { era, data: null, promise: null };

    prefetch.promise = fetchWithRetry(era)
      .then((data) => {
        if (prefetch.era === era) prefetch.data = data;
      })
      .catch(() => {
        if (prefetch.era === era) prefetch = { era: null, data: null, promise: null };
      });
  }

  // ── Display ───────────────────────────────────────────────────────────────

  function showLoading(era) {
    artwork.classList.remove("visible");

    if (firstLoad) {
      // Entrance card is already visible — don't activate poem card
      return;
    }

    empty.classList.add("hidden");

    const eraData = eras.find((e) => e.slider_position === era);
    if (eraData) {
      document.getElementById("loading-era-name").textContent = eraData.label;
      document.getElementById("loading-poem-text").innerHTML =
        eraData.bio_poem.replace(/\n/g, "<br>");
    }

    loading.classList.add("active");
  }

  function revealImage(src) {
    return new Promise((resolve) => {
      artwork.onload = () => {
        loading.classList.remove("active");

        if (firstLoad) {
          firstLoad = false;
          const card = document.querySelector(".entrance-card");
          if (card) card.classList.add("fading");
          // Cross-fade: start showing artwork while entrance card fades
          setTimeout(() => artwork.classList.add("visible"), 400);
          // After fade completes, hide the empty state and resolve
          setTimeout(() => {
            empty.classList.add("hidden");
            resolve();
          }, 2200);
        } else {
          artwork.classList.add("visible");
          resolve();
        }
      };
      artwork.src = src;
    });
  }

  // ── End of cycle ─────────────────────────────────────────────────────────

  function endCycle() {
    cycleEnd.classList.add("active");
  }

  // ── UI helpers ────────────────────────────────────────────────────────────

  function setSlider(position) {
    slider.value = position;
    document.querySelectorAll(".slider-label").forEach((el) => {
      el.classList.toggle("active", parseInt(el.dataset.position) === position);
    });
  }

  function setEraInfo(position) {
    const era = eras.find((e) => e.slider_position === position);
    if (!era) return;
    eraLabel.textContent = era.label;
    eraAge.textContent = era.age_range;
  }

  function renderSliderLabels() {
    sliderLabels.innerHTML = "";
    eras.forEach((era) => {
      const label = document.createElement("span");
      label.className = "slider-label";
      label.textContent = era.label;
      label.dataset.position = era.slider_position;
      sliderLabels.appendChild(label);
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
    document.querySelectorAll(".slider-label").forEach((label) => {
      const value = parseInt(label.dataset.position);
      const left = thumbWidth / 2 + ((value - min) / range) * trackWidth;
      label.style.left = left + "px";
    });
  }

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  window.addEventListener("resize", positionLabels);

  init();
})();
