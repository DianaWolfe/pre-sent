/**
 * pre.SENT - Gallery Interaction
 *
 * Handles the era slider, triggers image generation,
 * and manages the painterly reveal animation.
 * Auto-advances through eras after each image loads.
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
  let generating = false;
  let pendingEra = null;
  let debounceTimer = null;
  let autoAdvanceTimer = null;
  let userInteracting = false;
  let userInteractTimer = null;

  // How long to display each image before advancing (ms)
  const AUTO_ADVANCE_DELAY = 12000;
  // How long after manual interaction before auto-play resumes (ms)
  const RESUME_DELAY = 30000;

  // Load era definitions from server
  async function loadEras() {
    try {
      const res = await fetch("/api/eras");
      eras = await res.json();
      renderSliderLabels();
      updateEraInfo(1);
      // Auto-start at era 1
      generate(1);
    } catch (e) {
      console.error("Failed to load eras:", e);
    }
  }

  function renderSliderLabels() {
    sliderLabels.innerHTML = "";
    eras.forEach((era) => {
      const label = document.createElement("span");
      label.className = "slider-label";
      label.textContent = era.label;
      label.dataset.position = era.slider_position;
      label.addEventListener("click", () => {
        slider.value = era.slider_position;
        onSliderChange();
      });
      sliderLabels.appendChild(label);
    });
    highlightLabel(1);
    // Position after paint so slider has rendered width
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

  function highlightLabel(position) {
    document.querySelectorAll(".slider-label").forEach((el) => {
      el.classList.toggle("active", parseInt(el.dataset.position) === position);
    });
  }

  function updateEraInfo(position) {
    const era = eras.find((e) => e.slider_position === position);
    if (!era) return;

    eraLabel.textContent = era.label;
    eraAge.textContent = era.age_range;
    eraPoem.innerHTML = era.bio_poem.replace(/\n/g, "<br>");
  }

  function scheduleAutoAdvance() {
    clearTimeout(autoAdvanceTimer);
    autoAdvanceTimer = setTimeout(() => {
      if (!userInteracting) {
        const current = parseInt(slider.value);
        const next = current >= 6 ? 1 : current + 1;
        slider.value = next;
        highlightLabel(next);
        updateEraInfo(next);
        generate(next);
      }
    }, AUTO_ADVANCE_DELAY);
  }

  // Generate artwork for the current era
  async function generate(eraPosition) {
    if (generating) {
      pendingEra = eraPosition;
      return;
    }

    generating = true;

    // Show loading state
    empty.classList.add("hidden");
    loading.classList.add("active");
    artwork.classList.remove("visible");

    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ era: eraPosition }),
      });

      if (res.status === 429) {
        const data = await res.json();
        showRateLimit(data.error);
        return;
      }

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`);
      }

      const data = await res.json();

      artwork.onload = function () {
        loading.classList.remove("active");
        setTimeout(() => {
          artwork.classList.add("visible");
          // Schedule advance to next era after image is visible
          scheduleAutoAdvance();
        }, 200);
      };

      artwork.src = data.image;

    } catch (e) {
      console.error("Generation failed:", e);
      loading.classList.remove("active");
      // Still try to advance even on error
      scheduleAutoAdvance();
    } finally {
      generating = false;

      if (pendingEra !== null) {
        const next = pendingEra;
        pendingEra = null;
        generate(next);
      }
    }
  }

  function showRateLimit(message) {
    loading.classList.remove("active");
    let msg = document.querySelector(".rate-limit-msg");
    if (!msg) {
      msg = document.createElement("p");
      msg.className = "rate-limit-msg";
      document.querySelector(".slider-container").appendChild(msg);
    }
    msg.textContent = message;
    setTimeout(() => {
      msg.textContent = "";
    }, 5000);
  }

  // Slider interaction with debounce
  function onSliderChange() {
    const position = parseInt(slider.value);
    highlightLabel(position);
    updateEraInfo(position);

    // Mark as user-interacting, pause auto-advance
    userInteracting = true;
    clearTimeout(autoAdvanceTimer);
    clearTimeout(userInteractTimer);

    // Resume auto-play after inactivity
    userInteractTimer = setTimeout(() => {
      userInteracting = false;
    }, RESUME_DELAY);

    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      generate(position);
    }, 600);
  }

  slider.addEventListener("input", onSliderChange);
  window.addEventListener("resize", positionLabels);

  // Initialize
  loadEras();
})();
