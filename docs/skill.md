# Drosselau Häuserbilder — Arbeitsanweisung

Ein Katalogbild pro Ort, in der eingefrorenen Reihenfolge. Nie mehr als drei Bilder am Stück, dann warten.

## Quelle der Wahrheit (zuerst lesen)

1. `docs/orte/Drosselau_Orte_Final_2512.md` — jeder Ort, Bezirksregeln, Verbote.
2. `docs/queue.md` — nummerierte Packs und 10-Prozent-QA-Stopps.
3. `docs/prompt-template.md` — wie ein Vollprompt gebaut wird.
4. `docs/qa.md` — Fehlerliste bei jedem QA-Stopp.

Kein Gebäude erfinden, das nicht in Orte_Final steht. Keine Bezirkstoken mischen.

## Hartes visuelles Gesetz

- 2512 IC Empire-Flecken, etwa 800 Seelen. Bedeckt, nasse Wolle, Matsch, Holzrauch.
- Kein Dom, kein Marmor-Hospiz, keine geschlossene Morr-Tür, kein lateinisches Kruzifix als Hauptzeichen, kein lesbares Wort WARHAMMER auf Stein.
- Katalogmarke nur am unteren Rand (Nummer oder unnummerierter Name).
- Ganzes Objekt im Bild. Augenhohe Dreiviertelansicht, etwa 35 mm.
- Kultzeichen nur am richtigen Ort (Hammer+Komet auf 18 und Wegstock; offenes Portal + Rabe + dunkle Rosen auf 56/Garten; X und Würfel auf 6; versteckte Schreinsprache auf 57; Taube/Herz abgenutzt auf Shallya).

## Ein Pack (nie überspringen)

1. Die nächsten drei IDs aus `docs/queue.md` nehmen.
2. Für jede ID den Bezirksblock + die Ortszeile aus Orte_Final in einen Vollprompt nach `docs/prompt-template.md` kopieren.
3. Alle drei vollständigen Prompts im Chat zeigen (deutsche Einleitung, englischer Promptkörper).
4. Genau drei Bilder erzeugen (Querformat), nach `katalog_fotos/<ID>.jpg` kopieren.
5. Sortiertes PDF mit `python3 scripts/build_bildkatalog.py` neu bauen.
6. Danach dreizeiliger Selbstcheck je ID (Bezirk ok / Objekt ok / Verbotenes vorhanden?).
7. Stoppen. Auf den Nutzer warten. Kein nächstes Pack beginnen.

## Qualität — alle 10 Prozent

Queue-Länge 117 Orte. Zehn Prozent sind 12 Orte (vier Packs).

Bei Packs 4, 8, 12, 16, 20, 24, 28, 32, 36, 39 (Ende) QA-Stopp statt sofort nächstes Pack:

1. Orte_Final für die letzten 12 IDs erneut lesen.
2. Jedes Bild gegen `docs/qa.md` prüfen.
3. Fehler in einer kurzen Tabelle (ID, Fehler, Fix).
4. Bei Hard-Law-Fehler nur die kaputten IDs neu erzeugen.
5. Nicht weiter, bis der Nutzer QA oder Fixes akzeptiert.

## Bereits erledigt (nicht wiederholen, außer auf Anweisung)

- 18 Sigmarstempel (behalten; nie wieder das Wort WARHAMMER auf den Sturz).
- Shallya-Altar.
- 56 Morr-Kapelle (beim ersten QA oder Morr-Pack neu erzeugen — aktueller Stand hat Türflügel, verboten).

Start bei Pack 1 (`1 · 70 · 2`), nicht beim Kult-Trio.

## Fortschrittslog

Eine Zeile pro fertigem Pack nach `logs/Drosselau_Bilder_Log.md`:

`Pack N | IDs | Datum | QA? | Notizen`
