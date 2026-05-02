#!/usr/bin/env python3
"""
Generiše lessons.json za face2face Elementary 2nd ed.
Lekcije 1A–12C (bez Welcome, bez xD).
Extra Practice je po jedinicama (jedna dvostrana/obnovna celina na kraju knjige) — vezano za sve lekcije te jedinice.
"""

from __future__ import annotations

import json
from pathlib import Path

OUT_JSON = Path(__file__).resolve().parent.parent / "data" / "lessons.json"
OUT_EMBED = Path(__file__).resolve().parent.parent / "data" / "lessons.embed.js"

# štampane ref. iz Contents (student’s book)
EXTRA_PRACTICE_META = [
    {
        "n": 1,
        "sb_page_printed": "p115",
        "language_summary_page": "128",
        "portfolio_en": "At the hotel",
        "portfolio_wb_printed": "p64",
        "pronunciation_ref": "Word stress i slogovi (HB str. štampane ~15)",
        "summary_sr": (
            "Obnova jedinice 1: kombinacija vokabulera (zemlje, poslovi, brojevi, predmeti) "
            "i glagola be u sve tri varijante (+ Wh- i yes/no). U knjizi obično sledi blok "
            "'Help with Pronunciation' oko udara reči na slogove."
        ),
        "priorities_sr": [
            "Ponovi kratke odgovore sa be u paru.",
            "Vezba izgovor stress-a na nationality i job words.",
            "Portfolio: popunjavanje hotel registarskog obrasca na engleskom (Workbook kao produžena praksa).",
        ],
    },
    {
        "n": 2,
        "sb_page_printed": "p116",
        "language_summary_page": "130",
        "portfolio_en": "My favourite thing",
        "portfolio_wb_printed": "p66",
        "pronunciation_ref": "Schwa /ə/ (HB ~23)",
        "summary_sr": (
            "Ponavljanje: pridevi redosled i very + have got; porodica i genitiv; vreme/cene/prepositions of place."
        ),
        "priorities_sr": [
            "Razjasni have got naspram simply have gde zbunjuje.",
            "Whose …? + possessed item — tipični završni blok jedinice 2.",
            "Portfolio opis omiljenog predmeta uz veliko/pravopis pravila koja knjiga radi u paraleli.",
        ],
    },
    {
        "n": 3,
        "sb_page_printed": "p117",
        "language_summary_page": "132",
        "portfolio_en": "All about me",
        "portfolio_wb_printed": "p68",
        "pronunciation_ref": "Kako izgovaramo ‘th’ (HB ~31)",
        "summary_sr": (
            "Present Simple rutine vs slobodno vreme + datumi; prilozi učestalosti; subject/object zamene."
        ),
        "priorities_sr": [
            "don't vs doesn't u brzini govora.",
            "Object pronouns u zavisnim rečenica-pitanjima (ko koga poziva?).",
            "Portfolio: kraći learner profil sa veznicima iz knjige (and/but/because ako predavač traži pun obim).",
        ],
    },
    {
        "n": 4,
        "sb_page_printed": "p118",
        "language_summary_page": "134",
        "portfolio_en": "Going out",
        "portfolio_wb_printed": "p70",
        "pronunciation_ref": "/ʃ/, /tʃ/, /dʒ/ (HB ~39)",
        "summary_sr": (
            "He/she/it u Present Simple, like + -ing tema, pristojne ponude/zamolbe u kafićima, countable/uncountable."
        ),
        "priorities_sr": [
            "Does + infinitiva bez nastavka na glagol.",
            "some/any u ponudi i zamolbi (restoran konteksti).",
            "Portfolio tekst situacije 'going out'.",
        ],
    },
    {
        "n": 5,
        "sb_page_printed": "p119",
        "language_summary_page": "136",
        "portfolio_en": "A night to remember",
        "portfolio_wb_printed": "p72",
        "pronunciation_ref": "Slovo o (HB ~47)",
        "summary_sr": (
            "Past Simple uz was/were, zatim pravilni/ne pravilni glagoli; jezici interesovanja u razgovoru; intenzifikatori uz prideve."
        ),
        "priorities_sr": [
            "Pravilna upotreba time expressions (ago, last week).",
            "Backchannel fraze kao deo komunikacije (knjiga ih radi kroz situacije sa vikendom).",
            "Portfolio: kratko pisanje o jednoj noći ili događaju koji pamtiš (prilagodi jeziku iz Workbook-a).",
        ],
    },
    {
        "n": 6,
        "sb_page_printed": "p120",
        "language_summary_page": "138",
        "portfolio_en": "Text me!",
        "portfolio_wb_printed": "p74",
        "pronunciation_ref": "Past Simple pravilnih glagola na izgovoru (HB ~55)",
        "summary_sr": (
            "Past Simple yes/no negacije did; can/can't, could/couldn't; jezici vesti i članovi a/an/the."
        ),
        "priorities_sr": [
            "didn't umesto wasn't kad glavni glagol nije be.",
            "Modal can/could uz tehnološku temu kao u lekciji 6.",
            "Portfolio pisana poruka/email kratkog formata ako je tako u Workbook nastavku.",
        ],
    },
    {
        "n": 7,
        "sb_page_printed": "p121",
        "language_summary_page": "140",
        "portfolio_en": "Renting a flat",
        "portfolio_wb_printed": "p76",
        "pronunciation_ref": "/ɔː/ i /ɜː/ (HB ~63)",
        "summary_sr": (
            "There is / there are, How much/many sa some/any/a, jezik prodavnice kao Real World blok."
        ),
        "priorities_sr": [
            "Is there / Are there inverzije i kratko odgovori.",
            "Kvantifikatori kod kupovine — tipični završni test jedinice 7.",
            "Portfolio tekst najma stana uz reklamski oglas.",
        ],
    },
    {
        "n": 8,
        "sb_page_printed": "p122",
        "language_summary_page": "142",
        "portfolio_en": "Finding a job",
        "portfolio_wb_printed": "p78",
        "pronunciation_ref": "/ɪ/ i /iː/ (HB ~71)",
        "summary_sr": (
            "Present Continuous vs Present Simple; jezici poruka telefonom; pridevi/prilozi u opisu aktivnosti."
        ),
        "priorities_sr": [
            "Kad koristiš 'now/today/sometimes' kao signal za tense.",
            "Telefonske fraze kraće i funkcionalno — potrebno automatizovanje.",
            "Portfolio: dokumenti tipa biznis kartica ili kratko motivaciono ako Workbook tako vodi.",
        ],
    },
    {
        "n": 9,
        "sb_page_printed": "p123",
        "language_summary_page": "144",
        "portfolio_en": "Places to go",
        "portfolio_wb_printed": "p80",
        "pronunciation_ref": "Silent letters — neme slova u rečima (HB ~79)",
        "summary_sr": (
            "Infinitive of purpose, comparatives, odluka šta radiš na izletu + like/would like uz patterne koji knjiga uči."
        ),
        "priorities_sr": [
            "Komparacije krace/duzeg oblika kao u tabelama Language Summary.",
            "Plan jednog izlet-dana — vežbanje funkcionalnog govora uz video blok knjige.",
            "Portfolio pisanje o mestima za jednodnevni izlet.",
        ],
    },
    {
        "n": 10,
        "sb_page_printed": "p124",
        "language_summary_page": "146",
        "portfolio_en": "The advice page",
        "portfolio_wb_printed": "p82",
        "pronunciation_ref": "Slovo a kao znak (HB ~87)",
        "summary_sr": (
            "Imperativi saveta; should/shouldn't; kao/izgleda i karakter lika u pitanju; zdravlje i vreme."
        ),
        "priorities_sr": [
            "Šta razlikuje pitanje What … like? od Like + -ing gde zbunjuje početnika.",
            "Should za blagi savet lekaru ili drugu osobi.",
            "Portfolio kao stranica saveta ili kratkog članka kao u workbook temi.",
        ],
    },
    {
        "n": 11,
        "sb_page_printed": "p125",
        "language_summary_page": "148",
        "portfolio_en": "A town by the sea",
        "portfolio_wb_printed": "p84",
        "pronunciation_ref": "/ʊ/ i /uː/ (HB ~95)",
        "summary_sr": (
            "be going to + might varijacije u knjizi; jezici uputa i email sa uputstvima; kolokacije kao završeni blok."
        ),
        "priorities_sr": [
            "might kao manje izvesna opcija paralelno uz going to.",
            "Giving directions kao ritualnu frazu bez zastoja.",
            "Portfolio: opis destinacije na moru i mejl sa uputstvima (Workbook kao u štampi).",
        ],
    },
    {
        "n": 12,
        "sb_page_printed": "p126",
        "language_summary_page": "150",
        "portfolio_en": "At the airport",
        "portfolio_wb_printed": "p86",
        "pronunciation_ref": "pregled samoglasničkih zvukova (HB ~102)",
        "summary_sr": (
            "Superlativi uz velike brojeve; Present Perfect iskustvo + Have you ever …?; jezici aerodroma i pozdravljanja na rastanku."
        ),
        "priorities_sr": [
            "Kontrast ever/never kod iskustava.",
            "Lista past participle za nepravilne koje knjiga prati.",
            "Portfolio i End of Course Review (štampano ~p103) kao zajednički zaključak kursa.",
        ],
    },
]


