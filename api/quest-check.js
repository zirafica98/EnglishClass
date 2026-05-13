/**
 * Vercel Serverless: provera speaking odgovora (EN).
 * - Gramatika: LanguageTool (bez ključa).
 * - AI: prvo Claude ako postoji ANTHROPIC_API_KEY, inače OpenAI ako postoji OPENAI_API_KEY.
 *   Strukturisan JSON (srpski + revised_en), uz LanguageTool kao kontekst.
 */
const fs = require("fs");
const path = require("path");

/** Popuni process.env iz site/.env.local ako vercel dev nije ubacio ključ u funkciju (čest slučaj). */
function hydrateEnvFromSiteRoot() {
  if (process.env.ANTHROPIC_API_KEY || process.env.OPENAI_API_KEY) return;
  const root = path.join(__dirname, "..");
  for (const fname of [".env.local", ".env"]) {
    const fp = path.join(root, fname);
    if (!fs.existsSync(fp)) continue;
    try {
      const text = fs.readFileSync(fp, "utf8");
      for (const line of text.split(/\r?\n/)) {
        const t = line.trim();
        if (!t || t.startsWith("#")) continue;
        const eq = t.indexOf("=");
        if (eq < 1) continue;
        const key = t.slice(0, eq).trim();
        let val = t.slice(eq + 1).trim();
        if (
          (val.startsWith('"') && val.endsWith('"')) ||
          (val.startsWith("'") && val.endsWith("'"))
        ) {
          val = val.slice(1, -1);
        }
        if (key && val && process.env[key] == null) process.env[key] = val;
      }
    } catch (_) {
      /* ignore */
    }
    if (process.env.ANTHROPIC_API_KEY || process.env.OPENAI_API_KEY) break;
  }
}

