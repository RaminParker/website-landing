"""
Spinfood Landing Page - Components
===================================
Reusable UI component functions for building the landing page.
Each function creates a single, focused component.
"""

from fasthtml.common import (
    Nav, Div, A, H1, H2, H3, P, Span, Button, Section, Ul, Li, Img, Video, Source
)

from config import (
    CLASS, CONTACT_EMAIL, CURRENT_EVENTS, SPONSOR_LIST, FAQ_LIST,
    PARTNER_UNIVERSITIES, PARTNER_EVENT_ORGANIZERS,
    AGB_LIST, IMPRESSUM_DATA, DATENSCHUTZ_DATA,
    HERO_TITLE_LINE1, HERO_TITLE_LINE2, HERO_SUBTITLE,
    USE_HERO_VIDEO, HERO_VIDEO_HEIGHT, CURRENT_YEAR,
    EVENT_ACCENT_COLORS, TEAM_MEMBERS, UEBER_UNS_DATA
)


# =============================================================================
# Navigation
# =============================================================================

def NavigationBar():
    """Create the fixed navigation bar at the top of the page."""
    return Nav(
        Div(
            A(
                Img(src="/images/intern/logo.png", alt="Spinfood Logo", cls=CLASS['navbar_logo_img']),
                "SPINFOOD",
                href="#",
                cls=CLASS['navbar_logo']
            ),
            Div(
                A("Für Veranstalter", href="#organizer", cls=CLASS['navbar_link']),
                A("Event finden", href="#events", cls=CLASS['navbar_cta']),
                cls=CLASS['navbar_menu']
            ),
            cls=CLASS['navbar_container']
        ),
        cls=CLASS['navbar']
    )


# =============================================================================
# Hero Section
# =============================================================================

def HeroVideo():
    """
    Create a hero video element with progressive loading.

    Uses a blur thumbnail that fades out once the video is ready.
    WebM format is preferred with MP4 fallback.
    """
    return Div(
        # Blur thumbnail (low-res, loads instantly)
        Div(cls=CLASS['hero_video_thumbnail'], id="hero-thumbnail"),
        # Video with multi-format support
        Video(
            Source(
                src="/videos/landingpage/optim.webm",
                type='video/webm; codecs="vp8, vorbis"'
            ),
            Source(
                src="/videos/landingpage/optim.mp4",
                type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'
            ),
            poster="/videos/landingpage/thumbnail@low.png",
            autoplay=True,
            loop=True,
            muted=True,
            playsinline=True,
            preload="auto",
            cls=CLASS['hero_video'],
            id="hero-video"
        ),
        cls=CLASS['hero_video_container']
    )


def HeroImagePlaceholder():
    """Create the static placeholder for the hero section (fallback/original)."""
    return Div(
        Div("👥", cls=CLASS['hero_image_icon']),
        P("Studenten beim gemeinsamen Kochen"),
        cls=CLASS['hero_image_placeholder']
    )


def HeroSection():
    """Create the main hero section with gradient background."""
    # Use video or static placeholder based on feature flag
    hero_media = HeroVideo() if USE_HERO_VIDEO else HeroImagePlaceholder()

    # Dynamic height from config (allows customization without CSS changes)
    hero_image_style = f"height: {HERO_VIDEO_HEIGHT}px;"

    return Div(
        Div(
            Div(
                H1(
                    HERO_TITLE_LINE1,
                    Span(HERO_TITLE_LINE2, cls=CLASS['highlight']),
                    cls=CLASS['hero_title']
                ),
                P(
                    HERO_SUBTITLE,
                    cls=CLASS['hero_subtitle']
                ),
                Div(
                    A("🎓 Event organisieren", href="#organizer",
                      cls=CLASS['hero_cta_primary']),
                    A("📍 Event finden", href="#events",
                      cls=CLASS['hero_cta_secondary']),
                    cls=CLASS['hero_buttons']
                ),
                cls=CLASS['hero_content']
            ),
            Div(
                hero_media,
                cls=CLASS['hero_image'],
                style=hero_image_style
            ),
            cls=CLASS['hero_container']
        ),
        cls=CLASS['hero']
    )


# =============================================================================
# Problem Section
# =============================================================================

