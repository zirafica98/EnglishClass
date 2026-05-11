"""
10 varijanti testova u stilu „TEST 4 – PREPARATION“ (open-ended vežbanje).
Obuhvat lekcija: 7A, 7B, 7C, 7D, 8A, 8B, 8D, 9A, 9B, 9D, 10A, 10B.

Svaka varijanta ima iste sekcije (1–7) kao u primeru korisnika; rečenice i kolokacije
prate vokabular i gramatiku iz tih lekcija (there is/are, shops, clothes, work PC,
transport, adverbs, holiday activities, comparatives, like/enjoy/would like,
imperatives/should, appearance vs character).
"""

from __future__ import annotations

INSTR_1 = (
    "1. Put the verbs in brackets into the Present Simple or Present Continuous."
)
INSTR_2 = "2. Put the following sentences into the Past Simple tense."
INSTR_3 = (
    "3. Put the verbs in brackets into the correct verb form. "
    "Use the infinitive, the infinitive with ‘to’ or verb+ing."
)
INSTR_4 = (
    "4. Complete the sentences with comparatives or superlatives of the adjectives in brackets."
)
INSTR_5 = "5. Complete the sentences with the appropriate adverbs."
INSTR_6 = (
    "6. Complete the following expressions and collocations with appropriate words. "
    "Sometimes more than one answer is possible."
)
INSTR_7 = "7. Make questions with like, look like or like doing."


def _sec(n: int, instruction: str, items: list[str]) -> dict:
    return {"n": n, "instruction": instruction, "items": items}


def _ak(n: int, items: list[str]) -> dict:
    return {"n": n, "items": items}


# Varijanta 1 — blizu korisnikovog primera, drugačiji kontekst u 7.
PREP_1 = {
    "id": "prep-1",
    "variant": 1,
    "title_sr": "Priprema · 1",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) She ________ (have) English classes every Tuesday evening.",
            "b) They __________ (have) lunch with a customer right now.",
            "c) Ben usually ________ (work) in an office, but today he ___________ (work) from home.",
        ]),
        _sec(2, INSTR_2, [
            "a) Is Maria buying a new pair of trainers?",
            "b) We don’t travel by public transport very often.",
            "c) I need some aspirin from the chemist’s.",
            "d) He takes the bus to the supermarket every Saturday.",
        ]),
        _sec(3, INSTR_3, [
            "a) I stopped _________ (watch) TV late at night last year.",
            "b) Do you want _________ (try) on these jeans?",
            "c) I’d rather _________ (walk) to the station today.",
            "d) She enjoys _________ (go) on a guided tour in new cities.",
            "e) We’re planning _________ (visit) the museum this afternoon.",
            "f) Let’s _________ (meet) outside the department store.",
            "g) Could you _________ (carry) these bags for me, please?",
            "h) You shouldn’t _________ (eat) chocolate before dinner.",
            "i) They flew to Egypt _________ (see) the Pyramids.",
        ]),
        _sec(4, INSTR_4, [
            "a) What was _______________ (bad) day of your holiday?",
            "b) This hotel is ___________ (modern) than the one we stayed in last year.",
            "c) Who is __________ (good) singer in your family?",
            "d) What is ___________ (high) mountain in your country?",
            "e) Travelling by train is ______________ (relaxing) than driving in traffic jams.",
            "f) That was my _____________ (nice) experience in a clothes shop.",
        ]),
        _sec(5, INSTR_5, [
            "a) You should speak more _________ (slow) in the meeting.",
            "b) He didn’t feel _________ (good) after the long journey.",
            "c) Do you always get up _________ (early) at the weekend?",
            "d) She doesn’t get angry _________ (easy).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ notes during the conference",
            "b) go on a guided _________",
            "c) use _________ transport",
            "d) ________ foot",
            "e) ________ the housework",
            "f) have a ________ (when you are ill)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Paul likes going camping and skiing in winter.",
            "   b) My manager is very hard-working and reliable.",
            "   c) Anna is quite tall and she’s got long fair hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) has", "b) are having", "c) works; isn’t working / is not working"]),
        _ak(2, [
            "a) Did Maria buy a new pair of trainers?",
            "b) We didn’t travel by public transport very often.",
            "c) I needed some aspirin from the chemist’s.",
            "d) He took the bus to the supermarket every Saturday.",
        ]),
        _ak(3, [
            "a) watching", "b) to try", "c) walk", "d) going", "e) to visit",
            "f) meet", "g) carry", "h) eat", "i) to see",
        ]),
        _ak(4, [
            "a) the worst", "b) more modern", "c) the best", "d) the highest",
            "e) more relaxing", "f) nicest / the nicest",
        ]),
        _ak(5, ["a) slowly", "b) well", "c) early", "d) easily"]),
        _ak(6, ["a) take", "b) tour", "c) public", "d) on", "e) do", "f) headache / cold / cough (headache fits illness collocation best)"]),
        _ak(7, [
            "a) What does Paul like doing? / What does Paul like to do?",
            "b) What’s your manager like?",
            "c) What does Anna look like?",
        ]),
    ],
}