module.exports = async (req, res) => {
  hydrateEnvFromSiteRoot();

  res.setHeader("Content-Type", "application/json; charset=utf-8");

  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ error: "method", message: "Koristi POST." });
  }

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch {
      return res.status(400).json({ error: "json", message: "Neispravan JSON." });
    }
  }

  const answer = String(body?.answer ?? "").trim();
  const question = String(body?.question ?? "");
  const sectionTitle = String(body?.sectionTitle ?? "");
  const modelAnswer = String(body?.modelAnswer ?? "");
  const tipSr = String(body?.tipSr ?? "");

  if (answer.length > 2500) {
    return res.status(400).json({ error: "length", message: "Tekst je predugačak (max 2500 znakova)." });
  }

  if (!answer) {
    return res.status(200).json({
      empty: true,
      message_sr: "Napiši bar jednu ili dve rečenice na engleskom, pa ponovi „Proveru“.",
      grammar: { matches: [] },
      ai: null,
      aiMode: "off",
    });
  }

  let ltMatches = [];
  try {
    const params = new URLSearchParams();
    params.set("text", answer);
    params.set("language", "en-US");
    const ltRes = await fetch("https://api.languagetool.org/v2/check", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: params,
    });
    if (ltRes.ok) {
      const ltJson = await ltRes.json();
      ltMatches = (ltJson.matches || []).slice(0, 18).map((m) => ({
        message: m.message,
        shortMessage: m.shortMessage || "",
        offset: m.offset,
        length: m.length,
        snippet:
          answer.slice(Math.max(0, m.offset - 24), m.offset) +
          "[" +
          answer.slice(m.offset, m.offset + m.length) +
          "]" +
          answer.slice(m.offset + m.length, Math.min(answer.length, m.offset + m.length + 24)),
        replacements: (m.replacements || []).slice(0, 4).map((r) => r.value),
      }));
    }
  } catch {
    ltMatches = [];
  }

  const grammarHintsForAi = ltMatches
    .slice(0, 8)
    .map((m) => `${m.message} (around: "${answer.slice(m.offset, m.offset + m.length)}")`)
    .join(" | ");

  const payload = JSON.stringify(
    {
      sectionTitle,
      question,
      tipForStudent_sr: tipSr,
      referenceAnswer_en: modelAnswer,
      studentAnswer_en: answer,
      languageToolHints: grammarHintsForAi || "(none)",
    },
    null,
    0
  );

  const systemPrompt = `You are a supportive CEFR A2 English speaking examiner coach.
Rules:
- Be fair: short answers can still be "weak" not "empty" if they attempt the task.
- sectionTitle tells the expected grammar focus (e.g. Present Simple). Comment if tense does not match.
- The examiner question may have several parts — check all parts are addressed.
- Use LanguageTool hints when useful; do not contradict obvious spelling/grammar flags without reason.
- revised_en: write 2–5 natural A2 English sentences that improve the student's answer (fix grammar, keep their meaning when possible). Do NOT copy the reference answer verbatim.
- All *_sr fields: Serbian Latin script, clear classroom language, max ~2 sentences each.
Reply with ONLY a single raw JSON object (no markdown fences, no commentary) with exactly these keys:
grade_hint (string: one of ok, weak, empty),
fit_sr (string: does the answer match the question and all sub-parts?),
grammar_sr (string: tense vs section + 1–2 concrete fixes),
encourage_sr (string: one positive point about vocabulary, ideas, or structure),
revised_en (string: improved version as above),
exam_tip_sr (string: one practical tip for the oral exam, e.g. time markers, linking words).`;

  const userContent = `Evaluate this speaking attempt.\n${payload}`;

  function stripPossibleJsonFence(text) {
    let t = String(text).trim();
    if (t.startsWith("```")) {
      t = t.replace(/^```(?:json)?\s*/i, "");
      const end = t.lastIndexOf("```");
      if (end !== -1) t = t.slice(0, end).trim();
    }
    return t;
  }

  function applyParsed(parsed) {
    const fit_sr = String(parsed.fit_sr || "").trim();
    const grammar_sr = String(parsed.grammar_sr || "").trim();
    const encourage_sr = String(parsed.encourage_sr || "").trim();
    const revised_en = String(parsed.revised_en || "").trim();
    const exam_tip_sr = String(parsed.exam_tip_sr || "").trim();
    const legacySummary = String(parsed.summary_sr || "").trim();

    const ai = {
      grade_hint: String(parsed.grade_hint || "ok").toLowerCase(),
      fit_sr,
      grammar_sr,
      encourage_sr,
      revised_en,
      exam_tip_sr,
      summary_sr: legacySummary,
    };

    const hasStructured = fit_sr || grammar_sr || encourage_sr || revised_en || exam_tip_sr;
    if (!hasStructured && !legacySummary) {
      return { ai: { error: true, parse: true }, aiMode: "error" };
    }
    if (!hasStructured && legacySummary) {
      ai.summary_only = true;
    }
    return { ai, aiMode: "on" };
  }

  const anthropicKey = process.env.ANTHROPIC_API_KEY;
  const openaiKey = process.env.OPENAI_API_KEY;

  let ai = null;
  let aiMode = anthropicKey || openaiKey ? "pending" : "off";

  if (!anthropicKey && !openaiKey) {
    aiMode = "off";
  } else {
    try {
      let rawText = null;
      let httpStatus = 0;

      if (anthropicKey) {
        const anthropicModel =
          process.env.ANTHROPIC_MODEL || "claude-haiku-4-5-20251001";
        const ar = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: {
            "x-api-key": anthropicKey,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            model: anthropicModel,
            max_tokens: 1024,
            system: systemPrompt,
            messages: [{ role: "user", content: userContent }],
            temperature: 0.3,
          }),
        });
        httpStatus = ar.status;
        if (ar.ok) {
          const ad = await ar.json();
          const block = Array.isArray(ad.content) ? ad.content.find((c) => c.type === "text") : null;
          rawText = block?.text || null;
        }
      }

      if (rawText == null && openaiKey) {
        const openaiModel = process.env.OPENAI_MODEL || "gpt-4o-mini";
        const completion = await fetch("https://api.openai.com/v1/chat/completions", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${openaiKey}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            model: openaiModel,
            messages: [
              { role: "system", content: systemPrompt },
              { role: "user", content: userContent },
            ],
            response_format: { type: "json_object" },
            temperature: 0.3,
            max_tokens: 900,
          }),
        });
        httpStatus = completion.status;
        if (completion.ok) {
          const data = await completion.json();
          rawText = data.choices?.[0]?.message?.content || null;
        }
      }

      if (rawText == null) {
        aiMode = "error";
        ai = { error: true, httpStatus: httpStatus || undefined };
      } else {
        const cleaned = stripPossibleJsonFence(rawText);
        let parsed;
        try {
          parsed = JSON.parse(cleaned);
        } catch {
          aiMode = "error";
          ai = { error: true, parse: true };
          parsed = null;
        }
        if (parsed) {
          const out = applyParsed(parsed);
          ai = out.ai;
          aiMode = out.aiMode;
        }
      }
    } catch {
      aiMode = "error";
      ai = { error: true };
    }
  }

  return res.status(200).json({
    empty: false,
    grammar: { matches: ltMatches },
    ai,
    aiMode,
  });
};
