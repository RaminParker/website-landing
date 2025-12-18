# Spinfood Landing Page

## Übersicht

FastHTML-basierte Landing Page für Spinfood - eine Plattform für Running Dinner Events an deutschen Universitäten.

**Tech Stack:** Python, FastHTML, Uvicorn

## Projektstruktur

```
website-landing/
├── app.py              # Hauptanwendung (Routes, Server)
├── config.py           # Konfiguration & Konstanten
├── components.py       # UI-Komponenten
├── static/
│   ├── css/styles.css  # Alle Styles
│   └── js/main.js      # JavaScript (FAQ, Modal, etc.)
└── images/             # Statische Bilder
```

## Architektur

### Modulare Struktur

| Datei | Verantwortung |
|-------|---------------|
| `app.py` | Server-Setup, Routes, Logging |
| `config.py` | APP_TITLE, CURRENT_EVENTS, FAQ_LIST, CLASS-Dictionary |
| `components.py` | Alle UI-Komponenten (NavigationBar, HeroSection, etc.) |

### CSS-Klassen (Single Source of Truth)

Alle CSS-Klassennamen sind in `config.py` im `CLASS`-Dictionary definiert:
```python
from config import CLASS
cls=CLASS['navbar']  # statt cls="navbar"
```

## Workflows

### Server starten
```bash
conda activate landingpage_spinfood
python app.py
# -> http://localhost:5001
```

### Content ändern
- Events: `config.py` → `CURRENT_EVENTS`
- FAQs: `config.py` → `FAQ_LIST`
- Sponsoren: `config.py` → `SPONSOR_LIST`

### Neuen Abschnitt hinzufügen
1. Komponente in `components.py` erstellen
2. CSS-Klassen in `config.py` → `CLASS` hinzufügen
3. Styles in `static/css/styles.css` hinzufügen
4. Komponente in `app.py` → `get()` einbinden

## Wichtige Hinweise

- **Keine Inline-Styles** in Komponenten (außer dynamische Werte)
- **CLASS-Dictionary verwenden** für alle CSS-Klassennamen
- **Config-Änderungen** erfordern Server-Neustart
- **CSS/JS-Änderungen** werden bei Page-Refresh geladen
