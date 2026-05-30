(function () {
  "use strict";

  /** @typedef {{ id: string, title: string }} Section */
  /** @typedef {{ n: number, sectionId: string, q: string, tip_sr: string, phrases_en: string[], model_en: string }} Item */

  /** @type {Section[]} */
  const SECTIONS = [
    { id: "present-simple", title: "Present Simple" },
    { id: "past-simple", title: "Past Simple" },
    { id: "present-continuous", title: "Present Continuous" },
    { id: "comparatives", title: "Comparatives / Superlatives" },
    { id: "advice", title: "Giving advice (should / shouldn’t)" },
    { id: "future", title: "Future plans" },
  ];

  /** @type {Item[]} */
  const ITEMS = [
    {
      n: 1,
      sectionId: "present-simple",
      q: "What’s your daily routine like? What do you like doing in your free time?",
      tip_sr:
        "Odgovori u sadašnjem prostom: ujutru, posle posla, vikendom. Poveži dve teme u 3–4 rečenice — rutina, pa slobodno vreme.",
      phrases_en: [
        "I usually get up at…",
        "After work I often…",
        "In my free time I enjoy… / I’m keen on…",
      ],
      model_en:
        "I usually get up at seven and have a quick breakfast before work. After work I often go for a walk. In my free time I enjoy reading and meeting friends.",
    },
    {
      n: 2,
      sectionId: "present-simple",
      q: "Do you like your job? Why? / Why not? What are your colleagues like?",
      tip_sr:
        "Prvo da/ne i kratak razlog, zatim opis kolega (ljubazni, pomažu, smešni). Koristi like / be + adjective.",
      phrases_en: [
        "Yes, I do, because… / No, not really. The main reason is…",
        "My colleagues are friendly and helpful.",
        "We get on well.",
      ],
      model_en:
        "Yes, I do, because the work is interesting and I learn new things. My colleagues are friendly and we get on well — they always help when I’m busy.",
    },
    {
      n: 3,
      sectionId: "present-simple",
      q: "Describe your home. Do you like living there and why? Would you like to move house and why?",
      tip_sr:
        "Opiši tip stana/kuće, sobe, kvart. Zatim zašto ti odgovara ili ne, i da li bi preselio — jedan jasan razlog.",
      phrases_en: [
        "I live in a flat / a house with…",
        "There are two bedrooms and a small balcony.",
        "I like it because it’s quiet / close to work.",
        "I’d like to move because I need more space.",
      ],
      model_en:
        "I live in a small flat on the third floor; it has a living room, a bedroom and a tiny kitchen. I like living there because it’s close to my office. One day I’d like to move to a bigger place with a garden.",
    },
    {
      n: 4,
      sectionId: "present-simple",
      q: "What is your favourite place/town/city in your country? Talk about the things that are and aren’t in this place (hotels, restaurants, parks, etc.).",
      tip_sr:
        "Imenuj mesto, reci šta IMA (there are / there is), šta NEMA (there isn’t / there aren’t) — kontrast je poenta zadatka.",
      phrases_en: [
        "My favourite city is…",
        "There are plenty of cafés and parks.",
        "There aren’t many big hotels.",
        "It’s famous for…",
      ],
      model_en:
        "My favourite town is Novi Sad. There are nice restaurants along the river and several parks. There aren’t many expensive hotels, but there are small guest houses. It isn’t very crowded.",
    },
    {
      n: 5,
      sectionId: "present-simple",
      q: "Do you have any hobbies? Do you prefer indoor or outdoor activities? Why?",
      tip_sr:
        "Navedi 1–2 hobija, izaberi indoor ili outdoor i objasni jednom rečenicom (weather, relax, meet people).",
      phrases_en: [
        "I’m interested in…",
        "I prefer outdoor activities because…",
        "When it rains, I stay at home and…",
      ],
      model_en:
        "I have a few hobbies — I swim and I like photography. I prefer outdoor activities because I enjoy fresh air and sunshine. When the weather is bad, I read at home.",
    },
    {
      n: 6,
      sectionId: "present-simple",
      q: "How do you usually get to work? Do you travel by public transport a lot? If not, do you know anybody who does?",
      tip_sr:
        "Kako stigneš na posao (by bus / on foot). Ako ne koristiš javni prevoz, spomeni nekoga ko koristi — treći lice u sadašnjem prostom.",
      phrases_en: [
        "I usually go to work by…",
        "I don’t use public transport very often.",
        "My friend takes the tram every day.",
      ],
      model_en:
        "I usually drive to work; it takes about twenty minutes. I don’t use public transport a lot because there’s no metro in my town. My colleague takes the bus every day — she says it’s cheaper.",
    },
    {
      n: 7,
      sectionId: "present-simple",
      q: "What’s your favourite way of travelling and why? Describe your best ride ever.",
      tip_sr:
        "Prvi deo: omiljeni način + razlog. Drugi deo: jedno konkretno putovanje (gde, sa kim, zašto je bilo sjajno).",
      phrases_en: [
        "I prefer travelling by train because…",
        "The best trip was when…",
        "I felt relaxed / excited.",
      ],
      model_en:
        "My favourite way of travelling is by train because I can read and look out of the window. My best ride ever was last summer to the coast with my family — the train was comfortable and we arrived right on time.",
    },
    {
      n: 8,
      sectionId: "present-simple",
      q: "How much time do you spend on the internet a day? Say the reasons why you go online.",
      tip_sr:
        "Procena vremena (about an hour) + 2–3 razloga: posao, društvene mreže, vesti, učenje.",
      phrases_en: [
        "I spend about… hours online every day.",
        "I mainly go online to…",
        "I also use the internet for…",
      ],
      model_en:
        "I spend about two hours on the internet every day. I go online to check my email and read the news. I also use it to study English and watch short videos.",
    },
    {
      n: 9,
      sectionId: "present-simple",
      q: "Where do you usually get your news? Is listening to the news important to you?",
      tip_sr:
        "Izvor (TV, app, radio, prijatelji) + važnost da/ne i jedna rečenica zašto.",
      phrases_en: [
        "I usually get my news from…",
        "Listening to the news is important to me because…",
        "I don’t follow the news very closely, but…",
      ],
      model_en:
        "I usually get my news from a news app on my phone and sometimes from TV in the evening. Yes, it’s important to me because I want to know what’s happening in my country and abroad.",
    },
    {
      n: 10,
      sectionId: "present-simple",
      q: "What TV programmes do you prefer watching? Do you download them or watch them on TV? How often do you watch TV and what time of the day?",
      tip_sr:
        "Tip emisija + gde gledaš + učestalost (twice a week) + doba dana (in the evening).",
      phrases_en: [
        "I prefer documentaries / series / sport.",
        "I usually stream them on my laptop.",
        "I watch TV three or four times a week, mostly after dinner.",
      ],
      model_en:
        "I prefer documentaries and crime series. I usually stream them on my laptop; I rarely watch live TV. I watch something about four evenings a week, after nine o’clock when I finish my chores.",
    },
    {
      n: 11,
      sectionId: "present-simple",
      q: "How do you feel about shopping? What shops do you usually go to? What do you most like/hate buying?",
      tip_sr:
        "Stav prema kupovini + konkretne prodavnice (supermarket, pijaca) + šta voliš / ne voliš da kupuješ.",
      phrases_en: [
        "I don’t mind shopping / I find shopping boring.",
        "I usually go to the local supermarket.",
        "I hate buying shoes because…",
      ],
      model_en:
        "I don’t mind shopping if I’m not in a hurry. I usually go to a supermarket near my home and sometimes to the market at weekends. I like buying food but I hate buying clothes because sizes are never right.",
    },
    {
      n: 12,
      sectionId: "past-simple",
      q: "Where were you last weekend? What did you do?",
      tip_sr:
        "Mesto + 2–3 aktivnosti u prošlom vremenu (went, visited, stayed, watched).",
      phrases_en: [
        "Last weekend I was at home / in…",
        "On Saturday I… and on Sunday…",
        "Nothing special — I just relaxed.",
      ],
      model_en:
        "Last weekend I was at my parents’ house in the countryside. On Saturday we went for a long walk and in the evening we watched a film. On Sunday I drove back home in the afternoon.",
    },
    {
      n: 13,
      sectionId: "past-simple",
      q: "What things could you do when you were younger and you can’t do anymore?",
      tip_sr:
        "Koristi when I was younger / I could… but now I can’t. Dva primera su dovoljna.",
      phrases_en: [
        "When I was a child, I could…",
        "These days I can’t because…",
        "I used to play football every day.",
      ],
      model_en:
        "When I was younger, I could stay awake all night and still feel fine the next day — I can’t do that anymore. I also used to run very fast, but now my knee hurts if I run too long.",
    },
    {
      n: 14,
      sectionId: "past-simple",
      q: "When did you last go on holiday? Who did you go with and where? Why did you visit that place? What did you do?",
      tip_sr:
        "Lanac: kada → sa kim → gde → zašto ta destinacija → šta ste radili (4–5 kratkih rečenica).",
      phrases_en: [
        "I last went on holiday in…",
        "I went with…",
        "We chose that place because…",
        "We spent our time swimming and sightseeing.",
      ],
      model_en:
        "I last went on holiday last August. I went to Greece with my partner. We chose an island because we wanted sea and quiet beaches. We swam every day, tried local food and visited one old town.",
    },
    {
      n: 15,
      sectionId: "past-simple",
      q: "Where did you last go sightseeing? How did you travel? What did you see? Did you go on a guided tour or on your own/with friends? What did you like most about it?",
      tip_sr:
        "Odgovori na SVA podpitanja redom — kratko je u redu ako je jasno.",
      phrases_en: [
        "The last place I went sightseeing was…",
        "We travelled by coach / train.",
        "We went on our own / We had a guided tour.",
        "What I liked most was…",
      ],
      model_en:
        "The last time I went sightseeing was in Belgrade last spring. I travelled by train with two friends. We saw the fortress and the main pedestrian street. We didn’t take a guided tour — we used a map. I liked the views from the fortress most.",
    },
    {
      n: 16,
      sectionId: "past-simple",
      q: "What’s the most important decision you made in your life/career?",
      tip_sr:
        "Jedna odluka + kada + zašto je bila važna + posledica (then I…).",
      phrases_en: [
        "The most important decision was…",
        "I made it when…",
        "After that, my life changed because…",
      ],
      model_en:
        "The most important decision in my career was to change my job two years ago. I made it because I wasn’t learning anything new. After that I felt more motivated and my salary improved.",
    },
    {
      n: 17,
      sectionId: "past-simple",
      q: "What did you do last week? (On Monday morning, on Tuesday evening, last night, yesterday afternoon, the day before yesterday, etc.)",
      tip_sr:
        "Pokaži vremenske izraze: uveži 3–4 tačke u prošlom (različiti vremenski markeri).",
      phrases_en: [
        "On Monday morning I…",
        "The day before yesterday I…",
        "Last night I stayed at home and…",
        "Yesterday afternoon I met…",
      ],
      model_en:
        "On Monday morning I had a long meeting at work. The day before yesterday I went to the gym after work. Yesterday afternoon I met a friend for coffee. Last night I stayed at home and watched a series.",
    },
    {
      n: 18,
      sectionId: "present-continuous",
      q: "What are you and your family doing today?",
      tip_sr:
        "Sadašnji kontinuirani za plan za danas / šta rade sada: we’re having, my brother is working, I’m studying…",
      phrases_en: [
        "Today we’re not doing anything special.",
        "My parents are visiting…",
        "I’m working from home this afternoon.",
      ],
      model_en:
        "Today my parents are shopping and fixing lunch. My sister is studying for an exam. I’m working until four, and this evening we’re having dinner together at home.",
    },
    {
      n: 19,
      sectionId: "present-continuous",
      q: "Imagine that you’re having an office party now. Describe how your colleagues look like. What are you doing at the moment? Who’s enjoying the party the most? Why?",
      tip_sr:
        "Zamisli sadašnjicu: izgled (is wearing, looks happy), šta radiš ti, ko je najodusevljeniji i zašto.",
      phrases_en: [
        "Right now everyone is chatting and laughing.",
        "Anna is wearing a red dress; she looks relaxed.",
        "I’m holding a drink and talking to my manager.",
        "The intern is enjoying it most because…",
      ],
      model_en:
        "Right now the music is playing and people are dancing. My colleague Mark is wearing a blue shirt and looks very happy. I’m standing near the buffet and talking to two friends from HR. I think the youngest colleague is enjoying it most — it’s her first party with us.",
    },
    {
      n: 20,
      sectionId: "present-continuous",
      q: "Talk about some things that you normally don’t do but you’re doing this week, or vice versa. Explain why.",
      tip_sr:
        "Kontrast usually + this week I’m… / or Normally I… but this week I’m not… Završi sa because…",
      phrases_en: [
        "I usually don’t cook, but this week I’m cooking every evening because…",
        "Normally I go to the gym, but this week I’m resting because I’m ill.",
      ],
      model_en:
        "I usually don’t walk to work, but this week I’m walking every day because my car is at the garage. Normally I watch TV late, but this week I’m going to bed early — I have an important exam.",
    },
    {
      n: 21,
      sectionId: "present-continuous",
      q: "Describe your perfect dinner with your family and/or friends as if it is happening now.",
      tip_sr:
        "Pričaj u „sada“: we’re sitting, we’re eating, someone is telling a story — atmosfera.",
      phrases_en: [
        "We’re sitting around a big table…",
        "The candles are shining and everyone is smiling.",
        "We’re eating my favourite dish…",
      ],
      model_en:
        "We’re sitting on the terrace and the sun is setting. Everyone is relaxed and laughing. We’re eating grilled fish and salad, and my friend is telling a funny story about his holiday. I’m feeling really happy to be with them.",
    },
    {
      n: 22,
      sectionId: "present-continuous",
      q: "Imagine that you’re late for a very important meeting and you can’t find a taxi. Describe what you’re doing and how you’re feeling at the moment.",
      tip_sr:
        "Emocije (I’m feeling stressed) + radnje (I’m looking at my phone, I’m walking fast).",
      phrases_en: [
        "I’m getting really nervous.",
        "I’m trying to call a taxi app but…",
        "My heart is beating fast.",
      ],
      model_en:
        "I’m standing on a busy corner and I’m checking my watch every minute. I’m trying to order a taxi on my phone but no one is accepting. I’m feeling stressed and angry with myself because I left too late.",
    },
    {
      n: 23,
      sectionId: "present-continuous",
      q: "Imagine that you’re watching your favourite film right now. What’s happening in the film?",
      tip_sr:
        "Opiši scenu u sadašnjem kontinuiranom: the hero is running, they’re arguing…",
      phrases_en: [
        "In this scene the main character is…",
        "The police are chasing…",
        "It’s raining in the street while…",
      ],
      model_en:
        "In my favourite film, this is the moment when the detective is following the suspect through the train station. People are rushing past and the music is getting louder. He’s hiding behind a column and talking quietly on the phone.",
    },
    {
      n: 24,
      sectionId: "comparatives",
      q: "Compare two people you know very well. Use “than” and as many adjectives as you can.",
      tip_sr:
        "Minimum dve poređanja sa than: taller than, more patient than, busier than…",
      phrases_en: [
        "X is older than Y, but Y is more outgoing.",
        "X works harder than Y.",
        "They’re both kind, but X is more practical than Y.",
      ],
      model_en:
        "My two cousins are very different. Ana is taller than Miloš and more serious than him. Miloš is funnier and more relaxed than Ana, but Ana is more organised than he is. They both care about family more than about money.",
    },
    {
      n: 25,
      sectionId: "comparatives",
      q: "Talk about your family. Who’s the oldest, prettiest…. etc. person in your family?",
      tip_sr:
        "Superlativi: the oldest, the youngest, the most helpful — uz ime i kratku rečenicu.",
      phrases_en: [
        "The oldest person in my family is…",
        "My aunt is the most creative person I know.",
        "In my opinion, my sister is the prettiest — but we joke about it!",
      ],
      model_en:
        "The oldest person in my family is my grandfather — he’s eighty-two. My mother is probably the hardest-working member. My little nephew is the cutest child in the family, everyone says that!",
    },
    {
      n: 26,
      sectionId: "comparatives",
      q: "Compare two places you know well.",
      tip_sr:
        "Dva mesta + than / more… than: gužva, cene, priroda, ljudi.",
      phrases_en: [
        "X is bigger than Y, but Y is greener.",
        "Life is more expensive in… than in…",
        "I prefer… because it’s quieter than…",
      ],
      model_en:
        "I know Novi Sad and Subotica well. Novi Sad is busier and more crowded than Subotica. Subotica is smaller but more relaxed than Novi Sad. The architecture in Subotica is more unusual than in most Serbian towns.",
    },
    {
      n: 27,
      sectionId: "comparatives",
      q: "Who do you think has the best life of all the people you know? Why? Use as many superlatives as possible to describe that person’s life.",
      tip_sr:
        "Izaberi jednu osobu i „naj…“: happiest, richest, most balanced — sa objašnjenjem.",
      phrases_en: [
        "I think my friend Mark has the best life.",
        "He has the most interesting job…",
        "He seems the happiest person in our group.",
      ],
      model_en:
        "I think my friend Ivana has the best life of all the people I know. She has the most interesting job — she travels a lot. She lives in the nicest flat I’ve seen, and she always looks the calmest and happiest in stressful situations.",
    },
    {
      n: 28,
      sectionId: "advice",
      q: "What advice would you give someone who wants to get fit?",
      tip_sr:
        "Moraš eksplicitno should i shouldn’t (bar po jednom). 3–4 saveta.",
      phrases_en: [
        "You should exercise regularly and drink more water.",
        "You shouldn’t skip meals or expect quick results.",
        "You should start slowly if you’re a beginner.",
      ],
      model_en:
        "You should start with short walks or easy workouts three times a week. You should also sleep enough and eat more vegetables. You shouldn’t sit all day or try extreme diets — they aren’t healthy.",
    },
    {
      n: 29,
      sectionId: "advice",
      q: "What advice would you give someone who wants to learn English well?",
      tip_sr:
        "should za dobre navike, shouldn’t za greške (samo gramatika, bez slušanja…).",
      phrases_en: [
        "You should practise a little every day.",
        "You should find a speaking partner.",
        "You shouldn’t be afraid of making mistakes.",
      ],
      model_en:
        "You should read and listen to English as often as you can, even for ten minutes. You should speak even when you feel shy. You shouldn’t rely only on translation apps — try to think in English sometimes.",
    },
    {
      n: 30,
      sectionId: "advice",
      q: "What advice would you give someone who doesn’t want to lose a job?",
      tip_sr:
        "Poslovni saveti: reliable, on time, communicate — should / shouldn’t.",
      phrases_en: [
        "You should always be on time.",
        "You should communicate clearly with your boss.",
        "You shouldn’t gossip or ignore feedback.",
      ],
      model_en:
        "You should be reliable and finish your tasks on time. You should ask questions if you don’t understand something. You shouldn’t argue rudely with colleagues or miss deadlines without warning.",
    },
    {
      n: 31,
      sectionId: "advice",
      q: "What advice would you give someone who can’t decide where to spend a peaceful and relaxing holiday?",
      tip_sr:
        "Predloži korake: think about budget, quiet place, shouldn’t overplan…",
      phrases_en: [
        "You should write a list of what you need — sea, mountains, silence.",
        "You shouldn’t choose a very busy city if you want peace.",
        "You should read reviews from other travellers.",
      ],
      model_en:
        "You should decide if you prefer the countryside or a small coastal town. You shouldn’t pick a huge tourist resort if you want peace and quiet. You should book a place with a garden or a view — that helps you relax.",
    },
    {
      n: 32,
      sectionId: "advice",
      q: "What advice would you give someone who is going to become a parent soon?",
      tip_sr:
        "Empatija + praktično: sleep, help, shouldn’t expect perfection.",
      phrases_en: [
        "You should rest while you can before the baby arrives.",
        "You should accept help from family.",
        "You shouldn’t compare yourself to perfect parents on social media.",
      ],
      model_en:
        "You should prepare the home and talk openly with your partner about duties. You should visit a doctor regularly and stay calm. You shouldn’t expect everything to be perfect — the first months are tiring for everyone.",
    },
    {
      n: 33,
      sectionId: "future",
      q: "Are you going to look for a better job? Why? / Why not?",
      tip_sr:
        "going to za plan. Kratak odgovor + razlog (money, learning, stability).",
      phrases_en: [
        "Yes, I’m going to start looking next year because…",
        "No, I’m not going to change jobs right now because…",
        "I’m going to wait until I finish this project.",
      ],
      model_en:
        "Yes, I’m probably going to look for a better job next year because I want a higher salary and more responsibility. I’m not going to rush — I’m going to update my CV first and then apply carefully.",
    },
    {
      n: 34,
      sectionId: "future",
      q: "Would you like to move/travel abroad? What are you going to do there?",
      tip_sr:
        "Would like to za želju, going to za konkretne planove na destinaciji.",
      phrases_en: [
        "I’d like to live in… for a few years.",
        "I’m going to study / work / improve my language skills.",
        "First I’m going to visit, then decide.",
      ],
      model_en:
        "I’d like to travel abroad more, especially to Germany or Austria. If I go next summer, I’m going to visit museums and practise my German every day. Maybe later I’m going to apply for a short work programme.",
    },
  ];

  const METHOD_HTML = `
    <p>
      Zamisao je da za svako pitanje prvo pročitaš <strong>gramatičku celinu</strong> u naslovu sekcije (da znaš koji oblik vremena očekuju),
      zatim u glavu ili naglas složiš <strong>2–4 kratke rečenice</strong> koristeći fraze iz okvira ispod.
    </p>
    <p>
      Pišeš svoj odgovor u polju (opciono), otvaraš <strong>„Saveti i primer“</strong> i upoređuješ — ponavljaš iste strukture dok ti ne postanu automatske;
      na ispitu ne učiš napamet ceo tekst, već <strong>šablone</strong> (rutina, razlog, kontrast, savet sa should/shouldn’t).
    </p>
    <p>

    </p>
  `;

  const escapeHtml = window.escapeHtml || function(s) {
    return String(s).replace(/[&<>'"]/g, (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch])
    );
  };

  function aiGradeBoxClass(hint) {
    const h = String(hint || "ok").toLowerCase();
    if (h === "weak") return "qs-ai-box--weak";
    if (h === "empty") return "qs-ai-box--warn";
    return "qs-ai-box--ok";
  }

  /** @param {Record<string, unknown>} ai */
  function formatAiFeedbackHtml(ai) {
    const hint = String(ai.grade_hint || "ok").toLowerCase();
    const badgeClass =
      hint === "weak" ? "qs-ai-badge--weak" : hint === "empty" ? "qs-ai-badge--empty" : "qs-ai-badge--ok";
    const head = `<div class="qs-ai-head"><strong>AI provera</strong> <span class="qs-ai-badge ${badgeClass}" title="procena za vežbu">${escapeHtml(hint)}</span></div>`;

    if (ai.summary_only && ai.summary_sr) {
      return `<div class="qs-ai-box ${aiGradeBoxClass(hint)}">${head}<p class="qs-ai-lead">${escapeHtml(String(ai.summary_sr))}</p></div>`;
    }

    const blocks = [];
    if (ai.fit_sr) {
      blocks.push(
        `<div class="qs-ai-part"><span class="qs-ai-label">Pitanje i kompletnost</span><p>${escapeHtml(String(ai.fit_sr))}</p></div>`
      );
    }
    if (ai.grammar_sr) {
      blocks.push(
        `<div class="qs-ai-part"><span class="qs-ai-label">Tenz i gramatika</span><p>${escapeHtml(String(ai.grammar_sr))}</p></div>`
      );
    }
    if (ai.encourage_sr) {
      blocks.push(
        `<div class="qs-ai-part"><span class="qs-ai-label">Šta je dobro</span><p>${escapeHtml(String(ai.encourage_sr))}</p></div>`
      );
    }
    if (ai.exam_tip_sr) {
      blocks.push(
        `<div class="qs-ai-part"><span class="qs-ai-label">Savet za usmeni</span><p>${escapeHtml(String(ai.exam_tip_sr))}</p></div>`
      );
    }
    if (ai.revised_en) {
      blocks.push(
        `<div class="qs-ai-part qs-ai-part--en"><span class="qs-ai-label">Predlog boljeg odgovora (EN, A2)</span><p>${escapeHtml(String(ai.revised_en))}</p></div>`
      );
    }

    if (!blocks.length && ai.summary_sr) {
      return `<div class="qs-ai-box ${aiGradeBoxClass(hint)}">${head}<p class="qs-ai-lead">${escapeHtml(String(ai.summary_sr))}</p></div>`;
    }
    if (!blocks.length) {
      return `<div class="qs-ai-box qs-ai-box--warn">${head}<p>Nema teksta od AI — probaj ponovo.</p></div>`;
    }

    return `<div class="qs-ai-box ${aiGradeBoxClass(hint)}">${head}<div class="qs-ai-struct">${blocks.join("")}</div></div>`;
  }

  function renderPhrases(phrases) {
    if (!phrases || !phrases.length) return "";
    return `<ul class="qs-phrases">${phrases.map((p) => `<li>${escapeHtml(p)}</li>`).join("")}</ul>`;
  }

  function renderItem(it) {
    return `
      <article class="qs-card" id="q-${it.n}" data-q="${it.n}">
        <h3><span class="qs-num">${it.n}.</span> ${escapeHtml(it.q)}</h3>
        <div class="qs-write">
          <label for="ta-${it.n}">Tvoj odgovor (piši ovde ili vežbaj naglas)</label>
          <textarea id="ta-${it.n}" rows="4" autocomplete="off" placeholder="Npr. 2–4 rečenice na engleskom…"></textarea>
          <div class="qs-check-row">
            <button type="button" class="qs-check-btn" data-quest-check="${it.n}">Proveri odgovor</button>
            <span class="qs-check-status" id="qs-status-${it.n}" aria-live="polite"></span>
          </div>
          <div class="qs-check-out" id="qs-out-${it.n}" hidden></div>
        </div>
        <details class="qs-details">
          <summary>Saveti i primer (klikni)</summary>
          <p class="qs-tip">${escapeHtml(it.tip_sr)}</p>
          ${renderPhrases(it.phrases_en)}
          <div class="qs-model"><strong>Primer odgovora (EN)</strong><br />${escapeHtml(it.model_en)}</div>
        </details>
      </article>
    `;
  }

  function renderSection(sec) {
    const items = ITEMS.filter((x) => x.sectionId === sec.id);
    const body = items.map(renderItem).join("");
    return `
      <section class="qs-section" id="${escapeHtml(sec.id)}" aria-labelledby="h-${sec.id}">
        <h2 id="h-${sec.id}">${escapeHtml(sec.title)}</h2>
        ${body}
      </section>
    `;
  }

  function renderToc() {
    const lis = SECTIONS.map(
      (s) => `<li><a href="#${escapeHtml(s.id)}">${escapeHtml(s.title)}</a></li>`
    ).join("");
    return `
      <nav class="qs-toc" aria-label="Sadržaj sekcija">
        <h2>Brzi skok</h2>
        <ul>${lis}</ul>
      </nav>
    `;
  }

  const mount = document.getElementById("quest-speek-root");
  if (!mount) return;

  mount.innerHTML = `
    <div class="qs-wrap">
      <header class="qs-top">
        <div>
          <h1>Speaking questions · A2 final</h1>
          <p class="qs-sub">SPEAKING QUESTIONS A2 – FINAL EXAMINATION</p>
        </div>

      </header>

      <section class="qs-method" aria-labelledby="method-h">
        <h2 id="method-h">Kako da vežbaš odgovor (2–3 rečenice po pitanju)</h2>
        ${METHOD_HTML}
      </section>

      <section class="qs-image-link">
        <p><a href="./quest-image.html" class="qs-image-btn">📷 Primeri gotovih odgovora</a></p>
        <p class="muted">Pogledaj primere odgovora na pitanja sa opisom slika — korisno za vežbanje vokabulara i gramatičkih struktura.</p>
      </section>

      ${renderToc()}

      ${SECTIONS.map(renderSection).join("")}
      <p class="qs-foot">Tekst pitanja je za vežbanje govora (A2). Primeri su skraćeni; na ispitu važi prirodan tok i ispravna gramatika, ne doslovno pamćenje. Provera radi na hostingu sa API rutom (npr. Vercel); lokalno samo <code>index.html</code> bez servera ne može da pozove <code>/api/quest-check</code>.</p>
    </div>
  `;

  const sectionTitleById = new Map(SECTIONS.map((s) => [s.id, s.title]));
  const itemByN = new Map(ITEMS.map((it) => [it.n, it]));

  mount.addEventListener("click", async (e) => {
    const btn = e.target.closest("button[data-quest-check]");
    if (!btn || !mount.contains(btn)) return;
    const n = Number(btn.getAttribute("data-quest-check"));
    const it = itemByN.get(n);
    if (!it) return;

    const ta = mount.querySelector(`#ta-${n}`);
    const out = mount.querySelector(`#qs-out-${n}`);
    const status = mount.querySelector(`#qs-status-${n}`);
    if (!ta || !out || !status) return;

    const text = ta.value.trim();
    if (!text) {
      out.hidden = false;
      out.className = "qs-check-out qs-check-out--warn";
      out.innerHTML = `<p>Napiši odgovor u polju iznad, pa klikni ponovo.</p>`;
      status.textContent = "";
      return;
    }

    btn.disabled = true;
    status.textContent = "Proveravam…";
    out.hidden = true;

    try {
      const r = await fetch("/api/quest-check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          answer: text,
          question: it.q,
          sectionTitle: sectionTitleById.get(it.sectionId) || it.sectionId,
          modelAnswer: it.model_en,
          tipSr: it.tip_sr,
        }),
      });

      let data = {};
      try {
        data = await r.json();
      } catch {
        data = {};
      }

      if (!r.ok) {
        const msg = data.message || `Server je vratio ${r.status}.`;
        throw new Error(msg);
      }

      if (data.empty) {
        out.hidden = false;
        out.className = "qs-check-out qs-check-out--warn";
        out.innerHTML = `<p>${escapeHtml(data.message_sr || "Napiši odgovor.")}</p>`;
        status.textContent = "";
        return;
      }

      const matches = data.grammar && data.grammar.matches ? data.grammar.matches : [];
      let gramHtml = "";
      if (!matches.length) {
        gramHtml =
          '<p class="qs-gram-summary qs-gram-summary--ok">LanguageTool: nema uočljivih grešaka (ili servis trenutno ne odgovara).</p>';
      } else {
        gramHtml = `<p class="qs-gram-lead">LanguageTool — ${matches.length} napomena:</p><ul class="qs-gram-list">`;
        for (const m of matches) {
          const reps = (m.replacements || []).filter(Boolean).join(", ");
          gramHtml += `<li><span class="qs-gram-msg">${escapeHtml(m.message)}</span>`;
          if (m.snippet) {
            gramHtml += `<code class="qs-gram-snip">${escapeHtml(m.snippet)}</code>`;
          }
          if (reps) {
            gramHtml += `<span class="qs-gram-rep">Predlog: ${escapeHtml(reps)}</span>`;
          }
          gramHtml += `</li>`;
        }
        gramHtml += `</ul>`;
      }

      let aiHtml = "";
      if (data.aiMode === "error" || (data.ai && data.ai.error)) {
        aiHtml = `<div class="qs-ai-box qs-ai-box--warn"><strong>AI trenutno ne radi</strong> (ključ, kvota, parsiranje ili mreža). Gramatika iznad i dalje važi.</div>`;
      } else if (data.aiMode === "off") {
        aiHtml = `<div class="qs-ai-box qs-ai-box--muted"><strong>AI savet isključen.</strong> Gore vidi automatsku gramatiku. Dodaj <code>ANTHROPIC_API_KEY</code> (Claude) ili <code>OPENAI_API_KEY</code> u Vercel <em>Environment Variables</em> / u <code>site/.env.local</code> za <code>vercel dev</code>, pa redeployuj ako je produkcija.</div>`;
      } else if (data.aiMode === "on" && data.ai && !data.ai.error) {
        aiHtml = formatAiFeedbackHtml(data.ai);
      }

      out.hidden = false;
      out.className = "qs-check-out";
      out.innerHTML = gramHtml + aiHtml;
      status.textContent = "Gotovo.";
    } catch (err) {
      out.hidden = false;
      out.className = "qs-check-out qs-check-out--warn";
      const fallback =
        "Ne mogu da pozovem /api/quest-check. Ako otvaraš HTML sa diska (file://) ili statički server bez API-ja, pokreni Vercel deploy ili <code>vercel dev</code> iz foldera <code>site</code>.";
      out.innerHTML = `<p>${escapeHtml(String(err && err.message ? err.message : fallback))}</p>`;
      status.textContent = "";
    } finally {
      btn.disabled = false;
    }
  });

  /* ---------- sidebar: speaking categories ---------- */
  const speakNav = document.getElementById("lesson-nav");
  const speakPane = speakNav ? speakNav.closest(".nav-pane") : null;
  const speakHead = speakPane ? speakPane.querySelector(".nav-head .label") : null;
  if (speakHead) speakHead.textContent = "Govor · kategorije";

  if (speakNav) {
    speakNav.innerHTML = "";

    function clearSpeakActives() {
      speakNav.querySelectorAll("button.active").forEach((b) => b.classList.remove("active"));
    }

    const details = document.createElement("details");
    details.open = true;
    const sum = document.createElement("summary");
    sum.textContent = "Govor";
    const chip = document.createElement("span");
    chip.className = "unit-chip";
    chip.textContent = "6 kategorija";
    sum.append(chip);
    details.append(sum);

    const ul = document.createElement("ul");
    ul.className = "qs-nav-list";

    const SHORT_LABELS = {
      "present-simple": "Pres",
      "past-simple": "Past",
      "present-continuous": "PCon",
      comparatives: "Comp",
      advice: "Adv",
      future: "Fut",
    };

    SECTIONS.forEach((sec) => {
      const li = document.createElement("li");
      const btn = document.createElement("button");
      btn.className = "qs-nav-btn";
      btn.textContent = sec.title;
      btn.setAttribute("data-section-id", sec.id);
      btn.setAttribute("data-short", SHORT_LABELS[sec.id] || sec.title);
      btn.addEventListener("click", () => {
        clearSpeakActives();
        btn.classList.add("active");
        const el = document.getElementById(sec.id);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      li.append(btn);
      ul.append(li);
    });

    details.append(ul);
    speakNav.append(details);

    /* nav link: Primeri gotovih odgovora */
    const imgLink = document.createElement("a");
    imgLink.href = "./quest-image.html";
    imgLink.className = "qs-nav-link";
    imgLink.textContent = "📷 Primeri gotovih odgovora";
    speakNav.append(imgLink);

    /* scroll spy — highlight active section */
    const sectionEls = SECTIONS.map((s) => document.getElementById(s.id)).filter(Boolean);
    const speakBtns = SECTIONS.map((s) => speakNav.querySelector(`button[data-section-id="${s.id}"]`)).filter(Boolean);

    function onScroll() {
      let activeId = null;
      const scrollY = window.scrollY + 100;
      for (let i = sectionEls.length - 1; i >= 0; i--) {
        if (sectionEls[i].offsetTop <= scrollY) {
          activeId = SECTIONS[i].id;
          break;
        }
      }
      speakBtns.forEach((b) => {
        b.classList.toggle("active", b.getAttribute("data-section-id") === activeId);
      });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