def lesson(
    lid: str,
    unit: int,
    code: str,
    title_en: str,
    toc_vocab_en: str,
    toc_grammar_en: str,
    toc_rw_en: str,
    overview_sr: str,
    vocab: list[dict[str, str]],
    grammar: list[dict[str, object]],
    priorities_sr: list[str],
    real_world_sr: str,
) -> dict[str, object]:
    ep = {**EXTRA_PRACTICE_META[unit - 1]}
    ep[
        "note_sr"
    ] = "Vežba na kraju knjige zajednička je celoj jedinici (1A–1D); tebi su vidljive lekcije 1A–1C — istu obnovu veži uz sve tri."
    return {
        "id": lid,
        "unit": unit,
        "code": code,
        "title_en": title_en,
        "toc_vocab_en": toc_vocab_en,
        "toc_grammar_en": toc_grammar_en,
        "toc_rw_en": toc_rw_en,
        "overview_sr": overview_sr,
        "vocab": vocab,
        "grammar": grammar,
        "priorities_sr": priorities_sr,
        "real_world_sr": real_world_sr,
        "extra_practice": ep,
    }


# ---- 36 lessons 1A–12C -------------------------------------------------------------------------------
LESSONS: list[dict[str, object]] = [
    lesson(
        "1a",
        1,
        "1A",
        "How are you?",
        "countries and nationalities",
        "be (1): positive and Wh- questions; subject pronouns and possessive adjectives",
        "introducing people",
        "Predstavljanje ljudi iz različitih zemlja; nationality pridevi i države. Osnova ‘be’, Wh- obrasci.",
        [
            {"en": "Brazil / Egyptian / Warsaw", "sr": "primer: država, pridev nacionalnosti, grad kao u UDžbeniku"},
            {"en": "British / Brazilian / Serbian", "sr": "„Britanac / Brazilac / Srbin“ + pridev iz knjige"},
            {"en": "Where are you from?", "sr": "odakle ste (formal plural you)"},
            {"en": "What’s your name?", "sr": "molim ime / sa kim govorimo"},
            {"en": "This is … / Meet …", "sr": "neformalno predstavljanje treće osobe"},
        ],
        [
            {
                "topic": "be (1) + Wh- pitanja",
                "points": [
                    "am / is / are u pozitivi",
                    "What / Who / Where + be + …",
                    "Possessive adjectives uz imenicu",
                ],
                "examples": ["She’s Egyptian.", "What’s your nationality?"],
            },
        ],
        ["Mapirati subjekte i pravilan oblik be.", "Inverzija u svakoj Wh-", "Possessives uz imenicu, ne zamenicom"],
        "Predstavljanje ljudi na skupu kao u video/listening delu udžbenika.",
    ),
    lesson(
        "1b",
        1,
        "1B",
        "Coffee break",
        "jobs; a and an",
        "be (2): negative, yes/no questions and short answers",
        "Workplace small talk kao u liste slušanja (What do you do?)",
        "Poslovi, zanimanja, a/an kod profesija; pun krug Yes/No i negacije sa be.",
        [
            {"en": "dentist / manager / salesperson", "sr": "zanimanja sa CD vežbi"},
            {"en": "a university student / an hour", "sr": "primer gde član ide po zvuku, ne slovu"},
            {"en": "unemployed / retired / part-time", "sr": "status zaposlenja"},
            {"en": "What do you do?", "sr": "„čime se baviš?“ funkcionalni minimum"},
        ],
        [
            {
                "topic": "Negacija i kratak odgovor",
                "points": ["isn't / aren't / not after be", "Are you …? Short answers paired"],
                "examples": ["He isn’t a teacher.", "Are they architects? Yes, they are."],
            },
            {
                "topic": "Članovi a / an",
                "points": ["Pre zanimanja koja počinju vokalnim zvukom — an engineer"],
                "examples": [],
            },
        ],
        ["a/an samo uz zanimanja u pojedininom", "Kratko Yes/No u istoj intonacijskoj liniji", "Lista poslova glasovno naučiti napamet"],
        "Kafa-pauza: šta osoba radi i koji posao ima.",
    ),
    lesson(
        "1c",
        1,
        "1C",
        "Personal details",
        "numbers 20–100",
        "asking for personal details; asking people to repeat things",
        "",
        "Brojevi 20–100 u govoru; formular-lični podaci; fraze da tražiš ponavljanje i spelling.",
        [
            {"en": "mobile number / postcode", "sr": "mobilni / poštanski broj kao u registru"},
            {"en": "repeat / spell / slowly", "sr": "Molba za sporije ili slovima iz knjige"},
            {"en": "How do you spell …?", "sr": "staviti tačku i crticu slova pojedinačno"},
            {"en": "first name / surname / address", "sr": "osnovni formular jezik"},
        ],
        [
            {
                "topic": "Komunikacijske funkcije bez novog tense-a",
                "points": ["What’s your (+ noun)", "Molba za repetitions / spelling"],
                "examples": [],
            },
        ],
        ["Spelling naglas slova koja zvuče slično (G/J itd.)", "Brojeve javiti kao na telefonu", "Molba za repetitions učljivo"],
        "Iznajmljivanje auta / popunjavanje formulara uz Real World blok knjige.",
    ),
    lesson(
        "2a",
        2,
        "2A",
        "What's important?",
        "adjectives (1); adjective word order and very",
        "have got: positive and negative, questions and short answers",
        "Describing possessions / priorities like u anketi udžbenika",
        "Kombinacija pridevnog reda i jakog have got kao 'imati/imam'.",
        [
            {"en": "lucky / lonely / noisy", "sr": "prilagođeni primeri kao u poglavlju o vrednostima"},
            {"en": "very + adjective", "sr": "intenzifikator kao u pravili knjige"},
            {"en": "a big red car pattern", "sr": "redosled reči kojim knjiga modeluje kolokacije boje/veličine"},
            {"en": "I've got … / Have you got …?", "sr": "pitanje posedovanja kao u BV British English udžbenika"},
        ],
        [
            {
                "topic": "have got",
                "points": [
                    "'ve got / hasn't got struktura koja se pojavljuje u Language Summary-u",
                    "Yes/No pitanje Have you got …?",
                ],
                "examples": ["We’ve got a small flat.", "Has she got a bicycle?"],
            },
            {
                "topic": "Adjective position & very",
                "points": ["very + descriptive adjectives", "Pridevi ispred predmeta kojeg poseduješ"],
                "examples": ["It’s very important.", "I've got two really good friends."],
            },
        ],
        ["British have got automatizacija", "Razmisli kada native speaker kaže Have you got vs Do you have", "Stress na bitnim pridevima u opisu"],
        "Anketiranje što je nekome najvažnije + predstavljanje stvari kojima raspolažeš.",
    ),
    lesson(
        "2b",
        2,
        "2B",
        "The Browns",
        "family",
        "possessive ’s",
        "Photos & family tree aktivnosti kao u štampanim stranicama",
        "Članovi porodice, genitiv sa apostrofom, priča o ljubavnim/partnerskim vezama što knjiga prati kao temu.",
        [
            {"en": "cousin / stepfather / granddaughter", "sr": "široke porodične oznake koje pojaviš u drvetu sledećih strana"},
            {"en": "husband / wife / partner / single", "sr": "statni kao u društvenoj anketi udžbenika"},
            {"en": "the Browns / Nick’s mum", "sr": "'s kod imena i kolektivnog prezimena kao u materijalu za slušanje"},
        ],
        [
            {
                "topic": "Possessive 's",
                "points": ["Ime + ’s kod osoba", "Possessives posle plurale koje udžbenik daje u tabeli"],
                "examples": ["Lisa’s boyfriend is Hungarian.", "My parents’ house is big."],
            },
        ],
        ["Nikad John's / hes — zarez između genitiva i kopule", "'s kod imena koja završe na -s — prati što je u Language Summary štamp.", "Familijske strukture crtati tokom ponavljanja"],
        "Priča o Fotografiji porodica i poređenju u paru koju knjiga predlaže kao video/listening nastavak.",
    ),
    lesson(
        "2c",
        2,
        "2C",
        "Time and money",
        "time words",
        "telling the time; talking about the time; saying prices; buying tickets at the cinema",
        "",
        "Sat, pola i četvrtine po britanskom obrascu; cene karata kao u Real World vežbi kod bioskopa.",
        [
            {"en": "quarter past / half past / ten to nine", "sr": "sistem past/to kojim knjiga drži sve vežbe"},
            {"en": "How much …? / euros / cents", "sr": "ciljna komunikacija cene kao u cenovnik-foto"},
            {"en": "starts at … / lasts two hours", "sr": "filmski raspored kao u video dijelogu udžbenika"},
        ],
        [
            {
                "topic": "The time expressions",
                "points": ["It’s twenty past …", "Konekcija koliko dugo traje kao u funkcionalnoj sekciji knjige"],
                "examples": ["The film starts at quarter past eight.", "Tickets are €12.50."],
            },
        ],
        ["Nikad zbuniti thirteen sa thirty u ceni", "Pripremi karticu sa satom za brzi drill", "Fraze kao at the cinema učiti fonetski zajedno"],
        "Konverzacija kod karte za film kao u štampanim video-notes delu.",
    ),
    lesson(
        "3a",
        3,
        "3A",
        "My day",
        "daily routines",
        "Present Simple (1): positive and Wh- questions (I/you/we/they)",
        "Behind the camera rutine dokumentaraca kao u štampanom nastavnom putu knjige",
        "Čitanje i opis rutine koja se stalno ponavlja; prvo lice + they-you mišljaj.",
        [
            {"en": "wake up / have a shower / go to bed", "sr": "osnovni string koji knjiga uči redom časova"},
            {"en": "usually / at six / after work", "sr": "vremensko sidro za Present Simple kao u funkcionalnoj tabeli"},
            {"en": "What time do you … ?", "sr": "pitaj sve rutine kolege"},
        ],
        [
            {
                "topic": "Present Simple afirmacija + Wh-",
                "points": ["Uz navike rutine bez -s kod I/you/we/they", "What time … do you start? struktura koja se izvodi iz poglavlja"],
                "examples": ["I usually leave home at 7.", "Where do they work on Fridays?"],
            },
        ],
        ["Uz svaku rečenicu napiši frekvency marker ako je moguce", "Kolokacije have breakfast kao fiksna fraza na eng.", "Uzmi audio script posle pushtanja kao self-check"],
        "Opis sopstvenog ili tuđeg tipičnog radnog dana kao u dokumentarnom isečku iz knjige.",
    ),
    lesson(
        "3b",
        3,
        "3B",
        "Free time",
        "free time activities (1); time phrases with on, in, at, every",
        "Present Simple (2): negative and yes/no questions (I/you/we/they)",
        "Find two people / office party blokovi iz content listinga",
        "Negacija Present Simple kod hobija i dopunski obrasci kad ne aktivnost ne radiš.",
        [
            {"en": "once a week / on Sundays / every summer", "sr": "fraze sa on/in/at/every koja knjiga tabelično obrađuje"},
            {"en": "go swimming / read blogs / chill out", "sr": "primeri kolocations na listi koja prati poglavlja"},
            {"en": "don’t … / Do you …?", "sr": "model negacije kojim se završi drugi blok PS"},
        ],
        [
            {
                "topic": "don't + bazni infinitiv",
                "points": ["I don't swim in winter kao template", "Do you …? kraći odgovor Yes, I do / No, I don't"],
                "examples": ["We don't watch TV late.", "Do they surf at weekends?"],
            },
        ],
        ["Nikad dodaj do posle auxiliary", "Kada ide every vs on u smislu dana nedelje", "Napravite Find someone who aktivnost koja knjiga daje kao speaking"],
        "Traženje nekoga ko deli isti hobi kao u party speaking vežbi knjige.",
    ),
    lesson(
        "3c",
        3,
        "3C",
        "Special days",
        "months; dates",
        "phrases for special days; talking about days and dates; suggestions",
        "VIDEO A birthday present + datumi kao u poglavlja",
        "Kalendarski jezik; Let's / Shall we predlozi kao funkcionalni deo što knjiga uči na kraju blokova.",
        [
            {"en": "Mother’s Day / wedding anniversary / public holiday", "sr": "događaji što knjiga nabraja kao specijalnim danima"},
            {"en": "the fifth of May / March the third", "sr": "dva formata koja se nalaze paralelno u BS knjizi"},
            {"en": "Let’s celebrate / Shall we get …?", "sr": "kolaboracija oko poklona što knjiga uči kroz narativ"},
        ],
        [
            {
                "topic": "Datumi",
                "points": ["Months + ordinal brojevi što knjiga tabeluje", "in March / on Friday razlikuj"],
                "examples": ["My birthday's on the 12th of June.", "Shall we meet on Saturday evening?"],
            },
        ],
        ["Uk/US format datumu – drži se što nastavnica kaže kao standard", "Let's + base infinitiva — ne dopunjavaj to", "Narativ oko birthdays iz video poglavlja iskoristi za auditivni repeat"],
        "Plan poklona / rođendanskog ispisa kao što knjiga daje VIDEO scenario.",
    ),
    lesson(
        "4a",
        4,
        "4A",
        "Away from home",
        "free time activities (2)",
        "Present Simple (3): positive and negative (he/she/it)",
        "Activities at observatory narration iz content listing-a",
        "Treće lice singled + negacija kada opisuješ navike nekoga ili životinjama okruženosti.",
        [
            {"en": "He plays / She doesn’t go / It rains", "sr": "primeri kojima započne treći blok PS"},
            {"en": "always late / trains every Monday", "sr": "uvežbavanje zajedno sa freq adv iz drugih stranica zajednog review-a"},
            {"en": "third person singular -s", "sr": "pravilo + izuzeci (studies…) po Language Summary-u"},
        ],
        [
            {
                "topic": "-s / doesn't",
                "points": ["Dodaje se -es kada glagol završava što knjiga daje pravilo", "doesn't kao helper u negacija"],
                "examples": ["He studies medicine.", "The cafe doesn’t close early.", "She goes abroad every winter."],
            },
        ],
        ["Nikad dodaj dvostruku trećinu (does goes)", "Prepoznavanje subjekta u slušaonicama", "Uzmi život kao u opservatorijskom eseju knjige"],
        "Lagani narativ naučnog ambijenta kroz reading/listening blok.",
    ),
    lesson(
        "4b",
        4,
        "4B",
        "First Date!",
        "things you like and don’t like; verb+ing",
        "Present Simple (4): questions and short answers (he/she/it)",
        "Markov prvi randevu kao video/listening tema",
        "Like + aktivnost koja se završava na -ing; Does he/she pitanje radi trećeg lica kao u blokovima što knjiga zove First Date storyline.",
        [
            {"en": "love going / hate waiting / prefer walking", "sr": "Uz glagole volje + ing pattern iz tabele"},
            {"en": "Does she enjoy …?", "sr": "Pitanje u trećem licu"},
            {"en": "spicy street food / karaoke nights", "sr": "primeri što knjiga daje kod preferencije"},
        ],
        [
            {
                "topic": "Does + subject + verb base",
                "points": ["Samo jedan marker trećeg lica jer postoji auxiliary", "like + noun / like + verb-ing"],
                "examples": ["Does Liam like jazz?", "She loves chatting online.", "He doesn’t smoke."],
            },
        ],
        ["Nikad dodaj drugi -s u glavnoj reči ako već ima does", "Nauči par fraza flirt small talk što knjiga daje audio skriptama", "Kolokacije enjoy + -ing automatizacija"],
        "Small talk prvog randevua — Markova priča što knjiga drži kao video scenario.",
    ),
    lesson(
        "4c",
        4,
        "4C",
        "Eating out",
        "food and drink (1)",
        "requests and offers",
        "VIDEO At the Sun Café blok iz content liste",
        "Funkcionalni jezik ponude/restoranske narudžbine iz Real World blokova što knjiga vezuje meni i audio.",
        [
            {"en": "Could I have …? Would you like …?", "sr": "Formalno-prijateljsko naručivanje koje udžbenik drži zajednim"},
            {"en": "still or sparkling?", "sr": "primer dijaloga što knjiga stavlja u kafić funkcionalni jezik"},
            {"en": "main course / bill / takeaway", "sr": "fraze što knjiga daje kod menija"},
        ],
        [
            {
                "topic": "Želje i zamolbe",
                "points": ["can/could kao blagi zahtjev", "would like offers sa intonacija naglaska"],
                "examples": ["Could we sit outside?", "Would you like some water? Yes, please."],
            },
        ],
        ["Ženski i muški intonacije na Would you … — sluši audio što knjižica daje", "Razmotri politeness upgrade sa please", "Konstruiši vlastiti mini meni na srpskim proizvodima za drill"],
        "Realistični dijalog u kafići uz video što knjižni materijali nose.",
    ),
    lesson(
        "5a",
        5,
        "5A",
        "Three generations",
        "adjectives (2); years",
        "Past Simple (1): be (positive and negative, questions and short answers)",
        "Family generations discussion / timelines",
        "was/were u biografijskom kontekstu i pridevi što opisuju generacije ljudi što knjiga vodi Timeline vežbom.",
        [
            {"en": "grandparents generation / millennials", "sr": "generacijski skupovi što knjiga daje za diskusioni list"},
            {"en": "born in 1999 / Was it …?", "sr": "datum + Past be koji knjiga tabeluje"},
            {"en": "strict / cheerful / hardworking", "sr": "prilike prideva za karakter ljudi na fotografiji"},
        ],
        [
            {
                "topic": "Past of be",
                "points": ["was/weren’t parovi", "What year were you …? struktura koja se često ponavlja u listening scriptovima"],
                "examples": ["They were teenagers in the 1960s.", "Was Harry at home yesterday?"],
            },
        ],
        ["Nikad zbuniti I'm born — budi was born kad treba kao u summary", "Poveži broje godine sa intonation drop", "Koristi timeline strip koji knjiga daje kao scaffold"],
        "Tri generacije kao u foto-reading vežbi knjige uz diskusije „When was …?”.",
    ),
    lesson(
        "5b",
        5,
        "5B",
        "Famous films",
        "life events",
        "Past Simple (2): regular and irregular verbs (positive and Wh- questions)",
        "Biographical narrative from favourite movie characters",
        "Događaji u životu kroz pravilne i nepravilne proste prošle oblike — knjiga vodi storyline filmova.",
        [
            {"en": "direct / win award / marry / divorce", "sr": "životni event glagoli koje liste verb table prate materijalom"},
            {"en": "last night / yesterday / ago", "sr": "markers prošlost sto knjižiš na margini"},
            {"en": "When did …? / Who did she …?", "sr": "Wh- struktura koja zahteva did + base koju poglavlja tabelišu"},
        ],
        [
            {
                "topic": "Past simple questions",
                "points": ["Did + pronoun + base", "Past Wh- koja zadrži did"],
                "examples": ["Did he move to Rome?", "What did she study at university?", "They didn’t marry in 1985."],
            },
        ],
        ["Nepravilnosti — bar deset glagola iz liste nepravilnih na kraju knjige.", "Više radnji u prošlosti u istoj poruci kad knjiga dopušta.", "Film kao motiv za govornu minijaturu"],
        "Kratko prepričavanje filmskog junaka kao što knjiga daje kombinacije reading/speaking zadataka.",
    ),
    lesson(
        "5c",
        5,
        "5C",
        "Four weekends",
        "weekend activities",
        "showing interest; asking follow-up questions",
        "VIDEO How was your weekend?",
        "Jezični signali što pokazuju slušanje + follow-up pitanje — vežva se kroz Weekend notes block.",
        [
            {"en": "Really? Tell me more. / Lucky you!", "sr": "funkcijske pozadinske oznake pažnje"},
            {"en": "What did you do then?", "sr": "dopunsko pitanje posle početnog odgovora"},
            {"en": "We went surfing / chilled at home", "sr": "krajnje aktivnosti što knjiga daje u audio skript"},
        ],
        [
            {
                "topic": "Discourse markers",
                "points": ["Back-channel responses", "Wh- dopune sa Past Simple strukturom koja ostaje"],
                "examples": ["Sounds fun!", "Who did you go with?", "And what happened next?"],
            },
        ],
        ["Nikad skidaj pažnju od partnera kod pairwork — knjiži note tokom govora kao zadatak nastavnica predlaže", "Replicirai intonacije audio skipta za naturalnost", "Kolekcija kraćih wow odgovori"],
        "Video weekend review koji knjiga vezuje interesovanjem i nastavnim pitanjem.",
    ),
    lesson(
        "6a",
        6,
        "6A",
        "Google it!",
        "the internet",
        "Past Simple (3): negative, yes/no questions and short answers",
        "Planet Google / Find someone who anecdotes",
        "Did / didn't pattern za događaje koji se opisuju u digitalnom narativima knjiga daje kao Google timeline.",
        [
            {"en": "website / wifi / bookmark / spam", "sr": "minimalni vocab internet okruženja"},
            {"en": "click / browse / surf", "sr": "internet glagolske kolokacije koje poglavlja daje"},
            {"en": "Did you google …?", "sr": "gugl kao glagol u govornoj šali ali formalnije formulacija did you search"},
        ],
        [
            {
                "topic": "Past yes/no recap",
                "points": ["Did + pronoun … ? short answers ako knjiga stranici", "was/were ostaje paralelna linija što ne zbunjuje"],
                "examples": ["Did you find the directions online?", "We didn’t have wifi in that hotel.", "Did they reply? Yes, they did."],
            },
        ],
        ["Nikad zbuniti was i did kao hibrid ako glavni glagol nije be", "Koristi find someone kao game loop što knjiga pridaje poglavlja", "Nauči lexical chunk 'search for information' kao alternativa google kao glagol"],
        "Lagani interview o 'first time internet' anecdotes koji poglavlja daje kao komunikacija.",
    ),
    lesson(
        "6b",
        6,
        "6B",
        "Changing technology",
        "mobile phones and TVs; past time phrases",
        "can/can't; could/couldn't",
        "",
        "Poređanje sposobnosti onda vs sada; modali can/could što knjiga vezuje sa device timeline.",
        [
            {"en": "streaming / rechargeable / touchscreen", "sr": "fraze koja knjiga modern device description"},
            {"en": "could text / couldn't record video", "sr": "sposobnost u prošlostima — modali što knjiga daje funkcionalnim taskovima"},
            {"en": "In 2008 we couldn't … Now we can …", "sr": "template za kontrast modala na vremenskoj liniji"},
        ],
        [
            {
                "topic": "can / can't / could(n't)",
                "points": ["Modal + base kao u poglavlja", "Negacija kao can't / couldn't"],
                "examples": ["I can unlock my phone now.", "We couldn't send photos instantly in 1995."],
            },
        ],
        ["Nikad dodaj infinitivan to posle kan direktnog modala što knjiga drži pravilo.", "Prepoznavanje unstressed kan u audio što knjiga Help with Listening ima", "Analogija tehnoloških uređaja motivator"],
        "Priča prvog mobilnog što knjiga audio skript ima kao storytelling.",
    ),
    lesson(
        "6c",
        6,
        "6C",
        "The news",
        "verbs from news stories",
        "talking about the news",
        "VIDEO Talking about the news blok",
        "Headline glagolske kolokacije; Past Simple narration da prepričaš štampani strip vesti što knjiga daje.",
        [
            {"en": "rescue flood victims / riot / reopen airport", "sr": "scenariji što knjiga daje u mini vestima radi listening"},
            {"en": "breaking news according to … / sources say …", "sr": "fraze za meta-komentar što knjiga stavlja u script margin"},
            {"en": "presenter / eyewitness / reporter", "sr": "uloge medija ljudi koja knjiga kroz video objašnjavaju"},
        ],
        [
            {
                "topic": "Talking about headlines",
                "points": ["Use simple past kao default za događaj što se desio", "Sequencers: First, Then, Afterwards"],
                "examples": ["A plane landed safely.", "Thousands of tourists left the island.", "Authorities closed the motorway."],
            },
        ],
        ["Nikad zbuniti present continuous za vest ako događaji završeni — držaj past simple što knjiga modeluje.", "Uzmi headline skraceno pa ga proširivanje u paru što knjiga predviđa aktivnost", "Prepoznavanje stressing u help sekciji knjiga daje kao Task"],
        "Parafrazacija video vesti koja knjiga stavlja posle poglavlja 6C kao group task.",
    ),
    lesson(
        "7a",
        7,
        "7A",
        "Where I live",
        "places in a town",
        "there is/there are",
        "",
        "Mesta u gradu; postoji/ne postoji konstrukt koji knjiga vezuje kroz kartu i spot-the-difference zadatkima iz contents listing.",
        [
            {"en": "library / roundabout / outskirts", "sr": "mesta koja knjiga stavlja u map task"},
            {"en": "There’s a café on the corner.", "sr": "template postojanja što knjiga stavlja u speaking loop"},
            {"en": "next to / opposite / behind (with place nouns)", "sr": "kombajn sa prepositions from unit 7 map"},
        ],
        [
            {
                "topic": "There is / there are",
                "points": ["Singular plural agreement", "Is there …? inversion"],
                "examples": ["There's a supermarket near my house.", "Are there good schools nearby? Yes, there are."],
            },
        ],
        ["Nikad zbuniti it is i there is što srpsk govorniku često", "Upari kartu sa activity page i speaking pairwork-om kao u udžbeniku", "Nauči kombinacije there + preposition što knjiga daje u Language Summary"],
        "Opis sopstvenog kvarta koji knjiga zove Places near my home listening activity.",
    ),
    lesson(
        "7b",
        7,
        "7B",
        "A new home",
        "rooms and things in a house",
        "How much …? and How many …?; some, any, a",
        "",
        "Kvantifikacija + some any u kontekstu kupovine nameštaja što knjiga vezuje oglasima za stan.",
        [
            {"en": "wardrobe / carpet / kettle", "sr": "stavke nameštaja koje fotografije knjiga daje"},
            {"en": "How much furniture?", "sr": "razlika many/m za brojivi vs nebrojivi predmet što knjiga tabela prikazuje"},
            {"en": "some milk / any sugar / a carton of juice", "sr": "kvantifikacije koje paralelna stranica kombinuje sa shop temom"},
        ],
        [
            {
                "topic": "How much / How many",
                "points": ["Countable vs uncounable po pravilima koje poglavlja 7B kombinuju", "some/any u pitanju i ponudi"],
                "examples": ["How many chairs are there?", "There's some space in the kitchen.", "Is there any hot water?"],
            },
        ],
        ["Drill countable vs uncounable paralel unit 4 kombinacije", "Nauči some u poz pozitivi i offer", "Uzmi adverts for flat što knjiga daje kao reading uz brojanje"],
        "Reading oglasa koji knjiga portfolio vežbu najma kao produžetu temu poglavlja.",
    ),
    lesson(
        "7c",
        7,
        "7C",
        "At the shops",
        "shops; things to buy",
        "what sales assistants say; what customers say",
        "VIDEO Can I help you?",
        "Funkcionalni dijalozi prodaje i klijenta što knjiga vodi kao role-play u dept store page.",
        [
            {"en": "changing rooms / refunds / size medium", "sr": "fraze customer service koja knjiga daje u script margin"},
            {"en": "Can I pay by card?", "sr": "kraće zahtev što knjiga listening loop"},
            {"en": "Are you looking for anything in particular?", "sr": "asistent-opening line koja knjiga modeluje pozdravnim audio"},
        ],
        [
            {
                "topic": "Service encounter language",
                "points": [
                    "Asistent pola-pitanje + ponuda",
                    "Kupci odgovor + politely decline — knjiga script margin",
                ],
                "examples": [
                    "I’m just looking.",
                    "I’ll take this jumper, thanks.",
                ],
            },
        ],
        ["Intonacije pristojnog odbijanja 'just looking'", "Uzmi funkcionalnu list fraza iz Real World što knjiga stavlja pored video", "Kombinacija some/any u shopping cart što knjiga prati"],
        "Video department store blok koji knjiga ima kao Can I help you scenario.",
    ),
    lesson(
        "8a",
        8,
        "8A",
        "The meeting",
        "work",
        "Present Continuous: positive and negative, questions and short answers",
        "Conversations office / Present continuous tasks from contents listing",
        "Kontrast now/routine što knjiga veže office storyline i listening loop o sastanskima koji se dešavaju 'right now'.",
        [
            {"en": "at the moment / today / currently", "sr": "vremena signala koja knjiga chapter 8A"},
            {"en": "She’s presenting / We’re revising budgets", "sr": "-ing strukture koja knjiga daje u office script"},
            {"en": "Is he joining us online?", "sr": "PC question pattern"},
        ],
        [
            {
                "topic": "Present Continuous",
                "points": ["Am/is/are + verb-ing kao u poglavlja", "negacija kao isn’t reviewing"],
                "examples": [
                    "They’re negotiating a deal today.",
                    "I’m not working late this evening.",
                ],
            },
        ],
        ["Nikad zbuniti now meaning scheduled today vs actually now — knjiga listening activities objašnjavaju situ", "Uzmi diary comparison activity što teacher notes predlaže", "Office kolokacije (hold a meeting) pamti kao chunk"],
        "Office komunikacije koje poglavlja daje kao video/listening blok The meeting.",
    ),
    lesson(
        "8b",
        8,
        "8B",
        "It’s snowing!",
        "types of transport; travelling verbs and phrases",
        "Present Simple or Present Continuous",
        "Usually & today juxtaposition storyline knjiga contents listing kao Snow day blok",
        "Transport glagolske kombinacije; odluka između trajanj i slike trenutka na osnovu vremenskih signala koja knjiga daje paralel Snow day temi.",
        [
            {"en": "delayed / diverted / commuter train", "sr": "vokab transport situacija koja knjiga daje u weather-travel kombinacije"},
            {"en": "I usually drive but today I’m taking the tram", "sr": "template kontrast habitual vs now"},
            {"en": "traffic jam / motorway / platform", "sr": "mesta koja knjiga stavlja u reading gap tasks"},
        ],
        [
            {
                "topic": "PS vs PC",
                "points": [
                    "Signal words habitual vs happening now",
                    "Temporary situations takođe idi sa PC što knjiga Language Summary tabeluje",
                ],
                "examples": [
                    "It’s snowing heavily right now but it usually melts quickly.",
                ],
            },
        ],
        ["Nikad zbuniti stative verbs gde udžbenik ima mini list ako je predavač istakao restriction", "Koristi 'today' kao trigger da prebaciš tense", "Uzmi spotting difference activity paralel poglavlja 8"],
        "Vremensko putovanje u snegu paralel poglavlja 8 storyline i video loop.",
    ),
    lesson(
        "8c",
        8,
        "8C",
        "On the phone",
        "talking on the phone",
        "functional phone language embedded with PC/PS review",
        "VIDEO Can I call you back? blok",
        "Telefonske fraze što knjiga daje kroz voicemail i live call script u contents listing funkcionalnoj sekciji.",
        [
            {"en": "Can I ring you later? / Wrong number!", "sr": "fraze voicemail loop"},
            {"en": "I’ll text you back / Speak up, it’s noisy", "sr": "kolokacije koja knjiga daje u marginal notes"},
            {"en": "hold the line / put you through", "sr": "fraze što knjiga daje u office phone extension tasks"},
        ],
        [
            {
                "topic": "Phone routines",
                "points": [
                    "Short ellipsis sentences typical for phone english",
                    "Present continuous for ‘I’m calling about…’ if knjiga skript tako modeluje",
                ],
                "examples": [
                    "I’m calling about the invoice.",
                    "Can you hear me okay?",
                ],
            },
        ],
        ["Sluši weak forms help sekcije knjiga listening margin", "Nauči skraćivanja gonna/wanna samo kao awareness ako profesor dopušta", "Par role-play voicemail loop"],
        "Video phone messages scenario koji knjiga vezuje sa Emily phone calls blokom iz contents listing-a.",
    ),
    lesson(
        "9a",
        9,
        "9A",
        "Holiday South Africa",
        "holiday activities",
        "infinitive of purpose",
        "Help with Listening weak forms snippet + Safari holiday storyline",
        "To + infinitiv radi objašnjenja cilja putovanja (go to Cape Town **to see**…) — paralel poglavlja 9A holiday reading.",
        [
            {"en": "guided tour / wildlife / selfies on safari", "sr": "holiday lexical set koji poglavlja 9 ima"},
            {"en": "I went there to explore", "sr": "primer infinitiva svrhe koja knjiga daje funkcionalnoj tabeli"},
            {"en": "so that / in order to (ako summary spominje synonyms)", "sr": "samo ako Language Summary paralel pokazuje — inače drži simplest to"},
        ],
        [
            {
                "topic": "to + verb for purpose",
                "points": ["Poslije glagol kretanja", "Answers Why ...? što knjiga activities traže"],
                "examples": ["We flew to Johannesburg to visit friends.", "I’m studying English to travel more."],
            },
        ],
        ["Ne mešati -ing cilj sa to infinit za svrhu ako knjiga summary strikt names each", "Koristi map task holiday South Africa paralel poglavlja", "Intonation na why question responses"],
        "Listening o odmoru u Južnoj Africi paralel što knjiga daje u holiday activities story.",
    ),
    lesson(
        "9b",
        9,
        "9B",
        "A trip to Egypt",
        "natural places",
        "comparatives",
        "Listening natural places comparative tasks",
        "Komparacije između dva prirodna destinacije — knjiga reading/listening pyramids i photo tasks.",
        [
            {"en": "sand dune / coral reef / cliff", "sr": "nouns natural places koja knjiga daje u photo captions"},
            {"en": "more peaceful / cheaper / longer than", "sr": "comparatives pattern iz summary tabele"},
            {"en": "the Nile is longer than … / This beach is hotter", "sr": "primere paralel što knjiga daje u speaking cards"},
        ],
        [
            {
                "topic": "Comparatives formation",
                "points": [
                    "short adj + –er vs more + long",
                    "Irregular comparisons good better best — knjiga summary note",
                    "than usage",
                ],
                "examples": ["Luxor is hotter than Alexandria in July.", "The desert is quieter than the city centre."],
            },
        ],
        ["Double comparative grešaka izbegavanje 'more hotter'", "Koristi than posle poređenje", "Kombinacija reading 'Two people i know' zadatak što knjiga daje u contents listing"],
        "Opis Egipatskih destinacija paralel foto/listening blokovima knjiga daje poglavlja 9B.",
    ),
    lesson(
        "9c",
        9,
        "9C",
        "A day out",
        "animals",
        "deciding what to do (like / would like / suggestions)",
        "VIDEO Planning a day out blok",
        "Životinjice + planiranje dana zajednice — jezici kao Would you like … / Shall we što knjiga vodi VIDEO plan loop.",
        [
            {"en": "aquarium keeper / flamingo enclosure", "sr": "što knjiga reading box daje u day out lexical pack"},
            {"en": "How about visiting …? / Let's start with …", "sr": "suggestion structures parallel activities lists"},
            {"en": "I’d prefer to … / Shall we grab lunch first?", "sr": "funkcionalni blok za dogovaranje"},
        ],
        [
            {
                "topic": "Making decisions politely",
                "points": [
                    "Would like vs like doing — knjiga verb pattern section posle unit 9D ali već počinju da se javljaju kombinacije u activities",
                    "Let's + base kao standard",
                ],
                "examples": ["Let’s feed the dolphins first.", "Would you prefer to watch the parade or rest?"],
            },
        ],
        ["Kolektivnu odluku vodi tako da koristis softeners 'maybe'", "Nikad zbuniti like + noun vs would like structure", "Koristi VIDEO script kao scaffolding"],
        "Video plan jednog izlaska koji knjiga zove Planning a day out interaktiv.",
    ),
    lesson(
        "10a",
        10,
        "10A",
        "Stay fit and healthy",
        "verb phrases; frequency expressions",
        "imperatives; should/shouldn’t",
        "Fitness tips adverts + commands",
        "Imperativi saveta kao u Get fit for free oglasu; should za blago upozorenje što knjiga stavlja u health campaign reading.",
        [
            {"en": "stretch / hydrate / quit smoking / sleep seven hours", "sr": "imperativno zdravlje koja knjiga daje u advice poster"},
            {"en": "You should eat less salt.", "sr": "should pattern koja knjiga stavlja u doctor advice loop"},
            {"en": "Don’t lift heavy weights alone.", "sr": "negativni imperative tip za gym safety"},
        ],
        [
            {
                "topic": "Imperatives",
                "points": ["Verb base command", "Don’t za zabranu"],
                "examples": ["Drink plenty of water.", "Don’t ignore chest pain.", "Eat more greens."],
            },
            {
                "topic": "should",
                "points": [
                    "should / shouldn’t kao predlog",
                    "Frequency expressions recycles earlier units što knjiga kombinuje",
                ],
                "examples": ["You shouldn’t skip breakfast.", "We should stretch before running."],
            },
        ],
        ["Imperativ intonation da ne zvuči grubo", "should mekši od must — zadrži pragmatic awareness", "Kombinacija health vocabulary sa earlier food unit"],
        "Reading saveta što knjiži Get fit blok iz contents listing kao functional health adverts.",
    ),
    lesson(
        "10b",
        10,
        "10B",
        "What’s she like?",
        "appearance; character",
        "questions with like",
        "Describing Leo’s girlfriend adverts / character appearance tasks",
        "What … like? struktura koja razdvaja izgled i karakter ljudi što knjiga daje The Break adverts + reading task.",
        [
            {"en": "fair hair / curly / medium height / shy / outgoing", "sr": "pojmovi što knjiga daje u character grid"},
            {"en": "What does he look like? vs What’s he like?", "sr": "razlika koja knjiga Help with Grammar posebno markira ako predavač uradi"},
            {"en": "She looks like her mum / She’s really chatty", "sr": "kombajn look vs be like"},
        ],
        [
            {
                "topic": "like questions",
                "points": [
                    "What … like za karakter/general impression",
                    "look like fizički kao alternativa",
                ],
                "examples": ["What’s your new roommate like?", "He looks tired today."],
            },
        ],
        ["Ne mešati 'like' kao glagol volje bez konteksta", "Koristi opis ljudi što knjiga daje u video advert", "Nauči collocation curly hair vs hairs"],
        "Video The Break blok koji knjiga ima kao adverts describing people.",
    ),
    lesson(
        "10c",
        10,
        "10C",
        "I feel ill",
        "health problems; treatment",
        "talking about health",
        "VIDEO Get well soon / doctor sympathetic listening",
        "Simptomi + jezik lekarskih saveta paralel što knjiga daje u medical role-plays funkcionalnoj sekciji.",
        [
            {"en": "rash / dizziness / prescribe tablets / antibiotics", "sr": "simptomi što knjiga daje u waiting room script"},
            {"en": "I’ve got a temperature / headache", "sr": "'ve got + symptom pattern"},
            {"en": "Take this twice a day / rest for two days", "sr": "treatment fraze koja knjiga daje u doctor advice"},
        ],
        [
            {
                "topic": "Health functional language",
                "points": [
                    "Symptoms with have got / feel",
                    "Polite reassurance responses parallel listening sympathetic help section",
                ],
                "examples": ["I've had this cough for four days.", "You should drink more herbal tea.", "Stay in bed tonight."],
            },
        ],
        ["Intonation empathy kad slušaš nekoga bolnog", "Koristi bilingual dictionary za preciznu medicinsku terminologiju što knjiga gloss daje?", "Nikad zbuniti ache vs pain context"],
        "Video Get well soon scenario koji knjiga ima kao conversational health storyline.",
    ),
    lesson(
        "11a",
        11,
        "11A",
        "Happy New Year!",
        "New Year’s resolutions",
        "be going to (1): positive, negative and Wh- questions",
        "Listening New Year resolutions + plans story",
        "Going to struktura koja knjiga language summary poglavlja 11 počinje planiranjem januarskih odluka.",
        [
            {"en": "save money / quit coffee / train for marathon", "sr": "resolutions lexical pack koja knjiga daje u survey tasks"},
            {"en": "I’m going to move house", "sr": "am/is/are + going to verb base"},
            {"en": "What are you going to do?", "sr": "Wh- question template"},
        ],
        [
            {
                "topic": "be going to (affirmative/negative/Wh-)",
                "points": [
                    "Form as knjiga grammar spread",
                    "Negation sa not kao u poglavlja (I'm not going to...)",
                ],
                "examples": ["We're going to visit grandparents.", "He isn’t going to change jobs now.", "Who are they going to meet?"],
            },
        ],
        ["Razmisli razliku između going to kao planiranje od will spontaneous kada knjiga kasnije re-introd", "Nikad zbuniti go + to + place vs going to kao structure", "Koristi countdown speaking board sto knjiga daje"],
        "Contents listing New Year blok sa listening loop za resolutions.",
    ),
    lesson(
        "11b",
        11,
        "11B",
        "No more exams!",
        "studying",
        "be going to or might; be going to (2): yes/no questions and short answers",
        "Find one person interview game about future plans exams",
        "Might kao manje čvrsti plan paralel uz going to što knjiga daje u exam stress storyline.",
        [
            {"en": "might move abroad / Definitely retake exams", "sr": "kombajn izvesnosti koja knjiga daje u speaking prompt"},
            {"en": "Are you going to …? Yes, I am / No I'm not.", "sr": "Yes/No blok round 11B"},
            {"en": "revision timetable / postgraduate course", "sr": "lexical studying pack"},
        ],
        [
            {
                "topic": "going to Yes/No",
                "points": [
                    "Inversion Are + subject + going to …",
                    "Might modal base — knjiga usage as possibility",
                ],
                "examples": ["Are you going to study tonight? Maybe—I might revise later.", "We might celebrate if we pass."],
            },
        ],
        ["Intonation na maybe da zvuči ne izvesno", "Nikad zbuniti might + to inf — might + base kao modal", "Koristi questionnaire find one person scenario"],
        "Speaking loop 'Find one person who' futures oko ispita koji poglavlja 11 koristi kao motivacija.",
    ),
    lesson(
        "11c",
        11,
        "11C",
        "Directions",
        "directions; asking for and giving directions",
        "functional imperative directions grammar minimal",
        "VIDEO Giving directions + email directions tasks",
        "Uputstva typ turn left / cross bridge — knjiga functional pages i video route tasks.",
        [
            {"en": "carry straight on / roundabout second exit / footpath", "sr": "imperative/route chunks kao u map activity"},
            {"en": "Is it far?", "sr": "pitanje udaljenosti"},
            {"en": "You’ll pass a church on your left.", "sr": "landmark narration fraze"},
        ],
        [
            {
                "topic": "Imperatives + sequencing",
                "points": [
                    "Base verb commands for walker",
                    "Sequence markers Next / Then / After that",
                ],
                "examples": [
                    "Go past the bakery and turn right at the pharmacy.",
                    "Keep going until you see the marina.",
                ],
            },
        ],
        ["Practise drawing map from partner instructions što knjiga zove maze activity", "Intonation na politely asking help", "Kombinacija 'you will' kao future marker u uputstvima što knjiga modeluje"],
        "Video Directions holiday home scenario koji poglavlja 11 ima uz email practice.",
    ),
    lesson(
        "12a",
        12,
        "12A",
        "It’s a world record",
        "big and small numbers",
        "superlatives",
        "World Quiz + record breakers content listing",
        "Veliki brojevi + superlative formiranje paralel što knjiga daje World Quiz reading/speaking.",
        [
            {"en": "billion / degree Celsius / metre / population", "sr": "numbers science pack koji knjiga daje u quiz cards"},
            {"en": "the longest river / most crowded city / least expensive", "sr": "superlative combos iz summary grammar"},
            {"en": "How high is …? / measurement verbs", "sr": "FAQ pattern oko rekorda"},
        ],
        [
            {
                "topic": "Superlatives",
                "points": [
                    "-est / most + long adjective što knjiga tabela daje",
                    "the obligatory before superlative noun phrase",
                    "comparison groups of three+ entities",
                ],
                "examples": ["Everest is the highest mountain.", "London is one of the most expensive cities.", "What's the quickest route?"],
            },
        ],
        ["Razmisli syllable stressing superlatives (important → most important)", "Brojevi readability — pause po grupama što knjiga listening traži", "Koristi trivia speaking board"],
        "World Quiz blok koji poglavlja 12 počinje sa record breakers story.",
    ),
    lesson(
        "12b",
        12,
        "12B",
        "Have you ever … ?",
        "past participles",
        "Present Perfect: positive and negative; Have you ever ... ? questions and short answers",
        "Life experiences interviewing loop",
        "Have you ever + past participle; Present Perfect affirmative/negative kako knjiga Language Summary 12 obrađuje.",
        [
            {"en": "been abroad / ridden a camel / eaten sushi", "sr": "life experience collocations koja knjiga daje u survey sheet"},
            {"en": "Have you flown business class?", "sr": "ever question variants"},
            {"en": "No, I haven't / Yes, twice last year.", "sr": "Short answers što knjiga drži paralel answering cards"},
        ],
        [
            {
                "topic": "Present Perfect experience",
                "points": [
                    "have/has + past participle",
                    "ever in questions",
                    "never u negacije experience",
                    "still link to irregular participle charts stranice knjiga daje appendix",
                ],
                "examples": ["I've never scuba dived.", "Have they visited Kyoto before?", "She’s worked abroad."],
            },
        ],
        ["Participles memorization koristi appendix list koja knjiga daje p167 kao guided self-study loop", "Ne mešaj simple past ako je eksplicit timeframe osim knjiganog kontrast poglavlja", "Self-employed holiday stories listening loop koji knjiga daje u contents listing"],
        "Experiences anecdotes koji knjiga zove my life experiences + interview carousel.",
    ),
    lesson(
        "12c",
        12,
        "12C",
        "See you soon!",
        "things and places at an airport",
        "at the airport; saying goodbye",
        "VIDEO At the airport / Saying goodbye",
        "Funkcionalni jezik leta (gate, baggage, runway) kao i emotional goodbye fraze koja knjiga završava kurs funkcionalnim video blokom.",
        [
            {"en": "boarding pass / baggage reclaim / runway", "sr": "aerodrom glossary koji knjiga štampa paralel poglavlja 12"},
            {"en": "Have a safe journey / Keep in touch!", "sr": "goodbye formulae"},
            {"en": "Check-in closes in twenty minutes!", "sr": "stress situacija announcement language"},
        ],
        [
            {
                "topic": "Airport + farewell routines",
                "points": [
                    "Short functional sentences under pressure",
                    "Mix present perfect recap 'have you packed…' if knjiga script uses",
                    "Politeness escalation when saying goodbye socially",
                ],
                "examples": ["They're calling our gate.", "Text me when you land.", "We've had such a great trip—see you soon!"],
            },
        ],
        ["Intonation emotional goodbye bez awkward pause", "Koristi Portfolio 12 at airport workbook stranicu kao proširené písanie", "Kombinacija sa End of Course review p103 kao final checklist"],
        "Video blokovi At the airport + Saying goodbye koji knjiga završavaju kurs komunikacije.",
    ),
]

COURSE_NOTE_SR = (
    "Kratki rezimesi sintetizuju sadržaj face2face Elementary (2nd ed.) prema štampanom "
    "'Contents' koji je tekstualno izvučen iz tvojeg SB.pdf. Stranice lekcije u udžbeniku su uglavnom "
    "bez izvučenog teksta (grafika), dok su sadržaj i neke uputne strane čitljive; zato "
    "'Extra Practice (štampano p115–126)' ostaje strukturalni rezime + upućivanje na Workbook "
    "/ Language Summary jer te stranice u PDF‑u nemaju OCR teksta."
)


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "course": {
            "title": "face2face Elementary · Lekcije 1A–12C (+ Extra Practice po jedinicama)",
            "notes_sr": COURSE_NOTE_SR,
        },
        "lessons": LESSONS,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_EMBED.write_text(
        "// Auto-generated — do not edit by hand.\n"
        "window.__LESSONS_DATA__ = "
        + json.dumps(payload, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )
    print("Wrote", OUT_JSON, OUT_EMBED, "lessons:", len(LESSONS))


if __name__ == "__main__":
    main()

