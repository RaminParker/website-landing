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

# General Settings
CURRENT_YEAR = 2026  # Used for copyright notices and last-updated dates

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

    # Impressum Page
    'impressum_page': 'impressum-page',
    'impressum_block': 'impressum-block',
    'impressum_block_title': 'impressum-block-title',
    'impressum_block_intro': 'impressum-block-intro',
    'impressum_section': 'impressum-section',
    'impressum_section_title': 'impressum-section-title',
    'impressum_section_content': 'impressum-section-content',
    'impressum_last_updated': 'impressum-last-updated',
    'impressum_copyright': 'impressum-copyright',
    'impressum_back_link': 'impressum-back-link',

    # Datenschutz Page
    'datenschutz_page': 'datenschutz-page',
    'datenschutz_block': 'datenschutz-block',
    'datenschutz_block_title': 'datenschutz-block-title',
    'datenschutz_block_intro': 'datenschutz-block-intro',
    'datenschutz_section': 'datenschutz-section',
    'datenschutz_section_title': 'datenschutz-section-title',
    'datenschutz_section_content': 'datenschutz-section-content',
    'datenschutz_last_updated': 'datenschutz-last-updated',
    'datenschutz_back_link': 'datenschutz-back-link',

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
        "Sommersemester 2026",
        "Gießen-kocht!",
        "Das Gießener Kult-Event - seit Jahren einmal pro Semester",
        "https://www.giessenkocht.de/"
    ),
    (
        "Sommersemester 2026",
        "BamBuS Dinner",
        "Organisiert durch die Studierendengruppe BamBuS der Uni Bamberg",
        "https://www.bambusev.de/bambus-dinner"
    ),
    (
        "Sommersemester 2026",
        "Studi-Dinner",
        "Angebote vom Studentischen Gesundheitsmanagament der Uni Tübingen",
        "https://uni-tuebingen.de/einrichtungen/zentrale-einrichtungen/hochschulsport/sgm-betabalance/studi-dinner/"
    ),
    (
        "Sommersemester 2026",
        "Koch Bachelor Osnabrück",
        "Der kleine Brunder vom beliebten Bier Bachelor",
        "https://www.kochbachelor.de/"
    ),
    (
        "Sommersemester 2026",
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
    ("/images/uni_logos/uni_bamberg.png", "Universität Bamberg Logo", "Universität Bamberg"),
    ("/images/uni_logos/uni_erlangen.svg", "Universität Erlangen Logo", "Universität Erlangen"),
    ("/images/uni_logos/uni_giessen.png", "Universität Gießen Logo", "Universität Gießen"),
    ("/images/uni_logos/uni_marburg.png", "Universität Marburg Logo", "Universität Marburg"),
    ("/images/uni_logos/uni_tuebingen.svg", "Universität Tübingen Logo", "Universität Tübingen"),
    ("/images/uni_logos/uni_wuerzburg.png", "Universität Würzburg Logo", "Universität Würzburg"),
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

# =============================================================================
# Impressum (Legal Notice) Content
# =============================================================================

IMPRESSUM_DATA = {
    'id': 'impressum',
    'title': 'Impressum',
    'intro': 'Angaben gemäß § 5 TMG',
    'sections': [
        (
            'Anbieter',
            'Spinfood Beravat Ramin, Beravat Schirin, Eichhorn Rene GbR\nWilhelm-Späth-Straße 80\n90461 Nürnberg\n\nVertreten durch: Dr. Ramin Beravat, Schirin Beravat und René Eichhorn'
        ),
        (
            'Kontakt',
            'Telefon: (anzeigen)\nE-Mail: hi@spinfood.de'
        ),
        (
            'Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV',
            'Dr. Ramin Beravat, Schirin Beravat und René Eichhorn (Anschrift wie oben)'
        ),
        (
            'EU-Streitbeilegung',
            'Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: https://ec.europa.eu/consumers/odr.\nUnsere E-Mail-Adresse finden Sie oben im Impressum.'
        ),
        (
            'Verbraucherstreitbeilegung/Universalschlichtungsstelle',
            'Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.'
        ),
        (
            'Haftungsausschluss',
            'Die Inhalte unserer Internetseite werden mit größter Sorgfalt recherchiert. Dennoch kann der Anbieter keine Haftung für die Richtigkeit, Vollständigkeit und Aktualität der bereitgestellten Informationen übernehmen.'
        )
    ],
    'last_updated': f'Januar {CURRENT_YEAR}',
    'copyright': f'© {CURRENT_YEAR} Spinfood – Alle Rechte vorbehalten'
}

# =============================================================================
# Datenschutz (Privacy Policy) Content
# =============================================================================

DATENSCHUTZ_DATA = {
    'id': 'datenschutz',
    'title': 'Datenschutz',
    'intro': 'Wow, du liest sogar die Datenschutzerklärung - cool!\n\nWir freuen uns riesig über deinen Besuch auf unser Website. Der Schutz deiner personenbezogenen Daten während deines gesamten Geschäftsprozesses ist für uns ein wichtiges Anliegen. Deshalb betreiben wir unser Internetportal in Übereinstimmung mit den geltenden Gesetzen zum Datenschutz und zur Datensicherheit. Im Folgenden erläutern wir dir, wie wir den Schutz deiner Daten gewährleisten und welche Art von Daten zu welchem Zweck erhoben werden.',
    'sections': [
        (
            'Datenschutz',
            'Spinfood weist den Kunden darauf hin, dass die im Rahmen des Vertragsschlusses aufgenommenen Daten gemäß dem Bundesdatenschutzgesetz (BDSG) zur Erfüllung der Verpflichtungen aus dem Kaufvertrag erhoben, verarbeitet und genutzt werden. Mit dem Absenden von Info- oder sonstigen Anfragen oder Bestellungen per von uns zur Verfügung gestelltem Formular erklärt sich der Anwender damit einverstanden, dass seine Angaben zur Bearbeitung in unserer EDV erfasst werden.\n\nBei der Anmeldung zum Newsletter wird die E-Mail-Adresse und der Name des Nutzers mit dessen Einwilligung für Werbemaßnahmen von Spinfood genutzt, bis der Kunde den Newsletter von Spinfood wieder abbestellt.\n\nAlle Daten werden nur zu dem genannten Zweck verwendet und nicht an unberechtigte Dritte weitergegeben.'
        ),
        (
            'Allgemein',
            'Der Besuch dieser Website ist mit der Verarbeitung von personenbezogenen Daten verbunden. Zwar sind beim bloßen Aufrufen der Seite grundsätzlich keine Angaben über personenbezogene Daten erforderlich, da jedoch bestimmte Funktionen der Website und damit möglicherweise verbundener Dienste einen Verarbeitungsvorgang hervorrufen können, sollen alle Besucher an dieser Stelle über die für die Verarbeitung verantwortliche Stelle, den Zweck und den Umfang der Verarbeitung und natürlich über ihre Rechte als Betroffene informiert werden. Alle Datenverarbeitungsvorgänge auf dieser Website erfolgen im Einklang mit den datenschutzrechtlichen gesetzlichen Vorschriften, insbesondere mit der Datenschutz-Grundverordnung (DSGVO) und dem Bundesdatenschutzgesetz (BDSG). Es wird daher von den Betroffenen eine Einwilligung für die Verarbeitung eingeholt, wenn nicht eine gesetzliche Grundlage für den einzelnen Verarbeitungsvorgang vorhanden ist. Wenn ein Drittanbieter für uns als Auftragsverarbeiter tätig wird, schließen wir mit diesem einen Vertrag über die Auftragsverarbeitung.\n\nDurch die Nutzung unserer Internetpräsenz erklärst du dich damit einverstanden, dass eine Erhebung, Verarbeitung und Nutzung von Daten gemäß der nachfolgenden Beschreibung erfolgt.\nPersonenbezogene Daten werden nur erhoben, wenn du dies durch Einwilligung gestattest. Die Einwilligung erfolgt durch das Setzen eines Hakens im Web-Formular, in dem es heißt: "Mit der Anmeldung akzeptiere ich die [Teilnahmegebühren &] AGB´s. Mit der Anmeldung erklärst du dein Einverständnis zu den untenstehenden Regelungen zur Verwendung persönlicher Daten durch Spinfood. Nach Maßgabe des Gebotes der Datenvermeidung und -sparsamkeit erhebt Spinfood dabei nur solche Daten, die für die Organisation und Koordination der Veranstaltung erforderlich sind.\nIm Rahmen von Spinfood werden deine Anmeldedaten zum Zwecke der Zusammenstellung von Teams eines jeweiligen Gangs verarbeitet. Ferner werden die von dir bei der Anmeldung angegebenen Informationen zu einem Nutzerprofil zusammengefügt, um die Koordination der Veranstaltung persönlich auf Dich zugeschnitten anbieten zu können.\nDie erforderlichen Daten für Spinfood Events sind im Einzelnen:\n• Dein Vor- und Nachname\n• Dein Geschlecht\n• Dein Alter\n• Deine Adresse (Straße, Hausnummer, Stockwerk, Postleitzahl, Stadt, Bundesland)\n• Deine Telefonnummer, unter der du während der Durchführung der Veranstaltung erreichbar bist\n• Deine E-Mail-Adresse, um dir gegebenenfalls wichtige Informationen, die Durchführung der Veranstaltung betreffend, zukommen zu lassen\n• Deine Angabe, ob du eine vegetarische, vegane oder eine Runde mit Fleisch bevorzugst.\n• Deine Angabe, ob du für das Event von Spinfood eine Küche bereitstellen kannst.\nDie im Rahmen von Spinfood erhobenen personenbezogenen Daten werden nur zur Organisation und Koordination der Veranstaltungen und zur Bearbeitung deiner Anfragen genutzt. Da die Einwilligung in die Nutzung deiner Daten in die vorgenannten Zwecke auch die Übermittlung deiner Daten an andere Teilnehmer von Spinfood umfasst, können deine Daten an diesen Personenkreis weitergegeben werden. Dabei beschränkt sich die Weitergabe auf deinen Vor- und Nachnamen, deine Adresse sowie deine Telefonnummer und immer nur auf die Teilnehmer des jeweiligen Gangs. Im Übrigen findet keine Weitergabe an sonstige Dritte statt.'
        ),
        (
            'Verantwortliche Stelle',
            'Verantwortlicher im Sinne der DSGVO und des BDSG ist:\n\nDr. Ramin Beravat & René Eichhorn\nBielingstraße 14\n90419 Nürnberg\n\nE-Mail: hi@spinfood.de'
        ),
        (
            'Cookies',
            'Auf dieser Website kommen sogenannte Cookies zum Einsatz (Session-Cookies und Permanent-Cookies). Cookies sind von einem Server generierte Textdateien, in denen Informationen über den auf die Seite zugreifenden Nutzer gespeichert und auf dessen Gerät abgelegt werden. Session-Cookies werden nur für die Dauer des Besuches der Website, Permanent-Cookies hingegen werden dauerhaft auf dem Gerät des Nutzers gespeichert. Bei erneutem Zugriff auf die Website kann der Server den Nutzer über die Permanent-Cookies identifizieren und die auf diese Weise hinterlegten Informationen auswerten. Die durch den Einsatz von Cookies erhobenen Daten können mit den mittels Erstellung von Nutzungsprofilen erhobenen Daten zusammengeführt werden.\n\nWenn der Nutzer mit dem Einsatz von Cookies nicht einverstanden ist, hat er die Möglichkeit, über Einstellungen des Browsers das Setzen von Cookies zu verhindern und auch bereits gesetzte Cookies zu löschen. Es ist dann jedoch nicht sichergestellt, dass die Website vollständig angezeigt wird und alle Funktionen genutzt werden können.\n\nZweck des Einsatzes von Cookies ist, die Nutzung der Website zu vereinfachen und in Teilen überhaupt zu ermöglichen. Es sollen durch die Auswertung der mittels Cookies erhobenen Daten außerdem die Qualität der Website und der Inhalte verbessert werden.'
        ),
        (
            'Statistik, Darstellung, Zusammenarbeit mit Behörden',
            'Zur Erstellung von Zugriffsstatistiken, für die korrekte Darstellung der Inhalte sowie zur bestmöglichen Zusammenarbeit mit den Strafverfolgungsbehörden im Falle eines Cyberangriffs werden beim Besuch dieser Website die folgenden Daten erfasst:\n• IP-Adresse\n• URL der abgerufenen Seite\n• Referer (die vorhergehende Seite, von der an die aufgerufene Seite weiterverwiesen wurde)\n• Seiten, die über diese Website aufgerufen werden\n• Datum und Uhrzeit des Zugriffs\n• Dauer des Zugriffs\n• Informationen über den Internet-Service-Provider, das genutzte Betriebssystem und den genutzten Browser\nDiese beim Besuch der Website erhobenen Daten werden getrennt von anderen Daten, die im Rahmen der Nutzung der Website möglicherweise eingegeben werden, gespeichert und werden nur intern zu den genannten Zwecken genutzt und nicht an Dritte weitergegeben, es sei denn, dazu besteht eine gesetzliche Verpflichtung. Eine Zuordnung dieser Daten zu einer bestimmten Person ist nicht möglich.'
        ),
        (
            'Kontaktaufnahme per E-Mail',
            'Sie haben die Möglichkeit, uns per E-Mail persönliche Daten zu übermitteln. Den Umfang und die Art der so übermittelten Daten bestimmen Sie grundsätzlich selbst durch den Inhalt der E-Mail. Wir verstehen den Versand einer E-Mail an uns als Einwilligung in die Verarbeitung der so übermittelten Daten.\n\nDie so übermittelten Daten werden von uns zunächst dafür genutzt, um Ihnen weitere Informationen zu unseren Leistungen zukommen zu lassen. Dies kann eine vorvertragliche Maßnahme sein, wenn Sie sich zu einem Vertragsschluss mit uns entscheiden. Die Daten würden von uns sodann auch zur Vertragserfüllung genutzt.\n\nWir weisen an dieser Stelle darauf hin, dass es Ihnen jederzeit freisteht, die Einwilligung zur Erhebung, Verarbeitung und/oder Nutzung der an uns übermittelten Daten zu widerrufen. Ein solcher Widerruf ist nicht an eine bestimmte Form gebunden und kann daher auf dem von Ihnen bevorzugten Kommunikationsweg übermittelt werden. Wir löschen die bei uns gespeicherten Daten sodann umgehend, soweit wir sie nicht zur Vertragserfüllung benötigen oder eine Aufbewahrung gesetzlich vorgeschrieben ist.'
        ),
        (
            'Newsletter',
            'Das Angebot, Sie per Newsletter über unsere Leistungen allgemein und über aktuelle Angebote zu informieren, ist ebenfalls mit der Erhebung, Verarbeitung und Nutzung von Daten verbunden. Wenn Sie uns über das entsprechende Formular auf der Website oder durch die Angabe auf anderem Wege Ihre E-Mail-Adresse mitteilen, speichern wir diese für den Versand des Newsletters. Wenn wir eine personalisierte Form des Versands anbieten, fragen wir außerdem nach Ihrem Namen und gegebenenfalls weitere personenbezogene Daten ab, die wir dann ebenfalls und ausschließlich für den Versand des Newsletters speichern.\n\nWir führen vor dem ersten Versand das sogenannte Double-Opt-In-Verfahren durch, d.h. nach Erhalt Ihrer E-Mail-Adresse senden wir Ihnen an diese Adresse zunächst eine E-Mail und bitten um Ihre Bestätigung und Ihre Einwilligung in die Verarbeitung Ihrer Daten für den Newsletter-Versand. Erst wenn uns Ihre Bestätigung vorliegt, verarbeiten und nutzen wir Ihre Daten für den Versand des Newsletters. Geht eine Bestätigung nicht innerhalb von vier Wochen nach dem Versand unserer E-Mail an Sie bei uns ein, löschen wir Ihre Daten wieder.\n\nWenn Sie uns eine Bestätigung senden, erfassen wir die IP-Adresse, das Datum und die Uhrzeit der Anmeldung, speichern diese jedoch nur für interne Zwecke und zur Vorbeugung gegen Missbrauch.\n\nWir nutzen Ihre Daten nur für den Versand des Newsletters und geben Sie nicht an Dritte weiter. Von dem Newsletter können Sie sich jederzeit wieder abmelden. Die Abmeldung wird von uns als Widerruf der Einwilligung in die Datenverarbeitung verstanden. Sie können sich über den in jedem Newsletter enthaltenen Link abmelden. Selbstverständlich können Sie uns aber auch in anderer Form benachrichtigen, wenn Sie den Newsletter nicht länger erhalten möchten. Auch dies verstehen wir als Widerruf der Einwilligung. In allen Fällen werden wir Ihre Daten unmittelbar nach Erhalt Ihrer Mitteilung löschen, wenn wir nicht gesetzlich zur Aufbewahrung verpflichtet sind.'
        ),
        (
            'Google Analytics',
            'Auf dieser Website ist das von der Google Inc., 1600 Amphitheatre Pkwy, Mountain View, CA 94043-1351, USA (im Folgenden: Google) entwickelte Tool Google Analytics (mit Anonymisierungsfunktion) eingebunden. Google Analytics ist ein Analyse-Dienst, der Daten von den Besuchern von Websites erhebt, sammelt und auswertet. Es wird unter anderem erfasst, von welcher Website die Besucher auf diese Website gekommen sind (sogenannte Referrer), auf welche Seiten bzw. Unterseiten zugegriffen wird, von welchem Ort und wie häufig und für welche Dauer die Seiten besucht und welches Betriebssystem und welcher Browser dabei eingesetzt wurden. Google Analytics wird überwiegend zur Optimierung der Website und zur Analyse der Besucherdaten für die Wirksamkeit von Werbemaßnahmen eingesetzt.\n\nBeim Einsatz von Google Analytics wird von der Anonymisierungsfunktion Gebrauch gemacht. Das hat zur Folge, dass die IP-Adresse des Besuchers von Google gekürzt und anonymisiert wird, wenn der Zugriff auf die Seite aus einem Mitgliedstaat der Europäischen Union oder aus einem anderen Vertragsstaat des Abkommens über den Europäischen Wirtschaftsraum erfolgt.\n\nZweck des Einsatzes von Google Analytics ist die Analyse der Besucher und deren Verhalten auf der Website. Google nutzt die so erhobenen Daten, um denjenigen, der Google Analytics einsetzt, mit den dadurch gewonnen Informationen (also Daten) in Form eines Berichts zu versorgen und gegebenenfalls weitere mit der Nutzung der Website in Verbindung stehende Leistungen zu erbringen.\n\nGoogle Analytics setzt Cookies ein. Die Funktionsweise von Cookies wird unter der entsprechenden Überschrift im Rahmen dieser Erklärung erläutert. Durch den Einsatz der Cookies kann Google die Benutzung der Website analysieren. Es können so dort, wo Google Analytics und Cookies zum Einsatz kommen, der Besuch der einzelnen Seiten erfasst und an Google übermittelt werden.\n\nDadurch kann Google Daten der Besucher, wie die IP-Adresse und die übrigen oben genannten Daten, erfassen und nachvollziehen, woher der Zugriff auf die Seiten erfolgt ist und welche Seiten im einzelnen besucht wurden. Unter anderem werden die so erhobenen Daten für die Provisionsabrechnung von Google Werbemaßnahmen genutzt.\n\nMittels des Cookies werden personenbezogene Informationen, das sind neben der IP-Adresse zum Beispiel die Zugriffszeit, der Ort, von dem ein Zugriff erfolgt, und die Häufigkeit der Besuche dieser Website gespeichert. Bei jedem Besuch der Website werden diese personenbezogenen Daten an Google und damit in die Vereinigten Staaten von Amerika übermittelt und dort gespeichert. Google gibt diese durch das beschriebene Verfahren erhobenen personenbezogenen Daten unter Umständen an Dritte weiter.\n\nDie Google Analytics Daten werden für einen Zeitraum von 50 Monaten gespeichert.\n\nDie Datenerhebung mittels Cookies kann durch eine entsprechende Einstellung im Browser oder durch den Einsatz anderer entsprechender Software ebenso verhindert werden wie das dauerhafte Ablegen (Setzen) von Cookies auf dem System des Besuchers. Ein von Google bereits gesetzter Cookie kann jederzeit durch eine entsprechende Einstellung im Browser oder durch den Einsatz anderer entsprechender Software gelöscht werden.\n\nEs besteht die Möglichkeit, der Erhebung und der Verarbeitung der durch Google erzeugten Daten, die sich auf die Nutzung dieser Website beziehen, durch Google zu widersprechen. Dazu muss ein Browser-Add-On, das unter https://tools.google.com/dlpage/gaoptout heruntergeladen werden kann, installiert werden. Durch das Add-On wird Google mitgeteilt, dass Daten und Informationen zu den Besuchen von Websites nicht über Google Analytics übermittelt werden dürfen. Google wertet die Installation des Browser-Add-Ons als Widerspruch zu der Datenerhebung und -verarbeitung. Bei einer Löschung, Formatierung oder Neuinstallation auf dem System des Besuchers bedarf es mitunter einer Neuinstallation des Browser-Add-Ons oder der Einstellungen in der entsprechenden Software, um die Funktionen von Google Analytics zu deaktivieren. Bei Deinstallation oder Deaktivierung des Browser-Add-Ons findet eine Datenerhebung und -verarbeitung wieder statt. Es besteht sodann die Möglichkeit einer Neuinstallation oder einer erneuten Aktivierung des Browser-Add-Ons.\n\nWeitere Informationen und die aktuellen Datenschutzbestimmungen von Google können unter https://www.google.de/intl/de/policies/privacy/ und unter http://www.google.com/analytics/terms/de.html abgerufen werden. Informationen zu Google Analytics sind unter https://www.google.com/intl/de_de/analytics/ abrufbar.'
        ),
        (
            'YouTube',
            'Auf dieser Website kommt ein Plugin von YouTube zum Einsatz. YouTube ist ein Service der YouTube, LLC, 901 Cherry Ave., San Bruno, CA 94066, USA (YouTube), einer Tochtergesellschaft der Google Inc., 1600 Amphitheatre Pkwy, Mountain View, CA 94043-1351, USA (Google). YouTube ist ein Internet-Videoportal, auf dem Nutzer kostenlos Videos bereitstellen und andere Nutzer diese in der Regel kostenlos ansehen, bewerten und kommentieren können, wobei das Bewerten und Kommentieren der Anmeldung auf dem Portal bedarf.\n\nAuf anderen Websites besteht die Möglichkeit, die Inhalte von YouTube zu integrieren (einzubetten) und so die auf der YouTube-Plattform bereitgestellten Inhalte auf der anderen Website darzustellen. Weitere Informationen sind unter https://www.youtube.com/yt/about/de/ abrufbar. Auf diese Weise können YouTube und Google nachvollziehen, auf welcher Seite Nutzer die Inhalte angesehen haben. Wenn der Nutzer einen Account bei YouTube hat und in diesem angemeldet ist, kann YouTube erkennen, welche konkrete(n) Unterseite(n) der anderen Website der Nutzer besucht und diese Informationen dem Account des Nutzers zuordnen. Diese Datenerhebung und die Zuordnung kann auch erfolgen, wenn der Nutzer die Seite nur besucht, die Inhalte aber nicht ansieht. Der Nutzer kann dies durch das Abmelden von seinem Account vor dem Besuch der anderen Website verhindern.\n\nWeitere Informationen über YouTube, deren Datenschutzbestimmungen und über die Erhebung, Verarbeitung und Nutzung personenbezogener Daten durch YouTube und Google sind unter https://www.google.de/intl/de/policies/privacy/ abrufbar.'
        ),
        (
            'Speicherdauer und Löschung',
            'Die auf dieser Website verarbeiteten Daten werden nach der Erreichung des mit der Verarbeitung jeweils beabsichtigten Zweckes, nicht jedoch vor Ablauf einer gesetzlichen Aufbewahrungsfrist gelöscht. Insoweit die Daten für den Abschluss eines Vertrages, die Vertragserfüllung und/oder die Vertragsbeendigung erforderlich sind, werden sie für die dafür jeweils notwendige Zeit gespeichert und nach Beendigung der vertraglichen Beziehung gelöscht, soweit es nicht vertragliche und/oder gesetzliche Pflichten zur Speicherung der Daten gibt.'
        ),
        (
            'Rechtsgrundlage',
            'Rechtsgrundlage für die Verarbeitung von Daten ist Art. 6 Abs. 1 lit. a) DSGVO, wenn die Daten nach einer Einwilligung des Betroffenen verarbeitet werden. Regelmäßig wird die Datenverarbeitung jedoch zur Vertragserfüllung (Art. 6 Abs. 1 lit. b) DSGVO) oder zur Wahrung berechtigter Interessen (Art. 6 Abs. 1 lit. f) DSGVO) erforderlich sein. Das berechtigte Interesse der Verarbeitung ist hier die Bereitstellung und Aufrechterhaltung des Online-Angebots zur Information der (potentiellen) Kunden und (potentiellen) Geschäftspartner sowie anderer an dem Internetauftritt Interessierter. In Ausnahmefällen ist Rechtsgrundlage auch ein anderer in Art. 6 Abs. 1 lit. c) – e) DSGVO aufgeführter Grund.'
        ),
        (
            'Ihre Rechte',
            'Nach der DSGVO bzw. dem BDSG haben die von der Datenverarbeitung Betroffenen ein Auskunftsrecht (Art.15 DSGVO) über die von ihnen erhobenen Daten, können eine Bestätigung über die Datenverarbeitung und eine Zurverfügungstellung einer Kopie der Daten verlangen sowie ein Beschwerderecht bei der zuständigen Aufsichtsbehörde (Art. 77 DSGVO). Sie haben ein Recht auf Berichtigung (Art. 16 DSGVO), das auch in der Vervollständigung der Daten liegen kann. Sie haben ein Recht auf Löschung („Vergessenwerden") (Art. Art. 17 DSGVO) und ein Recht auf Einschränkung der Verarbeitung (Art. 18 DSGVO) sowie ein Recht auf Datenübertragbarkeit (Art. 20 DSGVO). Betroffene haben ein Recht auf Widerspruch (Art. 21 DSGVO) der künftigen Verarbeitung der Daten und es gelten die Einschränkungen zu den Automatisierten Entscheidungen im Einzelfall einschließlich Profiling (Art. 22 DSGVO). Wenn Sie in die Datenverarbeitung eingewilligt haben und die Daten auf dieser Grundlage verarbeitet werden, haben Sie jederzeit ein Recht auf Widerruf dieser Einwilligung.'
        )
    ],
    'last_updated': f'Januar {CURRENT_YEAR}'
}
