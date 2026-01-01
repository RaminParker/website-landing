"""
Spinfood Landing Page - Configuration
======================================
Central configuration file for all constants, content data, and CSS class names.
Single source of truth for easy maintenance.
"""

# =============================================================================
# Application Settings
# =============================================================================

APP_TITLE = "Running Dinner Events - Powered by Spinfood"
APP_DESCRIPTION = (
    "Schlüsselfertig für Fachschaften, Unis und studentische Gruppen. "
    "Triff 6-12 neue Leute an einem Abend beim Running Dinner in deiner Uni-Stadt."
)
CONTACT_EMAIL = "hi@spinfood.de"

# Hero Section Content
HERO_TITLE_LINE1 = "Running Dinner Events"
HERO_TITLE_LINE2 = "Powered by Spinfood"
HERO_SUBTITLE = "Schlüsselfertig für Fachschaften, Unis und studentische Gruppen."

# =============================================================================
# CSS Class Names (Single Source of Truth)
# =============================================================================
# Using a dictionary prevents typos and enables IDE autocomplete.

CLASS = {
    # Layout
    'container': 'container',
    'section': 'section',
    'bg_white': 'bg-white',
    'bg_gray': 'bg-gray',
    'cards_grid': 'cards-grid',
    'fade_in': 'fade-in',

    # Typography
    'section_title': 'section-title',
    'section_subtitle': 'section-subtitle',

    # Navigation
    'navbar': 'navbar',
    'navbar_container': 'navbar-container',
    'navbar_logo': 'navbar-logo',
    'navbar_menu': 'navbar-menu',
    'navbar_link': 'navbar-link',
    'navbar_cta': 'navbar-cta',

    # Hero
    'hero': 'hero',
    'hero_container': 'hero-container',
    'hero_content': 'hero-content',
    'hero_title': 'hero-title',
    'hero_subtitle': 'hero-subtitle',
    'hero_buttons': 'hero-buttons',
    'hero_cta_primary': 'hero-cta-primary',
    'hero_cta_secondary': 'hero-cta-secondary',
    'hero_image': 'hero-image',
    'hero_image_placeholder': 'hero-image-placeholder',
    'hero_image_icon': 'hero-image-icon',
    'logo': 'logo',
    'tagline': 'tagline',
    'highlight': 'highlight',

    # Step Cards
    'step_card': 'step-card',
    'step_number': 'step-number',
    'step_icon': 'step-icon',
    'expandable': 'expandable',

    # Benefit Cards
    'benefit_card': 'benefit-card',
    'benefit_icon': 'benefit-icon',

    # Event Cards
    'event_card': 'event-card',
    'event_date': 'event-date',
    'event_cta': 'event-cta',

    # FAQ
    'faq_item': 'faq-item',
    'faq_question': 'faq-question',
    'faq_answer': 'faq-answer',
    'faq_arrow': 'faq-arrow',

    # Testimonials
    'testimonial_card': 'testimonial-card',

    # CTA Section
    'cta_section': 'cta-section',
    'cta_buttons': 'cta-buttons',
    'cta_button_primary': 'cta-button-primary',
    'cta_button_secondary': 'cta-button-secondary',

    # Team Section
    'team_section': 'team-section',
    'team_container': 'team-container',
    'team_image_wrapper': 'team-image-wrapper',
    'team_image': 'team-image',
    'team_content': 'team-content',
    'team_divider': 'team-divider',
    'team_description': 'team-description',
    'team_highlight': 'team-highlight',
    'team_buttons': 'team-buttons',
    'team_btn_primary': 'team-btn-primary',
    'team_btn_secondary': 'team-btn-secondary',
    'team_locations': 'team-locations',
    'team_location': 'team-location',

    # Partner Section
    'partner_section': 'partner-section',
    'partner_container': 'partner-container',
    'partner_label': 'partner-label',
    'partner_subtitle': 'partner-subtitle',
    'partner_logos': 'partner-logos',
    'partner_logo_item': 'partner-logo-item',
    'partner_logo': 'partner-logo',
    'partner_name': 'partner-name',

    # Sponsors Section
    'sponsors_section': 'sponsors-section',
    'sponsors_container': 'sponsors-container',
    'sponsors_label': 'sponsors-label',
    'sponsors_subtitle': 'sponsors-subtitle',
    'sponsors_grid': 'sponsors-grid',
    'sponsor_item': 'sponsor-item',
    'sponsor_icon': 'sponsor-icon',
    'sponsor_name': 'sponsor-name',
    'sponsor_type': 'sponsor-type',

    # Organizer Section
    'organizer_section': 'organizer-section',
    'organizer_content': 'organizer-content',
    'organizer_text': 'organizer-text',
    'organizer_benefits': 'organizer-benefits',
    'organizer_cta': 'organizer-cta',
    'organizer_image': 'organizer-image',

    # Footer
    'footer_section': 'footer-section',
    'footer_container': 'footer-container',
    'footer_column': 'footer-column',
    'footer_bottom': 'footer-bottom',
    'social_links': 'social-links',

    # Modal
    'modal': 'modal',
    'modal_content': 'modal-content',
    'modal_close': 'modal-close',
    'modal_email': 'modal-email',
}