def ProblemSection():
    """Create the problem statement section."""
    return Div(
        Div(
            Div("😔", cls=CLASS['section_emoji']),
            H2("Kennst du das?", cls=CLASS['section_title']),
            P(
                "Hunderte Anmeldungen in einer Excel-Tabelle. Endlose E-Mail-Ketten "
                "wegen Absagen und Nachrückern. Stundenlange manuelle Team-Zuteilung "
                "– und am Ende beschwert sich trotzdem jemand. Die Organisation eines "
                "Running Dinners kann zur Vollzeitbeschäftigung werden.",
                cls=CLASS['section_subtitle']
            ),
            P("Muss nicht sein.", cls=CLASS['problem_statement']),
            cls=CLASS['container']
        ),
        cls=f"{CLASS['section']} {CLASS['bg_white']}"
    )


# =============================================================================
# Solution Section
# =============================================================================

def SolutionSection():
    """Create the solution/value proposition section after the problem."""
    return Div(
        Div(
            Div("🚀", cls=CLASS['section_emoji']),
            H2("Running Dinner in deiner Stadt", cls=CLASS['solution_title']),
            P("Wir liefern die Plattform, ihr den Spaß", cls=CLASS['solution_tagline']),
            P(
                "Die schlüsselfertige Lösung für Fachschaften, Unis und studentische "
                "Gruppen.",
                cls=CLASS['section_subtitle']
            ),
            cls=CLASS['container']
        ),
        cls=f"{CLASS['section']} {CLASS['bg_gray']}"
    )


# =============================================================================
# How It Works Section
# =============================================================================

def StepCard(number: int, icon: str, title: str, description: str, details: str):
    """
    Create a single step card with expandable details.

    Args:
        number: Step number (1-3)
        icon: Emoji icon for the step
        title: Card title
        description: Short description
        details: Expandable detailed content
    """
    card_id = f"step-{number}"
    return Div(
        Div(str(number), cls=CLASS['step_number']),
        Div(icon, cls=CLASS['step_icon']),
        H3(title),
        P(description, cls=CLASS['step_description']),
        Button(
            "Mehr erfahren ↓",
            onclick=f"toggleExpand('{card_id}')",
            cls=CLASS['step_expand_btn']
        ),
        Div(
            P(details, cls=CLASS['expandable_content']),
            id=card_id,
            cls=CLASS['expandable']
        ),
        cls=f"{CLASS['step_card']} {CLASS['fade_in']}"
    )


def HowItWorksSection():
    """Create the 'How It Works' section with three step cards."""
    return Div(
        Div(
            H2("So funktioniert's", cls=CLASS['section_title']),
            Div(
                StepCard(
                    1, "📝",
                    "Anmelden & Matchen",
                    "Anmeldung online. Kochpartner wird zugelost oder als Paar anmelden.",
                    "Teilnahme als 2er-Team oder solo möglich. Jedes Team wird einem "
                    "Gang zugewiesen (Vorspeise, Hauptgang oder Dessert) und mit "
                    "anderen Teilnehmenden gematcht. Auch Kochanfänger sind herzlich "
                    "willkommen!"
                ),
                StepCard(
                    2, "🍽️",
                    "Kochen & Besuchen",
                    "Ein Gang wird zuhause gekocht, zwei weitere bei anderen Teams genossen.",
                    "Jedes Team kocht einen Gang für insgesamt 6 Personen in der eigenen Küche. "
                    "Die weiteren beiden Gänge werden bei anderen Teilnehmenden serviert. "
                    "So lernt man verschiedene Wohnungen und Stadtteile kennen!"
                ),
                StepCard(
                    3, "🎉",
                    "After Party",
                    "Zum Abschluss treffen sich alle Teilnehmende zur gemeinsamen Party (optional).",
                    "Nach dem Dinner kommen alle Teilnehmende zur After-Party zusammen. "
                    "Hier entstehen neue Kontakte und Freundschaften. Die Party geht "
                    "oft bis spät in die Nacht!"
                ),
                cls=CLASS['cards_grid']
            ),
            cls=CLASS['container']
        ),
        id="how",
        cls=f"{CLASS['section']} {CLASS['bg_gray']}"
    )


# =============================================================================
# Benefits Section
# =============================================================================

def BenefitCard(icon: str, title: str, text: str):
    """
    Create a single benefit card with floating animation.

    Args:
        icon: Emoji icon
        title: Benefit title (Food/Fun/Friends)
        text: Description text
    """
    return Div(
        Div(icon, cls=CLASS['benefit_icon']),
        H3(title),
        P(text),
        cls=f"{CLASS['benefit_card']} {CLASS['fade_in']}"
    )