PREP_2 = {
    "id": "prep-2",
    "variant": 2,
    "title_sr": "Priprema · 2",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) The museum ________ (open) at 10 a.m. every day except Monday.",
            "b) Look! It __________ (snow) heavily in central London today.",
            "c) I usually ________ (cycle) to work, but this week I _________ (take) the bus.",
        ]),
        _sec(2, INSTR_2, [
            "a) Are they waiting for a taxi outside the theatre?",
            "b) She doesn’t want to buy a map of the city.",
            "c) We enjoy spending time in the countryside.",
            "d) He wears a suit in the office every day.",
        ]),
        _sec(3, INSTR_3, [
            "a) I stopped _________ (look) for a flat near the park.",
            "b) Do you need _________ (get) any stamps at the post office?",
            "c) I’d rather _________ (stay) with friends than in a hotel.",
            "d) Tom hates _________ (do) the housework on Sundays.",
            "e) Where are you planning _________ (go) on holiday?",
            "f) Don’t _________ (forget) your guide book.",
            "g) Could you _________ (sign) this letter, please?",
            "h) You shouldn’t _________ (drive) so fast in the snow.",
            "i) We went to the beach _________ (relax).",
        ]),
        _sec(4, INSTR_4, [
            "a) What is _______________ (interesting) place you have visited?",
            "b) The market is ___________ (busy) than the supermarket on Saturday mornings.",
            "c) Who is __________ (tall), you or your brother?",
            "d) What is ___________ (large) city in your country?",
            "e) Learning French is ______________ (difficult) than learning English for me.",
            "f) That was the _____________ (bad) traffic jam of the year.",
        ]),
        _sec(5, INSTR_5, [
            "a) She answered the phone very _________ (polite).",
            "b) I can’t ski very _________ (good).",
            "c) Does the train always arrive _________ (late)?",
            "d) He works _________ (hard) every day.",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a message (on the phone)",
            "b) travel by _________ transport",
            "c) go ________ a picnic",
            "d) ________ sightseeing",
            "e) ________ fit (exercise and health)",
            "f) get on / ________ the bus",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Chris loves going to museums and reading history books.",
            "   b) My colleagues are friendly and very kind.",
            "   c) James is quite good-looking and he’s got a beard.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) opens", "b) is snowing", "c) cycle; am taking / ’m taking"]),
        _ak(2, [
            "a) Were they waiting for a taxi outside the theatre?",
            "b) She didn’t want to buy a map of the city.",
            "c) We enjoyed spending time in the countryside.",
            "d) He wore a suit in the office every day.",
        ]),
        _ak(3, [
            "a) looking", "b) to get", "c) stay", "d) doing", "e) to go",
            "f) forget", "g) sign", "h) drive", "i) to relax",
        ]),
        _ak(4, [
            "a) the most interesting", "b) busier", "c) taller", "d) the largest",
            "e) more difficult", "f) worst",
        ]),
        _ak(5, ["a) politely", "b) well", "c) late", "d) hard"]),
        _ak(6, ["a) take / leave", "b) public", "c) on", "d) go", "e) get", "f) off"]),
        _ak(7, [
            "a) What does Chris like doing?",
            "b) What are your colleagues like?",
            "c) What does James look like?",
        ]),
    ],
}

