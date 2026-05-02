(function () {
  "use strict";

  const root = document.getElementById("lesson-view");
  const nav = document.getElementById("lesson-nav");
  const data = window.__LESSONS_DATA__ || null;

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
        nav.querySelectorAll("button.active").forEach((b) => b.classList.remove("active"));
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
        nav.querySelectorAll("button.active").forEach((b) => b.classList.remove("active"));
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

  const firstBtn = nav.querySelector("button");
  if (firstBtn) {
    firstBtn.classList.add("active");
    const first = data.lessons.find((l) => l.id === firstBtn.dataset.id);
    if (first) renderLesson(first);
  }
})();