def BenefitsSection():
    """Create the benefits section showcasing Food, Fun, Friends."""
    return Section(
        Div(
            H2("Was ist ein Running Dinner Event?", cls=CLASS['section_title']),
            P(
                "Bei einem Running Dinner ziehen Teams durch die Stadt und erleben "
                "drei Gänge in drei verschiedenen Wohnungen – bei jedem Gang mit neuen "
                "Leuten. Klingt einfach, ist es aber nicht: Hinter einem gelungenen Event "
                "steckt ein komplexes Puzzle aus Anmeldungen, Team-Matching, Routen-Planung "
                "und Kommunikation. Genau hier kommt Spinfood ins Spiel.",
                cls=CLASS['section_subtitle']
            ),
            Div(
                BenefitCard(
                    "🍝", "Food",
                    "Zusammen leckere Gerichte kochen. Von einfach bis "
                    "extravagant - alles dabei!"
                ),
                BenefitCard(
                    "✨", "Fun",
                    "Ein Abend voller Überraschungen. Falls gewünscht auch mit legendärer "
                    "After-Dinner-Party zum Abschluss."
                ),
                BenefitCard(
                    "👥", "Friends",
                    "Echte Verbindungen entstehen beim gemeinsamen Kochen und "
                    "Essen. Nicht oberflächlich, sondern echt!"
                ),
                cls=CLASS['cards_grid']
            ),
            cls=CLASS['container']
        ),
        cls=f"{CLASS['section']} {CLASS['bg_white']}"
    )


# =============================================================================
# Events Section
# =============================================================================

def EventCard(date: str, title: str, description: str, link: str = "#", accent_color: str = None):
    """
    Create a single event card with optional accent color.

    Args:
        date: Event date/semester
        title: Event name
        description: Short event description
        link: URL for the 'Mehr' button
        accent_color: Optional accent color for the left border (dynamic value)
    """
    # Dynamic style for accent color - legitimate inline style per CLAUDE.md
    style = f"border-left-color: {accent_color};" if accent_color else ""
    return Div(
        Div(
            Span(date, cls=CLASS['event_date']),
            H3(title),
            P(description, cls=CLASS['event_description'])
        ),
        A("Mehr →", href=link, cls=CLASS['event_cta']),
        cls=f"{CLASS['event_card']} {CLASS['fade_in']}",
        style=style
    )


def EventsSection():
    """Create the events section listing all current Running Dinner events."""
    return Section(
        Div(
            H2("Aktuelle Events", cls=CLASS['section_title']),
            P(
                "Finde das nächste Running Dinner in deiner Stadt.",
                cls=CLASS['section_subtitle']
            ),
            Div(
                *[EventCard(date, title, desc, link, EVENT_ACCENT_COLORS[i % len(EVENT_ACCENT_COLORS)])
                  for i, (date, title, desc, link) in enumerate(CURRENT_EVENTS)],
                cls=CLASS['events_list']
            ),
            cls=CLASS['container']
        ),
        id="events",
        cls=f"{CLASS['section']} {CLASS['bg_gray']}"
    )


# =============================================================================
# Organizer Section
# =============================================================================

def OrganizerSection():
    """Create the section for event organizers."""
    return Div(
        Div(
            Div(
                H2(
                    "Running Dinner Events",
                    Span("veranstalten", cls=CLASS['organizer_highlight']),
                    cls=CLASS['organizer_text']
                ),
                P(
                    "Konzentriert euch auf die Werbung – die Technik übernehmen wir."
                ),
                Ul(
                    Li("Automatische Benachrichtigungen bei Änderungen"),
                    Li("Self-Service für Teilnehmende – weniger Rückfragen"),
                    Li("Flexibles Teilnehmer-Management mit wenigen Klicks"),
                    Li("Integrierte PayPal-Zahlung mit Überblick"),
                    Li("Event-Statistiken & E-Mail-Protokoll"),
                    Li("Persönliche Beratung aus jahrelanger Erfahrung"),
                    cls=CLASS['organizer_benefits']
                ),
                P(
                    "Kein Excel, keine manuellen E-Mails, keine Kopfschmerzen. "
                    "Wir halten euch den Rücken frei – ihr kümmert euch um das Event.",
                    cls=CLASS['organizer_note']
                ),
                Button(
                    "Jetzt Kontakt aufnehmen",
                    onclick="showContactModal()",
                    cls=CLASS['organizer_cta']
                ),
                cls=CLASS['organizer_text']
            ),
            Div(
                H3("Für wen ist Spinfood?", cls=CLASS['organizer_sidebar_title']),
                P(
                    "Fachschaften, studentische Initiativen, AStAs und "
                    "Hochschulgruppen, die ein Running Dinner in ihrer Stadt "
                    "veranstalten möchten – ohne sich mit Excel-Tabellen und "
                    "E-Mail-Chaos herumzuschlagen.",
                    cls=CLASS['organizer_sidebar_text']
                ),
                P(
                    "Wir liefern nicht nur das Tool – wir stehen euch mit "
                    "Erfahrung zur Seite. Alles im Blick, alles unter Kontrolle.",
                    cls=CLASS['organizer_sidebar_emphasis']
                ),
                cls=CLASS['organizer_image']
            ),
            cls=CLASS['organizer_content']
        ),
        id="organizer",
        cls=CLASS['organizer_section']
    )


