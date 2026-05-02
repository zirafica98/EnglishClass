#!/usr/bin/env python3
"""OCR svaku stranicu SB.pdf u tekstualne fajlove ocr_pages/pNNN.txt."""
from __future__ import annotations

import io
import sys
import time
from pathlib import Path

import fitz  # PyMuPDF
import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "docs" / "SB.pdf"
OUT_DIR = ROOT / "ocr_pages"


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    doc = fitz.open(PDF)
    n = len(doc)
    t0 = time.time()
    for i in range(n):
        out = OUT_DIR / f"p{i + 1:03d}.txt"
        if out.exists() and out.stat().st_size > 30:
            continue  # već uradjeno
        pix = doc[i].get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang="eng")
        out.write_text(text, encoding="utf-8")
        elapsed = time.time() - t0
        print(f"{i + 1:3d}/{n}  {len(text):5d} chars  | t={elapsed:5.1f}s", flush=True)
    print("Gotovo.")


if __name__ == "__main__":
    main()
