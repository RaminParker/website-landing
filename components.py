"""
Spinfood Landing Page - Components
===================================
Reusable UI component functions for building the landing page.
Each function creates a single, focused component.
"""

from fasthtml.common import (
    Nav, Div, A, H1, H2, H3, P, Span, Button, Section, Ul, Li, Img
)

from config import (
    CLASS, CONTACT_EMAIL, CURRENT_EVENTS, SPONSOR_LIST, FAQ_LIST,
    PARTNER_UNIVERSITIES, TEAM_LOCATIONS,
    HERO_TITLE_LINE1, HERO_TITLE_LINE2, HERO_SUBTITLE
)


# =============================================================================
# Navigation
# =============================================================================

def NavigationBar():
    """Create the fixed navigation bar at the top of the page."""
    return Nav(
        Div(
            A("🍝 SPINFOOD", href="#", cls=CLASS['navbar_logo']),
            Div(
                A("Für Teilnehmende", href="#", cls=f"{CLASS['navbar_link']} active"),
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

def HeroSection():
    """Create the main hero section with gradient background."""
    return Div(
        Div(
            Div(
                Div("SPINFOOD", cls=CLASS['logo']),
                Div("Food. Fun. Friends.", cls=CLASS['tagline']),
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
                    A("📍 Nächstes Event finden", href="#events",
                      cls=CLASS['hero_cta_primary']),
                    A("🎓 Event organisieren", href="#organizer",
                      cls=CLASS['hero_cta_secondary']),
                    cls=CLASS['hero_buttons']
                ),
                cls=CLASS['hero_content']
            ),
            Div(
                Div(
                    Div("👥", cls=CLASS['hero_image_icon']),
                    P("Studenten beim gemeinsamen Kochen"),
                    cls=CLASS['hero_image_placeholder']
                ),
                cls=CLASS['hero_image']
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
            Div("😔", style="font-size: 4rem; text-align: center; margin-bottom: 1rem;"),
            H2("Kennst du das?", cls=CLASS['section_title']),
            P(
                "Hunderte Anmeldungen in einer Excel-Tabelle. Endlose E-Mail-Ketten "
                "wegen Absagen und Nachrückern. Stundenlange manuelle Team-Zuteilung "
                "– und am Ende beschwert sich trotzdem jemand. Die Organisation eines "
                "Running Dinners kann zur Vollzeitbeschäftigung werden.",
                cls=CLASS['section_subtitle']
            ),
            P(
                "Muss nicht sein.",
                style="font-size: 1.8rem; font-weight: 700; text-align: center; "
                      "color: var(--primary-pink); margin-top: -1rem;"
            ),
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
            Div("🚀", style="font-size: 4rem; text-align: center; margin-bottom: 1rem;"),
            H2(
                "Running Dinner in deiner Stadt",
                style="font-size: 3.5rem; margin-bottom: 0.5rem; text-align: center; "
                      "color: var(--text-dark);"
            ),
            P(
                "Wir liefern die Plattform, ihr den Spaß",
                style="font-size: 2rem; font-weight: 600; text-align: center; "
                      "color: var(--primary-teal); margin-bottom: 2rem;"
            ),
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
        P(description, style="color: #495057; margin-bottom: 1rem;"),
        Button(
            "Mehr erfahren ↓",
            onclick=f"toggleExpand('{card_id}')",
            style="background: none; border: none; color: var(--primary-pink); "
                  "cursor: pointer; font-weight: 600; font-size: 1.1rem;"
        ),
        Div(
            P(details, style="margin-top: 1rem; color: #495057;"),
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
        accent_color: Optional accent color for the left border
    """
    style = f"border-left-color: {accent_color};" if accent_color else ""
    return Div(
        Div(
            Span(date, cls=CLASS['event_date']),
            H3(title),
            P(description, style="color: #495057;")
        ),
        A("Mehr →", href=link, cls=CLASS['event_cta']),
        cls=f"{CLASS['event_card']} {CLASS['fade_in']}",
        style=style
    )


def EventsSection():
    """Create the events section listing all current Running Dinner events."""
    # City-based accent colors for visual variety
    accent_colors = ["#E91E63", "#4CAF50", "#2196F3", "#FF9800"]

    return Section(
        Div(
            H2("Aktuelle Events", cls=CLASS['section_title']),
            P(
                "Finde das nächste Running Dinner in deiner Stadt",
                style="text-align: center; color: var(--text-light); margin-bottom: 2rem;"
            ),
            Div(
                *[EventCard(date, title, desc, link, accent_colors[i % len(accent_colors)])
                  for i, (date, title, desc, link) in enumerate(CURRENT_EVENTS)],
                style="max-width: 800px; margin: 0 auto;"
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
                    Span("veranstalten", cls="organizer-highlight"),
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
                    style="font-size: 1.3rem; color: var(--text-dark); "
                          "font-weight: 500; margin-bottom: 2rem;"
                ),
                Button(
                    "Jetzt Kontakt aufnehmen",
                    onclick="showContactModal()",
                    cls=CLASS['organizer_cta']
                ),
                cls=CLASS['organizer_text']
            ),
            Div(
                H3(
                    "Für wen ist Spinfood?",
                    style="color: var(--primary-pink); margin-bottom: 1rem; "
                          "font-size: 1.9rem;"
                ),
                P(
                    "Fachschaften, studentische Initiativen, AStAs und "
                    "Hochschulgruppen, die ein Running Dinner in ihrer Stadt "
                    "veranstalten möchten – ohne sich mit Excel-Tabellen und "
                    "E-Mail-Chaos herumzuschlagen.",
                    style="margin-bottom: 1.5rem; font-size: 1.3rem; line-height: 1.7;"
                ),
                P(
                    "Wir liefern nicht nur das Tool – wir stehen euch mit "
                    "Erfahrung zur Seite. Alles im Blick, alles unter Kontrolle.",
                    style="font-weight: 500; font-size: 1.3rem; line-height: 1.7;"
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
        P(text, style="font-style: italic; margin-bottom: 1rem;"),
        P(f"- {author}", style="color: var(--text-light);"),
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
            P(answer, style="color: #000000 !important; font-weight: 400 !important;"),
            cls=CLASS['faq_answer'],
            id=f"faq-answer-{item_id}",
            style="color: #000000 !important;"
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
                style="max-width: 800px; margin: 0 auto;"
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
                        src="/images/team.png",
                        alt="Spinfood Team",
                        style="width: 100%; height: 100%; object-fit: cover; "
                              "border-radius: 30px;"
                    ),
                    cls=CLASS['team_image']
                ),
                cls=CLASS['team_image_wrapper']
            ),
            Div(
                H2(
                    "Und wer steckt hinter ",
                    Span("Spinfood?"),
                    cls="team-title"
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
                    cls=CLASS['team_buttons']
                ),
                Div(
                    *[Div("📍", Span(loc), cls=CLASS['team_location'])
                      for loc in TEAM_LOCATIONS],
                    cls=CLASS['team_locations']
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
    """Create the partner universities section."""
    return Div(
        Div(
            H2("Vertraut von führenden Universitäten", cls=CLASS['partner_label']),
            P(
                "Viele tausende Studierende haben bereits über unsere Plattform an den Uni-Events teilgenommen",
                cls=CLASS['partner_subtitle']
            ),
            Div(
                *[Div(
                    Div(
                        Img(
                            src=img_path,
                            alt=alt_text,
                            style="width: 100%; height: 100%; object-fit: contain;"
                        ),
                        cls=CLASS['partner_logo']
                    ),
                    Span(name, cls=CLASS['partner_name']),
                    cls=CLASS['partner_logo_item']
                ) for img_path, alt_text, name in PARTNER_UNIVERSITIES],
                cls=CLASS['partner_logos']
            ),
            cls=CLASS['partner_container']
        ),
        cls=CLASS['partner_section']
    )


# =============================================================================
# Sponsors Section
# =============================================================================

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
                *[Div(
                    Div(icon, cls=CLASS['sponsor_icon']),
                    Div(name, cls=CLASS['sponsor_name']),
                    Div(sponsor_type, cls=CLASS['sponsor_type']),
                    cls=CLASS['sponsor_item']
                ) for icon, name, sponsor_type in SPONSOR_LIST],
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
                P("Running Dinner Events für Studenten in Deutschland."),
                Div(
                    A("📺 YouTube", href="#"),
                    A("📷 Instagram", href="#"),
                    cls=CLASS['social_links']
                ),
                cls=CLASS['footer_column']
            ),
            Div(
                H3("Support"),
                A("Kontakt", href="#", onclick="showContactModal(); return false;"),
                cls=CLASS['footer_column']
            ),
            Div(
                H3("Rechtliches"),
                A("Impressum", href="#"),
                A("Datenschutz", href="#"),
                A("AGB", href="#"),
                cls=CLASS['footer_column']
            ),
            cls=CLASS['footer_container']
        ),
        Div(
            P("© 2025 Spinfood. Made with ❤️ in Germany"),
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