PREP_3 = {
    "id": "prep-3",
    "variant": 3,
    "title_sr": "Priprema · 3",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) There ________ (be) a beautiful park near my house.",
            "b) There __________ (be) some problems with the traffic today.",
            "c) She normally ________ (wear) jeans, but today she _________ (wear) a dress.",
        ]),
        _sec(2, INSTR_2, [
            "a) Is there a chemist’s in this street?",
            "b) They don’t have any plants in the living room.",
            "c) She works in a bookshop on Saturdays.",
            "d) She takes children to school every morning.",
        ]),
        _sec(3, INSTR_3, [
            "a) I stopped _________ (smoke) five years ago.",
            "b) Do you need _________ (ask) her a question?",
            "c) I’d rather _________ (stay) home tonight.",
            "d) Tom enjoys _________ (play) chess.",
            "e) Where are you planning _________ (go)?",
            "f) Let’s _________ (have) dinner now.",
            "g) Could you _________ (hold) this for me, please?",
            "h) You shouldn’t _________ (take) lifts every day.",
            "i) We went to Egypt _________ (see) the pyramids.",
        ]),
        _sec(4, INSTR_4, [
            "a) What is _______________ (unusual) thing you did last year?",
            "b) Lisa is ___________ (pretty) than her sister.",
            "c) Who is a __________ (good) lawyer, Henry or his wife?",
            "d) What is ___________ (tall) building in the world?",
            "e) I think French is ______________ (difficult) than English.",
            "f) What was your _____________ (important) decision?",
        ]),
        _sec(5, INSTR_5, [
            "a) You should drive ____________ (careful).",
            "b) She didn’t feel __________ (good) yesterday.",
            "c) Do you always get up _________ (late)?",
            "d) I never get stressed __________ (easy).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ notes",
            "b) go on a guided _________",
            "c) use _________ transport",
            "d) ________ foot",
            "e) ________ housework",
            "f) have a ________",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Tina likes going to the gym and travelling.",
            "   b) My colleagues are hard-working and reliable.",
            "   c) Brendon is very good-looking and has got dark curly hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) is", "b) are", "c) wears; is wearing / ’s wearing"]),
        _ak(2, [
            "a) Was there a chemist’s in this street?",
            "b) They didn’t have any plants in the living room.",
            "c) She worked in a bookshop on Saturdays.",
            "d) She took children to school every morning.",
        ]),
        _ak(3, [
            "a) smoking", "b) to ask", "c) stay", "d) playing", "e) to go",
            "f) have", "g) hold", "h) take", "i) to see",
        ]),
        _ak(4, [
            "a) the most unusual", "b) prettier", "c) better", "d) the tallest",
            "e) more difficult", "f) most important / the most important",
        ]),
        _ak(5, ["a) carefully", "b) well", "c) late", "d) easily"]),
        _ak(6, ["a) take", "b) tour", "c) public", "d) on", "e) do", "f) headache / cold / cough"]),
        _ak(7, [
            "a) What does Tina like doing?",
            "b) What are your colleagues like?",
            "c) What does Brendon look like?",
        ]),
    ],
}

PREP_4 = {
    "id": "prep-4",
    "variant": 4,
    "title_sr": "Priprema · 4",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) He ________ (have) meetings every Monday at noon.",
            "b) We __________ (have) a meeting now.",
            "c) Tim ________ (work) very hard, but he ___________ (not work) today.",
        ]),
        _sec(2, INSTR_2, [
            "a) Is Jack watching a tennis match?",
            "b) They don’t spend their holidays abroad.",
            "c) I see my friends at the weekend.",
            "d) She takes children to school in the morning.",
        ]),
        _sec(3, INSTR_3, [
            "a) I’d love _________ (live) by the sea one day.",
            "b) Teenagers enjoy _________ (go) out with friends.",
            "c) Would you like _________ (move) house?",
            "d) I need _________ (find) a job in the city.",
            "e) She stopped _________ (look) for work in the country.",
            "f) Let’s _________ (rent) a car in Cairo.",
            "g) Could you _________ (tell) me how much this is?",
            "h) You shouldn’t _________ (sit) all day.",
            "i) We took the ferry _________ (save) money.",
        ]),
        _sec(4, INSTR_4, [
            "a) The countryside is ___________ (quiet) than the city centre.",
            "b) Who is __________ (funny) person in your class?",
            "c) This skirt is ___________ (long) than that one.",
            "d) Sharm El Sheikh was ___________ (hot) place we visited.",
            "e) The department store is ______________ (expensive) than the market.",
            "f) That was the _____________ (easy) question in the test.",
        ]),
        _sec(5, INSTR_5, [
            "a) He speaks English very _________ (fluent).",
            "b) They didn’t play _________ (good) in the match.",
            "c) Please drive more _________ (careful) in the rain.",
            "d) She finished the report very _________ (quick).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a shower instead of a bath",
            "b) go for a ________ (exercise)",
            "c) ________ the windows / the car",
            "d) ________ time and money",
            "e) a pair of ________ / trainers",
            "f) ________ a suit in the week (wear)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Laura likes going to the beach and windsurfing.",
            "   b) My boss is selfish but very funny.",
            "   c) Mark is middle-aged and he’s got short grey hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) has", "b) are having", "c) works; isn’t working / is not working"]),
        _ak(2, [
            "a) Did Jack watch a tennis match?",
            "b) They didn’t spend their holidays abroad.",
            "c) I saw my friends at the weekend.",
            "d) She took children to school in the morning.",
        ]),
        _ak(3, [
            "a) to live", "b) going", "c) to move", "d) to find", "e) looking",
            "f) rent", "g) tell", "h) sit", "i) to save",
        ]),
        _ak(4, [
            "a) quieter", "b) the funniest", "c) longer", "d) the hottest",
            "e) more expensive", "f) easiest",
        ]),
        _ak(5, ["a) fluently", "b) well", "c) carefully", "d) quickly"]),
        _ak(6, ["a) Have", "b) run", "c) Wash", "d) Save", "e) jeans", "f) wear"]),
        _ak(7, [
            "a) What does Laura like doing?",
            "b) What’s your boss like? / What is your boss like?",
            "c) What does Mark look like?",
        ]),
    ],
}