# =============================================================================
# Testimonials Section
# =============================================================================

def TestimonialCard(text: str, author: str):
    """
    Create a single testimonial card.

    Args:
        text: Testimonial quote
        author: Person's name and location
    """
    return Div(
        P(text, cls=CLASS['testimonial_text']),
        P(f"- {author}", cls=CLASS['testimonial_author']),
        cls=CLASS['testimonial_card']
    )


def TestimonialsSection():
    """Create the testimonials section with participant feedback."""
    return Section(
        Div(
            H2("Das sagen Teilnehmende", cls=CLASS['section_title']),
            TestimonialCard(
                "Ich war neu in der Stadt und kannte niemanden. Nach dem Running "
                "Dinner hatte ich direkt eine Gruppe von Freunden, mit denen ich "
                "heute noch regelmäßig was unternehme!",
                "Lisa, Teilnehmerin in Marburg"
            ),
            TestimonialCard(
                "Die Mischung aus Kochen, neuen Leuten und Party ist einfach "
                "perfekt. Ich war schon bei 3 Events dabei und es war jedes Mal "
                "großartig!",
                "Tom, Teilnehmer in Gießen"
            ),
            cls=CLASS['container']
        ),
        cls=f"{CLASS['section']} {CLASS['bg_white']}"
    )


# =============================================================================
# FAQ Section
# =============================================================================

def FAQItem(question: str, answer: str, item_id: str):
    """
    Create a single FAQ item with toggle functionality.

    Args:
        question: FAQ question text
        answer: FAQ answer text
        item_id: Unique ID for the FAQ item
    """
    return Div(
        Div(
            Span(question),
            Span("▼", cls=CLASS['faq_arrow']),
            cls=CLASS['faq_question'],
            onclick=f"toggleFAQ('{item_id}')"
        ),
        Div(
            P(answer, cls=CLASS['faq_answer_text']),
            cls=CLASS['faq_answer'],
            id=f"faq-answer-{item_id}"
        ),
        cls=f"{CLASS['faq_item']} {CLASS['fade_in']}",
        id=item_id
    )


def FAQSection():
    """Create the FAQ section with expandable questions and answers."""
    return Section(
        Div(
            H2("Häufige Fragen", cls=CLASS['section_title']),
            Div(
                *[FAQItem(q, a, f"faq-{i}") for i, (q, a) in enumerate(FAQ_LIST)],
                cls=CLASS['faq_list']
            ),
            cls=CLASS['container']
        ),
        cls=f"{CLASS['section']} {CLASS['bg_gray']}"
    )


# =============================================================================
# CTA Section
# =============================================================================

def CTASection():
    """Create the call-to-action section before the footer."""
    return Div(
        H2("Bereit für dein erstes Running Dinner?"),
        P(
            "Melde dich jetzt für das nächste Event an und erlebe einen "
            "unvergesslichen Abend voller neuer Freundschaften!"
        ),
        Div(
            A("Event auswählen", href="#events", cls=CLASS['cta_button_primary']),
            Button(
                "Noch Fragen?",
                onclick="showContactModal()",
                cls=CLASS['cta_button_secondary']
            ),
            cls=CLASS['cta_buttons']
        ),
        cls=CLASS['cta_section']
    )


# =============================================================================
# Team Section
# =============================================================================

def TeamSection():
    """Create the team/about section."""
    return Div(
        Div(
            Div(
                Div(
                    Img(
                        src="/images/intern/team.png",
                        alt="Spinfood Team",
                        cls=CLASS['team_img']
                    ),
                    cls=CLASS['team_image']
                ),
                cls=CLASS['team_image_wrapper']
            ),
            Div(
                H2(
                    "Und wer steckt hinter ",
                    Span("Spinfood?"),
                    cls=CLASS['team_title']
                ),
                Div(cls=CLASS['team_divider']),
                P(
                    "Wir sind drei Hobby-Köche aus Berlin, Dresden und Nürnberg "
                    "und arbeiten in leidenschaftlich an diesem Projekt. Wenn du "
                    "Fragen oder Anregungen hast, melde dich gerne bei uns. Wir "
                    "wollen Spinfood kontinuierlich verbessern und auch an deine Uni bringen!",
                    cls=CLASS['team_description']
                ),
                P(
                    "Unser Ziel: Running Dinner Events in jeder deutschen Uni-Stadt "
                    "etablieren.",
                    cls=CLASS['team_highlight']
                ),
                Div(
                    Button(
                        "✉️ Schreib uns",
                        onclick="showContactModal()",
                        cls=CLASS['team_btn_primary']
                    ),
                    A(
                        "Über uns",
                        href="/ueber-uns",
                        cls=CLASS['team_btn_secondary']
                    ),
                    cls=CLASS['team_buttons']
                ),
                cls=CLASS['team_content']
            ),
            cls=CLASS['team_container']
        ),
        cls=CLASS['team_section']
    )


