# Zootopia mit API

## Projektbeschreibung

Zootopia erzeugt aus einem Tiernamen eine Webseite mit Informationen zu den
passenden Tieren. Die Daten kommen live von der
[Animals API von API Ninjas](https://api-ninjas.com/api/animals).

Statt Tierinformationen von Hand zusammenzusuchen, gibt man einen Namen ein
und erhält eine fertige HTML-Seite mit einer Karte pro Tier: Ernährung,
Lebensraum, Typ, Temperament und Hauttyp. Gibt es zu dem Namen kein Tier,
zeigt die Seite einen entsprechenden Hinweis.

Zielgruppe sind Tierinteressierte, die sich schnell einen Überblick über eine
Tierart verschaffen möchten, und Python-Einsteiger, die an einem kleinen
Beispiel sehen wollen, wie man eine API abruft und daraus HTML erzeugt.

Das Programm besteht aus zwei Teilen:

- `data_fetcher.py` ruft die Tierdaten von der API ab.
- `animals_web_generator.py` fragt nach dem Tiernamen und erzeugt daraus die
  Webseite `animals.html` auf Basis von `animals_template.html`.

## Nutzung

### Installation

```bash
pip install -r requirements.txt
```

### Konfiguration

Für die API wird ein kostenloser API-Key von
[api-ninjas.com](https://api-ninjas.com) benötigt. Lege im Projektverzeichnis
eine Datei `.env` an:

```
API_KEY = "dein-api-key"
URL = "https://api.api-ninjas.com/v1/animals"
```

### Programm starten

```bash
python3 animals_web_generator.py
```

Beispiel:

```
Please enter an animal: Fox
Website was successfully generated to the file animals.html.
```

Anschließend `animals.html` im Browser öffnen.