PREP_5 = {
    "id": "prep-5",
    "variant": 5,
    "title_sr": "Priprema · 5",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) The train ________ (leave) at 8.15 every morning.",
            "b) Look at the traffic! We __________ (miss) the meeting.",
            "c) Kate ________ (not usually wear) trainers at work, but today she _________ (wear) them.",
        ]),
        _sec(2, INSTR_2, [
            "a) Do you write reports every Monday?",
            "b) He doesn’t answer emails on Sunday.",
            "c) We go on holiday to the mountains every winter.",
            "d) She buys her vegetables at the market.",
        ]),
        _sec(3, INSTR_3, [
            "a) I enjoy _________ (read) in the garden.",
            "b) I want _________ (buy) a new jacket for the party.",
            "c) Would you like _________ (come) with us to the museum?",
            "d) You need _________ (rest) more.",
            "e) He stopped _________ (take) the bus and started cycling.",
            "f) Let’s _________ (use) public transport today.",
            "g) Could you _________ (help) me with the shopping?",
            "h) You shouldn’t _________ (eat) so much fast food.",
            "i) They went to the lake _________ (go) sailing.",
        ]),
        _sec(4, INSTR_4, [
            "a) A flat in the city centre is ___________ (cheap) than a house in the village.",
            "b) Who runs __________ (fast) in your team?",
            "c) The river is ___________ (wide) here than near the bridge.",
            "d) That was ___________ (good) meal we had on holiday.",
            "e) The forest is ______________ (dark) than the wood near our town.",
            "f) She made _____________ (stupid) mistake of her life.",
        ]),
        _sec(5, INSTR_5, [
            "a) He drives too _________ (fast) in town.",
            "b) Did you sleep _________ (good) last night?",
            "c) Please listen _________ (careful) to the instructions.",
            "d) I can’t hear you; please speak more _________ (loud).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ to a meeting / a conference",
            "b) ________ by bike / by plane",
            "c) ________ on holiday",
            "d) ________ a good time",
            "e) ________ the shopping / the bags",
            "f) ________ a temperature (illness)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Sophie likes going camping and walking in the countryside.",
            "   b) My neighbour is shy but very generous.",
            "   c) David is young and he’s got blue eyes and fair hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) leaves", "b) are missing / ’re missing", "c) doesn’t usually wear; is wearing / ’s wearing"]),
        _ak(2, [
            "a) Did you write reports every Monday?",
            "b) He didn’t answer emails on Sunday.",
            "c) We went on holiday to the mountains every winter.",
            "d) She bought her vegetables at the market.",
        ]),
        _ak(3, [
            "a) reading", "b) to buy", "c) to come", "d) to rest", "e) taking",
            "f) use", "g) help", "h) eat", "i) to go",
        ]),
        _ak(4, [
            "a) cheaper", "b) (the) fastest", "c) wider", "d) the best",
            "e) darker", "f) the stupidest / the most stupid",
        ]),
        _ak(5, ["a) fast", "b) well", "c) carefully", "d) loudly"]),
        _ak(6, ["a) Go", "b) Travel / Go", "c) Go", "d) Have", "e) Carry", "f) Have"]),
        _ak(7, [
            "a) What does Sophie like doing?",
            "b) What’s your neighbour like?",
            "c) What does David look like?",
        ]),
    ],
}