# =============================================================================
# Partner Section
# =============================================================================

def PartnerSection():
    """Create the partner section with universities and event organizers."""
    return Div(
        Div(
            # Main section title
            H2("Teil der Spinfood-Community", cls=CLASS['partner_label']),
            P(
                "Von Nord bis Süd – diese Partner haben bereits auf unsere Plattform vertraut.",
                cls=CLASS['partner_subtitle']
            ),
            # Universities subsection
            H3("Universitäten & Fachschaften", cls=CLASS['partner_label_secondary']),
            Div(
                *[A(
                    Div(
                        Img(
                            src=img_path,
                            alt=alt_text,
                            cls=CLASS['partner_img']
                        ),
                        cls=CLASS['partner_logo']
                    ),
                    Span(name, cls=CLASS['partner_name']),
                    href=url,
                    target="_blank",
                    rel="noopener noreferrer",
                    cls=CLASS['partner_logo_item']
                ) for img_path, alt_text, name, url in PARTNER_UNIVERSITIES],
                cls=CLASS['partner_logos']
            ),
            # Event organizers subsection
            H3("Eventpartner", cls=CLASS['partner_label_secondary']),
            Div(
                *[A(
                    Div(
                        Img(
                            src=img_path,
                            alt=alt_text,
                            cls=CLASS['partner_img']
                        ),
                        cls=CLASS['partner_logo']
                    ),
                    Span(name, cls=CLASS['partner_name']),
                    href=url,
                    target="_blank",
                    rel="noopener noreferrer",
                    cls=CLASS['partner_logo_item']
                ) for img_path, alt_text, name, url in PARTNER_EVENT_ORGANIZERS],
                cls=CLASS['partner_logos']
            ),
            cls=CLASS['partner_container']
        ),
        cls=CLASS['partner_section']
    )


# =============================================================================
# Sponsors Section
# =============================================================================

def _sponsor_icon(icon_or_path, name):
    """Create sponsor icon element - image if path, text if emoji."""
    if icon_or_path.startswith("/"):
        return Img(src=icon_or_path, alt=f"{name} Logo", cls=CLASS['sponsor_icon'])
    return Div(icon_or_path, cls=CLASS['sponsor_icon'])


def SponsorsSection():
    """Create the sponsors section with a grid of sponsor cards."""
    return Div(
        Div(
            H2("Unsere Partner & Sponsoren", cls=CLASS['sponsors_label']),
            P(
                "Diese Unternehmen unterstützen uns dabei, unvergessliche Events "
                "für Studierende zu schaffen",
                cls=CLASS['sponsors_subtitle']
            ),
            Div(
                *[A(
                    _sponsor_icon(icon_or_path, name),
                    Div(name, cls=CLASS['sponsor_name']),
                    Div(sponsor_type, cls=CLASS['sponsor_type']),
                    href=url,
                    target="_blank",
                    cls=CLASS['sponsor_item']
                ) for icon_or_path, name, sponsor_type, url in SPONSOR_LIST],
                cls=CLASS['sponsors_grid']
            ),
            cls=CLASS['sponsors_container']
        ),
        cls=CLASS['sponsors_section']
    )


# =============================================================================
# Footer Section
# =============================================================================

