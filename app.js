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

  if (!data || !root || !nav) {
    console.error("Nedostaju podaci ili markup.");
    return;
  }

  const titleEl = document.getElementById("course-title");
  const notesEl = document.getElementById("course-notes");
  if (titleEl) titleEl.textContent = "Lekcije 1A – 12C";
  if (notesEl) notesEl.textContent = data.course.notes_sr;

  const byUnit = new Map();
  data.lessons.forEach((lesson) => {
    const k = String(lesson.unit);
    if (!byUnit.has(k)) byUnit.set(k, []);
    byUnit.get(k).push(lesson);
  });

  const orderedKeys = Array.from(byUnit.keys()).sort((a, b) => Number(a) - Number(b));

  function escapeHtml(s) {
    return String(s).replace(/[&<>'"]/g, (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch])
    );
  }

  const testsByUnit = new Map();
  (data.unit_tests || []).forEach((t) => testsByUnit.set(t.unit, t));

  function renderTest(test) {
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

      <section class="block book-text">
        <details>
          <summary><span>Originalni tekst lekcije iz knjige</span><span class="hint">OCR sa stranice ${escapeHtml(lesson.book_page)}</span></summary>
          <pre class="ocr">${lessonText || "(tekst nije pronađen u OCR izlazu)"}</pre>
        </details>
      </section>

      <section class="block ep">
        <details>
          <summary><span>Extra Practice ${ep.n || "–"} · ${escapeHtml(lesson.code)}</span><span class="hint">${escapeHtml(ep.sb_page_printed || "")}</span></summary>
          <pre class="ocr">${epText || "(nije pronađen blok za ovu podlekciju u OCR izlazu)"}</pre>
        </details>
      </section>
    `;
  }

  root.addEventListener("input", (e) => {
    const t = e.target;
    if (!t.matches(".prep-input, .prep-area")) return;
    const row = t.closest(".prep-row");
    if (row) prepClearRowMarks(row);
    const sum = document.getElementById("prep-check-summary");
    if (sum) sum.textContent = "";
  });

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
        clearNavActives();
        btn.classList.add("active");
        renderLesson(lesson);
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

      ul.append(li);
    });

    const test = testsByUnit.get(Number(key));
    if (test) {
      const li = document.createElement("li");
      li.className = "test-item";
      const tbtn = document.createElement("button");
      tbtn.type = "button";
      tbtn.className = "test-btn";
      tbtn.textContent = `📝 Test · 10 pitanja`;
      tbtn.title = `Test posle Jedinice ${key}`;
      tbtn.dataset.testUnit = String(test.unit);
      tbtn.addEventListener("click", () => {
        clearNavActives();
        tbtn.classList.add("active");
        renderTest(test);
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      li.append(tbtn);
      ul.append(li);
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
        clearNavActives();
        pb.classList.add("active");
        renderPrepPractice(pt);
        if (window.matchMedia("(max-width: 900px)").matches) {
          root.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
          root.scrollTo({ top: 0 });
        }
      });
      li.appendChild(pb);
      prepUl.appendChild(li);
    });
    prepDetails.appendChild(prepUl);
    nav.appendChild(prepDetails);
  }

  const firstBtn = nav.querySelector("button");
  if (firstBtn) {
    firstBtn.classList.add("active");
    const first = data.lessons.find((l) => l.id === firstBtn.dataset.id);
    if (first) renderLesson(first);
  }
})();