PREP_6 = {
    "id": "prep-6",
    "variant": 6,
    "title_sr": "Priprema · 6",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) How many bedrooms ________ (there be) in your new flat?",
            "b) How much furniture ________ (there be) in the living room at the moment?",
            "c) He ________ (study) French every evening, but tonight he _________ (watch) a film.",
        ]),
        _sec(2, INSTR_2, [
            "a) Are there any good restaurants near here?",
            "b) I don’t need any help in the shop, thanks.",
            "c) She works for a big company in London.",
            "d) They sign the contract on Monday mornings.",
        ]),
        _sec(3, INSTR_3, [
            "a) I hate _________ (get) up early on Mondays.",
            "b) I’d like _________ (book) a table for four, please.",
            "c) She enjoys _________ (listen) to music on the train.",
            "d) Do you want _________ (pay) by card?",
            "e) We stopped _________ (have) a picnic by the river.",
            "f) Don’t _________ (worry) about the traffic.",
            "g) Could you _________ (repeat) that, please?",
            "h) You shouldn’t _________ (wear) those shoes in the snow.",
            "i) They flew to Rome _________ (visit) friends.",
        ]),
        _sec(4, INSTR_4, [
            "a) The market square is ___________ (old) part of the town.",
            "b) This coat is ___________ (warm) than my jacket.",
            "c) Who is __________ (young) person in your family?",
            "d) Cairo is ___________ (crowded) than a small village.",
            "e) The hotel by the sea was ______________ (comfortable) than the one in the city.",
            "f) It was the _____________ (boring) guided tour I’ve ever been on.",
        ]),
        _sec(5, INSTR_5, [
            "a) She explained everything very _________ (clear).",
            "b) I don’t feel _________ (good) today; I’ve got a cold.",
            "c) He always arrives _________ (early) for meetings.",
            "d) They solved the problem _________ (easy).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a contract / a letter",
            "b) ________ messages / notes",
            "c) ________ on foot",
            "d) ________ diving / skiing",
            "e) ________ twice a week (frequency)",
            "f) ________ the bus one stop earlier (health tip)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Emma likes going to museums and taking photos.",
            "   b) My sister is lazy but very kind.",
            "   c) Tom is overweight and he’s got a moustache.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) are there", "b) is there", "c) studies; is watching / ’s watching"]),
        _ak(2, [
            "a) Were there any good restaurants near here?",
            "b) I didn’t need any help in the shop, thanks.",
            "c) She worked for a big company in London.",
            "d) They signed the contract on Monday mornings.",
        ]),
        _ak(3, [
            "a) getting", "b) to book", "c) listening", "d) to pay", "e) to have",
            "f) worry", "g) repeat", "h) wear", "i) to visit",
        ]),
        _ak(4, [
            "a) the oldest", "b) warmer", "c) the youngest", "d) more crowded",
            "e) more comfortable", "f) most boring / the most boring",
        ]),
        _ak(5, ["a) clearly", "b) well", "c) early", "d) easily"]),
        _ak(6, ["a) Sign", "b) Take", "c) Go", "d) Go", "e) Go / Exercise", "f) Get off"]),
        _ak(7, [
            "a) What does Emma like doing?",
            "b) What’s your sister like?",
            "c) What does Tom look like?",
        ]),
    ],
}