def FooterSection():
    """Create the footer with three columns of links and information."""
    return Div(
        Div(
            Div(
                H3("Spinfood"),
                P("Running Dinner Events für Studierende in Deutschland."),
                Div(
                    A(Img(src="/images/social/youtube.svg", alt="YouTube", cls=CLASS['social_icon_img']), " YouTube", href="https://www.youtube.com/channel/UCKMWgTM0S1iix4U5z3C3BQw", target="_blank"),
                    A(Img(src="/images/social/instagram.svg", alt="Instagram", cls=CLASS['social_icon_img']), " Instagram", href="https://www.instagram.com/giessenkocht.de/", target="_blank"),
                    A(Img(src="/images/social/tiktok.svg", alt="TikTok", cls=CLASS['social_icon_img']), " TikTok", href="https://www.tiktok.com/@giessen.kocht?lang=en", target="_blank"),
                    cls=CLASS['social_links']
                ),
                cls=CLASS['footer_column']
            ),
            Div(
                H3("Support"),
                A("Kontakt", href="#", onclick="showContactModal(); return false;"),
                A("Über uns", href="/ueber-uns"),
                cls=CLASS['footer_column']
            ),
            Div(
                H3("Rechtliches"),
                A("Impressum", href="/impressum"),
                A("Datenschutz", href="/datenschutz"),
                A("AGB", href="/agb"),
                cls=CLASS['footer_column']
            ),
            cls=CLASS['footer_container']
        ),
        Div(
            P(f"© {CURRENT_YEAR} Spinfood. Made with ❤️ in Germany"),
            cls=CLASS['footer_bottom']
        ),
        cls=CLASS['footer_section']
    )


# =============================================================================
# Contact Modal
# =============================================================================

def ContactModal():
    """Create the contact modal that appears when users click contact buttons."""
    return Div(
        Div(
            Button("×", onclick="closeContactModal()", cls=CLASS['modal_close']),
            H3("Kontakt 📬"),
            P(
                "Wenn Du weitere Fragen, Anregungen oder Wünsche hast, kannst du "
                "uns jeder Zeit eine Email schicken an"
            ),
            A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls=CLASS['modal_email']),
            cls=CLASS['modal_content']
        ),
        id="contactModal",
        cls=CLASS['modal']
    )


# =============================================================================
# AGB Page Components
# =============================================================================

def AGBNavigation():
    """Create the simplified navigation bar for child pages."""
    return Nav(
        Div(
            A(
                Img(src="/images/intern/logo.png", alt="Spinfood Logo", cls=CLASS['navbar_logo_img']),
                "SPINFOOD",
                href="/",
                cls=CLASS['navbar_logo']
            ),
            cls=CLASS['navbar_container']
        ),
        cls=CLASS['navbar']
    )


def LegalPageSection(heading: str, content: str, css_prefix: str, preserve_linebreaks: bool = False):
    """
    Generische Section-Komponente für rechtliche Seiten (AGB, Impressum, Datenschutz).

    Args:
        heading: Section heading
        content: Section content text
        css_prefix: Prefix für CSS-Klassen ('agb', 'impressum', 'datenschutz')
        preserve_linebreaks: True für white-space: pre-line
    """
    content_cls = CLASS[f'{css_prefix}_section_content']
    if preserve_linebreaks:
        content_cls = f"{content_cls} {CLASS['pre_line']}"

    return Div(
        H3(heading, cls=CLASS[f'{css_prefix}_section_title']),
        P(content, cls=content_cls),
        cls=CLASS[f'{css_prefix}_section']
    )


def AGBSection(heading: str, content: str):
    """Create a single AGB section with heading and content."""
    return LegalPageSection(heading, content, 'agb', preserve_linebreaks=False)


def AGBBlock(agb_data: dict):
    """
    Create a complete AGB block with title, intro, and all sections.

    Args:
        agb_data: Dictionary with keys: id, title, intro, sections, last_updated
    """
    return Div(
        H2(agb_data['title'], cls=CLASS['agb_block_title'], id=agb_data['id']),
        P(agb_data['intro'], cls=CLASS['agb_block_intro']),
        *[AGBSection(heading, content) for heading, content in agb_data['sections']],
        P(f"Stand: {agb_data['last_updated']}", cls=CLASS['agb_last_updated']),
        cls=CLASS['agb_block']
    )


def AGBPageNav():
    """Create the quick navigation for jumping between AGB sections."""
    return Div(
        *[A(agb['title'].split(' - ')[1], href=f"#{agb['id']}", cls=CLASS['agb_nav_item'])
          for agb in AGB_LIST],
        cls=CLASS['agb_nav']
    )


def AGBPageContent():
    """Create the main content area with all AGB blocks."""
    return Div(
        Div(
            A("← Zurück zur Startseite", href="/", cls=CLASS['agb_back_link']),
            H1("Allgemeine Geschäftsbedingungen", cls=CLASS['section_title']),
            AGBPageNav(),
            *[AGBBlock(agb) for agb in AGB_LIST],
            cls=CLASS['container']
        ),
        cls=CLASS['agb_page']
    )


# =============================================================================
# Impressum Page Components
# =============================================================================

