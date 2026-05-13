#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jednokratno (Mac): ako su slike u site/quest-image/ kao 01.heic … 34.heic (ili jpg/png),
pokušava OCR (Tesseract, eng) i upisuje prepoznat tekst u site/quest-image-data.json
u polje "answer" za svaki broj gde postoji slika.

Posle pokretanja UVEK proveri JSON — OCR često pogreši, spoji pitanje i odgovor na jednoj slici, itd.

Pokretanje iz foldera site:
  python3 scripts/ocr_quest_images_to_json.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
IMG_DIR = SITE / "quest-image"
JSON_PATH = SITE / "quest-image-data.json"
EXTS = (".heic", ".HEIC", ".jpg", ".jpeg", ".png", ".webp")


def find_image(n: int) -> Path | None:
    pad = f"{n:02d}"
    for ext in EXTS:
        p = IMG_DIR / f"{pad}{ext}"
        if p.is_file():
            return p
    return None


def raster_for_tesseract(src: Path) -> Path:
    suf = src.suffix.lower()
    if suf in (".jpg", ".jpeg", ".png", ".webp"):
        return src
    if sys.platform != "darwin":
        print(
            f"Upozorenje: HEIC ({src.name}) — konverzija 'sips' radi samo na macOS. "
            f"Konvertuj ručno u PNG/JPG ili pokreni skriptu na Macu.",
            file=sys.stderr,
        )
        return src
    out = Path(tempfile.mkdtemp(prefix="qiocr_")) / "page.png"
    r = subprocess.run(
        ["sips", "-s", "format", "png", str(src), "--out", str(out)],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0 or not out.is_file():
        raise RuntimeError(f"sips ne može HEIC → PNG: {src}\n{r.stderr}")
    return out


def ocr_image(img: Path) -> str:
    r = subprocess.run(
        ["tesseract", str(img), "stdout", "-l", "eng", "--psm", "3"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return ""
    lines = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    return " ".join(lines)


def main() -> int:
    if not JSON_PATH.is_file():
        print("Nedostaje", JSON_PATH, file=sys.stderr)
        return 1
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("JSON mora biti niz objekata.", file=sys.stderr)
        return 1

    updated = 0
    missing_img: list[int] = []

    for item in data:
        if not isinstance(item, dict) or "n" not in item:
            continue
        n = int(item["n"])
        src = find_image(n)
        if src is None:
            missing_img.append(n)
            continue
        try:
            work = raster_for_tesseract(src)
            text = ocr_image(work)
            if text:
                item["answer"] = text
                updated += 1
                print(f"OK #{n} ← {src.name} ({len(text)} znakova)")
            else:
                print(f"Prazan OCR #{n} ← {src.name}", file=sys.stderr)
        except (OSError, RuntimeError, subprocess.CalledProcessError) as e:
            print(f"Greška #{n} ({src.name}): {e}", file=sys.stderr)

    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nGotovo. Ažurirano odgovora iz slika: {updated} / {len(data)}.")
    if missing_img:
        print("Bez slike (ostaje stari answer u JSON):", ", ".join(map(str, sorted(missing_img))))
    print("Proveri i ispravi quest-image-data.json ručno gde OCR smeta.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
