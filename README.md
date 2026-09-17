# Drosselau Häuserbilder

Photorealistischer Gebäudekatalog des Marktfleckens **Drosselau**, Reich, 2512 IC.

117 Orte, Bezirk für Bezirk, Packs zu je drei Bildern, Qualitätsstopp alle 12 Orte (10 %).

> Platzhalterstand. Die kanonische Ortsliste (`docs/orte/Drosselau_Orte_Final_2512.md`) wird nachgeliefert. Bis dahin gilt die Queue und das Prompt-Template als Arbeitsvertrag.

## Was hier liegt

| Pfad | Rolle |
| --- | --- |
| `docs/skill.md` | Arbeitsanweisung für die Bildfolge |
| `docs/queue.md` | 39 Packs, QA-Stopps |
| `docs/prompt-template.md` | Vollprompt, nicht kürzen |
| `docs/qa.md` | Hard-Fail / Soft-Fail |
| `docs/orte/` | Quelltext der 117 Orte (Platzhalter) |
| `docs/bezirke.md` | Stoffgesetze je Bezirk |
| `katalog_fotos/` | Fertige Katalog-JPGs (`<ID>.jpg`) |
| `scripts/build_bildkatalog.py` | Sortiertes PDF aus den JPGs |
| `logs/Drosselau_Bilder_Log.md` | Pack-Protokoll |

## Visuelles Gesetz (kurz)

- Reich-Flecken, ca. 800 Seelen. Bedeckt, nasse Wolle, Matsch, Holzrauch.
- Kein Dom, kein Marmor-Hospiz, keine geschlossene Morr-Tür, kein lateinisches Kruzifix als Hauptzeichen, kein lesbares Wort `WARHAMMER` auf Stein.
- Katalogmarke nur am unteren Bildrand (Nummer oder unnummerierter Name).
- Ganzes Objekt im Bild. Augenhohe Dreiviertelansicht, etwa 35 mm.
- Kultzeichen nur am richtigen Ort.

## Ablauf eines Packs

1. Nächste drei IDs aus `docs/queue.md`.
2. Bezirk + Ortszeile in das Template gießen.
3. Genau drei Bilder erzeugen, nach `katalog_fotos/<ID>.jpg` legen.
4. PDF neu bauen: `python3 scripts/build_bildkatalog.py`.
5. Dreizeiliger Selbstcheck je ID.
6. Stoppen. Warten.

Start: **Pack 1** — `1 · 70 · 2`.

## Lizenz / IP

Eigenes Material (Prompts, Queue, Pipeline, Originalbeschreibungen) unter MIT, soweit nicht anders gekennzeichnet.

Warhammer Fantasy, das Imperium und zugehörige Namen sind geistiges Eigentum von Games Workshop. Dieses Repo ist ein inoffizielles Fanprojekt, nicht lizenziert, nicht offiziell.
