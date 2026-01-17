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
│   └── js/main.js      # JavaScript (FAQ, Modal, Video-Loading)
├── images/             # Statische Bilder
└── videos/landingpage/ # Hero-Video (WebM, MP4, Thumbnails)
```

## Architektur

### Modulare Struktur

| Datei | Verantwortung |
|-------|---------------|
| `app.py` | Server-Setup, Routes (`/`, `/agb`, `/impressum`, `/datenschutz`), Logging |
| `config.py` | APP_TITLE, CURRENT_EVENTS, FAQ_LIST, AGB_LIST, IMPRESSUM_DATA, DATENSCHUTZ_DATA, EVENT_ACCENT_COLORS, CLASS-Dictionary |
| `components.py` | Alle UI-Komponenten (NavigationBar, HeroSection, LegalPageSection, AGBPageContent, ImpressumPageContent, DatenschutzPageContent, etc.) |
| `environment_dev.yml` | Conda-Umgebung Definition mit allen Python-Dependencies |

### CSS-Klassen (Single Source of Truth)

Alle CSS-Klassennamen sind in `config.py` im `CLASS`-Dictionary definiert:
```python
from config import CLASS
cls=CLASS['navbar']  # statt cls="navbar"
```

Das Dictionary ist in logische Gruppen unterteilt:
- **Layout**: `container`, `section`, `bg_white`, `bg_gray`, `cards_grid`
- **Typography**: `section_title`, `section_subtitle`
- **Navigation**: `navbar`, `navbar_logo`, `navbar_menu`, etc.
- **Hero**: `hero`, `hero_title`, `hero_buttons`, etc.
- **Components**: `step_card`, `benefit_card`, `event_card`, `faq_item`, etc.
- **Child Pages**: `agb_page`, `agb_block`, `agb_section`, `agb_nav`, `impressum_*`, `datenschutz_*`, etc.
- **Utility Classes**: `section_emoji`, `problem_statement`, `solution_title`, `pre_line`, etc.

### Dynamische Inline-Styles

Einzige Ausnahme für Inline-Styles sind **dynamische Werte**, z.B.:
```python
# EventCard - Akzentfarbe wird zur Laufzeit gesetzt
style = f"border-left-color: {accent_color};" if accent_color else ""

# Impressum - Telefonnummer-Reveal (Anti-Spam)
onclick="this.textContent='0160 5819759'; this.style.cursor='default';"
```

## Workflows

### Server starten

**WICHTIG:** Der Server kann nur gestartet werden, wenn die Conda-Umgebung zuvor aktiviert wurde!

```bash
# Conda-Umgebung aktivieren (erforderlich!)
conda activate landingpage_spinfood

# Server starten
python app.py
# -> http://localhost:5001
```

Die Conda-Umgebung `landingpage_spinfood` ist in [environment_dev.yml](environment_dev.yml) definiert und enthält:
- Python 3.11
- python-fasthtml
- uvicorn[standard]
- python-multipart, httpx, jinja2, python-dotenv, monsterui

Falls die Umgebung noch nicht existiert:
```bash
conda env create -f environment_dev.yml
```

### Content ändern
- Events: `config.py` → `CURRENT_EVENTS`
- Event-Akzentfarben: `config.py` → `EVENT_ACCENT_COLORS`
- FAQs: `config.py` → `FAQ_LIST`
- Sponsoren: `config.py` → `SPONSOR_LIST` (Format: icon/image_path, name, type, url)
- AGBs: `config.py` → `AGB_SPINFOOD`, `AGB_GIESSEN_KOCHT`, `AGB_LIST`
- Impressum: `config.py` → `IMPRESSUM_DATA`
- Datenschutz: `config.py` → `DATENSCHUTZ_DATA`
- **Jahreszahl (Copyright & Last-Updated)**: `config.py` → `CURRENT_YEAR` (wird automatisch in Footer, Impressum, AGB und Datenschutz verwendet)

### Hero-Video konfigurieren
In `config.py`:
```python
USE_HERO_VIDEO = True   # False = statischer Placeholder
HERO_VIDEO_HEIGHT = 600 # Höhe in Pixel (Standard: 600)
```

Video-Dateien in `videos/landingpage/`:
- `optim.webm` / `optim.mp4` - Video-Formate
- `thumbnail@low.png` - Blur-Placeholder (12KB, lädt sofort)

### Neuen Abschnitt hinzufügen
1. Komponente in `components.py` erstellen
2. CSS-Klassen in `config.py` → `CLASS` hinzufügen
3. Styles in `static/css/styles.css` hinzufügen
4. Komponente in `app.py` → `get()` einbinden

### Neue Child-Page hinzufügen
1. Content-Daten in `config.py` definieren (z.B. Dictionary-Struktur)
2. CSS-Klassen in `config.py` → `CLASS` hinzufügen
3. Komponenten in `components.py` erstellen
4. Neue Route in `app.py` mit `@rt("/pagename")` hinzufügen
5. Styles in `static/css/styles.css` hinzufügen
6. Links im Footer oder Navigation anpassen

### Generische Legal Page Section

Alle rechtlichen Seiten (AGB, Impressum, Datenschutz) nutzen die generische `LegalPageSection()` Komponente:
```python
# components.py
def LegalPageSection(heading, content, css_prefix, preserve_linebreaks=False):
    """Generische Section für AGB/Impressum/Datenschutz"""
