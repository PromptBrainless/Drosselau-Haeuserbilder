#!/usr/bin/env python3
"""Baue ein sortiertes PDF aus katalog_fotos/ in Queue-Reihenfolge.

Platzhalter: läuft auch ohne Bilder (erzeugt Hinweisseite).
Echte Montage braucht pillow + reportlab.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "docs" / "queue.md"
FOTOS = ROOT / "katalog_fotos"
OUT = ROOT / "output" / "Drosselau_Bildkatalog.pdf"


def parse_queue_ids(text: str) -> list[str]:
    ids: list[str] = []
    for line in text.splitlines():
        if not line.strip().startswith("- Pack"):
            continue
        _, rest = line.split(":", 1)
        for token in rest.replace("·", " ").split():
            token = token.strip()
            if token:
                ids.append(token)
    return ids


def main() -> None:
    ids = parse_queue_ids(QUEUE.read_text(encoding="utf-8"))
    present = []
    missing = []
    for i in ids:
        jpg = FOTOS / f"{i}.jpg"
        if jpg.exists():
            present.append(i)
        else:
            missing.append(i)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "Drosselau Bildkatalog — Platzhalterlauf",
        f"Queue-IDs: {len(ids)}",
        f"Vorhanden: {len(present)}",
        f"Fehlend: {len(missing)}",
        "",
        "Vorhanden: " + ", ".join(present[:40]) if present else "Vorhanden: —",
        "Nächste fehlende: " + ", ".join(missing[:12]) if missing else "Vollständig.",
    ]
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas

        c = canvas.Canvas(str(OUT), pagesize=A4)
        width, height = A4
        y = height - 72
        for line in report:
            c.drawString(72, y, line[:110])
            y -= 18
        c.save()
        print(f"geschrieben: {OUT}")
    except ImportError:
        stub = OUT.with_suffix(".txt")
        stub.write_text("\n".join(report) + "\n", encoding="utf-8")
        print(f"reportlab fehlt — Stub: {stub}")


if __name__ == "__main__":
    main()
