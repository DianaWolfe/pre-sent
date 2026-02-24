/**
 * pre.SENT - Gallery Interaction
 *
 * Handles the era slider, triggers image generation,
 * and manages the painterly reveal animation.
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

  // Load era definitions from server
  async function loadEras() {
    try {
      const res = await fetch("/api/eras");
      eras = await res.json();
      renderSliderLabels();
      updateEraInfo(1);
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
    // Render poem with line breaks preserved
    eraPoem.innerHTML = era.bio_poem.replace(/\n/g, "<br>");
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

      // Load image and do painterly reveal
      artwork.onload = function () {
        loading.classList.remove("active");
        // Small delay before reveal for dramatic effect
        setTimeout(() => {
          artwork.classList.add("visible");
        }, 200);
      };

      artwork.src = data.image;

    } catch (e) {
      console.error("Generation failed:", e);
      loading.classList.remove("active");
    } finally {
      generating = false;

      // If a new era was requested while generating, start that one
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

    // Debounce to avoid rapid generation while sliding
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      generate(position);
    }, 600);
  }

  slider.addEventListener("input", onSliderChange);

  // Initialize
  loadEras();
})();