```

Beispiel AGB-Page (`/agb`):
```python
# config.py - Content-Struktur
AGB_EXAMPLE = {
    'id': 'example',
    'title': 'Titel - Untertitel',
    'intro': 'Einleitungstext...',
    'sections': [
        ('§1 Überschrift', 'Inhalt des Paragraphen...'),
    ],
    'last_updated': f'Januar {CURRENT_YEAR}'
}
AGB_LIST = [AGB_EXAMPLE]  # Alle AGBs hier auflisten
```

Beispiel Impressum-Page (`/impressum`):
```python
# config.py - Content-Struktur
IMPRESSUM_DATA = {
    'id': 'impressum',
    'title': 'Impressum',
    'intro': 'Angaben gemäß § 5 TMG',
    'sections': [
        ('Anbieter', 'Firmenname\nAdresse\n\nVertreten durch: ...'),
        ('Kontakt', 'Telefon: (anzeigen)\nE-Mail: kontakt@example.com'),
    ],
    'last_updated': f'Januar {CURRENT_YEAR}',
    'copyright': f'© {CURRENT_YEAR} Firmenname – Alle Rechte vorbehalten'
}
```

**Besonderheit Impressum:** Die Telefonnummer wird mit "(anzeigen)" versteckt und beim Klick sichtbar (Anti-Spam-Maßnahme). Die `ImpressumSection` Komponente erkennt automatisch "Telefon: (anzeigen)" und ersetzt es durch einen klickbaren Link.

Beispiel Datenschutz-Page (`/datenschutz`):
```python
# config.py - Content-Struktur
DATENSCHUTZ_DATA = {
    'id': 'datenschutz',
    'title': 'Datenschutz',
    'intro': 'Einleitungstext zur Datenschutzerklärung...',
    'sections': [
        ('Cookies', 'Informationen zu Cookies...'),
        ('Google Analytics', 'Informationen zu Google Analytics...'),
    ],
    'last_updated': f'Januar {CURRENT_YEAR}'
}
```

## Wichtige Hinweise

- **Keine Inline-Styles** in Komponenten (außer dynamische Werte)
- **CLASS-Dictionary verwenden** für alle CSS-Klassennamen
- **Config-Änderungen** erfordern Server-Neustart
- **CSS/JS-Änderungen** werden bei Page-Refresh geladen

## CSS-Struktur (styles.css)

Die CSS-Datei ist in nummerierte Abschnitte gegliedert:

1. CSS Variables & Root Styles
2. Global Styles & Scroll Animations
3. Layout & Container Classes
4. Typography
5. Navigation Bar
6. Hero Section
7. Step Cards (How It Works)
8. Benefit Cards
9. Event Cards
10. FAQ Section
11. Testimonial Cards
12. CTA Section
13. Team/About Section
14. Partner Section
15. Sponsors Section
16. Organizer Section
17. Footer Section
18. Modal (Contact)
19. Utility Classes (inkl. `.pre-line` für Zeilenumbrüche)
20. AGB Page
21. Impressum Page
22. Datenschutz Page
23. Responsive Design