PREP_7 = {
    "id": "prep-7",
    "variant": 7,
    "title_sr": "Priprema · 7",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) Water ________ (boil) at 100°C.",
            "b) Listen! Someone ________ (play) the piano in the next room.",
            "c) I ________ (not know) the answer right now — I _________ (think).",
        ]),
        _sec(2, INSTR_2, [
            "a) Does she take the tube to work?",
            "b) We aren’t looking for a new flat this month.",
            "c) He likes wearing jeans at the weekend.",
            "d) They stay with friends when they visit Paris.",
        ]),
        _sec(3, INSTR_3, [
            "a) I’d rather _________ (have) a shower than a bath.",
            "b) She needs _________ (see) the dentist soon.",
            "c) We enjoy _________ (walk) in the park after work.",
            "d) Do you want _________ (try) on this pair of trousers?",
            "e) He stopped _________ (work) at 6 p.m. yesterday.",
            "f) Let’s _________ (meet) at the café near the station.",
            "g) Could you _________ (wait) a moment, please?",
            "h) You shouldn’t _________ (drink) coffee late at night.",
            "i) They travelled by coach _________ (save) money.",
        ]),
        _sec(4, INSTR_4, [
            "a) The Pyramids are ___________ (famous) monuments in Egypt.",
            "b) The sea was ___________ (calm) than the day before.",
            "c) Who is __________ (reliable) friend you have?",
            "d) This T-shirt is ___________ (small) than the one I bought last week.",
            "e) Winter in Moscow is ______________ (cold) than winter in London.",
            "f) It was my _____________ (happy) day of the trip.",
        ]),
        _sec(5, INSTR_5, [
            "a) He answered all my questions _________ (patient).",
            "b) She didn’t sing very _________ (good) at the concert.",
            "c) Please sit _________ (comfortable) and relax.",
            "d) I can’t hear the news; can you turn it up _________ (loud)?",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a boat trip",
            "b) ________ camping",
            "c) ________ sightseeing",
            "d) ________ with friends or family (accommodation)",
            "e) ________ a headache / a cold",
            "f) ________ well soon (when someone is ill)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Ryan likes going skiing and sailing in summer.",
            "   b) My teacher is strict but very fair.",
            "c) Helen is slim and she’s got long dark hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) boils", "b) is playing / ’s playing", "c) don’t know; ’m thinking / am thinking"]),
        _ak(2, [
            "a) Did she take the tube to work?",
            "b) We weren’t looking for a new flat this month.",
            "c) He liked wearing jeans at the weekend.",
            "d) They stayed with friends when they visited Paris.",
        ]),
        _ak(3, [
            "a) have", "b) to see", "c) walking", "d) to try", "e) working",
            "f) meet", "g) wait", "h) drink", "i) to save",
        ]),
        _ak(4, [
            "a) the most famous", "b) calmer", "c) the most reliable", "d) smaller",
            "e) colder", "f) happiest",
        ]),
        _ak(5, ["a) patiently", "b) well", "c) comfortably", "d) loudly"]),
        _ak(6, ["a) Go on / Take", "b) Go", "c) Go", "d) Stay", "e) Have", "f) Get"]),
        _ak(7, [
            "a) What does Ryan like doing?",
            "b) What’s your teacher like?",
            "c) What does Helen look like?",
        ]),
    ],
}

PREP_8 = {
    "id": "prep-8",
    "variant": 8,
    "title_sr": "Priprema · 8",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) The shop ________ (close) at 6 p.m. on weekdays.",
            "b) Shh! The baby ________ (sleep) — please be quiet.",
            "c) They usually ________ (travel) by plane, but this time they _________ (go) by train.",
        ]),
        _sec(2, INSTR_2, [
            "a) Is he signing the contract today?",
            "b) She doesn’t work for that company any more.",
            "c) I enjoy going to the beach in summer.",
            "d) We need some chocolate from the baker’s.",
        ]),
        _sec(3, INSTR_3, [
            "a) I’d love _________ (learn) to windsurf.",
            "b) She hates _________ (wait) in long queues.",
            "c) Would you like _________ (sit) by the window?",
            "d) You need _________ (show) your PIN, please.",
            "e) I stopped _________ (buy) cigarettes last year.",
            "f) Let’s _________ (take) the ferry to the island.",
            "g) Could you _________ (spell) your name, please?",
            "h) You shouldn’t _________ (forget) your passport.",
            "i) We went to the countryside _________ (relax).",
        ]),
        _sec(4, INSTR_4, [
            "a) The island was ___________ (peaceful) place we visited.",
            "b) The hotel in Sharm was ___________ (cheap) than the hotel in Cairo.",
            "c) Who is __________ (good) driver, you or your father?",
            "d) The hill is ___________ (high) than the small wood behind it.",
            "e) Snorkelling was ______________ (exciting) than lying on the beach.",
            "f) That was the _____________ (long) journey of my life.",
        ]),
        _sec(5, INSTR_5, [
            "a) Drive _________ (slow) near schools.",
            "b) I don’t feel _________ (good) — I’ve got toothache.",
            "c) He works _________ (hard) but he hardly ever rests.",
            "d) Please write your email address _________ (clear).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a customer / a company",
            "b) ________ the phone / an email",
            "c) ________ a traffic jam",
            "d) ________ snorkelling",
            "e) ________ some exercise / the housework",
            "f) ________ stressed (feel)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Nina likes going on boat trips and diving.",
            "   b) My doctor is patient and very professional.",
            "   c) Greg is tall and he’s got a beard and glasses.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) closes", "b) is sleeping / ’s sleeping", "c) travel; are going / ’re going"]),
        _ak(2, [
            "a) Was he signing the contract today?",
            "b) She didn’t work for that company any more.",
            "c) I enjoyed going to the beach in summer.",
            "d) We needed some chocolate from the baker’s.",
        ]),
        _ak(3, [
            "a) to learn", "b) waiting", "c) to sit", "d) to show", "e) buying",
            "f) take", "g) spell", "h) forget", "i) to relax",
        ]),
        _ak(4, [
            "a) the most peaceful", "b) cheaper", "c) a better / the better", "d) higher",
            "e) more exciting", "f) longest",
        ]),
        _ak(5, ["a) slowly", "b) well", "c) hard", "d) clearly"]),
        _ak(6, ["a) Write to / Phone", "b) Answer", "c) Have", "d) Go", "e) Do", "f) Get"]),
        _ak(7, [
            "a) What does Nina like doing?",
            "b) What’s your doctor like?",
            "c) What does Greg look like?",
        ]),
    ],
}

