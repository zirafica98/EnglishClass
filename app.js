(function () {
  "use strict";

  const root = document.getElementById("lesson-view");
  const nav = document.getElementById("lesson-nav");
  const navPane = nav ? nav.closest(".nav-pane") : null;
  const data = window.__LESSONS_DATA__ || null;

  function clearNavActives() {
    if (navPane) {
      navPane.querySelectorAll("button.active").forEach((b) => b.classList.remove("active"));
    }
  }

  if (!data || !nav) {
    console.error("Nedostaju podaci ili markup.");
    return;
  }

  /* ---------- theme toggle ---------- */
  const THEME_KEY = "f2f_theme";
  const htmlEl = document.documentElement;
  function applyTheme(theme) {
    htmlEl.setAttribute("data-theme", theme);
    try { localStorage.setItem(THEME_KEY, theme); } catch {}
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = theme === "dark" ? "☀" : "☾";
    if (btn) btn.setAttribute("aria-label", theme === "dark" ? "Light mode" : "Dark mode");
  }
  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved === "dark" || saved === "light") {
      applyTheme(saved);
      return;
    }
    applyTheme(window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  }
  initTheme();
  const themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      const next = htmlEl.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
    });
  }
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
    if (!localStorage.getItem(THEME_KEY)) {
      applyTheme(e.matches ? "dark" : "light");
    }
  });

  /* ---------- nav toggle (mobile) ---------- */
  const navToggle = document.querySelector(".nav-toggle");
  const navBackdrop = document.createElement("div");
  navBackdrop.className = "nav-backdrop";
  document.querySelector(".layout").appendChild(navBackdrop);
  function hideNavOnMobile() {
    if (window.matchMedia("(max-width: 900px)").matches) {
      navPane.classList.add("collapsed");
      navBackdrop.classList.remove("visible");
      if (navToggle) navToggle.setAttribute("aria-expanded", "false");
    }
  }
  function updateNavBackdrop() {
    const isMobile = window.matchMedia("(max-width: 900px)").matches;
    navBackdrop.classList.toggle("visible", isMobile && !navPane.classList.contains("collapsed"));
  }
  if (navToggle) {
    navToggle.addEventListener("click", () => {
      navPane.classList.toggle("collapsed");
      const collapsed = navPane.classList.contains("collapsed");
      if (window.matchMedia("(min-width: 901px)").matches) {
        document.querySelector(".layout").classList.toggle("nav-collapsed");
        document.querySelectorAll("#lesson-nav details, .prep-nav-details").forEach((d) => {
          if (collapsed) {
            d.dataset.op = d.open ? "1" : "0";
            d.open = true;
          } else {
            d.open = d.dataset.op !== "0";
          }
        });
      }
      updateNavBackdrop();
      const expanded = !collapsed;
      navToggle.setAttribute("aria-expanded", String(expanded));
    });
    navBackdrop.addEventListener("click", () => {
      navPane.classList.add("collapsed");
      updateNavBackdrop();
      if (navToggle) navToggle.setAttribute("aria-expanded", "false");
    });
  }

  /* start collapsed on mobile */
  hideNavOnMobile();

  /* ---------- prep local storage ---------- */
  const PREP_LS_KEY = "f2f_prep_values";
  function loadPrepLS() {
    try { return JSON.parse(localStorage.getItem(PREP_LS_KEY)) || {}; } catch { return {}; }
  }
  function savePrepLS() {
    try { localStorage.setItem(PREP_LS_KEY, JSON.stringify(savedPrepValues)); } catch {}
  }

  let activePrepVariant = null;
  const savedPrepValues = loadPrepLS();

  /* ---------- keyboard navigation ---------- */
  const navItems = [];

  const titleEl = document.getElementById("course-title");
  if (titleEl) titleEl.textContent = "Lekcije 1A – 12C";

  /* ---------- brand info tooltip ---------- */
  const infoBtn = document.querySelector(".brand-info-btn");
  if (infoBtn && data.course) {
    const infoTip = document.createElement("div");
    infoTip.className = "brand-info-tip";
    infoTip.setAttribute("role", "tooltip");
    infoTip.textContent = data.course.notes_sr;
    infoTip.hidden = true;
    document.body.appendChild(infoTip);
    function showTip() {
      const rect = infoBtn.getBoundingClientRect();
      infoTip.style.position = "fixed";
      infoTip.style.top = (rect.bottom + 6) + "px";
      infoTip.style.left = Math.max(6, Math.min(rect.left, window.innerWidth - 270)) + "px";
      infoTip.hidden = false;
    }
    infoBtn.addEventListener("mouseenter", showTip);
    infoBtn.addEventListener("mouseleave", () => {
      infoTip.hidden = true;
      infoBtn.setAttribute("aria-expanded", "false");
    });
    infoTip.addEventListener("mouseenter", () => {
      infoTip.hidden = false;
    });
    infoTip.addEventListener("mouseleave", () => {
      infoTip.hidden = true;
      infoBtn.setAttribute("aria-expanded", "false");
    });
    window.addEventListener("resize", () => {
      if (!infoTip.hidden) showTip();
    });
  }

  const byUnit = new Map();
  data.lessons.forEach((lesson) => {
    const k = String(lesson.unit);
    if (!byUnit.has(k)) byUnit.set(k, []);
    byUnit.get(k).push(lesson);
  });

  const orderedKeys = Array.from(byUnit.keys()).sort((a, b) => Number(a) - Number(b));

  const escapeHtml = window.escapeHtml || function(s) {
    return String(s).replace(/[&<>'"]/g, (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch])
    );
  };

  const testsByUnit = new Map();
  (data.unit_tests || []).forEach((t) => testsByUnit.set(t.unit, t));

  function savePrepIfActive() {
    if (activePrepVariant === null) return;
    const vals = {};
    root.querySelectorAll(".prep-input, .prep-area").forEach((inp) => {
      vals[`${inp.dataset.sec}-${inp.dataset.row}-${inp.dataset.part || ""}`] = inp.value;
    });
    savedPrepValues[activePrepVariant] = vals;
  }

  function renderTest(test) {
    savePrepIfActive();
    const introCount = test.questions.length;
    const items = test.questions
      .map((qq, idx) => {
        const opts = qq.options
          .map(
            (opt, oi) => `
              <label class="opt" data-idx="${oi}">
                <input type="radio" name="q-${idx}" value="${oi}" />
                <span class="opt-letter">${String.fromCharCode(65 + oi)}</span>
                <span class="opt-text">${escapeHtml(opt)}</span>
                <span class="opt-mark"></span>
              </label>
            `
          )
          .join("");
        return `
          <article class="quiz-item" data-q="${idx}" data-answer="${qq.answer}">
            <h4 class="quiz-q"><span class="quiz-num">${idx + 1}.</span> ${escapeHtml(qq.q)}</h4>
            <div class="opts">${opts}</div>
            <p class="quiz-explain" hidden>${escapeHtml(qq.explain || "")}</p>
          </article>
        `;
      })
      .join("");

    root.innerHTML = `
      <header class="lesson-head test-head">
        <p class="lesson-code">Test · Jedinica ${test.unit}
          <span class="book-page">${introCount} pitanja</span>
        </p>
        <h2>Provera znanja · Jedinica ${test.unit}</h2>
        <p class="lead">Izaberi jedan odgovor za svako pitanje. Klikni "Proveri rezultat" dole da vidiš koliko si pogodio/-la i obrazloženje za svaki odgovor.</p>
      </header>

      <section class="quiz">
        ${items}
      </section>

      <div class="quiz-actions">
        <button type="button" class="btn-primary" id="quiz-check">Proveri rezultat</button>
        <button type="button" class="btn-secondary" id="quiz-reset">Resetuj</button>
        <p class="quiz-score" id="quiz-score" aria-live="polite"></p>
      </div>
    `;

    const container = root.querySelector(".quiz");
    const scoreEl = root.querySelector("#quiz-score");

    root.querySelector("#quiz-check").addEventListener("click", () => {
      let correct = 0;
      const items = container.querySelectorAll(".quiz-item");
      items.forEach((item) => {
        const chosen = item.querySelector('input[type="radio"]:checked');
        const answerIdx = Number(item.dataset.answer);
        item.classList.remove("right", "wrong", "missed");
        item.querySelectorAll(".opt").forEach((o) => {
          o.classList.remove("is-correct", "is-wrong", "is-chosen");
        });
        const correctOpt = item.querySelector(`.opt[data-idx="${answerIdx}"]`);
        correctOpt.classList.add("is-correct");

        if (!chosen) {
          item.classList.add("missed");
        } else {
          const chosenIdx = Number(chosen.value);
          const chosenOpt = item.querySelector(`.opt[data-idx="${chosenIdx}"]`);
          chosenOpt.classList.add("is-chosen");
          if (chosenIdx === answerIdx) {
            item.classList.add("right");
            correct += 1;
          } else {
            item.classList.add("wrong");
            chosenOpt.classList.add("is-wrong");
          }
        }
        const explain = item.querySelector(".quiz-explain");
        if (explain) explain.hidden = false;
      });

      const pct = Math.round((correct / items.length) * 100);
      let mood = "🌧";
      if (pct >= 90) mood = "🌟";
      else if (pct >= 70) mood = "✅";
      else if (pct >= 50) mood = "🙂";
      else mood = "📚";

      scoreEl.textContent = `${mood} Rezultat: ${correct} / ${items.length} (${pct}%)`;
      scoreEl.classList.add("visible");
      const firstWrong = container.querySelector(".quiz-item.wrong, .quiz-item.missed");
      if (firstWrong) {
        firstWrong.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });

    root.querySelector("#quiz-reset").addEventListener("click", () => {
      container.querySelectorAll(".quiz-item").forEach((item) => {
        item.classList.remove("right", "wrong", "missed");
        item.querySelectorAll('input[type="radio"]').forEach((r) => (r.checked = false));
        item.querySelectorAll(".opt").forEach((o) =>
          o.classList.remove("is-correct", "is-wrong", "is-chosen")
        );
        const explain = item.querySelector(".quiz-explain");
        if (explain) explain.hidden = true;
      });
      scoreEl.textContent = "";
      scoreEl.classList.remove("visible");
      root.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  function prepLineHasBlank(line) {
    return /_{3,}/.test(line);
  }

  function prepStripItemPrefix(s) {
    return String(s).replace(/^[a-z]\)\s*/i, "").trim();
  }

  /** Jedinstvena normalizacija za poređenje (bez ocene znakova interpunkcije na kraju). */
  function prepNormalize(s) {
    let t = prepStripItemPrefix(String(s))
      .replace(/[\u2018\u2019\u201A\u201B]/g, "'")
      .trim()
      .toLowerCase()
      .replace(/\s+/g, " ");
    t = t.replace(/[.?!…]+$/g, "").trim();
    return t;
  }

  function prepVariantsFromSegment(segment) {
    return String(segment)
      .split(/\s*\/\s*/)
      .map((p) => prepNormalize(p))
      .filter(Boolean);
  }

  /** Više delova odvojeno tačka-zarezom (više praznina u jednom redu). */
  function prepSegmentsFromKey(expectedFull) {
    const core = prepStripItemPrefix(expectedFull);
    if (!core) return [];
    return core.split(/\s*;\s*/).map((x) => x.trim()).filter(Boolean);
  }

  function prepClearRowMarks(row) {
    row.classList.remove("prep-row-ok", "prep-row-warn", "prep-row-bad");
    row.querySelectorAll(".prep-input, .prep-area").forEach((el) => {
      el.classList.remove("prep-check-ok", "prep-check-bad", "prep-check-empty");
    });
  }

  function prepGradeRow(row) {
    const enc = row.getAttribute("data-expected-enc") || "";
    let expectedFull = "";
    try {
      expectedFull = decodeURIComponent(enc);
    } catch {
      expectedFull = "";
    }

    const inputs = [...row.querySelectorAll(".prep-input, .prep-area")];
    prepClearRowMarks(row);

    if (!inputs.length || !expectedFull.trim() || expectedFull.trim() === "—") {
      row.classList.add("prep-row-warn");
      return { ok: 0, bad: 0, empty: 0, skip: 1 };
    }

    const segments = prepSegmentsFromKey(expectedFull);

    if (inputs.length >= 2) {
      if (segments.length === inputs.length) {
        let ok = 0;
        let bad = 0;
        let empty = 0;
        inputs.forEach((inp, i) => {
          const raw = inp.value;
          if (!raw.trim()) {
            inp.classList.add("prep-check-empty");
            empty++;
            return;
          }
          const u = prepNormalize(raw);
          const vars = prepVariantsFromSegment(segments[i] || "");
          const hit = vars.some((v) => v === u);
          if (hit) {
            inp.classList.add("prep-check-ok");
            ok++;
          } else {
            inp.classList.add("prep-check-bad");
            bad++;
          }
        });
        if (bad > 0) row.classList.add("prep-row-bad");
        else if (empty > 0) row.classList.add("prep-row-warn");
        else row.classList.add("prep-row-ok");
        return { ok, bad, empty, skip: 0 };
      }
      const joinedUser = prepNormalize(inputs.map((i) => i.value).join("; "));
      const joinedKey = prepNormalize(segments.join("; "));
      if (!inputs.some((i) => i.value.trim())) {
        inputs.forEach((i) => i.classList.add("prep-check-empty"));
        row.classList.add("prep-row-bad");
        return { ok: 0, bad: 0, empty: inputs.length, skip: 0 };
      }
      if (segments.length === 1 && inputs.length > 1) {
        inputs.forEach((inp) => {
          if (!inp.value.trim()) inp.classList.add("prep-check-empty");
          else inp.classList.add("prep-check-bad");
        });
        row.classList.add("prep-row-warn");
        return { ok: 0, bad: inputs.length, empty: 0, skip: 1 };
      }
      const hit = joinedUser === joinedKey;
      let emptyJoin = 0;
      inputs.forEach((inp) => {
        if (!inp.value.trim()) {
          inp.classList.add("prep-check-empty");
          emptyJoin++;
        } else if (hit) inp.classList.add("prep-check-ok");
        else inp.classList.add("prep-check-bad");
      });
      if (hit) {
        row.classList.add("prep-row-ok");
        return { ok: inputs.filter((i) => i.value.trim()).length, bad: 0, empty: emptyJoin, skip: 0 };
      }
      row.classList.add("prep-row-bad");
      return {
        ok: 0,
        bad: inputs.filter((i) => i.value.trim()).length,
        empty: emptyJoin,
        skip: 0,
      };
    }

    const inp = inputs[0];
    const raw = inp.value;
    if (!raw.trim()) {
      inp.classList.add("prep-check-empty");
      row.classList.add("prep-row-bad");
      return { ok: 0, bad: 0, empty: 1, skip: 0 };
    }
    const u = prepNormalize(raw);
    const stripped = prepStripItemPrefix(expectedFull);
    let hit = false;
    if (stripped.includes("/")) {
      hit = stripped
        .split(/\s*\/\s*/)
        .some((p) => prepNormalize(p) === u);
    } else {
      hit = prepNormalize(stripped) === u;
    }
    if (hit) {
      inp.classList.add("prep-check-ok");
      row.classList.add("prep-row-ok");
      return { ok: 1, bad: 0, empty: 0, skip: 0 };
    }
    inp.classList.add("prep-check-bad");
    row.classList.add("prep-row-bad");
    return { ok: 0, bad: 1, empty: 0, skip: 0 };
  }

  /**
   * Jedna stavka zadatka: ili polja gde su ___ crtice, ili jedno široko polje za celu rečenicu.
   * expected — tekst iz ključa za tu stavku (prikaže se kad korisnik traži predlog).
   */
  function renderPrepItem(line, secNum, rowIdx, expected) {
    const exp = expected != null ? String(expected) : "—";
    const enc = encodeURIComponent(exp);
    const hintBlock = `<p class="prep-expected" hidden><span class="prep-expected-label">Predlog:</span> ${escapeHtml(exp)}</p>`;

    if (!prepLineHasBlank(line)) {
      return `
        <li class="prep-row prep-row-wide" data-sec="${secNum}" data-row="${rowIdx}" data-expected-enc="${enc}">
          <div class="prep-prompt">${escapeHtml(line)}</div>
          <textarea class="prep-area" rows="2" spellcheck="false" data-sec="${secNum}" data-row="${rowIdx}" placeholder="Ovde upiši odgovor…"></textarea>
          ${hintBlock}
        </li>`;
    }

    const parts = line.split(/_{3,}/);
    const chunks = [];
    parts.forEach((part, i) => {
      chunks.push(`<span class="prep-part">${escapeHtml(part)}</span>`);
      if (i < parts.length - 1) {
        chunks.push(
          `<input type="text" class="prep-input" spellcheck="false" autocapitalize="off" autocomplete="off" data-sec="${secNum}" data-row="${rowIdx}" data-part="${i}" />`
        );
      }
    });

    return `
      <li class="prep-row prep-row-fill" data-sec="${secNum}" data-row="${rowIdx}" data-expected-enc="${enc}">
        <div class="prep-line-wrap">${chunks.join("")}</div>
        ${hintBlock}
      </li>`;
  }

  function renderPrepPractice(pt) {
    savePrepIfActive();
    activePrepVariant = pt.variant;

    const answersBySec = new Map();
    (pt.answer_key || []).forEach((block) => {
      answersBySec.set(block.n, block.items || []);
    });

    const sectionsHtml = (pt.sections || [])
      .map((sec) => {
        const expList = answersBySec.get(sec.n) || [];
        const items = (sec.items || [])
          .map((line, i) => renderPrepItem(line, sec.n, i, expList[i]))
          .join("");
        return `
        <section class="prep-sec" id="prep-sec-${sec.n}">
          <h3 class="prep-sec-head">${escapeHtml(sec.instruction)}</h3>
          <ul class="prep-items">${items}</ul>
        </section>`;
      })
      .join("");

    const answersHtml = (pt.answer_key || [])
      .map(
        (block) => `
        <section class="prep-ak-sec">
          <h4 class="prep-ak-h">Sekcija ${block.n}</h4>
          <ul class="prep-ak-list">
            ${(block.items || []).map((x) => `<li>${escapeHtml(x)}</li>`).join("")}
          </ul>
        </section>`
      )
      .join("");

    const prepActionsBar = `
        <div class="prep-actions">
          <button type="button" class="btn-primary prep-action-check">Proveri moje odgovore</button>
          <button type="button" class="btn-secondary prep-action-hints">Prikaži predloge uz zadatke</button>
          <button type="button" class="btn-secondary prep-action-clear">Očisti sva polja</button>
        </div>`;

    root.innerHTML = `
      <header class="lesson-head prep-head">
        <p class="lesson-code">${escapeHtml(pt.title_sr)}
          <span class="book-page">7A–10B</span>
        </p>
        <h2>TEST – PREPARATION</h2>
        <p class="lead">${escapeHtml(pt.scope_sr || "")}</p>
        <p class="prep-cta-banner"><strong>Provera:</strong> kada popuniš zadatke, skroluj do <strong>kraja stranice</strong> — tamo su dugmad <strong>„Proveri moje odgovore“</strong>, predlozi i brisanje.</p>
        <p class="prep-note">Tačna polja postanu zelena, netačna crvena, prazna žuta. Poređenje ignoriše velika/mala slova i znak na kraju (. ?). Ako u ključu piše <strong>/</strong>, važi bilo koja varijanta.</p>
      </header>
      <article class="prep-sheet">
        ${sectionsHtml}
        ${prepActionsBar}
        <p class="prep-check-summary" id="prep-check-summary" aria-live="polite"></p>
      </article>
      <details class="prep-key-wrap">
        <summary class="prep-key-sum">Ceo ključ odgovora (sve sekcije)</summary>
        <div class="prep-key-body">${answersHtml}</div>
      </details>
    `;

    const summaryEl = root.querySelector("#prep-check-summary");
    let hintsOn = false;

    function setHintsLabels(text) {
      root.querySelectorAll(".prep-action-hints").forEach((b) => {
        b.textContent = text;
      });
    }

    const runCheck = () => {
      const rows = root.querySelectorAll(".prep-row");
      let ok = 0;
      let bad = 0;
      let empty = 0;
      let skip = 0;
      rows.forEach((row) => {
        const r = prepGradeRow(row);
        ok += r.ok;
        bad += r.bad;
        empty += r.empty;
        skip += r.skip || 0;
      });
      if (summaryEl) {
        const parts = [`Tačno polja: ${ok}`, `netačno: ${bad}`, `prazno: ${empty}`];
        if (skip) parts.push(`bez ključa: ${skip}`);
        summaryEl.textContent = parts.join(" · ");
      }
      const firstBad = root.querySelector(".prep-row-bad, .prep-row-warn");
      if (firstBad) {
        firstBad.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      savePrepIfActive();
      savePrepLS();
    };

    root.querySelectorAll(".prep-action-check").forEach((btn) => {
      btn.addEventListener("click", runCheck);
    });

    root.querySelectorAll(".prep-action-hints").forEach((hintsBtn) => {
      hintsBtn.addEventListener("click", () => {
        hintsOn = !hintsOn;
        root.querySelectorAll(".prep-expected").forEach((el) => {
          el.hidden = !hintsOn;
        });
        setHintsLabels(hintsOn ? "Sakrij predloge uz zadatke" : "Prikaži predloge uz zadatke");
      });
    });

    root.querySelectorAll(".prep-action-clear").forEach((clearBtn) => {
      clearBtn.addEventListener("click", () => {
        root.querySelectorAll(".prep-row").forEach((row) => prepClearRowMarks(row));
        root.querySelectorAll(".prep-input, .prep-area").forEach((el) => {
          el.value = "";
        });
        if (activePrepVariant !== null) delete savedPrepValues[activePrepVariant];
        if (summaryEl) summaryEl.textContent = "";
        if (hintsOn) {
          hintsOn = false;
          root.querySelectorAll(".prep-expected").forEach((el) => {
            el.hidden = true;
          });
          setHintsLabels("Prikaži predloge uz zadatke");
        }
      });
    });

    if (savedPrepValues[pt.variant]) {
      const vals = savedPrepValues[pt.variant];
      root.querySelectorAll(".prep-input, .prep-area").forEach((inp) => {
        const k = `${inp.dataset.sec}-${inp.dataset.row}-${inp.dataset.part || ""}`;
        if (vals[k] !== undefined) inp.value = vals[k];
      });
    }
  }

  function renderPairTable(pairs, opts) {
    if (!pairs || !pairs.length) return "";
    const rows = pairs
      .map(
        (p) => `
          <tr>
            <td class="en">${escapeHtml(p.en)}</td>
            <td class="sr">${escapeHtml(p.sr)}</td>
          </tr>`
      )
      .join("");
    return `
      <div class="pair-table-wrap">
        <table class="pair-table">
          <thead>
            <tr>
              <th>${escapeHtml(opts.headEn)}</th>
              <th>${escapeHtml(opts.headSr)}</th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
    `;
  }

  function renderLesson(lesson) {
    savePrepIfActive();
    const ep = lesson.extra_practice || {};

    const tocRows = [
      `<div><dt>Vokabular</dt><dd>${escapeHtml(lesson.toc_vocab_en || "—")}</dd></div>`,
      `<div><dt>Gramatika</dt><dd>${escapeHtml(lesson.toc_grammar_en || "—")}</dd></div>`,
    ];
    if (lesson.toc_rw_en && lesson.toc_rw_en.trim()) {
      tocRows.push(
        `<div><dt>Real World</dt><dd>${escapeHtml(lesson.toc_rw_en)}</dd></div>`
      );
    }

    const priorities = (lesson.priorities_sr || [])
      .map((p) => `<li>${escapeHtml(p)}</li>`)
      .join("");

    const vocab = lesson.vocab || [];
    const phrases = lesson.phrases || [];
    const grammar = lesson.grammar_examples || [];

    const vocabBlock = vocab.length
      ? `
        <section class="block vocab" id="vocab">
          <header class="block-head">
            <h3>Rečnik · ${vocab.length} reči</h3>
            <p class="block-sub">Glavne reči i izrazi koje treba znati napamet — uz srpski prevod.</p>
          </header>
          ${renderPairTable(vocab, { headEn: "Engleski", headSr: "Srpski" })}
          <button type="button" class="vocab-quiz-start">🎯 Vežbaj rečnik</button>
          <div class="vocab-quiz" id="vocab-quiz" style="display:none"></div>
        </section>
      `
      : "";

    const phrasesBlock = phrases.length
      ? `
        <section class="block phrases" id="phrases">
          <header class="block-head">
            <h3>Ključne fraze · ${phrases.length}</h3>
            <p class="block-sub">Tipične rečenice i pitanja iz lekcije — funkcionalni jezik za upotrebu.</p>
          </header>
          ${renderPairTable(phrases, { headEn: "Engleski", headSr: "Srpski" })}
        </section>
      `
      : "";

    const grammarBlock = grammar.length
      ? `
        <section class="block grammar" id="grammar">
          <header class="block-head">
            <h3>Gramatički primeri · ${grammar.length}</h3>
            <p class="block-sub">Ključne forme i pravila iz HELP WITH GRAMMAR / VOCABULARY okvira.</p>
          </header>
          ${renderPairTable(grammar, { headEn: "Primer / pravilo", headSr: "Objašnjenje" })}
        </section>
      `
      : "";

    const lessonText = escapeHtml(lesson.lesson_text || "");
    const epText = escapeHtml(ep.ep_text || "");

    root.innerHTML = `
      <header class="lesson-head">
        <p class="lesson-code">Jedinica ${lesson.unit} · ${escapeHtml(lesson.code)}
          <span class="book-page">strana ${escapeHtml(lesson.book_page)}</span>
        </p>
        <h2>${escapeHtml(lesson.title_en)}</h2>
      </header>

      <dl class="toc-meta">${tocRows.join("")}</dl>

      <section class="block summary">
        <h3>Rezime na srpskom</h3>
        <p class="lead">${escapeHtml(lesson.summary_sr || "—")}</p>
      </section>

      ${vocabBlock}
      ${phrasesBlock}
      ${grammarBlock}

      ${priorities ? `
        <section class="block priorities">
          <h3>Šta prvo savladati</h3>
          <ol class="priorities-list">${priorities}</ol>
        </section>
      ` : ""}

      ${epText ? `
      <section class="block ep">
        <details>
          <summary><span>Extra Practice ${ep.n || "–"} · ${escapeHtml(lesson.code)}</span><span class="hint">${escapeHtml(ep.sb_page_printed || "")}</span></summary>
          <pre class="ocr">${epText}</pre>
        </details>
      </section>
      ` : ""}
      <button type="button" class="scroll-top-btn" aria-label="Skrol na vrh">↑</button>
    `;
    const stb = root.querySelector(".scroll-top-btn");
    if (stb) stb.addEventListener("click", () => root.firstElementChild?.scrollIntoView({ behavior: "smooth" }));

    const startBtn = root.querySelector(".vocab-quiz-start");
    const quizEl = root.querySelector("#vocab-quiz");
    if (startBtn && quizEl && vocab.length) {
      startBtn.addEventListener("click", () => startVocabQuiz(vocab, quizEl, startBtn));
    }
  }

  function startVocabQuiz(vocab, quizEl, startBtn) {
    startBtn.style.display = "none";

    function buildPool() {
      const pool = [];
      for (const l of data.lessons) {
        if (l.vocab) {
          for (const v of l.vocab) {
            if (v.en && v.sr) pool.push({ en: v.en, sr: v.sr });
          }
        }
      }
      return pool;
    }

    const allPool = buildPool();
    const items = shuffle(vocab).map((v) => ({ en: v.en, sr: v.sr }));
    let idx = 0;
    let score = 0;
    let answered = false;

    function showItem() {
      if (idx >= items.length) {
        showDone();
        return;
      }
      answered = false;
      const item = items[idx];
      const enToSr = Math.random() < 0.5;
      const question = enToSr ? item.en : item.sr;
      const correctAnswer = enToSr ? item.sr : item.en;
      const direction = enToSr ? "engleski → srpski" : "srpski → engleski";

      let wrongPool = allPool.filter((p) => p.en !== item.en);
      if (wrongPool.length < 3) {
        wrongPool = allPool.filter((p) => p.sr !== item.sr);
      }
      const wrongOptions = shuffle(wrongPool).slice(0, 3).map((p) => enToSr ? p.sr : p.en);
      const options = shuffle([correctAnswer, ...wrongOptions]);

      quizEl.style.display = "block";
      quizEl.innerHTML = `
        <div class="vocab-quiz-header">
          <h4>Vežbaj rečnik</h4>
          <span class="vocab-quiz-score">${score}/${idx}</span>
        </div>
        <p class="vocab-quiz-direction">${direction}</p>
        <p class="vocab-quiz-word">${escapeHtml(question)}</p>
        <div class="vocab-quiz-opts">
          ${options.map((opt) => `<button type="button">${escapeHtml(opt)}</button>`).join("")}
        </div>
        <p class="vocab-quiz-feedback"></p>
      `;

      const optBtns = quizEl.querySelectorAll(".vocab-quiz-opts button");
      const feedback = quizEl.querySelector(".vocab-quiz-feedback");

      optBtns.forEach((btn) => {
        btn.addEventListener("click", () => {
          if (answered) return;
          answered = true;
          const isCorrect = btn.textContent === correctAnswer;
          if (isCorrect) score++;
          optBtns.forEach((b) => b.disabled = true);
          optBtns.forEach((b) => {
            if (b.textContent === correctAnswer) b.classList.add("correct");
            else if (b === btn) b.classList.add("wrong");
          });
          feedback.textContent = isCorrect ? "✅ Tačno!" : `❌ Netočno. Tačan odgovor: ${escapeHtml(correctAnswer)}`;

          const scoreEl = quizEl.querySelector(".vocab-quiz-score");
          if (scoreEl) scoreEl.textContent = `${score}/${idx + 1}`;

          setTimeout(() => {
            idx++;
            showItem();
          }, 1200);
        });
      });
    }

    function showDone() {
      const pct = Math.round((score / items.length) * 100);
      quizEl.innerHTML = `
        <div class="vocab-quiz-done">
          <p>Kviz završen!</p>
          <p class="score-frac">${score}/${items.length}</p>
          <p>${pct === 100 ? "Savršeno! 🎉" : pct >= 80 ? "Odlično! 👏" : pct >= 60 ? "Dobro 👍" : "Vežbaj još 💪"}</p>
          <button type="button" class="vocab-quiz-reset">Pokušaj ponovo</button>
        </div>
      `;
      const resetBtn = quizEl.querySelector(".vocab-quiz-reset");
      resetBtn.addEventListener("click", () => {
        idx = 0;
        score = 0;
        showItem();
      });
    }

    showItem();
  }

  if (root) {
  orderedKeys.forEach((key, idx) => {
    const lessons = byUnit.get(key);
    const details = document.createElement("details");
    details.open = idx === 0;

    const summary = document.createElement("summary");
    const titleSpan = document.createElement("span");
    titleSpan.textContent = `Jedinica ${key}`;
    summary.append(titleSpan);

    const chip = document.createElement("span");
    chip.className = "unit-chip";
    chip.textContent = lessons.map((l) => l.code).join(" · ");
    summary.append(chip);
    details.append(summary);

    const ul = document.createElement("ul");
    lessons.forEach((lesson) => {
      const li = document.createElement("li");
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = lesson.code;
      btn.title = lesson.title_en;
      btn.dataset.id = lesson.id;
      btn.addEventListener("click", () => {
        if (!root) {
          window.location.href = "./index.html?lesson=" + encodeURIComponent(lesson.id);
          return;
        }
        clearNavActives();
        btn.classList.add("active");
        renderLesson(lesson);
        hideNavOnMobile();
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      li.append(btn);

      const cap = document.createElement("span");
      cap.className = "lesson-title-hint";
      cap.textContent = lesson.title_en;
      li.append(cap);
      navItems.push({ type: "lesson", btn, lesson });

      ul.append(li);
    });

    const test = testsByUnit.get(Number(key));
    if (test) {
      const li = document.createElement("li");
      li.className = "test-item";
      const tbtn = document.createElement("button");
      tbtn.type = "button";
      tbtn.className = "test-btn";
      const tspan = document.createElement("span");
      tspan.textContent = `📝 Test · 10 pitanja`;
      tbtn.appendChild(tspan);
      tbtn.title = `Test posle Jedinice ${key}`;
      tbtn.dataset.testUnit = String(test.unit);
      tbtn.addEventListener("click", () => {
        if (!root) { window.location.href = "./index.html?test=" + test.unit; return; }
        clearNavActives();
        tbtn.classList.add("active");
        renderTest(test);
        hideNavOnMobile();
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      li.append(tbtn);
      ul.append(li);
      navItems.push({ type: "test", btn: tbtn, unit: test.unit });
    }

    details.append(ul);
    nav.append(details);
  });

  const prepTests = data.prep_practice_tests || [];
  if (prepTests.length && navPane) {
    const prepDetails = document.createElement("details");
    prepDetails.className = "prep-nav-details";
    const prepSum = document.createElement("summary");
    const prepTitle = document.createElement("span");
    prepTitle.textContent = "Vežbanje · Priprema";
    const prepChip = document.createElement("span");
    prepChip.className = "unit-chip";
    prepChip.textContent = "7A–10B · 1–10";
    prepSum.append(prepTitle, prepChip);
    prepDetails.appendChild(prepSum);

    const prepHint = document.createElement("p");
    prepHint.className = "prep-nav-hint";
    prepHint.textContent =
      "Izaberi broj ispod — zadaci se otvaraju desno. Dugmad za proveru su na dnu vežbe (skroluj do kraja).";
    prepDetails.appendChild(prepHint);

    const prepUl = document.createElement("ul");
    prepUl.className = "prep-nav-list";
    prepTests.forEach((pt) => {
      const li = document.createElement("li");
      li.className = "prep-nav-item";
      const pb = document.createElement("button");
      pb.type = "button";
      pb.className = "prep-variant-btn";
      pb.textContent = String(pt.variant);
      pb.setAttribute("aria-label", `Priprema, set ${pt.variant}`);
      pb.title = pt.scope_sr || "";
      pb.addEventListener("click", () => {
        if (!root) { window.location.href = "./index.html?prep=" + pt.variant; return; }
        clearNavActives();
        pb.classList.add("active");
        renderPrepPractice(pt);
        hideNavOnMobile();
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      navItems.push({ type: "prep", btn: pb, pt });
      li.appendChild(pb);
      prepUl.appendChild(li);
    });
    prepDetails.appendChild(prepUl);
    nav.appendChild(prepDetails);
  }

  /* ---------- vocabulary quiz sets ---------- */
  const vocabSets = [];
  const unitGroups = [
    [1, "1A–1D"],
    [2, "2A–2D"],
    [3, "3A–3D"],
    [4, "4A–4D"],
    [5, "5A–5D"],
    [6, "6A–6D"],
    [7, "7A–7D"],
    [8, "8A–8D"],
    [9, 10, "9A–10D"],
    [11, 12, "11A–12C"],
  ];
  unitGroups.forEach((g) => {
    const label = g.pop();
    const units = g;
    const items = [];
    units.forEach((u) => {
      const lessons = byUnit.get(String(u)) || [];
      lessons.forEach((l) => {
        if (l.vocab) {
          l.vocab.forEach((v) => {
            if (v.en && v.sr) items.push({ en: v.en, sr: v.sr });
          });
        }
      });
    });
    if (items.length) {
      vocabSets.push({ variant: vocabSets.length + 1, label, items });
    }
  });

  if (vocabSets.length && navPane) {
    const vqDetails = document.createElement("details");
    vqDetails.className = "prep-nav-details";
    const vqSum = document.createElement("summary");
    const vqTitle = document.createElement("span");
    vqTitle.textContent = "Vežbanje · Rečnik";
    const vqChip = document.createElement("span");
    vqChip.className = "unit-chip";
    vqChip.textContent = vocabSets[0].label + " – " + vocabSets[vocabSets.length - 1].label;
    vqSum.append(vqTitle, vqChip);
    vqDetails.appendChild(vqSum);

    const vqHint = document.createElement("p");
    vqHint.className = "prep-nav-hint";
    vqHint.textContent = "Izaberi broj ispod — rečnik iz datih lekcija. engleski ↔ srpski.";
    vqDetails.appendChild(vqHint);

    const vqUl = document.createElement("ul");
    vqUl.className = "prep-nav-list";
    vocabSets.forEach((vs) => {
      const li = document.createElement("li");
      li.className = "prep-nav-item";
      const vb = document.createElement("button");
      vb.type = "button";
      vb.className = "prep-variant-btn";
      vb.textContent = String(vs.variant);
      vb.setAttribute("aria-label", `Rečnik, set ${vs.variant} · ${vs.label}`);
      vb.title = vs.label + " · " + vs.items.length + " reči";
      vb.addEventListener("click", () => {
        if (!root) { window.location.href = "./index.html?vquiz=" + vs.variant; return; }
        clearNavActives();
        vb.classList.add("active");
        renderVocabQuiz(vs);
        hideNavOnMobile();
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      navItems.push({ type: "vquiz", btn: vb, variant: vs.variant });
      li.appendChild(vb);
      vqUl.appendChild(li);
    });
    vqDetails.appendChild(vqUl);
    nav.appendChild(vqDetails);
  }
  }

  function renderVocabQuiz(set) {
    savePrepIfActive();
    const items = shuffle(set.items);
    const limit = Math.min(items.length, 15);
    const quizItems = shuffle(items).slice(0, limit);
    root.innerHTML = `
      <header class="lesson-head">
        <h2>Rečnik · Set ${set.variant}</h2>
        <p class="lesson-code">${set.label} · ${set.items.length} reči · ${limit} pitanja</p>
      </header>
      <div class="vocab-quiz" id="vocab-quiz"></div>
    `;
    const quizEl = root.querySelector("#vocab-quiz");
    startVocabQuizInline(quizItems, quizEl);
  }

  function startVocabQuizInline(items, quizEl) {
    let idx = 0;
    let score = 0;
    let answered = false;

    function buildPool() {
      const pool = [];
      for (const l of data.lessons) {
        if (l.vocab) {
          for (const v of l.vocab) {
            if (v.en && v.sr) pool.push({ en: v.en, sr: v.sr });
          }
        }
      }
      return pool;
    }
    const allPool = buildPool();

    function showItem() {
      if (idx >= items.length) { showDone(); return; }
      answered = false;
      const item = items[idx];
      const enToSr = Math.random() < 0.5;
      const question = enToSr ? item.en : item.sr;
      const correctAnswer = enToSr ? item.sr : item.en;
      const direction = enToSr ? "engleski → srpski" : "srpski → engleski";

      let wrongPool = allPool.filter((p) => p.en !== item.en);
      if (wrongPool.length < 3) wrongPool = allPool.filter((p) => p.sr !== item.sr);
      const wrongOptions = shuffle(wrongPool).slice(0, 3).map((p) => enToSr ? p.sr : p.en);
      const options = shuffle([correctAnswer, ...wrongOptions]);

      quizEl.innerHTML = `
        <div class="vocab-quiz-header">
          <h4>Vežbaj rečnik · ${idx + 1}/${items.length}</h4>
          <span class="vocab-quiz-score">${score}/${idx}</span>
        </div>
        <p class="vocab-quiz-direction">${direction}</p>
        <p class="vocab-quiz-word">${escapeHtml(question)}</p>
        <div class="vocab-quiz-opts">
          ${options.map((o) => `<button type="button">${escapeHtml(o)}</button>`).join("")}
        </div>
        <p class="vocab-quiz-feedback"></p>
      `;

      const btns = quizEl.querySelectorAll(".vocab-quiz-opts button");
      const feedback = quizEl.querySelector(".vocab-quiz-feedback");
      btns.forEach((btn) => {
        btn.addEventListener("click", () => {
          if (answered) return;
          answered = true;
          const isCorrect = btn.textContent === correctAnswer;
          if (isCorrect) score++;
          btns.forEach((b) => b.disabled = true);
          btns.forEach((b) => {
            if (b.textContent === correctAnswer) b.classList.add("correct");
            else if (b === btn) b.classList.add("wrong");
          });
          feedback.textContent = isCorrect ? "✅ Tačno!" : `❌ Netočno. Tačan odgovor: ${escapeHtml(correctAnswer)}`;
          const se = quizEl.querySelector(".vocab-quiz-score");
          if (se) se.textContent = `${score}/${idx + 1}`;
          setTimeout(() => { idx++; showItem(); }, 1200);
        });
      });
    }

    function showDone() {
      const pct = Math.round((score / items.length) * 100);
      quizEl.innerHTML = `
        <div class="vocab-quiz-done">
          <p>Kviz završen!</p>
          <p class="score-frac">${score}/${items.length}</p>
          <p>${pct === 100 ? "Savršeno! 🎉" : pct >= 80 ? "Odlično! 👏" : pct >= 60 ? "Dobro 👍" : "Vežbaj još 💪"}</p>
          <button type="button" class="vocab-quiz-reset">Pokušaj ponovo</button>
        </div>
      `;
      quizEl.querySelector(".vocab-quiz-reset")?.addEventListener("click", () => {
        idx = 0; score = 0; showItem();
      });
    }

    showItem();
  }

  if (!root) return;

  root.addEventListener("input", (e) => {
    const t = e.target;
    if (!t.matches(".prep-input, .prep-area")) return;
    const row = t.closest(".prep-row");
    if (row) prepClearRowMarks(row);
    const sum = document.getElementById("prep-check-summary");
    if (sum) sum.textContent = "";
    savePrepIfActive();
    savePrepLS();
  });

  /* ---------- keyboard navigation ---------- */
  let currentNavIdx = -1;
  function setCurrentNavIdx(idx) {
    if (idx < 0) idx = 0;
    if (idx >= navItems.length) idx = navItems.length - 1;
    currentNavIdx = idx;
  }
  function getCurrentNavIdx() {
    if (currentNavIdx >= 0) return currentNavIdx;
    const active = navPane.querySelector("button.active");
    if (active) {
      return navItems.findIndex((item) => item.btn === active);
    }
    return 0;
  }
  function activateNavItem(item) {
    if (!root) {
      if (item.type === "lesson") {
        window.location.href = "./index.html?lesson=" + encodeURIComponent(item.btn.dataset.id);
      } else if (item.type === "test") {
        window.location.href = "./index.html?test=" + item.unit;
      } else if (item.type === "prep") {
        window.location.href = "./index.html?prep=" + item.pt.variant;
      } else if (item.type === "vquiz") {
        window.location.href = "./index.html?vquiz=" + item.variant;
      } else {
        window.location.href = "./index.html";
      }
      return;
    }
    clearNavActives();
    item.btn.classList.add("active");
    if (item.type === "lesson") {
      renderLesson(item.lesson);
    } else if (item.type === "test") {
      const test = testsByUnit.get(Number(item.unit));
      if (test) renderTest(test);
    } else if (item.type === "prep") {
      renderPrepPractice(item.pt);
    } else if (item.type === "vquiz") {
      const vs = vocabSets.find((s) => s.variant === item.variant);
      if (vs) renderVocabQuiz(vs);
    }
    if (window.matchMedia("(max-width: 900px)").matches) {
      root.scrollIntoView({ behavior: "smooth", block: "start" });
    } else {
      root.scrollTo({ top: 0 });
    }
  }

  document.addEventListener("keydown", (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    if (e.target.closest("input, textarea, select, [contenteditable]")) return;
    const idx = getCurrentNavIdx();
    if (idx < 0) return;
    let next = idx;
    if (e.key === "ArrowLeft") next = idx - 1;
    if (e.key === "ArrowRight") next = idx + 1;
    if (next < 0 || next >= navItems.length) return;
    e.preventDefault();
    setCurrentNavIdx(next);
    activateNavItem(navItems[next]);
  });

  /* ---------- initial render ---------- */
  if (root) {
    const params = new URLSearchParams(location.search);
    const lessonId = params.get("lesson");
    const testUnit = params.get("test");
    const prepVariant = params.get("prep");
    const vquizVariant = params.get("vquiz");

    if (vquizVariant) {
      const vs = vocabSets.find((s) => String(s.variant) === vquizVariant);
      const vbtn = nav.querySelectorAll(".prep-variant-btn");
      const matchBtn = Array.from(vbtn).find((b) => b.textContent.trim() === vquizVariant && b.closest(".prep-nav-details")?.querySelector("summary span")?.textContent === "Vežbanje · Rečnik");
      if (vs && matchBtn) {
        matchBtn.classList.add("active");
        renderVocabQuiz(vs);
      } else if (vs) {
        renderVocabQuiz(vs);
      } else {
        fallbackFirst();
      }
    } else if (testUnit) {
      const test = testsByUnit.get(Number(testUnit));
      const tbtn = nav.querySelector(`button[data-test-unit="${CSS.escape(testUnit)}"]`);
      if (test && tbtn) {
        tbtn.classList.add("active");
        renderTest(test);
      } else if (test) {
        renderTest(test);
      } else {
        fallbackFirst();
      }
    } else if (prepVariant) {
      const pt = data.prep_practice_tests.find((p) => String(p.variant) === prepVariant);
      const pbtn = nav.querySelector(`.prep-variant-btn`);
      const matchBtn = pbtn && pbtn.closest(".prep-nav-list")
        ? Array.from(pbtn.closest(".prep-nav-list").querySelectorAll(".prep-variant-btn")).find(
            (b) => b.textContent.trim() === prepVariant
          )
        : null;
      if (pt && matchBtn) {
        matchBtn.classList.add("active");
        renderPrepPractice(pt);
      } else if (pt) {
        renderPrepPractice(pt);
      } else {
        fallbackFirst();
      }
    } else if (lessonId) {
      const targetBtn = nav.querySelector(`button[data-id="${CSS.escape(lessonId)}"]`);
      if (targetBtn) {
        targetBtn.classList.add("active");
        const lesson = data.lessons.find((l) => l.id === targetBtn.dataset.id);
        if (lesson) renderLesson(lesson);
      } else {
        fallbackFirst();
      }
    } else {
      fallbackFirst();
    }

    function fallbackFirst() {
      const firstBtn = nav.querySelector("button");
      if (firstBtn) {
        firstBtn.classList.add("active");
        const lesson = data.lessons.find((l) => l.id === firstBtn.dataset.id);
        if (lesson) renderLesson(lesson);
      }
    }
  }
})();