def ImpressumSection(heading: str, content: str):
    """Create a single impressum section with heading and content.

    Special handling for phone number display in Kontakt section (anti-spam).
    """
    # Special handling for phone number display in Kontakt section
    if heading == "Kontakt" and "(anzeigen)" in content:
        parts = content.split("Telefon: (anzeigen)")
        before_phone = parts[0] if len(parts) > 0 else ""
        after_phone = parts[1] if len(parts) > 1 else ""

        content_cls = f"{CLASS['impressum_section_content']} {CLASS['pre_line']}"
        return Div(
            H3(heading, cls=CLASS['impressum_section_title']),
            P(
                before_phone,
                "Telefon: ",
                Span(
                    "(anzeigen)",
                    id="phone-reveal-link",
                    style="color: var(--primary-teal); cursor: pointer; text-decoration: underline;",
                    onclick="this.textContent='0160 5819759'; this.style.cursor='default'; this.style.textDecoration='none';"
                ),
                after_phone,
                cls=content_cls
            ),
            cls=CLASS['impressum_section']
        )

    return LegalPageSection(heading, content, 'impressum', preserve_linebreaks=True)


def ImpressumBlock(impressum_data: dict):
    """Create the impressum content block with title, intro, and all sections.

    Args:
        impressum_data: Dictionary with keys: id, title, intro, sections, last_updated, copyright
    """
    return Div(
        H2(impressum_data['title'], cls=CLASS['impressum_block_title'], id=impressum_data['id']),
        P(impressum_data['intro'], cls=CLASS['impressum_block_intro']),
        *[ImpressumSection(heading, content) for heading, content in impressum_data['sections']],
        P(f"Stand: {impressum_data['last_updated']}", cls=CLASS['impressum_last_updated']),
        P(impressum_data['copyright'], cls=CLASS['impressum_copyright']),
        cls=CLASS['impressum_block']
    )


def ImpressumPageContent():
    """Create the main content area with impressum block."""
    return Div(
        Div(
            A("← Zurück zur Startseite", href="/", cls=CLASS['impressum_back_link']),
            H1("Impressum", cls=CLASS['section_title']),
            ImpressumBlock(IMPRESSUM_DATA),
            cls=CLASS['container']
        ),
        cls=CLASS['impressum_page']
    )


# =============================================================================
# Datenschutz Page Components
# =============================================================================

def DatenschutzSection(heading: str, content: str):
    """Create a single datenschutz section with heading and content."""
    return LegalPageSection(heading, content, 'datenschutz', preserve_linebreaks=True)


def DatenschutzBlock(datenschutz_data: dict):
    """Create the datenschutz content block with title, intro, and all sections.

    Args:
        datenschutz_data: Dictionary with keys: id, title, intro, sections, last_updated
    """
    intro_cls = f"{CLASS['datenschutz_block_intro']} {CLASS['pre_line']}"
    return Div(
        H2(datenschutz_data['title'], cls=CLASS['datenschutz_block_title'], id=datenschutz_data['id']),
        P(datenschutz_data['intro'], cls=intro_cls),
        *[DatenschutzSection(heading, content) for heading, content in datenschutz_data['sections']],
        P(f"Stand: {datenschutz_data['last_updated']}", cls=CLASS['datenschutz_last_updated']),
        cls=CLASS['datenschutz_block']
    )


def DatenschutzPageContent():
    """Create the main content area with datenschutz block."""
    return Div(
        Div(
            A("← Zurück zur Startseite", href="/", cls=CLASS['datenschutz_back_link']),
            H1("Datenschutz", cls=CLASS['section_title']),
            DatenschutzBlock(DATENSCHUTZ_DATA),
            cls=CLASS['container']
        ),
        cls=CLASS['datenschutz_page']
    )


# =============================================================================
# Über uns Page Components
# =============================================================================

def UeberUnsHero():
    """Create the hero section with decorative food image."""
    return Div(
        Img(
            src="/images/food/fruit-desert.png",
            alt="Spinfood - Running Dinner",
            cls=CLASS['ueber_uns_hero_img']
        ),
        cls=CLASS['ueber_uns_hero']
    )


def TeamMemberCard(member: dict):
    """
    Create a single team member card.

    Args:
        member: Dictionary with name, role, description, responsibilities, image
    """
    return Div(
        Div(
            Img(
                src=member['image'],
                alt=f"{member['name']} - Spinfood Team",
                cls=CLASS['team_member_img']
            ),
            cls=CLASS['team_member_image']
        ),
        Div(
            H3(member['name'], cls=CLASS['team_member_name']),
            P(member['role'], cls=CLASS['team_member_role']),
            P(member['description'], cls=CLASS['team_member_description']),
            Ul(
                *[Li(resp) for resp in member['responsibilities']],
                cls=CLASS['team_member_responsibilities']
            ),
            cls=CLASS['team_member_content']
        ),
        cls=CLASS['team_member_card']
    )