PREP_9 = {
    "id": "prep-9",
    "variant": 9,
    "title_sr": "Priprema · 9",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) There ________ (not be) any milk in the fridge now.",
            "b) There ________ (be) a new clothes shop in our street — it opened last week.",
            "c) I ________ (look) for my keys every morning, and right now I _________ (look) under the sofa.",
        ]),
        _sec(2, INSTR_2, [
            "a) Are you paying by card or in cash?",
            "b) He doesn’t wear shorts at work.",
            "c) She answers the phone very politely.",
            "d) We go camping in France every July.",
        ]),
        _sec(3, INSTR_3, [
            "a) I enjoy _________ (spend) time with my family.",
            "b) I’d like _________ (move) to the country one day.",
            "c) Do you need _________ (ask) anything else?",
            "d) She stopped _________ (smoke) last month.",
            "e) Let’s _________ (have) a picnic in the park.",
            "f) Could you _________ (hold) the door, please?",
            "g) You shouldn’t _________ (take) lifts if you want to get fit.",
            "h) They went to the museum _________ (learn) about history.",
            "i) Would you like _________ (come) with us?",
        ]),
        _sec(4, INSTR_4, [
            "a) The coral reef was ___________ (colourful) thing we saw.",
            "b) The camel was ___________ (slow) than our car.",
            "c) Who is __________ (pretty), Lisa or her cousin?",
            "d) The mosque was ___________ (impressive) building in the photo.",
            "e) The desert was ______________ (hot) than we expected.",
            "f) It was the _____________ (bad) hotel on the website.",
        ]),
        _sec(5, INSTR_5, [
            "a) He speaks three languages _________ (fluent).",
            "b) Did you play _________ (good) in the match yesterday?",
            "c) She always dresses _________ (elegant) for work.",
            "d) I can’t solve this puzzle _________ (easy).",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a map / a newspaper",
            "b) ________ a pair of jeans",
            "c) ________ the shopping home",
            "d) ________ a conference",
            "e) ________ a sore throat",
            "f) ________ more (health advice with should)",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Oliver likes going to the zoo and taking photos of animals.",
            "   b) My cousin is funny and a bit lazy.",
            "   c) Julia is attractive and she’s got curly blonde hair.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) isn’t / is not", "b) is", "c) look; am looking / ’m looking"]),
        _ak(2, [
            "a) Were you paying by card or in cash?",
            "b) He didn’t wear shorts at work.",
            "c) She answered the phone very politely.",
            "d) We went camping in France every July.",
        ]),
        _ak(3, [
            "a) spending", "b) to move", "c) to ask", "d) smoking", "e) have",
            "f) hold", "g) take", "h) to learn", "i) to come",
        ]),
        _ak(4, [
            "a) the most colourful", "b) slower", "c) prettier", "d) the most impressive",
            "e) hotter", "f) worst",
        ]),
        _ak(5, ["a) fluently", "b) well", "c) elegantly", "d) easily"]),
        _ak(6, ["a) Buy / Get", "b) buy / get", "c) Carry", "d) Go to / Attend", "e) Have", "f) Walk"]),
        _ak(7, [
            "a) What does Oliver like doing?",
            "b) What’s your cousin like?",
            "c) What does Julia look like?",
        ]),
    ],
}

