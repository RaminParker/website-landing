# Spinfood Landing Page

Landing Page für Spinfood - eine Plattform für Running Dinner Events an deutschen Universitäten.

**Tech Stack:** Python, FastHTML, Uvicorn

## Projektstruktur

```
website-landing/
├── app.py                # Server-Setup, Routes, Logging
├── config.py             # Konfiguration, Content-Daten, CSS-Klassen
├── components.py         # UI-Komponenten (HeroSection, FAQSection, etc.)
├── static/
│   ├── css/styles.css    # Alle Styles (CSS Variables, responsive)
│   └── js/main.js        # JavaScript (FAQ-Toggle, Modal, Video-Loading)
├── images/               # Statische Bilder (Team, Uni-Logos, Social Icons)
└── videos/landingpage/   # Hero-Video (WebM, MP4, Thumbnails)
```

## Quick Start

```bash
conda activate landingpage_spinfood
python app.py
# -> http://localhost:5001
```

Alternativ mit pip:
```bash
pip install -r requirements.txt
python app.py
```

## Architektur

| Datei | Verantwortung |
|-------|---------------|
| `app.py` | FastHTML-App, Routes (`/`, `/agb`, `/impressum`, `/datenschutz`, `/ueber-uns`) |
| `config.py` | Single Source of Truth: Events, FAQs, Sponsoren, Legal Pages, Über uns, CSS-Klassen |
| `components.py` | Wiederverwendbare UI-Komponenten |

**Prinzip:** Alle CSS-Klassennamen sind im `CLASS`-Dictionary in `config.py` definiert. Content-Änderungen erfordern nur Anpassungen in `config.py`.

Detaillierte Dokumentation: [.claude/CLAUDE.md](.claude/CLAUDE.md)

## Konfiguration

In `config.py`:

```python
# Feature Flags
USE_HERO_VIDEO = True     # False = statischer Placeholder
HERO_VIDEO_HEIGHT = 600   # Video-Höhe in Pixel
CURRENT_YEAR = 2026       # Für Copyright & Last-Updated

# Content
CURRENT_EVENTS = [...]       # Running Dinner Events
EVENT_ACCENT_COLORS = [...]  # Farben für Event-Karten
FAQ_LIST = [...]             # Häufige Fragen
SPONSOR_LIST = [...]         # Partner & Sponsoren (icon/path, name, type, url)

# Legal Pages
AGB_LIST = [...]             # AGB-Dokumente
IMPRESSUM_DATA = {...}       # Impressum-Daten
DATENSCHUTZ_DATA = {...}     # Datenschutz-Daten

# Über uns Page
TEAM_MEMBERS = [...]         # Team-Mitglieder (Name, Rolle, Bild)
UEBER_UNS_DATA = {...}       # Philosophie, Kooperationen, Fachschaften
```

## Deployment

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```