# =============================================================================
# Content Data
# =============================================================================

# Current Running Dinner events
# Format: (date/semester, title, description, link)
CURRENT_EVENTS = [
    (
        "Sommersemester 2025",
        "Gießen-kocht!",
        "Das Gießener Kult-Event - seit Jahren einmal pro Semester",
        "https://www.giessenkocht.de/"
    ),
    (
        "Wintersemester 24/25",
        "Marburg-kocht!",
        "Organisiert durch die Studiengruppe der Uni Marburg",
        "https://www.marburgkocht.de/"
    ),
    (
        "Sommersemester 2025",
        "BamBuS Dinner",
        "Organisiert durch die Studierendengruppe BamBuS",
        "https://www.bambusev.de/bambus-dinner"
    ),
    (
        "Sommersemester 2025",
        "Laufgelage Erlangen",
        "Hochschulgruppe Erlangen-Nürnberg",
        "https://www.laufgelage.de/"
    ),
]

# Sponsors and partners
# Format: (icon, name, type)
SPONSOR_LIST = [
    ("🏪", "REWE", "Hauptsponsor"),
    ("🍕", "Domino's Pizza", "Food Partner"),
    ("🍺", "Krombacher", "Getränke Partner"),
    ("🏦", "Sparkasse", "Finanzieller Partner"),
    ("🎭", "Studentenwerk", "Unterstützer"),
    ("📱", "TechStart GmbH", "Tech Partner"),
]

# Frequently Asked Questions
# Format: (question, answer)
FAQ_LIST = [
    (
        "Was kostet Spinfood für uns als Veranstalter?",
        "Ihr habt zwei Optionen: Entweder die Teilnahme ist kostenlos und ihr zahlt "
        "eine einmalige Aufwandspauschale an uns. Oder die Teilnehmer zahlen eine "
        "kleine Gebühr bei der Anmeldung, von der wir einen Anteil erhalten. "
        "Welches Modell besser passt, besprechen wir gemeinsam."
    ),
    (
        "Wie viel Arbeit bleibt für uns übrig?",
        "Ihr kümmert euch um die Bewerbung des Events und die After-Party-Location (optional) – "
        "den Rest übernehmen wir. Anmeldung, Bezahlung, Rückerstattungen, Team-Zuteilung, Routen-Erstellung "
        "und die gesamte technische Teilnehmer-Kommunikation laufen automatisch über die Plattform."
    ),
    (
        "Können wir das Event an unsere Bedürfnisse anpassen?",
        "Ja! Ihr entscheidet über den Event-Namen, das Datum, die Anmeldefelder, das Einzugsgebiet, ob es "
        "eine Teilnahmegebühr gibt und vieles mehr. Auch euer eigenes Logo und eure "
        "Farben können integriert werden. Es ist euer Event – wir sind nur der technische Partner."
    ),
    (
        "Was passiert bei kurzfristigen Absagen?",
        "Kein Problem. Über das Teilnehmer-Management-System könnt ihr Absagen verarbeiten und "
        "Nachrücker einsetzen. Alle betroffenen Teams werden automatisch per E-Mail "
        "informiert – ihr müsst niemanden manuell kontaktieren. Was sonst ein unterschätzter "
        "Zeitfresser wäre, ist mit wenigen Klicks erledigt."
    ),
    (
        "Brauchen wir technisches Know-how?",
        "Nein. Die Plattform ist selbsterklärend, und wir begleiten euch beim ersten "
        "Event Schritt für Schritt. Bei Fragen sind wir jederzeit erreichbar. Wir haben "
        "jahrelange Erfahrung und wissen, worauf es bei der Organisation ankommt."
    ),
    (
        "Wie viele Teilnehmende kann die Plattform verwalten?",
        "Von 50 bis 5.000+ Teilnehmende – die Plattform skaliert problemlos. Ob kleine "
        "Fachschafts-Events oder stadtweite Großveranstaltungen: Wir haben beides erfolgreich umgesetzt."
    ),
    (
        "Wie schnell können wir starten?",
        "Sobald ihr euch bei uns meldet, kann euer Event innerhalb weniger Tage live "
        "gehen. Wir richten alles für euch ein – ihr müsst nur noch Werbung machen."
    ),
]

# Partner universities
# Format: (image_path, alt_text, name)
PARTNER_UNIVERSITIES = [
    ("/images/uni_giessen.png", "Universität Gießen Logo", "Universität Gießen"),
    ("/images/uni_erlangen.svg", "Universität Erlangen Logo", "Universität Erlangen"),
]

# Team locations
TEAM_LOCATIONS = ["Berlin", "Dresden", "Nürnberg"]
