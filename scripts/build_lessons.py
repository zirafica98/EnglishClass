#!/usr/bin/env python3
"""
Pravi site/data/lessons.json i lessons.embed.js iz OCR teksta knjige (face2face Elementary 2nd ed.).

Za svaku lekciju kombinuje 2 PDF stranice OCR teksta i izdvaja parče Extra Practice-a koje
pripada baš toj podlekciji. Dodaje srpski rezime i prioritete učenja.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR_DIR = ROOT / "ocr_pages"
OUT_JSON = ROOT / "site" / "data" / "lessons.json"
OUT_EMBED = ROOT / "site" / "data" / "lessons.embed.js"

sys.path.insert(0, str(Path(__file__).parent))
from vocab_data import LESSONS_VOCAB
from unit_tests import UNIT_TESTS

# ---------------------------------------------------------------------------
# Mapiranje lekcija → PDF stranice (1-based).
# Format: (id, unit, code, title_en, book_page, [pdf_pages], vocab_en, grammar_en, rw_en)
LESSON_MAP: list[tuple[str, int, str, str, int, list[int], str, str, str]] = [
    # ---- Unit 1 ----
    ("1a", 1, "1A", "How are you?", 8, [10, 11],
     "countries and nationalities",
     "be (1): positive and Wh- questions; subject pronouns and possessive adjectives",
     "introducing people"),
    ("1b", 1, "1B", "Coffee break", 10, [12, 13],
     "jobs; a and an",
     "be (2): negative, yes/no questions and short answers",
     ""),
    ("1c", 1, "1C", "Personal details", 12, [14, 15],
     "numbers 20–100",
     "",
     "asking for personal details; asking people to repeat things"),
    ("1d", 1, "1D", "Lost property", 14, [16, 17],
     "personal possessions; plurals; this, that, these, those",
     "",
     ""),
    # ---- Unit 2 ----
    ("2a", 2, "2A", "What's important?", 16, [18, 19],
     "adjectives (1); adjective word order and very",
     "have got: positive and negative, questions and short answers",
     ""),
    ("2b", 2, "2B", "The Browns", 18, [20, 21],
     "family",
     "possessive 's",
     ""),
    ("2c", 2, "2C", "Time and money", 20, [22, 23],
     "time words",
     "",
     "telling the time; talking about the time; saying prices; buying tickets at the cinema"),
    ("2d", 2, "2D", "Where's the baby?", 22, [24, 25],
     "things in a house; prepositions of place",
     "",
     ""),
    # ---- Unit 3 ----
    ("3a", 3, "3A", "My day", 24, [26, 27],
     "daily routines",
     "Present Simple (1): positive and Wh- questions (I/you/we/they)",
     ""),
    ("3b", 3, "3B", "Free time", 26, [28, 29],
     "free time activities (1); time phrases with on, in, at, every",
     "Present Simple (2): negative and yes/no questions (I/you/we/they)",
     ""),
    ("3c", 3, "3C", "Special days", 28, [30, 31],
     "months; dates",
     "",
     "phrases for special days; talking about days and dates; suggestions"),
    ("3d", 3, "3D", "Early bird?", 30, [32, 33],
     "frequency adverbs",
     "subject and object pronouns",
     ""),
    # ---- Unit 4 ----
    ("4a", 4, "4A", "Away from home", 32, [34, 35],
     "free time activities (2)",
     "Present Simple (3): positive and negative (he/she/it)",
     ""),
    ("4b", 4, "4B", "First Date!", 34, [36, 37],
     "things you like and don't like; verb+ing",
     "Present Simple (4): questions and short answers (he/she/it)",
     ""),
    ("4c", 4, "4C", "Eating out", 36, [38, 39],
     "food and drink (1)",
     "",
     "requests and offers"),
    ("4d", 4, "4D", "Breakfast time", 38, [40, 41],
     "food and drink (2); countable and uncountable nouns",
     "",
     ""),
    # ---- Unit 5 ----
    ("5a", 5, "5A", "Three generations", 40, [42, 43],
     "adjectives (2); years",
     "Past Simple (1): be (positive and negative, questions and short answers)",
     ""),
    ("5b", 5, "5B", "Famous films", 42, [44, 45],
     "life events",
     "Past Simple (2): regular and irregular verbs (positive and Wh- questions)",
     ""),
    ("5c", 5, "5C", "Four weekends", 44, [46, 47],
     "weekend activities",
     "",
     "showing interest; asking follow-up questions"),
    ("5d", 5, "5D", "Competitions", 46, [48, 49],
     "adjectives (3); adjectives with very, really, quite, too",
     "",
     ""),
    # ---- Unit 6 ----
    ("6a", 6, "6A", "Google it!", 48, [50, 51],
     "the internet",
     "Past Simple (3): negative, yes/no questions and short answers",
     ""),
    ("6b", 6, "6B", "Changing technology", 50, [52, 53],
     "mobile phones and TVs; past time phrases",
     "can/can't; could/couldn't",
     ""),
    ("6c", 6, "6C", "The news", 52, [54, 55],
     "verbs from news stories",
     "",
     "talking about the news"),
    ("6d", 6, "6D", "Mario Man", 54, [56, 57],
     "articles: a, an and the",
     "",
     ""),
    # ---- Unit 7 ----
    ("7a", 7, "7A", "Where I live", 56, [58, 59],
     "places in a town",
     "there is/there are",
     ""),
    ("7b", 7, "7B", "A new home", 58, [60, 61],
     "rooms and things in a house",
     "How much …? and How many …?; some, any, a",
     ""),
    ("7c", 7, "7C", "At the shops", 60, [62, 63],
     "shops; things to buy",
     "",
     "what sales assistants say; what customers say"),
    ("7d", 7, "7D", "What to wear", 62, [64, 65],
     "clothes; colours; plural nouns",
     "",
     ""),
    # ---- Unit 8 ----
    ("8a", 8, "8A", "The meeting", 64, [66, 67],
     "work",
     "Present Continuous: positive and negative, questions and short answers",
     ""),
    ("8b", 8, "8B", "It's snowing!", 66, [68, 69],
     "types of transport; travelling verbs and phrases",
     "Present Simple or Present Continuous",
     ""),
    ("8c", 8, "8C", "On the phone", 68, [70, 71],
     "talking on the phone",
     "",
     ""),
    ("8d", 8, "8D", "Life outdoors", 70, [72, 73],
     "indoor and outdoor activities; adjectives and adverbs",
     "",
     ""),
    # ---- Unit 9 ----
    ("9a", 9, "9A", "Holiday South Africa", 72, [74, 75],
     "holiday activities",
     "infinitive of purpose",
     ""),
    ("9b", 9, "9B", "A trip to Egypt", 74, [76, 77],
     "natural places",
     "comparatives",
     ""),
    ("9c", 9, "9C", "A day out", 76, [78, 79],
     "animals",
     "",
     "deciding what to do"),
    ("9d", 9, "9D", "Time for a change", 78, [80, 81],
     "verb patterns (like doing, would like to do, etc.)",
     "",
     ""),
    # ---- Unit 10 ----
    ("10a", 10, "10A", "Stay fit and healthy", 80, [82, 83],
     "verb phrases; frequency expressions",
     "imperatives; should/shouldn't",
     ""),
    ("10b", 10, "10B", "What's she like?", 82, [84, 85],
     "appearance; character",
     "questions with like",
     ""),
    ("10c", 10, "10C", "I feel ill", 84, [86, 87],
     "health problems; treatment",
     "",
     "talking about health"),
    ("10d", 10, "10D", "Winter blues", 86, [88, 89],
     "seasons; weather; word building",
     "",
     ""),
    # ---- Unit 11 ----
    ("11a", 11, "11A", "Happy New Year!", 88, [90, 91],
     "New Year's resolutions",
     "be going to (1): positive, negative and Wh- questions",
     ""),
    ("11b", 11, "11B", "No more exams!", 90, [92, 93],
     "studying",
     "be going to or might; be going to (2): yes/no questions and short answers",
     ""),
    ("11c", 11, "11C", "Directions", 92, [94, 95],
     "directions; asking for and giving directions",
     "",
     ""),
    ("11d", 11, "11D", "An invitation", 94, [96, 97],
     "collocations",
     "",
     ""),
    # ---- Unit 12 (ima samo A, B, C) ----
    ("12a", 12, "12A", "It's a world record", 96, [98, 99],
     "big and small numbers",
     "superlatives",
     ""),
    ("12b", 12, "12B", "Have you ever … ?", 98, [100, 101],
     "past participles",
     "Present Perfect: positive and negative; Have you ever ... ? questions and short answers",
     ""),
    ("12c", 12, "12C", "See you soon!", 100, [102, 103],
     "things and places at an airport",
     "",
     "at the airport; saying goodbye"),
]

EP_PDF_PAGE = {
    1: 117, 2: 118, 3: 119, 4: 120, 5: 121, 6: 122,
    7: 123, 8: 124, 9: 125, 10: 126, 11: 127, 12: 128,
}

# Srpski rezime + prioriteti po lekcijama (po sadržaju iz knjige)
SR: dict[str, dict[str, object]] = {
    "1a": dict(
        summary_sr=(
            "Predstavljanje sebe i drugih ljudi: pozdravi (Hello/Hi), pitanja o poreklu "
            "i nacionalnosti, glagol be u potvrdnoj rečenici i sa Wh- pitanjima. "
            "Vežbaš lične zamenice (I, you, he, she, we, they) i pridevsku formu prisvajanja (my, your, his, her, our, their)."
        ),
        priorities_sr=[
            "Skraćenice be: I'm, You're, He's, She's, We're, They're (audio drill).",
            "Razlika subject vs possessive: he ↔ his, she ↔ her, they ↔ their.",
            "Wh- pitanja: Where are you from? — pravilan red reči.",
        ],
    ),
    "1b": dict(
        summary_sr=(
            "Razgovor o poslovima i zanimanjima. Učiš kada ide a, a kada an pred zanimanjima "
            "(po prvom zvuku, ne slovu) i kako da postaviš negaciju i Yes/No pitanja sa be."
        ),
        priorities_sr=[
            "a + suglasnički zvuk, an + samoglasnički (an engineer, a university).",
            "isn't / aren't / I'm not — kratki oblik u govoru i pisanju.",
            "Kratki odgovori: Yes, I am. / No, I'm not.",
        ],
    ),
    "1c": dict(
        summary_sr=(
            "Lični podaci i brojevi 20–100 — popunjavanje obrasca (ime, prezime, adresa, broj telefona, e‑mail). "
            "Real World deo uči te kako da pristojno tražiš da neko ponovi (Sorry? / Could you say that again, please?)."
        ),
        priorities_sr=[
            "Razlika u akcentu: thirteen × thirty, fourteen × forty.",
            "Diktiranje broja telefona: 0 = oh, 11 = double one.",
            "How do you spell …? — sricanje slov po slovo.",
        ],
    ),
    "1d": dict(
        summary_sr=(
            "Lične stvari (wallet, keys, umbrella…) i kako se gradi množina (-s, -es, -ies + nepravilna kao men, women, children, people, teeth). "
            "Pokazne reči: this/that za jedninu, these/those za množinu, „here“ vs „there“."
        ),
        priorities_sr=[
            "Pravopis množine: -y → -ies (diary → diaries), -ch/-ss/-x/-sh → -es.",
            "Nepravilna množina: man → men, woman → women, child → children, person → people, tooth → teeth.",
            "Šablon: What's this/that in English? · What are these/those?",
        ],
    ),
    "2a": dict(
        summary_sr=(
            "Pridevi za stvari koje imamo (new/old, cheap/expensive, big/small...) i njihov red u rečenici (ispred imenice ili posle be). "
            "Učiš have got u potvrdnoj, odričnoj formi i pitanjima — britanska varijanta za posedovanje."
        ),
        priorities_sr=[
            "Pridev pre imenice: a small bag · Pridev posle be: It's small.",
            "very + adjective (very expensive, very late).",
            "Have you got …? → Yes, I have. / No, I haven't.",
        ],
    ),
    "2b": dict(
        summary_sr=(
            "Porodica (mother, father, husband, wife, brother, sister, son, daughter, parents, grandparents, cousin, aunt, uncle, grandchildren). "
            "Posesivni 's za pripadanje (Pam's sister) i razlika 's = is / 's = has / 's = pripadnost."
        ),
        priorities_sr=[
            "Apostrof + s: Tom's car (Tomov auto), Pam's husband.",
            "Razlikuj He's a doctor (= is) od He's got a car (= has) od Tom's car (= pripadnost).",
            "Plural posesiv: my parents' house (apostrof posle s).",
        ],
    ),
    "2c": dict(
        summary_sr=(
            "Vreme i novac. Kazivanje sata na britanski način (quarter past, half past, twenty to). "
            "Cene u funtama/evrima i Real World scena: kupovina karata u bioskopu (Can I have two tickets, please?)."
        ),
        priorities_sr=[
            "What time is it? / What's the time, please? / Have you got the time?",
            "Past = posle, To = pre punog sata: ten past nine, twenty to eight.",
            "Učenje fraza: How much is that? · Here you are. · You're welcome.",
        ],
    ),
    "2d": dict(
        summary_sr=(
            "Stvari u kući (sofa, mirror, lamp, bookcase…) i prepozicije mesta. "
            "Vežbaš gde je nešto smešteno: in / on / by / under / behind / in front of."
        ),
        priorities_sr=[
            "Kontrast in the box × on the table × under the chair.",
            "Whose …? + odgovor sa 's: Whose phone is this? It's Nick's.",
            "Pitanje Where's …? za singular i Where are …? za plural.",
        ],
    ),
    "3a": dict(
        summary_sr=(
            "Dnevna rutina (get up, have breakfast, leave home, start work, finish work, get home, go to bed). "
            "Present Simple u potvrdi i Wh- pitanjima za I/you/we/they — vremenske odredbe za doba dana."
        ),
        priorities_sr=[
            "Wh- + do + subjekat + infinitiv: What time do you get up?",
            "Glagol stoji u baznom obliku za I/you/we/they (bez -s).",
            "Vremenske fraze: in the morning, in the afternoon, in the evening, at night.",
        ],
    ),
    "3b": dict(
        summary_sr=(
            "Slobodno vreme (stay in, go out, eat out, go shopping, watch TV, phone friends…). "
            "Negacija Present Simple sa don't i Yes/No pitanja Do you …? — uz vremenske fraze on/in/at/every."
        ),
        priorities_sr=[
            "don't + bazni glagol: I don't watch TV every day.",
            "on Mondays, in the morning, at the weekend, every week — kog predloga sa kom rečju.",
            "Slušanje slabe forme: Do you /djə/ go out a lot?",
        ],
    ),
    "3c": dict(
        summary_sr=(
            "Posebni datumi (rođendani, Nova godina, godišnjice, venčanja). Meseci i datumi rednim brojevima "
            "(the fifth of May / May the fifth). Real World: predlozi sa Let's / Why don't we / What about …?"
        ),
        priorities_sr=[
            "Datum sa „of“: the third of June; piše se 3rd June ili June 3rd.",
            "Predlozi: Let's get her a book. / Why don't we get a DVD? / What about flowers?",
            "Reagovanje: Yes, that's a good idea. / Maybe. / I don't think so.",
        ],
    ),
    "3d": dict(
        summary_sr=(
            "Prilozi učestalosti (always, usually, often, sometimes, hardly ever, never) i njihov položaj u rečenici. "
            "Subjektne i objektne zamene (I ↔ me, he ↔ him, they ↔ them)."
        ),
        priorities_sr=[
            "Frekvencija ide POSLE be (She is always late) i PRE drugog glagola (I never watch TV).",
            "Object pronouns posle glagola/predloga: I see them. / Phone us.",
            "Pravac glagola: Subject + verb + Object: She calls me every day.",
        ],
    ),
    "4a": dict(
        summary_sr=(
            "Više aktivnosti u slobodnom vremenu (take photos, go cycling, play tennis, listen to music, go clubbing…). "
            "Present Simple u trećem licu jednine — dodaje -s/-es i koristi doesn't u negaciji."
        ),
        priorities_sr=[
            "Pravila pisanja: -ch/-sh/-x/-ss → +es; -y → -ies (study → studies); have → has.",
            "Linking u govoru: spaja se kraj reči i početak sledeće (and-all-of-the-people-are-nice).",
            "doesn't + bazni glagol: He doesn't like the weather.",
        ],
    ),
    "4b": dict(
        summary_sr=(
            "Šta voliš/ne voliš (love/like/don't mind/don't like/hate) + glagol-ing. "
            "Pitanja i kratki odgovori za he/she/it: Does he like …? — Yes, he does. / No, he doesn't."
        ),
        priorities_sr=[
            "Posle love/like/hate ide -ing oblik: I love cooking.",
            "Does + bazni glagol (bez -s) u pitanju: What does she watch?",
            "Kratak odgovor istog vremena: Yes, he does. / No, she doesn't.",
        ],
    ),
    "4c": dict(
        summary_sr=(
            "U restoranu/kafiću: hrana i piće (chicken salad, cheeseburger, sparkling water, espresso…). "
            "Pristojne molbe i ponude: Can I have …? · Could I have …? · Would you like …? — uz konobaricu/konobara."
        ),
        priorities_sr=[
            "Razlika molbe (Can/Could I have …?) i ponude (Would you like …?).",
            "Tipičan dijalog u kafeu: pozdrav → poručivanje → tražnje računa.",
            "Kratak odgovor na ponudu: Yes, please. / No, thanks.",
        ],
    ),
    "4d": dict(
        summary_sr=(
            "Doručak širom sveta — voće, pekarski proizvodi, mlečno, piće. "
            "Brojive vs nebrojive imenice i kada koristiš a/an, kada some, a kada nikakav član."
        ),
        priorities_sr=[
            "Brojivo (a banana, two bananas) × nebrojivo (some milk, a glass of milk).",
            "a/an = jedan/jedna pred brojivim; some = nešto pred množinom i nebrojivim.",
            "Bez člana (zero article) za uopštene navike: I have eggs for breakfast.",
        ],
    ),
    "5a": dict(
        summary_sr=(
            "Tri generacije: pridevi za karakter i lik (friendly, quiet, lively…) i godišta (in the 1970s). "
            "Past Simple od be: was / were u pozitivnoj, negativnoj i pitanju, sa kratkim odgovorima."
        ),
        priorities_sr=[
            "I/he/she/it was; you/we/they were; negacije wasn't / weren't.",
            "Was/Were + subjekat …? — Yes, I was. / No, they weren't.",
            "Vreme: yesterday, last week, in 1985, two years ago.",
        ],
    ),
    "5b": dict(
        summary_sr=(
            "Životne prekretnice: was born, started school, met, got married, had children, retired, died. "
            "Past Simple pravilnih (-ed) i nepravilnih glagola u potvrdi i Wh- pitanjima."
        ),
        priorities_sr=[
            "Pravilni: -ed (worked, lived, studied); izgovor /t/, /d/, /ɪd/.",
            "Najčešći nepravilni: be → was/were, have → had, go → went, do → did, get → got, make → made.",
            "Wh- pitanje: When did you start school? / Where did they meet?",
        ],
    ),
    "5c": dict(
        summary_sr=(
            "Pričanje o vikendu: aktivnosti, zanimljivost (sounded great!), follow-up pitanja. "
            "Real World fokus na pokazivanju zainteresovanosti u razgovoru."
        ),
        priorities_sr=[
            "Reagovanja: Really? / That's interesting. / Sounds great!",
            "Sledeća pitanja: What did you do? / Who did you go with? / How was it?",
            "Smenjivanje u dijalogu — slušanje pa pitanje, ne dva monologa.",
        ],
    ),
    "5d": dict(
        summary_sr=(
            "Takmičenja i pridevi sa stepenima jačine: very / really / quite / too. "
            "Razumeš nijansu: too znači negativno previše; quite je umereno; really = stvarno; very = jako."
        ),
        priorities_sr=[
            "too = previše (loše); very/really = jako (neutralno/pozitivno).",
            "Quite + adj: quite good = prilično dobro (BrE često blaže nego AmE).",
            "Pitanja za reakcije: How was it? — It was really good!",
        ],
    ),
    "6a": dict(
        summary_sr=(
            "Internet (search, browse, post, email…). Past Simple negacija i Yes/No pitanja sa did/didn't. "
            "Priča o osnivačima Google-a (Page i Brin) kao kontekst za vežbu prošlog vremena."
        ),
        priorities_sr=[
            "Did + subjekat + bazni glagol …? (Did you find it?)",
            "didn't + bazni glagol: They didn't like each other at first.",
            "Kratki odgovori: Yes, I did. / No, I didn't.",
        ],
    ),
    "6b": dict(
        summary_sr=(
            "Mobilni telefoni i televizori — kako se tehnologija menjala. Past time phrases (in 1995, ten years ago…). "
            "Modali can/can't (sad) i could/couldn't (u prošlosti) za sposobnosti i mogućnosti."
        ),
        priorities_sr=[
            "Modal + bazni glagol (bez to): I can swim. / He couldn't drive.",
            "Pitanje: Can you …? / Could you …? — bez do/did.",
            "Slušanje: razlikuj can /kən/ (slabo) od can't /kɑːnt/ (jako).",
        ],
    ),
    "6c": dict(
        summary_sr=(
            "Vesti i glagoli iz vesti (rescue, escape, find, kill, win, lose, hit). "
            "Real World: kako se prepričavaju vesti — Did you hear about …? / What happened?"
        ),
        priorities_sr=[
            "Past Simple + collocations vesti (a rescue team, a couple, a storm).",
            "Reagovanje na vest: Really? / That's terrible! / How awful!",
            "Slušanje sentence stress (3) — naglasak na ključnim informacijama.",
        ],
    ),
    "6d": dict(
        summary_sr=(
            "Mario Man — biografski profil tvorca igre. Članovi: a/an za prvo pominjanje i nepoznato; "
            "the za poznato/jedinstveno; bez člana za uopštena imena."
        ),
        priorities_sr=[
            "Prvo pominjanje a/an, dalje pominjanje the.",
            "the kod jedinstvenih: the sun, the internet, the news.",
            "Bez člana: meals, languages, school/work in general (go to school, have lunch).",
        ],
    ),
    "7a": dict(
        summary_sr=(
            "Mesta u gradu (post office, bank, library, museum, supermarket, cinema, park, station…). "
            "There is/There are za postojanje, sa negacijom i pitanjima."
        ),
        priorities_sr=[
            "There is + jednina; There are + množina.",
            "Negacije: There isn't / There aren't.",
            "Pitanja: Is there …? / Are there any …? / How many … are there?",
        ],
    ),
    "7b": dict(
        summary_sr=(
            "Sobe i nameštaj (kitchen, bathroom, fridge, cooker, washing machine, sofa, armchair…). "
            "Kvantifikatori: How much …? za nebrojivo, How many …? za brojivo; some/any/a u potvrdi/pitanju."
        ),
        priorities_sr=[
            "How much milk? × How many chairs?",
            "some u potvrdi i ponudi; any u pitanjima i negacijama.",
            "There's some / There isn't any / Are there any …?",
        ],
    ),
    "7c": dict(
        summary_sr=(
            "U prodavnicama: department store, butcher's, baker's, chemist's. "
            "Real World — fraze prodavca (Can I help you?) i kupca (I'm just looking; How much is it?)."
        ),
        priorities_sr=[
            "Politeness: Excuse me, please / I'd like …, please.",
            "Plaćanje: Can I pay by card / in cash?",
            "Vraćanje: Have you got this in a different size/colour?",
        ],
    ),
    "7d": dict(
        summary_sr=(
            "Garderoba i boje (shirt, T-shirt, jeans, dress, jacket, shoes, scarf…). "
            "Imenice koje uvek idu u množini: trousers, jeans, shorts, glasses, scissors."
        ),
        priorities_sr=[
            "Kažeš a pair of trousers/jeans (jedne pantalone).",
            "Boje + imenica: a red T-shirt, blue shoes.",
            "Slušanje: vokali /ɔː/ i /ɜː/ (HELP WITH PRONUNCIATION).",
        ],
    ),
    "8a": dict(
        summary_sr=(
            "Reči o poslu (have a meeting, write a report, send an email, take a break…). "
            "Present Continuous (am/is/are + glagol-ing) za radnje koje se dešavaju sada."
        ),
        priorities_sr=[
            "be + verb-ing: I'm waiting for a taxi.",
            "Pravopis -ing: write → writing, sit → sitting, lie → lying.",
            "Negacija/pitanje: She isn't working today. / Are they coming?",
        ],
    ),
    "8b": dict(
        summary_sr=(
            "Vrste prevoza i glagoli kretanja (drive, ride, fly, take the bus, walk). "
            "Razlika Present Simple (rutine, navike) i Present Continuous (sada, privremeno)."
        ),
        priorities_sr=[
            "Present Simple = obično/uvek/svaki dan. Present Continuous = baš sada/danas.",
            "Signalne reči: usually, every day, sometimes (PS) ↔ now, today, this week (PC).",
            "Stative verbs (know, like, want…) ne idu u Continuous.",
        ],
    ),
    "8c": dict(
        summary_sr=(
            "Telefonski razgovori — javljanje, traženje osobe, ostavljanje poruke. "
            "Real World fokus: Hello? · Can I speak to …? · Hold on, please. · Can I take a message?"
        ),
        priorities_sr=[
            "Skraćivanja u govoru: I'll call back, Speak to you later.",
            "Slušanje phone messages — vežbati slabe forme i linking.",
            "Vežbati šablon: pozdrav → ko zove → razlog → kraj.",
        ],
    ),
    "8d": dict(
        summary_sr=(
            "Aktivnosti u zatvorenom i napolju (read, sunbathe, play board games, go for a walk…). "
            "Razlika prideva (good) i priloga (well); nepravilan: good → well; fast → fast."
        ),
        priorities_sr=[
            "Pridev opisuje imenicu (a good driver), prilog opisuje glagol (drives well).",
            "Pravopis: -y → -ily (happy → happily), neki ostaju isti (fast/hard).",
            "Pažnja: He works hard (mnogo) ↔ He hardly works (jedva).",
        ],
    ),
    "9a": dict(
        summary_sr=(
            "Aktivnosti na odmoru (sunbathe, hire a car, go sightseeing, take photos…). "
            "Infinitive of purpose: koristimo to + glagol da kažemo zašto nešto radimo."
        ),
        priorities_sr=[
            "We went there to relax. / I'm calling to ask a question.",
            "Why …? — odgovor sa „To + glagol“.",
            "Ne mešaj: for + imenica (for a holiday), to + glagol (to relax).",
        ],
    ),
    "9b": dict(
        summary_sr=(
            "Prirodna mesta (sea, lake, mountain, forest, desert, river, beach, island). "
            "Komparacije pridevima — kraći -er, duži more, nepravilni (good/better, bad/worse)."
        ),
        priorities_sr=[
            "Jedan slog → -er (cold → colder); -y → -ier (happy → happier).",
            "Tri+ sloga → more (more beautiful, more interesting).",
            "Nepravilni: good → better, bad → worse, far → further.",
        ],
    ),
    "9c": dict(
        summary_sr=(
            "Životinje (lion, elephant, monkey, snake, bear…) i planiranje izleta. "
            "Real World: kako se odlučujemo: Why don't we …? · How about …? · Let's …"
        ),
        priorities_sr=[
            "Predloga forma: Let's + bazni glagol (Let's go).",
            "Slaganje/odbijanje: That's a great idea. / I'm not sure.",
            "Pitanje: What would you like to do? — Pristojno pitanje izbora.",
        ],
    ),
    "9d": dict(
        summary_sr=(
            "Šabloni glagola: like + -ing (volim raditi), would like + to + glagol (rado bih, jednom). "
            "Razlika u značenju: I like swimming (uopšte) ↔ I'd like to swim (sada/jednom)."
        ),
        priorities_sr=[
            "like / love / hate / enjoy + verb-ing.",
            "want / would like / need + to + verb (infinitive).",
            "I'd = I would (skraćeni oblik), pažnja na izgovor.",
        ],
    ),
    "10a": dict(
        summary_sr=(
            "Glagolske fraze za zdrav život (do exercise, eat well, sleep enough, drink water). "
            "Imperativi za savete (Eat more vegetables) i should/shouldn't za blaže preporuke."
        ),
        priorities_sr=[
            "Imperativ = bazni glagol bez subjekta: Eat fruit. / Don't smoke.",
            "should + bazni glagol: You should walk more.",
            "Frekvencija: once/twice a day, three times a week.",
        ],
    ),
    "10b": dict(
        summary_sr=(
            "Opis ljudi: izgled (tall, short, fair hair, blue eyes…) i karakter (kind, shy, generous, lazy…). "
            "Pitanja sa like — paziš na razliku What does he look like? × What is he like? × What does he like?"
        ),
        priorities_sr=[
            "What's he like? = kakav je (karakter).",
            "What does he look like? = kako izgleda.",
            "What does he like? = šta voli.",
        ],
    ),
    "10c": dict(
        summary_sr=(
            "Zdravstveni problemi (a cold, a cough, a headache, a sore throat, a stomach ache, flu) i lečenje (rest, take painkillers, see a doctor). "
            "Real World: kako da iskažeš empatiju (Oh dear / I hope you get better soon)."
        ),
        priorities_sr=[
            "I've got a + bolest: I've got a cold/headache.",
            "Saveti: You should rest. / You shouldn't go to work.",
            "Empatija: That's terrible! / Get well soon!",
        ],
    ),
    "10d": dict(
        summary_sr=(
            "Godišnja doba i vreme (sunny, cloudy, windy, raining, snowing). "
            "Word building: pridevi od imenica dodavanjem -y (sun → sunny, cloud → cloudy, wind → windy)."
        ),
        priorities_sr=[
            "Imenica + -y → pridev: sun/sunny, cloud/cloudy, fog/foggy.",
            "Pitanje: What's the weather like? — It's hot. / It's raining.",
            "Razlika spelling: hot → hotter (dupliranje), big → bigger.",
        ],
    ),
    "11a": dict(
        summary_sr=(
            "Novogodišnje odluke (lose weight, get fit, learn a language…). "
            "be going to (1) za planove i odluke unapred — potvrda, negacija i Wh- pitanja."
        ),
        priorities_sr=[
            "Form: be + going to + bazni glagol (I'm going to study harder).",
            "Negacija: I'm not going to …; They aren't going to …",
            "Wh- pitanje: What are you going to do? Where is she going to live?",
        ],
    ),
    "11b": dict(
        summary_sr=(
            "Studiranje i ispiti — going to ili might (kad nisi siguran). "
            "Yes/No pitanja: Are you going to …? Kratki odgovori i razlika u izvesnosti."
        ),
        priorities_sr=[
            "going to = sigurniji plan; might = možda (manje izvesno).",
            "Yes/No: Are you going to revise? — Yes, I am. / No, I'm not.",
            "might + bazni glagol (bez to): I might travel in summer.",
        ],
    ),
    "11c": dict(
        summary_sr=(
            "Ulice i upute kako stići (turn left/right, go straight on, take the second street, opposite, next to). "
            "Vežbe traženja i davanja uputstava na mapi."
        ),
        priorities_sr=[
            "Imperativ + on/along/past/across (Go past the bank, Cross the bridge).",
            "Pitanje za upute: Excuse me, how do I get to …?",
            "Lokacije: opposite, next to, between, on the corner of.",
        ],
    ),
    "11d": dict(
        summary_sr=(
            "Kolokacije za organizaciju događaja: have a party, send an invitation, get married, have a wedding. "
            "Vežbaš kako se ljudi pozivaju i kako se odgovara na pozivnicu."
        ),
        priorities_sr=[
            "have/hold + party; send + invitation; get + married/divorced.",
            "Linking review (slušanje povezivanja zvukova).",
            "Email pozivnica — kratak format sa datumom, mestom, RSVP.",
        ],
    ),
    "12a": dict(
        summary_sr=(
            "Veliki i mali brojevi (hundred, thousand, million; decimal point, decimals). "
            "Superlativi: -est za kraće prideve, the most za duže, nepravilni (good/best, bad/worst)."
        ),
        priorities_sr=[
            "the + superlativ + imenica: the highest mountain, the best film.",
            "Pravopis: long → longest, big → biggest, easy → easiest.",
            "Brojevi: 1.5 = one point five; 2,300 = two thousand three hundred.",
        ],
    ),
    "12b": dict(
        summary_sr=(
            "Past participle (treći oblik glagola) i Present Perfect za životna iskustva. "
            "Have you ever …? — Yes, I have. / No, I haven't (never)."
        ),
        priorities_sr=[
            "have/has + past participle: I've been to Italy.",
            "ever u pitanju, never u negaciji: I've never tried sushi.",
            "Pravilan PP = isto kao Past Simple (-ed); nepravilni: lista u dodatku knjige (be/been, do/done, go/been ili gone, see/seen…).",
        ],
    ),
    "12c": dict(
        summary_sr=(
            "Aerodrom (check-in, gate, boarding pass, passport, baggage, flight). "
            "Real World: kako se opraštamo (Have a safe trip, Keep in touch, See you soon)."
        ),
        priorities_sr=[
            "Funkcionalne fraze pri pozdravu: Have a safe trip! / Take care! / Keep in touch.",
            "Aerodromske obaveze: check in, go through security, board the plane.",
            "Pregled samoglasničkih zvukova (Help with Pronunciation).",
        ],
    ),
}

# ---------------------------------------------------------------------------

FOOTER_LINES = (
    "Cambridge University Press",
    "Vietata la vendita",
    "vendita e la diffusione",
)


def clean_text(t: str) -> str:
    out = []
    for ln in t.splitlines():
        s = ln.rstrip()
        if not s.strip():
            out.append("")
            continue
        if any(f in s for f in FOOTER_LINES):
            continue
        out.append(s)
    # collapse 3+ blank lines into 2
    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def read_pages(pdf_pages: list[int]) -> str:
    parts = []
    for n in pdf_pages:
        f = OCR_DIR / f"p{n:03d}.txt"
        if f.exists():
            parts.append(clean_text(f.read_text(encoding="utf-8")))
    return "\n\n— — —\n\n".join(parts)


SECTION_RE = re.compile(r"\b(\d{1,2})([A-D])\s*p\d{1,3}\b")


def slice_extra_practice(unit: int, code: str) -> str:
    page = OCR_DIR / f"p{EP_PDF_PAGE[unit]:03d}.txt"
    if not page.exists():
        return ""
    text = clean_text(page.read_text(encoding="utf-8"))
    # markeri kao "1A p8", "1B p10" ... + "Progress Portfolio"
    markers: list[tuple[int, str]] = []
    for m in SECTION_RE.finditer(text):
        markers.append((m.start(), f"{m.group(1)}{m.group(2)}"))
    pp_match = re.search(r"Progress Portfolio", text)
    if pp_match:
        markers.append((pp_match.start(), "PP"))
    markers.sort()
    if not markers:
        return text
    # nadji parče za zadati code
    for i, (idx, name) in enumerate(markers):
        if name == code:
            end = markers[i + 1][0] if i + 1 < len(markers) else len(text)
            return text[idx:end].strip()
    return ""


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    lessons = []
    for (lid, unit, code, title, book_p, pdf_pages, vocab_en, grammar_en, rw_en) in LESSON_MAP:
        sr = SR.get(lid, {"summary_sr": "", "priorities_sr": []})
        v = LESSONS_VOCAB.get(lid, {})
        lessons.append({
            "id": lid,
            "unit": unit,
            "code": code,
            "title_en": title,
            "book_page": f"p{book_p}",
            "pdf_pages": pdf_pages,
            "toc_vocab_en": vocab_en,
            "toc_grammar_en": grammar_en,
            "toc_rw_en": rw_en,
            "summary_sr": sr["summary_sr"],
            "priorities_sr": sr["priorities_sr"],
            "vocab": v.get("vocab", []),
            "phrases": v.get("phrases", []),
            "grammar_examples": v.get("grammar", []),
            "lesson_text": read_pages(pdf_pages),
            "extra_practice": {
                "n": unit,
                "sb_page_printed": f"p{114 + unit}",
                "ep_text": slice_extra_practice(unit, code),
            },
        })

    unit_tests_payload = []
    for unit_n in sorted(UNIT_TESTS.keys()):
        questions = UNIT_TESTS[unit_n]
        unit_tests_payload.append({
            "id": f"test-{unit_n}",
            "unit": unit_n,
            "title_sr": f"Test · Jedinica {unit_n}",
            "questions": questions,
        })

    payload = {
        "course": {
            "title": "face2face Elementary · 2nd edition",
            "notes_sr": (
                "Za svaku lekciju imaš ručno izvučen rečnik (English ↔ srpski), ključne fraze "
                "i gramatičke primere iz prvog zadatka i Real World/Help with Grammar boksova, "
                "uz srpski rezime i prioritete učenja. Posle svake jedinice imaš test od 10 pitanja "
                "sa instant proverom rezultata. Extra Practice je izdvojen iz dvostranice "
                "na kraju knjige po podlekcijama. Lekcija 12D ne postoji u knjizi (jedinica 12 ima samo A, B, C)."
            ),
        },
        "lessons": lessons,
        "unit_tests": unit_tests_payload,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_EMBED.write_text(
        "// Auto-generated — do not edit by hand.\n"
        "window.__LESSONS_DATA__ = " + json.dumps(payload, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print("Wrote", OUT_JSON, "lessons:", len(lessons))


if __name__ == "__main__":
    main()
