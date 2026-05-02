"""
Po 10 pitanja za svaku Unit (12 jedinica = 120 pitanja).
Format pitanja:
    {
        "q": "Tekst pitanja na srpskom (ili engleskom).",
        "options": ["A", "B", "C", "D"],
        "answer": <int 0-3>,           # indeks tačnog odgovora
        "explain": "Kratko objašnjenje na srpskom."
    }
Pitanja pokrivaju vokabular, gramatiku i Real World fraze iz svake jedinice.
"""

from __future__ import annotations

UNIT_TESTS: dict[int, list[dict]] = {
    # =================================================================
    # UNIT 1 — countries/nationalities, jobs, numbers, plurals, this/that
    # =================================================================
    1: [
        {
            "q": "Šta je nacionalnost za nekoga iz Brazila?",
            "options": ["Brazilic", "Brazilian", "Brazilish", "Braziler"],
            "answer": 1,
            "explain": "Brazil → Brazilian (sufiks -ian).",
        },
        {
            "q": "Šta je nacionalnost za nekoga iz Italije?",
            "options": ["Italic", "Italish", "Italian", "Italiano"],
            "answer": 2,
            "explain": "Italy → Italian (sufiks -ian).",
        },
        {
            "q": "Koji član ide pre 'engineer'?",
            "options": ["a engineer", "the engineer", "an engineer", "no article"],
            "answer": 2,
            "explain": "an + samoglasnički zvuk: an engineer.",
        },
        {
            "q": "Koji član ide pre 'university'?",
            "options": ["an university", "a university", "the university only", "no article"],
            "answer": 1,
            "explain": "Iako počinje slovom u, izgovara se /juː/ (suglasnički zvuk) → a university.",
        },
        {
            "q": "Pravilna množina od 'child' je …",
            "options": ["childs", "childes", "childies", "children"],
            "answer": 3,
            "explain": "child → children (nepravilna množina).",
        },
        {
            "q": "Pravilna množina od 'person' je …",
            "options": ["persons", "people", "personies", "peoples"],
            "answer": 1,
            "explain": "person → people (nepravilna množina).",
        },
        {
            "q": "Popuni: 'What ___ your name?'",
            "options": ["are", "is", "am", "be"],
            "answer": 1,
            "explain": "name je 3. lice jednine → is. Skraćeno: What's your name?",
        },
        {
            "q": "Koji je prevod 'Where are you from?'",
            "options": ["Kuda ideš?", "Gde si?", "Odakle si?", "Kako se zoveš?"],
            "answer": 2,
            "explain": "Where are you from? = Odakle si?",
        },
        {
            "q": "Pristojno tražiš da ti neko ponovi broj telefona. Šta kažeš?",
            "options": [
                "Repeat now!",
                "Could you say that again, please?",
                "What you say?",
                "Tell me one more!",
            ],
            "answer": 1,
            "explain": "Could you say that again, please? je standardna pristojna fraza.",
        },
        {
            "q": "Pokazuješ na više stvari pored sebe. Koju reč koristiš?",
            "options": ["this", "that", "these", "those"],
            "answer": 2,
            "explain": "these = ovi/ove (množina, blizu); this = ovaj (jednina, blizu).",
        },
    ],
    # =================================================================
    # UNIT 2 — adjectives, have got, family, time, things in house, prepositions
    # =================================================================
    2: [
        {
            "q": "Suprotno od 'expensive' je …",
            "options": ["cheap", "small", "old", "easy"],
            "answer": 0,
            "explain": "cheap (jeftin) ↔ expensive (skup).",
        },
        {
            "q": "Suprotno od 'early' je …",
            "options": ["fast", "late", "slow", "old"],
            "answer": 1,
            "explain": "early (rano) ↔ late (kasno).",
        },
        {
            "q": "Popuni: 'I ___ a new car.'",
            "options": ["has got", "have got", "got have", "am got"],
            "answer": 1,
            "explain": "I/you/we/they + have got. He/she/it + has got.",
        },
        {
            "q": "Popuni: 'She ___ a sister.'",
            "options": ["have got", "haven't got", "has got", "is got"],
            "answer": 2,
            "explain": "3. lice jednine: She has got = She's got.",
        },
        {
            "q": "Brat tvoje majke je tvoj …",
            "options": ["cousin", "uncle", "nephew", "grandfather"],
            "answer": 1,
            "explain": "uncle = stric/ujak/tetak.",
        },
        {
            "q": "Majka tvoga oca je tvoja …",
            "options": ["aunt", "sister", "grandmother", "mother-in-law"],
            "answer": 2,
            "explain": "grandmother = baka.",
        },
        {
            "q": "Kako kažeš 7:30 na britanski način?",
            "options": [
                "seven thirty past",
                "half past seven",
                "thirty past seven",
                "half to seven",
            ],
            "answer": 1,
            "explain": "half past seven = pola osam (7:30).",
        },
        {
            "q": "Kako kažeš 8:45?",
            "options": [
                "eight forty-five / quarter to nine",
                "quarter past nine",
                "fifteen past eight",
                "three quarter eight",
            ],
            "answer": 0,
            "explain": "8:45 = quarter to nine ili eight forty-five.",
        },
        {
            "q": "Popuni: 'Whose phone is this?' — 'It's ___.'",
            "options": ["Tom", "Tom phone", "Tom's", "of Tom"],
            "answer": 2,
            "explain": "Posesivni 's: Tom's = Tomov.",
        },
        {
            "q": "Mačka je IZA stolice. Engleska prepozicija je …",
            "options": ["in front of", "under", "behind", "next to"],
            "answer": 2,
            "explain": "behind = iza. In front of = ispred.",
        },
    ],
    # =================================================================
    # UNIT 3 — daily routines, present simple, free time, dates, frequency adverbs
    # =================================================================
    3: [
        {
            "q": "Šta znači 'I have breakfast at 8'?",
            "options": [
                "Imam doručak u 8.",
                "Doručkujem u 8.",
                "Pravim doručak u 8.",
                "Dobijam doručak u 8.",
            ],
            "answer": 1,
            "explain": "have breakfast = doručkovati. Slično: have lunch/dinner.",
        },
        {
            "q": "Popuni Wh- pitanje: '___ time do you get up?'",
            "options": ["Where", "How", "What", "When"],
            "answer": 2,
            "explain": "What time = u koliko sati. Pravilo: What time + do + subjekat + glagol.",
        },
        {
            "q": "Popuni: 'I ___ go shopping on Sundays.'",
            "options": ["am not", "no", "don't", "isn't"],
            "answer": 2,
            "explain": "Negacija u Present Simple za I/you/we/they: don't + bazni glagol.",
        },
        {
            "q": "Pitanje: '___ you live near here?'",
            "options": ["Are", "Is", "Do", "Does"],
            "answer": 2,
            "explain": "Yes/No pitanje za you u Present Simple: Do you …?",
        },
        {
            "q": "Koji je sledeći mesec posle 'June'?",
            "options": ["May", "July", "August", "September"],
            "answer": 1,
            "explain": "Redosled: May, June, July, August.",
        },
        {
            "q": "Kako pišeš datum '5. mart' na engleskom (BrE)?",
            "options": [
                "the five of March",
                "March five",
                "the fifth of March",
                "March fifth one",
            ],
            "answer": 2,
            "explain": "the + redni broj + of + mesec: the fifth of March.",
        },
        {
            "q": "Frekvencija: 0% =",
            "options": ["always", "sometimes", "hardly ever", "never"],
            "answer": 3,
            "explain": "never = nikad (0%); always = uvek (100%).",
        },
        {
            "q": "Gde stoji 'always' u rečenici 'She ___ late'?",
            "options": [
                "always She is late",
                "She always is late",
                "She is always late",
                "She is late always",
            ],
            "answer": 2,
            "explain": "Posle glagola be: She is always late.",
        },
        {
            "q": "Object pronoun za 'they' je …",
            "options": ["theirs", "them", "their", "they"],
            "answer": 1,
            "explain": "they → them. Phone them. / I see them.",
        },
        {
            "q": "Popuni predloga: 'I work ___ Monday mornings.'",
            "options": ["in", "on", "at", "every"],
            "answer": 1,
            "explain": "on + dani u nedelji: on Monday, on Saturday evening.",
        },
    ],
    # =================================================================
    # UNIT 4 — Present Simple 3rd person, like+ing, food/drink, countable/uncountable
    # =================================================================
    4: [
        {
            "q": "Popuni: 'He ___ tennis every weekend.'",
            "options": ["play", "plays", "playes", "is play"],
            "answer": 1,
            "explain": "3. lice jednine: dodaje se -s. He plays.",
        },
        {
            "q": "Popuni: 'She ___ DVDs in the evening.'",
            "options": ["watch", "watchs", "watches", "is watch"],
            "answer": 2,
            "explain": "Glagoli na -ch dobijaju -es: watch → watches.",
        },
        {
            "q": "Popuni: 'My brother ___ like cooking.'",
            "options": ["doesn't", "don't", "isn't", "not"],
            "answer": 0,
            "explain": "Negacija za he/she/it: doesn't + bazni glagol (bez -s).",
        },
        {
            "q": "Pitanje: '___ she watch TV a lot?'",
            "options": ["Do", "Does", "Is", "Has"],
            "answer": 1,
            "explain": "Does + subjekat + bazni glagol. Yes, she does.",
        },
        {
            "q": "Posle 'love' ide …",
            "options": [
                "infinitiv (to + glagol)",
                "verb + ing",
                "Past Simple",
                "samo imenica",
            ],
            "answer": 1,
            "explain": "love/like/hate/enjoy + verb-ing: I love cooking.",
        },
        {
            "q": "Kako se kaže 'voće' na engleskom?",
            "options": ["food", "fruit", "vegetables", "rice"],
            "answer": 1,
            "explain": "fruit = voće (i singular i koristi se kao kolektivno).",
        },
        {
            "q": "Šta znači 'sparkling water'?",
            "options": [
                "topla voda",
                "filtrirana voda",
                "gazirana voda",
                "negazirana voda",
            ],
            "answer": 2,
            "explain": "sparkling water = gazirana voda; still water = negazirana.",
        },
        {
            "q": "Konobar pita: 'Would you like to order now?' — kako pristojno odgovaraš ako želiš?",
            "options": [
                "Yes, I want.",
                "Yes, please.",
                "Of course no!",
                "Maybe yes.",
            ],
            "answer": 1,
            "explain": "Yes, please. / No, thanks. — pristojni kratki odgovori.",
        },
        {
            "q": "Imenica 'milk' je …",
            "options": [
                "brojiva (countable)",
                "nebrojiva (uncountable)",
                "uvek u množini",
                "nepravilna",
            ],
            "answer": 1,
            "explain": "milk = nebrojivo. Kažemo 'some milk', 'a glass of milk'.",
        },
        {
            "q": "Popuni: 'I have ___ eggs for breakfast.'",
            "options": ["a", "an", "some", "much"],
            "answer": 2,
            "explain": "some + množina ili nebrojivo: some eggs, some bread.",
        },
    ],
    # =================================================================
    # UNIT 5 — Past Simple be, life events, regular/irregular verbs, very/too
    # =================================================================
    5: [
        {
            "q": "Popuni: 'I ___ at school yesterday.'",
            "options": ["were", "was", "am", "did"],
            "answer": 1,
            "explain": "I/he/she/it + was. You/we/they + were.",
        },
        {
            "q": "Popuni: 'They ___ very tired.'",
            "options": ["was", "were", "are", "am"],
            "answer": 1,
            "explain": "they → were (Past Simple od be).",
        },
        {
            "q": "Past Simple od 'go' je …",
            "options": ["goed", "gone", "went", "gos"],
            "answer": 2,
            "explain": "go → went (nepravilan glagol).",
        },
        {
            "q": "Past Simple od 'have' je …",
            "options": ["haved", "hadded", "had", "having"],
            "answer": 2,
            "explain": "have → had (nepravilan).",
        },
        {
            "q": "Past Simple od 'study' je …",
            "options": ["studyed", "studyd", "studied", "stude"],
            "answer": 2,
            "explain": "Glagol na -y posle suglasnika: y → ied (study → studied).",
        },
        {
            "q": "Šta znači 'get married'?",
            "options": ["razvesti se", "venčati se", "dobiti dete", "voleti se"],
            "answer": 1,
            "explain": "get married = venčati se. Suprotno: get divorced.",
        },
        {
            "q": "Popuni: 'It was ___ cold to go out.' (negativno značenje)",
            "options": ["very", "really", "quite", "too"],
            "answer": 3,
            "explain": "too + adj = previše, uvek negativno: too cold = previše hladno.",
        },
        {
            "q": "Razlika: 'It was very interesting' i 'It was really interesting'?",
            "options": [
                "very = manje od really",
                "really = manje od very",
                "skoro isto, oba pojačavaju (jako)",
                "samo really radi sa pridevima",
            ],
            "answer": 2,
            "explain": "very i really su skoro istoznačni; oba pojačavaju (jako/stvarno).",
        },
        {
            "q": "Reagovanje na priču: 'I went to Paris last week.' — najprirodnije:",
            "options": [
                "Sounds great!",
                "I don't believe you.",
                "Goodbye.",
                "Sorry.",
            ],
            "answer": 0,
            "explain": "Sounds great! / Really? / That's interesting. — pokazuju zainteresovanost.",
        },
        {
            "q": "Popuni: 'Where ___ you go on holiday?'",
            "options": ["are", "did", "was", "do"],
            "answer": 1,
            "explain": "Past Simple Wh- pitanje: Wh- + did + subjekat + bazni glagol.",
        },
    ],
    # =================================================================
    # UNIT 6 — internet, past simple negation/questions, can/could, news, articles
    # =================================================================
    6: [
        {
            "q": "Popuni: 'I ___ go to school yesterday.' (negacija)",
            "options": ["didn't", "don't", "wasn't", "haven't"],
            "answer": 0,
            "explain": "Past Simple negacija: didn't + bazni glagol (bez -ed).",
        },
        {
            "q": "Past Simple pitanje: '___ you find the file?'",
            "options": ["Do", "Does", "Did", "Was"],
            "answer": 2,
            "explain": "Did + subjekat + bazni glagol. Yes, I did. / No, I didn't.",
        },
        {
            "q": "Šta znači 'a search engine'?",
            "options": [
                "uređaj za pretragu",
                "internet pretraživač (npr. Google)",
                "motor za vožnju",
                "servis za poruke",
            ],
            "answer": 1,
            "explain": "search engine = pretraživač (Google, Bing, …).",
        },
        {
            "q": "Popuni: 'I ___ swim very well.' (sposobnost sad)",
            "options": ["could", "can", "couldn't", "have"],
            "answer": 1,
            "explain": "can + bazni glagol = sadašnja sposobnost.",
        },
        {
            "q": "Popuni: 'When I was 5, I ___ read.' (sposobnost u prošlosti)",
            "options": ["can", "could", "did", "had"],
            "answer": 1,
            "explain": "could = sposobnost u prošlosti.",
        },
        {
            "q": "Past Simple od 'buy' je …",
            "options": ["buyed", "bough", "bought", "buyt"],
            "answer": 2,
            "explain": "buy → bought (nepravilan).",
        },
        {
            "q": "Past Simple od 'lose' je …",
            "options": ["losed", "lost", "loose", "loosed"],
            "answer": 1,
            "explain": "lose → lost (nepravilan).",
        },
        {
            "q": "Popuni: 'I saw a film. ___ film was great.'",
            "options": ["A", "An", "The", "—"],
            "answer": 2,
            "explain": "Drugi pomen već poznatog → the film.",
        },
        {
            "q": "Koji je tačan izraz?",
            "options": [
                "I go to the school every day.",
                "I go to school every day.",
                "I go to a school every day.",
                "I go to schools every day.",
            ],
            "answer": 1,
            "explain": "Ustaljeni izraz bez člana: go to school, go to bed, have lunch.",
        },
        {
            "q": "Reaguj na vest: 'Twenty people are in hospital after a crash.'",
            "options": [
                "Goodbye.",
                "Yes, I do.",
                "That's terrible!",
                "I'd like that.",
            ],
            "answer": 2,
            "explain": "That's terrible! / How awful! — empatija na lošu vest.",
        },
    ],
    # =================================================================
    # UNIT 7 — places in town, there is/are, rooms/furniture, much/many, shops, clothes
    # =================================================================
    7: [
        {
            "q": "Popuni: '___ a park near my house.'",
            "options": ["There is", "There are", "It is", "Is there"],
            "answer": 0,
            "explain": "There is + jednina (a park).",
        },
        {
            "q": "Popuni: '___ any good restaurants here?'",
            "options": ["Is there", "Are there", "There are", "Have there"],
            "answer": 1,
            "explain": "Pitanje: Are there any + množina?",
        },
        {
            "q": "Popuni: 'How ___ chairs are there?'",
            "options": ["much", "many", "any", "lot"],
            "answer": 1,
            "explain": "many + brojivo (chairs). much + nebrojivo.",
        },
        {
            "q": "Popuni: 'How ___ milk do we need?'",
            "options": ["many", "much", "any", "some"],
            "answer": 1,
            "explain": "much + nebrojivo (milk).",
        },
        {
            "q": "Popuni: 'I haven't got ___ time.'",
            "options": ["some", "any", "a", "much of"],
            "answer": 1,
            "explain": "any u negaciji i pitanju.",
        },
        {
            "q": "Gde kupuješ aspirin?",
            "options": ["a butcher's", "a baker's", "a chemist's", "a bookshop"],
            "answer": 2,
            "explain": "chemist's = apoteka. baker's = pekara, butcher's = mesara.",
        },
        {
            "q": "Prodavac kaže: 'Can I help you?' — pristojan odgovor ako samo razgledaš:",
            "options": [
                "Yes, give me!",
                "No, go away.",
                "I'm just looking, thanks.",
                "Help me, please.",
            ],
            "answer": 2,
            "explain": "I'm just looking, thanks. — vrlo uobičajen odgovor u prodavnici.",
        },
        {
            "q": "Šta znači 'jeans'?",
            "options": ["majica", "farmerke", "cipele", "košulja"],
            "answer": 1,
            "explain": "jeans = farmerke (uvek u množini, kažemo a pair of jeans).",
        },
        {
            "q": "'A ___ of trousers' — popuni:",
            "options": ["pair", "couple", "set", "two"],
            "answer": 0,
            "explain": "a pair of + uvek-pluralne imenice (jeans, trousers, glasses, scissors).",
        },
        {
            "q": "Popuni: 'I ___ buy a new pair of trainers.'",
            "options": ["am wanting", "want to", "want", "wanting"],
            "answer": 1,
            "explain": "want + to + bazni glagol.",
        },
    ],
    # =================================================================
    # UNIT 8 — work, present continuous, transport, simple vs continuous, phone
    # =================================================================
    8: [
        {
            "q": "Popuni: 'I ___ a report at the moment.'",
            "options": ["write", "am writing", "writes", "wrote"],
            "answer": 1,
            "explain": "Present Continuous za radnju koja se dešava sada: be + verb-ing.",
        },
        {
            "q": "-ing oblik od 'sit' je …",
            "options": ["siting", "sittin", "sitting", "sited"],
            "answer": 2,
            "explain": "CVC dupliranje suglasnika: sit → sitting; run → running.",
        },
        {
            "q": "-ing oblik od 'write' je …",
            "options": ["writeing", "writting", "writing", "writen"],
            "answer": 2,
            "explain": "Glagoli na -e gube e: write → writing; make → making.",
        },
        {
            "q": "Razlikuj: 'I usually drive, but today I ___ the bus.'",
            "options": ["take", "takes", "am taking", "took"],
            "answer": 2,
            "explain": "today = ovaj specifičan dan → Present Continuous.",
        },
        {
            "q": "Glagol koji NE ide u Present Continuous obliku je …",
            "options": ["work", "play", "know", "study"],
            "answer": 2,
            "explain": "Stative verbs (know, like, want, need) ne idu u Continuous.",
        },
        {
            "q": "'go on foot' znači:",
            "options": ["ići vozom", "ići peške", "trčati", "putovati avionom"],
            "answer": 1,
            "explain": "go on foot = ići peške; go by car/bus/plane.",
        },
        {
            "q": "Popuni: 'Hello, ___ I speak to John, please?'",
            "options": ["Do", "Could", "Am", "Will"],
            "answer": 1,
            "explain": "Could I speak to … ? — pristojna telefonska fraza.",
        },
        {
            "q": "Sekretarica: 'He's not here.' — ti predlažeš:",
            "options": [
                "I want him now.",
                "Can I take a message?",
                "Goodbye!",
                "What's wrong?",
            ],
            "answer": 1,
            "explain": "Can I take a message? = Da li da prenesem poruku?",
        },
        {
            "q": "Pridev za 'careful' (prilog) je …",
            "options": ["carefully", "carefuller", "carefuly", "careful"],
            "answer": 0,
            "explain": "Pridev + ly → prilog: careful → carefully.",
        },
        {
            "q": "Nepravilan prilog za 'good' je …",
            "options": ["goodly", "goodly", "well", "best"],
            "answer": 2,
            "explain": "good (pridev) → well (prilog). She speaks English well.",
        },
    ],
    # =================================================================
    # UNIT 9 — holiday activities, infinitive of purpose, comparatives, animals
    # =================================================================
    9: [
        {
            "q": "Šta znači 'go sightseeing'?",
            "options": [
                "ići u kupovinu",
                "razgledati znamenitosti",
                "ići u bioskop",
                "ići na večeru",
            ],
            "answer": 1,
            "explain": "go sightseeing = razgledati turističke znamenitosti.",
        },
        {
            "q": "Popuni: 'I went there ___ relax.'",
            "options": ["for", "to", "because", "of"],
            "answer": 1,
            "explain": "Infinitive of purpose: to + bazni glagol (zbog čega).",
        },
        {
            "q": "Popuni: 'They went there ___ a holiday.'",
            "options": ["to", "for", "in", "—"],
            "answer": 1,
            "explain": "for + imenica (for a holiday). to + glagol (to relax).",
        },
        {
            "q": "Komparativ od 'big' je …",
            "options": ["biger", "bigger", "more big", "bigest"],
            "answer": 1,
            "explain": "CVC dupliranje: big → bigger.",
        },
        {
            "q": "Komparativ od 'happy' je …",
            "options": ["happyer", "more happy", "happier", "happyest"],
            "answer": 2,
            "explain": "y → ier: happy → happier.",
        },
        {
            "q": "Komparativ od 'expensive' je …",
            "options": ["expensiver", "more expensive", "expensivest", "the expensive"],
            "answer": 1,
            "explain": "Duži pridevi: more + adj.",
        },
        {
            "q": "Komparativ od 'good' je …",
            "options": ["gooder", "more good", "best", "better"],
            "answer": 3,
            "explain": "good → better; bad → worse (nepravilni).",
        },
        {
            "q": "Predloga: 'How about ___ to the beach?'",
            "options": ["go", "going", "to go", "went"],
            "answer": 1,
            "explain": "How about + verb-ing? — predlog za aktivnost.",
        },
        {
            "q": "Razlika: 'I like swimming.' i 'I'd like to swim.'",
            "options": [
                "Skoro isto.",
                "Prvo = uopšte volim, drugo = sad bih plivao/-la.",
                "Drugo nije pravilno engleski.",
                "Prvo = jednom u životu, drugo = svaki dan.",
            ],
            "answer": 1,
            "explain": "like + ing = uopšte. would like + to + glagol = sada/jednom.",
        },
        {
            "q": "Posle 'enjoy' ide …",
            "options": ["bazni glagol", "to + glagol", "verb + ing", "Past Simple"],
            "answer": 2,
            "explain": "enjoy + verb-ing: I enjoy travelling.",
        },
    ],
    # =================================================================
    # UNIT 10 — verb phrases, imperatives, should, appearance, character, health
    # =================================================================
    10: [
        {
            "q": "Imperativ za 'Ne pušiti!' na engleskom je:",
            "options": ["Not smoke.", "Don't smoke.", "Don't smoking.", "No smoke."],
            "answer": 1,
            "explain": "Imperativ negacije: Don't + bazni glagol.",
        },
        {
            "q": "Savet: 'You ___ rest more.'",
            "options": ["should", "shouldn't", "must don't", "are"],
            "answer": 0,
            "explain": "should + bazni glagol = blag savet.",
        },
        {
            "q": "Savet: 'He ___ smoke so much.'",
            "options": ["should", "shouldn't", "didn't", "isn't"],
            "answer": 1,
            "explain": "shouldn't + bazni glagol = ne bi trebalo.",
        },
        {
            "q": "Pitanje za karakter osobe je:",
            "options": [
                "What does he like?",
                "What's he like?",
                "What does he look like?",
                "How is he?",
            ],
            "answer": 1,
            "explain": "What's he like? = Kakav je (po karakteru).",
        },
        {
            "q": "Pitanje za fizički izgled je:",
            "options": [
                "What's he like?",
                "What does he look like?",
                "What does he like?",
                "Who is he?",
            ],
            "answer": 1,
            "explain": "What does he look like? = Kako izgleda.",
        },
        {
            "q": "'She's got long, dark hair.' — koji se glagol koristi za izgled?",
            "options": ["be", "have got", "look", "do"],
            "answer": 1,
            "explain": "have got za izgled (boje očiju, kosa, brada). be za visinu/karakter.",
        },
        {
            "q": "'A headache' znači:",
            "options": ["bol u stomaku", "glavobolja", "kašalj", "groznica"],
            "answer": 1,
            "explain": "headache = glavobolja. stomach ache = bol u stomaku.",
        },
        {
            "q": "Empatija na bolest: prijatelj kaže 'I've got a cold.' Ti kažeš:",
            "options": [
                "OK, bye!",
                "Yes, please.",
                "I hope you get better soon.",
                "Take it.",
            ],
            "answer": 2,
            "explain": "Get well soon! / I hope you get better soon. — empatija.",
        },
        {
            "q": "Pridev od 'sun' (vreme) je:",
            "options": ["suny", "sunly", "sunny", "sunful"],
            "answer": 2,
            "explain": "Imenica + y → pridev: sun → sunny; cloud → cloudy; wind → windy.",
        },
        {
            "q": "Popuni: 'It ___ outside today.' (pada kiša SADA)",
            "options": ["rains", "is raining", "rain", "rained"],
            "answer": 1,
            "explain": "Trenutno vreme: Present Continuous → it is raining.",
        },
    ],
    # =================================================================
    # UNIT 11 — going to, might, studying, directions, invitations
    # =================================================================
    11: [
        {
            "q": "Popuni: 'I ___ get fit this year.' (siguran plan)",
            "options": [
                "going to",
                "am going to",
                "will going",
                "is going to",
            ],
            "answer": 1,
            "explain": "be + going to + bazni glagol. I'm going to get fit.",
        },
        {
            "q": "Popuni: 'They ___ travel next summer.' (siguran plan)",
            "options": [
                "are going to",
                "is going to",
                "going to",
                "am going to",
            ],
            "answer": 0,
            "explain": "they → are. They are going to travel.",
        },
        {
            "q": "Razlika: 'I'm going to study.' vs 'I might study.'",
            "options": [
                "isto značenje",
                "going to = sigurno; might = možda",
                "might = sigurno; going to = možda",
                "samo prošlo vreme",
            ],
            "answer": 1,
            "explain": "going to = siguran plan. might = neizvesno (možda da, možda ne).",
        },
        {
            "q": "Popuni: 'I might ___ to Italy.'",
            "options": ["to go", "go", "going", "goes"],
            "answer": 1,
            "explain": "might + bazni glagol (bez to).",
        },
        {
            "q": "'Pass an exam' znači:",
            "options": ["pasti na ispitu", "preskočiti ispit", "položiti ispit", "ići na ispit"],
            "answer": 2,
            "explain": "pass an exam = položiti. fail an exam = pasti.",
        },
        {
            "q": "Pravac: 'Skreni levo' = …",
            "options": ["Turn right.", "Go straight on.", "Turn left.", "Cross the road."],
            "answer": 2,
            "explain": "left = levo, right = desno, straight on = pravo.",
        },
        {
            "q": "'It's opposite the bank.' znači:",
            "options": [
                "pored banke",
                "preko puta banke",
                "iza banke",
                "pre banke",
            ],
            "answer": 1,
            "explain": "opposite = preko puta. next to = pored. behind = iza.",
        },
        {
            "q": "Pristojan kraj prijateljskog mejla je:",
            "options": [
                "Yours faithfully",
                "Yours sincerely",
                "Lots of love",
                "End of email",
            ],
            "answer": 2,
            "explain": "Lots of love / Best wishes — neformalno. Yours faithfully — formalno.",
        },
        {
            "q": "Popuni: 'Can I stay ___ you when I arrive?'",
            "options": ["with", "by", "on", "to"],
            "answer": 0,
            "explain": "stay with someone = biti kod nekoga (gost).",
        },
        {
            "q": "Pitanje: '___ you going to study tonight?'",
            "options": ["Do", "Are", "Is", "Will"],
            "answer": 1,
            "explain": "be going to pitanje: Are/Is + subjekat + going to + glagol.",
        },
    ],
    # =================================================================
    # UNIT 12 — superlatives, big numbers, present perfect, airport
    # =================================================================
    12: [
        {
            "q": "Superlativ od 'big' je …",
            "options": ["bigger", "biger", "biggest", "the most big"],
            "answer": 2,
            "explain": "Kratak pridev + dupliranje + -est: big → the biggest.",
        },
        {
            "q": "Superlativ od 'expensive' je …",
            "options": [
                "expensiver",
                "the expensive",
                "the most expensive",
                "the expensivest",
            ],
            "answer": 2,
            "explain": "Duži pridevi: the most + adj.",
        },
        {
            "q": "Superlativ od 'good' je …",
            "options": ["the best", "the goodest", "the better", "the most good"],
            "answer": 0,
            "explain": "good → the best (nepravilno).",
        },
        {
            "q": "Kako kažeš 1.5 na engleskom?",
            "options": [
                "one comma five",
                "one point five",
                "one and a half five",
                "one decimal five",
            ],
            "answer": 1,
            "explain": "Decimalna tačka u engleskom = point. 1.5 = one point five.",
        },
        {
            "q": "Past participle od 'go' je …",
            "options": ["gone/been", "went", "going", "goed"],
            "answer": 0,
            "explain": "go → went (Past Simple) → gone/been (PP).",
        },
        {
            "q": "Past participle od 'see' je …",
            "options": ["sawed", "saw", "seen", "seeing"],
            "answer": 2,
            "explain": "see → saw → seen.",
        },
        {
            "q": "Popuni: 'I ___ to Italy three times.'",
            "options": ["went", "have been", "go", "am going"],
            "answer": 1,
            "explain": "Iskustvo do sada (bez vremena) → Present Perfect: I've been to Italy.",
        },
        {
            "q": "Popuni: 'She ___ never tried sushi.'",
            "options": ["have", "has", "is", "did"],
            "answer": 1,
            "explain": "she → has + past participle: She has never tried.",
        },
        {
            "q": "Pitanje: '___ you ever been to London?'",
            "options": ["Did", "Have", "Are", "Were"],
            "answer": 1,
            "explain": "Have/Has + subjekat + ever + past participle?",
        },
        {
            "q": "Pristojan pozdrav pre puta: 'Have a ___ trip!'",
            "options": ["safe", "long", "fast", "sure"],
            "answer": 0,
            "explain": "Have a safe trip! = Srećan put! (sa željom za bezbednost).",
        },
    ],
}
