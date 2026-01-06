"""
Spinfood Landing Page - Configuration
======================================
Central configuration file for all constants, content data, and CSS class names.
Single source of truth for easy maintenance.
"""

# =============================================================================
# Application Settings
# =============================================================================

# Feature Flags
USE_HERO_VIDEO = True  # Set to False to use static placeholder instead of video
HERO_VIDEO_HEIGHT = 600  # Height in pixels (default: 600, max recommended: 800)

APP_TITLE = "Running Dinner Events - Powered by Spinfood"
APP_DESCRIPTION = (
    "Schlüsselfertig für Fachschaften, Unis und studentische Gruppen. "
    "Triff 6-12 neue Leute an einem Abend beim Running Dinner in deiner Uni-Stadt."
)
CONTACT_EMAIL = "hi@spinfood.de"

# Hero Section Content
HERO_TITLE_LINE1 = "Running Dinner organisieren –"
HERO_TITLE_LINE2 = "ohne den Stress"
HERO_SUBTITLE = "Die schlüsselfertige Plattform für Fachschaften und studentische Gruppen."

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
    'navbar_logo_img': 'navbar-logo-img',
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
    'highlight': 'highlight',
    # Hero Video
    'hero_video_container': 'hero-video-container',
    'hero_video': 'hero-video',
    'hero_video_thumbnail': 'hero-video-thumbnail',

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

    # AGB Page
    'agb_page': 'agb-page',
    'agb_header': 'agb-header',
    'agb_back_link': 'agb-back-link',
    'agb_nav': 'agb-nav',
    'agb_nav_item': 'agb-nav-item',
    'agb_block': 'agb-block',
    'agb_block_title': 'agb-block-title',
    'agb_block_intro': 'agb-block-intro',
    'agb_section': 'agb-section',
    'agb_section_title': 'agb-section-title',
    'agb_section_content': 'agb-section-content',
    'agb_last_updated': 'agb-last-updated',

    # Utility Classes (Extracted from Inline Styles)
    'section_emoji': 'section-emoji',
    'problem_statement': 'problem-statement',
    'solution_title': 'solution-title',
    'solution_tagline': 'solution-tagline',
    'step_description': 'step-description',
    'step_expand_btn': 'step-expand-btn',
    'expandable_content': 'expandable-content',
    'event_description': 'event-description',
    'events_list': 'events-list',
    'organizer_highlight': 'organizer-highlight',
    'organizer_note': 'organizer-note',
    'organizer_sidebar_title': 'organizer-sidebar-title',
    'organizer_sidebar_text': 'organizer-sidebar-text',
    'organizer_sidebar_emphasis': 'organizer-sidebar-emphasis',
    'testimonial_text': 'testimonial-text',
    'testimonial_author': 'testimonial-author',
    'faq_list': 'faq-list',
    'faq_answer_text': 'faq-answer-text',
    'team_title': 'team-title',
    'team_img': 'team-img',
    'partner_img': 'partner-img',
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

# =============================================================================
# AGB (Terms & Conditions) Content
# =============================================================================
# Each AGB entry: (id, title, sections)
# sections is a list of (heading, content) tuples

AGB_SPINFOOD = {
    'id': 'spinfood',
    'title': 'Allgemeine Geschäftsbedingungen - Spinfood',
    'intro': 'Nachfolgend finden Sie die Allgemeinen Geschäftsbedingungen für die Nutzung der Spinfood-Plattform.',
    'sections': [
        (
            '§1 Geltungsbereich',
            'Diese Allgemeinen Geschäftsbedingungen gelten für alle Nutzer der '
            'Spinfood-Plattform. Mit der Registrierung akzeptieren Sie diese Bedingungen.'
        ),
        (
            '§2 Leistungsbeschreibung',
            'Spinfood bietet eine Plattform zur Organisation von Running Dinner Events. '
            'Die Plattform ermöglicht die Anmeldung, Team-Zuteilung und Kommunikation '
            'zwischen Teilnehmenden.'
        ),
        (
            '§3 Anmeldung und Teilnahme',
            'Die Anmeldung zu einem Event erfolgt über die jeweilige Event-Seite. '
            'Mit der Anmeldung bestätigen Teilnehmende, dass sie die Teilnahmebedingungen '
            'gelesen haben und akzeptieren.'
        ),
        (
            '§4 Datenschutz',
            'Die Verarbeitung personenbezogener Daten erfolgt gemäß unserer '
            'Datenschutzerklärung und den geltenden Datenschutzgesetzen.'
        ),
        (
            '§5 Haftung',
            'Spinfood haftet nicht für Schäden, die durch die Teilnahme an Events '
            'entstehen. Die Teilnahme erfolgt auf eigene Verantwortung.'
        ),
        (
            '§6 Schlussbestimmungen',
            'Es gilt deutsches Recht. Gerichtsstand ist Berlin. Sollten einzelne '
            'Bestimmungen unwirksam sein, bleibt die Wirksamkeit der übrigen '
            'Bestimmungen unberührt.'
        ),
    ],
    'last_updated': 'Januar 2025'
}

AGB_GIESSEN_KOCHT = {
    'id': 'giessen-kocht',
    'title': 'Teilnahmebedingungen - Gießen kocht!',
    'intro': 'Nachfolgend finden Sie die Teilnahmebedingungen für das Event "Gießen kocht!".',
    'sections': [
        (
            '§1 Veranstalter',
            'Das Event "Gießen kocht!" wird von der Fachschaft [Name] der '
            'Justus-Liebig-Universität Gießen in Zusammenarbeit mit Spinfood organisiert.'
        ),
        (
            '§2 Teilnahmeberechtigung',
            'Teilnahmeberechtigt sind alle Studierenden der Justus-Liebig-Universität '
            'Gießen sowie deren Gäste. Eine gültige Anmeldung ist erforderlich.'
        ),
        (
            '§3 Anmeldegebühr',
            'Die Teilnahmegebühr beträgt [X] Euro pro Person. Die Zahlung erfolgt '
            'bei der Anmeldung über die Plattform. Bei Absage bis [Datum] ist eine '
            'Rückerstattung möglich.'
        ),
        (
            '§4 Ablauf des Events',
            'Teilnehmende kochen einen Gang (Vorspeise, Hauptgang oder Dessert) '
            'in ihrer eigenen Küche für insgesamt 6 Personen. Die anderen beiden '
            'Gänge werden bei anderen Teams eingenommen.'
        ),
        (
            '§5 Absagen und Nachrücker',
            'Bei Absage informieren Sie uns bitte umgehend über die Plattform. '
            'Kurzfristige Absagen können zu einer anteiligen Erstattung führen. '
            'Nachrücker werden automatisch benachrichtigt.'
        ),
        (
            '§6 Haftung',
            'Die Teilnahme erfolgt auf eigene Verantwortung. Die Veranstalter '
            'haften nicht für Personen- oder Sachschäden während des Events.'
        ),
    ],
    'last_updated': 'Januar 2025'
}

# List of all AGBs to display on the AGB page
AGB_LIST = [AGB_SPINFOOD, AGB_GIESSEN_KOCHT]
