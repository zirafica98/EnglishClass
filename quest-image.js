(function () {
  "use strict";

  const root = document.getElementById("qi-root");

  function escapeHtml(s) {
    return String(s).replace(/[&<>'"]/g, (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch])
    );
  }

  function norm(s) {
    return String(s)
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  function haystack(item) {
    return norm([item.n, item.section, item.q, item.answer, item.hint].join("\n"));
  }

  function matchesSearch(query, item) {
    const q = norm(query.trim());
    if (!q) return true;
    const h = haystack(item);
    const words = q.split(/\s+/).filter(Boolean);
    return words.every((w) => h.includes(w));
  }

  function parseQuickQuestionNum(raw, maxN) {
    const t = String(raw || "").trim();
    const m = t.match(/^#?(\d+)$/);
    if (!m) return null;
    const n = parseInt(m[1], 10);
    if (n >= 1 && n <= maxN) return n;
    return null;
  }

  function debounce(fn, ms) {
    let t = 0;
    return function (...args) {
      clearTimeout(t);
      t = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  /**
   * @param {unknown[]} data
   * @param {{ initialSearch?: string; initialHash?: string }} [opts]
   */
  function render(data, opts) {
    opts = opts || {};
    if (!root || !Array.isArray(data) || !data.length) {
      if (root) root.innerHTML = "<p>Niz u <code>quest-image-data.json</code> je prazan.</p>";
      return;
    }

    const maxN = Math.max(...data.map((d) => d.n));
    const sectionsOrdered = [];
    const seenSec = new Set();
    for (const it of data) {
      if (!seenSec.has(it.section)) {
        seenSec.add(it.section);
        sectionsOrdered.push(it.section);
      }
    }

    const chipsHtml = sectionsOrdered
      .map(
        (sec) =>
          `<button type="button" class="qi-chip" data-qi-section="${escapeHtml(sec)}" aria-pressed="false">${escapeHtml(
            sec
          )}</button>`
      )
      .join("");

    const cardsHtml = data
      .map(
        (it) => `
    <article class="qi-card" id="qi-p-${it.n}" data-qi-n="${it.n}">
      <h2 class="qi-q"><span class="qi-num">${it.n}.</span>${escapeHtml(it.q)}</h2>
      <p class="qi-answer">${escapeHtml(it.answer)}</p>
      <p class="qi-hint"><strong>Savet:</strong> ${escapeHtml(it.hint)}</p>
    </article>
  `
      )
      .join("");

    root.innerHTML = `
    <div class="qi-page">
    <div class="qi-wrap">
      <header class="qi-top">
        <h1 class="qi-title">Speaking · beležnica</h1>
        <label class="sr-only" for="qi-search">Pretraga</label>
        <input type="search" id="qi-search" class="qi-search" enterkeyhint="search" autocomplete="off" placeholder="Pretraga…" />
        <div class="qi-chips-wrap" role="group" aria-label="Filter po sekciji">
          <button type="button" class="qi-chip qi-chip--all qi-chip--active" data-qi-section-all="1" aria-pressed="true">Sve sekcije</button>
          ${chipsHtml}
        </div>
      </header>
      <p id="qi-empty" class="qi-empty" hidden role="status">Nema rezultata. <button type="button" class="qi-clear-filters">Obriši filtere</button></p>
      <div id="qi-cards">${cardsHtml}</div>
    </div>
    </div>
  `;

    const input = root.querySelector("#qi-search");
    const emptyEl = root.querySelector("#qi-empty");
    const cardsWrap = root.querySelector("#qi-cards");
    const cards = root.querySelectorAll(".qi-card");
    const chipAll = root.querySelector("[data-qi-section-all]");
    const sectionChips = root.querySelectorAll(".qi-chip[data-qi-section]");

    let selectedSection = null;

    function syncChipsUi() {
      if (chipAll) {
        const allOn = !selectedSection;
        chipAll.classList.toggle("qi-chip--active", allOn);
        chipAll.setAttribute("aria-pressed", allOn ? "true" : "false");
      }
      sectionChips.forEach((btn) => {
        const sec = btn.getAttribute("data-qi-section");
        const on = selectedSection === sec;
        btn.classList.toggle("qi-chip--active", on);
        btn.setAttribute("aria-pressed", on ? "true" : "false");
      });
    }

    function itemMatchesFilters(item) {
      if (!item) return false;
      const q = input ? input.value : "";
      const quick = parseQuickQuestionNum(q, maxN);
      if (quick !== null) return item.n === quick;
      if (selectedSection && item.section !== selectedSection) return false;
      return matchesSearch(q, item);
    }

    function applyFilter() {
      let visible = 0;
      cards.forEach((card) => {
        const n = Number(card.dataset.qiN);
        const item = data.find((x) => x.n === n);
        const ok = itemMatchesFilters(item);
        card.hidden = !ok;
        if (ok) visible += 1;
      });
      if (emptyEl) emptyEl.hidden = visible > 0;
      if (cardsWrap) cardsWrap.hidden = visible === 0;
    }

    function updateSearchUrlNow() {
      const s = input ? input.value.trim() : "";
      const url = new URL(location.href);
      if (s) url.searchParams.set("s", s);
      else url.searchParams.delete("s");
      url.searchParams.delete("q");
      history.replaceState(null, "", url.pathname + url.search + location.hash);
    }

    const pushUrlDebounced = debounce(updateSearchUrlNow, 400);

    if (input) {
      input.addEventListener("input", () => {
        applyFilter();
        pushUrlDebounced();
      });
      input.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          input.value = "";
          selectedSection = null;
          syncChipsUi();
          applyFilter();
          updateSearchUrlNow();
        }
      });
    }

    function clearFilters() {
      if (input) input.value = "";
      selectedSection = null;
      syncChipsUi();
      applyFilter();
      updateSearchUrlNow();
    }

    if (chipAll) {
      chipAll.addEventListener("click", () => {
        selectedSection = null;
        syncChipsUi();
        applyFilter();
      });
    }
    sectionChips.forEach((btn) => {
      btn.addEventListener("click", () => {
        const sec = btn.getAttribute("data-qi-section");
        if (selectedSection === sec) selectedSection = null;
        else selectedSection = sec;
        syncChipsUi();
        applyFilter();
      });
    });

    const clearBtn = root.querySelector(".qi-clear-filters");
    if (clearBtn) clearBtn.addEventListener("click", clearFilters);

    document.addEventListener("keydown", function qiSlashFocus(e) {
      if (e.key !== "/") return;
      const t = e.target;
      if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.tagName === "SELECT" || t.isContentEditable))
        return;
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      e.preventDefault();
      if (input) input.focus();
    });

    const initialSearch = (opts.initialSearch || "").trim();
    const hash = (opts.initialHash || location.hash || "").trim();
    const hashMatch = hash.match(/^#qi-p-(\d+)$/);
    if (hashMatch) {
      const hn = parseInt(hashMatch[1], 10);
      if (!initialSearch && hn >= 1 && hn <= maxN && input) input.value = String(hn);
      else if (input && initialSearch) input.value = initialSearch;
    } else if (initialSearch && input) input.value = initialSearch;

    syncChipsUi();
    applyFilter();
    pushUrlDebounced();

    if (hashMatch) {
      const id = "qi-p-" + hashMatch[1];
      requestAnimationFrame(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
  }

  async function main() {
    if (!root) return;

    let data;
    try {
      const r = await fetch("./quest-image-data.json", { cache: "no-store" });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      data = await r.json();
    } catch (e) {
      root.innerHTML = `<p class="qi-err">Ne mogu da učitam <code>quest-image-data.json</code>. Koristi server (npr. <code>vercel dev</code>). <span class="qi-err-msg">${escapeHtml(
        String(e && e.message ? e.message : e)
      )}</span></p>`;
      return;
    }

    if (!Array.isArray(data)) {
      root.innerHTML = '<p class="qi-err">quest-image-data.json mora biti JSON niz.</p>';
      return;
    }

    const params = new URLSearchParams(location.search);
    const initialSearch = params.get("s") || params.get("q") || "";
    render(data, { initialSearch, initialHash: location.hash });
  }

  main();
})();
