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

Das Dictionary ist in logische Gruppen unterteilt:
- **Layout**: `container`, `section`, `bg_white`, `bg_gray`, `cards_grid`
- **Typography**: `section_title`, `section_subtitle`
- **Navigation**: `navbar`, `navbar_logo`, `navbar_menu`, etc.
- **Hero**: `hero`, `hero_title`, `hero_buttons`, etc.
- **Components**: `step_card`, `benefit_card`, `event_card`, `faq_item`, etc.
- **Utility Classes**: `section_emoji`, `problem_statement`, `solution_title`, etc.

### Dynamische Inline-Styles

Einzige Ausnahme für Inline-Styles sind **dynamische Werte**, z.B.:
```python
# EventCard - Akzentfarbe wird zur Laufzeit gesetzt
style = f"border-left-color: {accent_color};" if accent_color else ""
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
19. Utility Classes (aus Inline-Styles extrahiert)
20. Responsive Design
