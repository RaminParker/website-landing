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
├── images/               # Statische Bilder (Team, Uni-Logos)
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
| `app.py` | FastHTML-App, statische Routen, Page-Composition |
| `config.py` | Single Source of Truth: Events, FAQs, Sponsoren, CSS-Klassen |
| `components.py` | Wiederverwendbare UI-Komponenten |

**Prinzip:** Alle CSS-Klassennamen sind im `CLASS`-Dictionary in `config.py` definiert. Content-Änderungen erfordern nur Anpassungen in `config.py`.

## Konfiguration

In `config.py`:

```python
# Feature Flags
USE_HERO_VIDEO = True     # False = statischer Placeholder
HERO_VIDEO_HEIGHT = 600   # Video-Höhe in Pixel

# Content
CURRENT_EVENTS = [...]    # Running Dinner Events
FAQ_LIST = [...]          # Häufige Fragen
SPONSOR_LIST = [...]      # Partner & Sponsoren
```

## Deployment

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```
