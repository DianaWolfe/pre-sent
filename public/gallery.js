/**
 * pre.SENT - Gallery
 *
 * Runs a continuous loop through all six eras.
 * Prefetches the next era in the background while the current one displays.
 * No user controls — the gallery advances on its own.
 */

(function () {
  const slider = document.getElementById("era-slider");
  const artwork = document.getElementById("artwork");
  const loading = document.getElementById("loading");
  const empty = document.getElementById("empty");
  const eraLabel = document.getElementById("era-label");
  const eraAge = document.getElementById("era-age");
  const eraPoem = document.getElementById("era-poem");
  const sliderLabels = document.getElementById("slider-labels");

  let eras = [];

  // How long to show each image (ms)
  const DISPLAY_DURATION = 30000;
  // When to start prefetching the next image (ms after current image appears)
  const PREFETCH_DELAY = 9000;
  // How long to wait before retrying a rate-limited request (ms)
  const RATE_LIMIT_RETRY = 10000;

  // Prefetch slot — holds at most one upcoming image
  let prefetch = { era: null, data: null, promise: null };

  // ── Initialization ───────────────────────────────────────────────────────

  async function init() {
    try {
      const res = await fetch("/api/eras");
      eras = await res.json();
      renderSliderLabels();
      loop(1);
    } catch (e) {
      console.error("Failed to load eras:", e);
    }
  }

  // ── Main loop ────────────────────────────────────────────────────────────

  async function loop(era) {
    setSlider(era);
    setEraInfo(era);
    showLoading();

    const data = await getImage(era);

    await revealImage(data.image);

    // Start prefetching the next era in the background
    const next = era >= 6 ? 1 : era + 1;
    setTimeout(() => startPrefetch(next), PREFETCH_DELAY);

    await sleep(DISPLAY_DURATION);

    loop(next);
  }

  // ── Image retrieval ──────────────────────────────────────────────────────

  async function getImage(era) {
    // Cache hit
    if (prefetch.era === era && prefetch.data) {
      const data = prefetch.data;
      prefetch = { era: null, data: null, promise: null };
      return data;
    }

    // Prefetch in-flight for this era — wait for it
    if (prefetch.era === era && prefetch.promise) {
      await prefetch.promise;
      if (prefetch.data) {
        const data = prefetch.data;
        prefetch = { era: null, data: null, promise: null };
        return data;
      }
    }

    // No cache — generate on demand
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
        if (prefetch.era === era) {
          prefetch.data = data;
        }
      })
      .catch(() => {
        if (prefetch.era === era) {
          prefetch = { era: null, data: null, promise: null };
        }
      });
  }

  // ── Display ──────────────────────────────────────────────────────────────

  function revealImage(src) {
    return new Promise((resolve) => {
      artwork.onload = () => {
        loading.classList.remove("active");
        artwork.classList.add("visible");
        resolve();
      };
      artwork.src = src;
    });
  }

  function showLoading() {
    empty.classList.add("hidden");
    artwork.classList.remove("visible");
    loading.classList.add("active");
  }

  // ── UI ───────────────────────────────────────────────────────────────────

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
    eraPoem.innerHTML = era.bio_poem.replace(/\n/g, "<br>");
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

  // ── Utilities ────────────────────────────────────────────────────────────

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  window.addEventListener("resize", positionLabels);

  init();
})();