PREP_10 = {
    "id": "prep-10",
    "variant": 10,
    "title_sr": "Priprema · 10",
    "scope_sr": "7A–7D, 8A, 8B, 8D, 9A–9D, 10A–10B",
    "sections": [
        _sec(1, INSTR_1, [
            "a) The Browns ________ (live) in that house for twelve years. (They still live there.)",
            "b) At the moment they ________ (paint) the kitchen.",
            "c) She ________ (not usually take) the tram, but today she _________ (take) it because of the snow.",
        ]),
        _sec(2, INSTR_2, [
            "a) Is there a bank opposite the cinema?",
            "b) We don’t have any aspirin at home.",
            "c) He recommends Ray as an excellent driver.",
            "d) They go on a guided tour of the city every Monday.",
        ]),
        _sec(3, INSTR_3, [
            "a) I need _________ (find) a cheaper hotel.",
            "b) She enjoys _________ (travel) around the country.",
            "c) I’d rather _________ (go) by bike than by car.",
            "d) Would you like _________ (order) now?",
            "e) He stopped _________ (drink) coffee in the evening.",
            "f) Let’s _________ (walk) up and down the stairs.",
            "g) Could you _________ (pass) the salt, please?",
            "h) You shouldn’t _________ (sit) in front of the computer all day.",
            "i) We went to Rome _________ (see) the sights.",
        ]),
        _sec(4, INSTR_4, [
            "a) What is _______________ (dangerous) sport you have tried?",
            "b) The living room is ___________ (big) than the bedroom.",
            "c) Who is __________ (kind) person you know?",
            "d) The queue at the post office was ___________ (long) than at the bank.",
            "e) Snakes are ______________ (frightening) than rabbits for many people.",
            "f) That was the _____________ (interesting) museum in the city.",
        ]),
        _sec(5, INSTR_5, [
            "a) Please read the instructions _________ (careful).",
            "b) I didn’t sleep _________ (good) because of the noise.",
            "c) He always drives _________ (careful) in the rain.",
            "d) She finished the letter _________ (quick) and posted it.",
        ]),
        _sec(6, INSTR_6, [
            "a) ________ a double bed / a single bed (furniture)",
            "b) ________ a ticket at the kiosk",
            "c) ________ by ferry / by coach",
            "d) ________ a good time on holiday",
            "e) ________ a shower instead of a bath",
            "f) What’s the matter? — I’ve got a ________",
        ]),
        _sec(7, INSTR_7, [
            "1. a) Victoria likes going to concerts and dancing.",
            "   b) My uncle is generous and very reliable.",
            "   c) Peter is short and he’s got dark curly hair and a cap.",
        ]),
    ],
    "answer_key": [
        _ak(1, ["a) live", "b) are painting / ’re painting", "c) doesn’t usually take; is taking / ’s taking"]),
        _ak(2, [
            "a) Was there a bank opposite the cinema?",
            "b) We didn’t have any aspirin at home.",
            "c) He recommended Ray as an excellent driver.",
            "d) They went on a guided tour of the city every Monday.",
        ]),
        _ak(3, [
            "a) to find", "b) travelling", "c) go", "d) to order", "e) drinking",
            "f) walk", "g) pass",             "h) sit", "i) to see",
        ]),
        _ak(4, [
            "a) the most dangerous", "b) bigger", "c) the kindest", "d) longer",
            "e) more frightening", "f) most interesting / the most interesting",
        ]),
        _ak(5, ["a) carefully", "b) well", "c) carefully", "d) quickly"]),
        _ak(6, ["a) a / Buy", "b) Buy / Get", "c) Travel / Go", "d) Have", "e) Have", "f) headache / cold / cough"]),
        _ak(7, [
            "a) What does Victoria like doing?",
            "b) What’s your uncle like?",
            "c) What does Peter look like?",
        ]),
    ],
}

PREP_PRACTICE_TESTS: list[dict] = [
    PREP_1,
    PREP_2,
    PREP_3,
    PREP_4,
    PREP_5,
    PREP_6,
    PREP_7,
    PREP_8,
    PREP_9,
    PREP_10,
]