def TeamGridSection():
    """Create the team grid with all team members."""
    return Div(
        Div(
            H2("Das Team", cls=CLASS['ueber_uns_title']),
            Div(cls=CLASS['ueber_uns_divider']),
            Div(
                *[TeamMemberCard(member) for member in TEAM_MEMBERS],
                cls=CLASS['team_grid']
            ),
            cls=CLASS['ueber_uns_container']
        ),
        cls=CLASS['ueber_uns_section']
    )


def UeberUnsPhilosophieSection():
    """Create the philosophy section with text and image."""
    data = UEBER_UNS_DATA['philosophie']
    return Div(
        Div(
            Div(
                H2(data['title'], cls=CLASS['philosophie_title']),
                Div(cls=CLASS['philosophie_divider']),
                P(data['text'], cls=CLASS['philosophie_text']),
                cls=CLASS['philosophie_content']
            ),
            Div(
                Img(
                    src=data['image'],
                    alt="Spinfood Philosophie",
                    cls=CLASS['philosophie_img']
                ),
                cls=CLASS['philosophie_image']
            ),
            cls=CLASS['philosophie_container']
        ),
        cls=CLASS['philosophie_section']
    )


def UeberUnsKooperationenSection():
    """Create the cooperation/partnership section."""
    data = UEBER_UNS_DATA['kooperationen']
    return Div(
        Div(
            H2(data['title'], cls=CLASS['kooperationen_title']),
            Div(cls=CLASS['kooperationen_divider']),
            P(data['intro'], cls=CLASS['kooperationen_intro']),
            P(
                Span("Schreib uns einfach an!", style="font-weight: bold;"),
                f" {data['text']}",
                cls=CLASS['kooperationen_text']
            ),
            Button(
                "✉️ Kontaktiere uns",
                onclick="showContactModal()",
                cls=CLASS['kooperationen_btn']
            ),
            cls=CLASS['kooperationen_container']
        ),
        cls=CLASS['kooperationen_section']
    )


def UeberUnsFachschaftenSection():
    """Create the Fachschaften and Social Media section."""
    data = UEBER_UNS_DATA['fachschaften']
    return Div(
        Div(
            Div(
                *[Img(
                    src=img_path,
                    alt="Spinfood Behind the Scenes",
                    cls=CLASS['fachschaften_img']
                ) for img_path in data['images']],
                cls=CLASS['fachschaften_images']
            ),
            Div(
                H2(data['title'], cls=CLASS['fachschaften_title']),
                Div(cls=CLASS['fachschaften_divider']),
                P(data['text'], cls=f"{CLASS['fachschaften_text']} {CLASS['pre_line']}"),
                Div(
                    A(
                        Img(src="/images/social/instagram.svg", alt="Instagram", cls=CLASS['social_icon_img']),
                        href="https://www.instagram.com/giessenkocht.de/",
                        target="_blank",
                        cls=CLASS['social_icon_link']
                    ),
                    A(
                        Img(src="/images/social/tiktok.svg", alt="TikTok", cls=CLASS['social_icon_img']),
                        href="https://www.tiktok.com/@giessen.kocht?lang=en",
                        target="_blank",
                        cls=CLASS['social_icon_link']
                    ),
                    A(
                        Img(src="/images/social/youtube.svg", alt="YouTube", cls=CLASS['social_icon_img']),
                        href="https://www.youtube.com/channel/UCKMWgTM0S1iix4U5z3C3BQw",
                        target="_blank",
                        cls=CLASS['social_icon_link']
                    ),
                    cls=CLASS['fachschaften_social']
                ),
                cls=CLASS['fachschaften_content']
            ),
            cls=CLASS['fachschaften_container']
        ),
        cls=CLASS['fachschaften_section']
    )


def UeberUnsPageContent():
    """Create the main content for the Über uns page."""
    return Div(
        UeberUnsHero(),
        Div(
            A("← Zurück zur Startseite", href="/", cls=CLASS['ueber_uns_back_link']),
            cls=CLASS['container']
        ),
        TeamGridSection(),
        UeberUnsPhilosophieSection(),
        UeberUnsKooperationenSection(),
        UeberUnsFachschaftenSection(),
        cls=CLASS['ueber_uns_page']
    )
