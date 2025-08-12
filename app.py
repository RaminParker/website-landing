from fasthtml.common import *

# Custom CSS as a string
custom_css = """
:root {
    --primary-pink: #E91E63;
    --primary-teal: #4CAF50;
    --dark-teal: #2E7D32;
    --light-pink: #FCE4EC;
    --light-teal: #E8F5E9;
    --text-dark: #212121;
    --text-light: #757575;
    --white: #FFFFFF;
    --gray-light: #F5F5F5;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    color: var(--text-dark);
    line-height: 1.6;
    overflow-x: hidden;
}

section {
    border: none !important;
    outline: none !important;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.section-title {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    text-align: center;
    color: var(--text-dark);
}

.section-subtitle {
    font-size: 1.4rem;
    color: var(--text-light);
    text-align: center;
    max-width: 800px;
    margin: 0 auto 3rem;
    line-height: 1.8;
}

.hero {
    min-height: 100vh;
    background: linear-gradient(135deg, #F48FB1 0%, #81C784 100%);
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    padding: 0;
}

.hero-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 40px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    width: 100%;
}

.hero-content {
    text-align: left;
}

.hero-title {
    font-size: clamp(3rem, 6vw, 4.5rem);
    line-height: 1.1;
    margin-bottom: 2rem;
    color: white;
    font-weight: 700;
}

.hero-title .highlight {
    color: #FFE082;
    display: block;
}

.hero-subtitle {
    font-size: 1.5rem;
    color: rgba(255,255,255,0.9);
    margin-bottom: 3rem;
    line-height: 1.6;
    font-weight: 400;
}

.hero-buttons {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.hero-cta-primary {
    background: var(--primary-pink);
    color: white;
    padding: 1.2rem 2.8rem;
    font-size: 1.2rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.hero-cta-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(0,0,0,0.3);
    background: #D81B60;
}

.hero-cta-secondary {
    background: transparent;
    color: white;
    padding: 1.2rem 2.8rem;
    font-size: 1.2rem;
    border: 2px solid rgba(255,255,255,0.8);
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
}

.hero-cta-secondary:hover {
    background: rgba(255,255,255,0.2);
    border-color: white;
    transform: translateY(-3px);
}

.hero-image {
    position: relative;
    height: 600px;
    border-radius: 20px;
    overflow: hidden;
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
}

.hero-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 20px;
}

.hero-image-placeholder {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: white;
    font-size: 1.2rem;
}

.hero-image-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
}

.logo {
    font-size: 2rem;
    font-weight: bold;
    color: white;
    margin-bottom: 3rem;
    letter-spacing: -1px;
}

.tagline {
    color: rgba(255,255,255,0.8);
    font-size: 1rem;
    margin-top: -2.5rem;
    margin-bottom: 2rem;
}

@media (max-width: 968px) {
    .hero-container {
        grid-template-columns: 1fr;
        gap: 40px;
        padding: 40px 20px;
    }
    
    .hero-content {
        text-align: center;
    }
    
    .hero-buttons {
        justify-content: center;
    }
    
    .hero-image {
        height: 400px;
        max-width: 500px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
    }
}

.section {
    padding: 100px 20px;
    border: none;
    margin: 0;
}

.bg-white { 
    background: white;
    border: none;
}

.bg-gray { 
    background: #F5F5F5;
    border: none;
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.step-card {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    text-align: center;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    position: relative;
}

.step-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, var(--primary-pink), var(--primary-teal));
    border-radius: 20px 20px 0 0;
}

.step-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.12);
}

.step-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
}

.step-card p {
    font-size: 1.1rem;
    line-height: 1.6;
}

.step-number {
    display: inline-block;
    width: 50px;
    height: 50px;
    line-height: 50px;
    background: var(--primary-teal);
    color: white;
    border-radius: 50%;
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.step-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.benefit-card {
    background: linear-gradient(135deg, var(--primary-pink), var(--primary-teal));
    padding: 3rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.benefit-card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.benefit-icon {
    font-size: 4.5rem;
    margin-bottom: 1.5rem;
}

.benefit-card h3 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.benefit-card p {
    font-size: 1.2rem;
    line-height: 1.6;
}

.event-card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
    border-left: 5px solid var(--primary-teal);
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.event-card:hover {
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transform: translateX(8px);
}

.event-date {
    background: var(--light-teal);
    color: var(--dark-teal);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 1rem;
    display: inline-block;
    margin-bottom: 0.8rem;
    font-weight: 600;
}

.event-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.event-card p {
    font-size: 1.1rem;
}

.event-cta {
    background: var(--text-dark);
    color: white;
    padding: 0.7rem 1.5rem;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    font-weight: 600;
    white-space: nowrap;
}

.event-cta:hover {
    background: var(--primary-pink);
    transform: scale(1.05);
}

.faq-item {
    background: white;
    margin-bottom: 1rem;
    border-radius: 10px;
    overflow: hidden;
}

.faq-question {
    padding: 1.5rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    transition: background 0.3s ease;
}

.faq-question:hover {
    background: var(--light-teal);
}

.faq-answer {
    padding: 0 1.5rem 1.5rem;
    color: var(--text-light);
    display: none;
}

.faq-item.active .faq-answer {
    display: block;
}

.testimonial-card {
    background: white;
    padding: 2.5rem;
    border-radius: 15px;
    margin: 2rem auto;
    max-width: 900px;
    position: relative;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.testimonial-card p {
    font-size: 1.2rem;
}

.testimonial-card::before {
    content: '"';
    position: absolute;
    top: -10px;
    left: 20px;
    font-size: 4rem;
    color: var(--primary-pink);
    opacity: 0.3;
}

.cta-section {
    padding: 100px 20px;
    background: linear-gradient(135deg, var(--primary-pink) 0%, var(--primary-teal) 100%);
    text-align: center;
    color: white;
}

.cta-section h2 {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    font-weight: 700;
}

.cta-section p {
    font-size: 1.4rem;
    margin-bottom: 3rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.95;
}

.cta-buttons {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
}

.cta-button-primary {
    background: var(--primary-pink);
    color: white;
    padding: 1rem 2.5rem;
    font-size: 1.2rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.cta-button-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    background: #D81B60;
}

.cta-button-secondary {
    background: transparent;
    color: white;
    padding: 1rem 2.5rem;
    font-size: 1.2rem;
    border: 2px solid white;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
}

.cta-button-secondary:hover {
    background: white;
    color: var(--primary-pink);
    transform: translateY(-2px);
}

.footer-section {
    background: #2C3E50;
    color: white;
    padding: 60px 20px 40px;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 3rem;
}

.footer-column h3 {
    color: var(--primary-pink);
    margin-bottom: 1rem;
    font-size: 1.3rem;
}

.footer-column p {
    margin-bottom: 1rem;
    opacity: 0.9;
    line-height: 1.6;
}

.footer-column a {
    color: white;
    text-decoration: none;
    display: block;
    margin-bottom: 0.8rem;
    transition: color 0.3s ease;
    opacity: 0.9;
}

.footer-column a:hover {
    color: var(--primary-teal);
    opacity: 1;
}

.social-links {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.social-links a {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.footer-bottom {
    text-align: center;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    opacity: 0.7;
}

@media (max-width: 768px) {
    .footer-container {
        grid-template-columns: 1fr;
        text-align: center;
    }
    
    .social-links {
        justify-content: center;
    }
    
    .cta-section h2 {
        font-size: 2rem;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
}

.expandable {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
}

.expandable.show {
    max-height: 500px;
}

.bg-white { background: white; }
.bg-gray { background: var(--gray-light); }

@media (max-width: 768px) {
    .event-card {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }
    
    .cards-grid {
        grid-template-columns: 1fr;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
    
    .section-title {
        font-size: 1.8rem;
    }
}
"""

# JavaScript code
js_code = """
function toggleExpand(id) {
    const element = document.getElementById(id);
    element.classList.toggle('show');
    const button = element.previousElementSibling;
    if (element.classList.contains('show')) {
        button.textContent = 'Weniger ↑';
    } else {
        button.textContent = 'Mehr erfahren ↓';
    }
}

function toggleFAQ(id) {
    const faqItem = document.getElementById(id);
    faqItem.classList.toggle('active');
    const answer = document.getElementById('faq-answer-' + id);
    if (faqItem.classList.contains('active')) {
        answer.style.display = 'block';
    } else {
        answer.style.display = 'none';
    }
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
"""

# Initialize FastHTML app
app, rt = fast_app()

# Hero Section Component
def HeroSection():
    return Div(
        Div(
            Div(
                Div("SPINFOOD", cls="logo"),
                Div("Food. Fun. Friends.", cls="tagline"),
                H1(
                    "Neue Freunde beim ",
                    Span("Running Dinner", cls="highlight"),
                    cls="hero-title"
                ),
                P(
                    "Koche einen Gang, besuche zwei Häuser und lerne 6-12 neue Leute bei einem unvergesslichen Abend kennen.",
                    cls="hero-subtitle"
                ),
                Div(
                    A(
                        "📍 Nächstes Event finden",
                        href="#events",
                        cls="hero-cta-primary"
                    ),
                    A(
                        "Wie es funktioniert",
                        href="#how",
                        cls="hero-cta-secondary"
                    ),
                    cls="hero-buttons"
                ),
                cls="hero-content"
            ),
            Div(
                Div(
                    Div("👥", cls="hero-image-icon"),
                    P("Studenten beim gemeinsamen Kochen"),
                    cls="hero-image-placeholder"
                ),
                cls="hero-image"
            ),
            cls="hero-container"
        ),
        cls="hero"
    )

# Problem Section Component
def ProblemSection():
    return Div(
        Div(
            Div("😔", style="font-size: 4rem; text-align: center; margin-bottom: 1rem;"),
            H2("Kennst du das?", cls="section-title"),
            P(
                "Neue Stadt, neues Studium, aber keine neuen Freunde? "
                "Die immer gleichen Leute im Hörsaal und in der Mensa? "
                "Zeit, das zu ändern!",
                cls="section-subtitle"
            ),
            cls="container"
        ),
        cls="section bg-white"
    )

# Step Card Component
def StepCard(number, icon, title, description, details):
    card_id = f"step-{number}"
    return Div(
        Div(str(number), cls="step-number"),
        Div(icon, cls="step-icon"),
        H3(title),
        P(description, style="color: var(--text-light); margin-bottom: 1rem;"),
        Button(
            "Mehr erfahren ↓",
            onclick=f"toggleExpand('{card_id}')",
            style="background: none; border: none; color: var(--primary-pink); cursor: pointer; font-weight: 600; font-size: 1.1rem;"
        ),
        Div(
            P(details, style="margin-top: 1rem; color: var(--text-light);"),
            id=card_id,
            cls="expandable"
        ),
        cls="step-card"
    )

# How It Works Section
def HowItWorksSection():
    return Div(
        Div(
            H2("So funktioniert's", cls="section-title"),
            Div(
                StepCard(
                    1, "📝", 
                    "Anmelden & gematcht werden",
                    "Melde dich online an und werde einem Kochteam zugeteilt.",
                    "Du meldest dich als 2er-Team oder alleine an. Wir teilen dich einem Gang zu (Vorspeise, Hauptgang oder Dessert) und matchen dich mit anderen Teilnehmern. Keine Sorge - auch Kochanfänger sind willkommen!"
                ),
                StepCard(
                    2, "🍽️",
                    "1 Gang kochen, 2 Häuser besuchen",
                    "Koche einen Gang zuhause und besuche zwei andere Teams.",
                    "Du kochst nur einen Gang für 4-6 Personen bei dir zuhause. Die anderen beiden Gänge genießt du bei anderen Teilnehmern. So lernst du verschiedene Wohnungen und Stadtteile kennen!"
                ),
                StepCard(
                    3, "🎉",
                    "After-Party mit allen",
                    "Triff alle Teilnehmer bei der gemeinsamen Party.",
                    "Nach dem Dinner treffen sich alle Teilnehmer zur After-Party. Hier kannst du die Leute wiedertreffen und neue Kontakte knüpfen. Die Party geht oft bis in die Nacht!"
                ),
                cls="cards-grid"
            ),
            cls="container"
        ),
        cls="section bg-gray"
    )

# Benefit Card Component
def BenefitCard(icon, title, text):
    return Div(
        Div(icon, cls="benefit-icon"),
        H3(title),
        P(text),
        cls="benefit-card"
    )

# Benefits Section
def BenefitsSection():
    return Section(
        Div(
            H2("Was erwartet dich?", cls="section-title"),
            Div(
                BenefitCard("🍝", "Food", "Leckere Gerichte bei dir und anderen. Von einfach bis extravagant - alles dabei!"),
                BenefitCard("✨", "Fun", "Ein Abend voller Überraschungen und die legendäre After-Party zum Abschluss."),
                BenefitCard("👥", "Friends", "6-12 neue Leute an einem Abend. Perfekt um dein Netzwerk zu erweitern!"),
                cls="cards-grid"
            ),
            cls="container"
        ),
        cls="section bg-white"
    )

# Event Card Component
def EventCard(date, title, description):
    return Div(
        Div(
            Span(date, cls="event-date"),
            H3(title),
            P(description, style="color: var(--text-light);")
        ),
        A("Mehr →", href="#", cls="event-cta"),
        cls="event-card"
    )

# Events Section
def EventsSection():
    events = [
        ("Sommersemester 2025", "Gießen-kocht!", "Das Gießener Kult-Event - seit Jahren einmal pro Semester"),
        ("Wintersemester 24/25", "Marburg-kocht!", "Organisiert durch die Studiengruppe der Uni Marburg"),
        ("Sommersemester 2025", "BamBuS Dinner", "Organisiert durch die Studierendengruppe BamBuS"),
        ("Sommersemester 2025", "Laufgelage Erlangen", "Hochschulgruppe Erlangen-Nürnberg"),
        ("Sommersemester 2025", "Running Dinner Würzburg", "Studierendenvertretung der Uni Würzburg")
    ]
    
    return Section(
        Div(
            H2("Aktuelle Events", cls="section-title"),
            P(
                "Finde das nächste Running Dinner in deiner Stadt",
                style="text-align: center; color: var(--text-light); margin-bottom: 2rem;"
            ),
            Div(
                *[EventCard(date, title, desc) for date, title, desc in events],
                style="max-width: 800px; margin: 0 auto;"
            ),
            cls="container"
        ),
        id="events",
        cls="section bg-gray"
    )

# Testimonial Component
def TestimonialCard(text, author):
    return Div(
        P(text, style="font-style: italic; margin-bottom: 1rem;"),
        P(f"- {author}", style="color: var(--text-light);"),
        cls="testimonial-card"
    )

# Testimonials Section
def TestimonialsSection():
    return Section(
        Div(
            H2("Das sagen Teilnehmer", cls="section-title"),
            TestimonialCard(
                "Ich war neu in der Stadt und kannte niemanden. Nach dem Running Dinner hatte ich direkt eine Gruppe von Freunden, mit denen ich heute noch regelmäßig was unternehme!",
                "Lisa, Teilnehmerin in Marburg"
            ),
            TestimonialCard(
                "Die Mischung aus Kochen, neuen Leuten und Party ist einfach perfekt. Ich war schon bei 3 Events dabei und es war jedes Mal großartig!",
                "Tom, Teilnehmer in Gießen"
            ),
            cls="container"
        ),
        cls="section bg-white"
    )

# FAQ Item Component
def FAQItem(question, answer, item_id):
    return Div(
        Div(
            Span(question),
            Span("▼", style="color: var(--primary-teal);"),
            cls="faq-question",
            onclick=f"toggleFAQ('{item_id}')"
        ),
        Div(
            P(answer),
            cls="faq-answer",
            id=f"faq-answer-{item_id}"
        ),
        cls="faq-item",
        id=item_id
    )

# FAQ Section
def FAQSection():
    faqs = [
        ("Muss ich gut kochen können?", 
         "Nein! Es geht nicht um Perfektion, sondern um Spaß. Auch einfache Gerichte sind willkommen. Viele kochen Pasta, Salat oder bestellen sogar Pizza - Hauptsache, ihr habt eine gute Zeit!"),
        ("Kann ich mich auch alleine anmelden?",
         "Ja, absolut! Viele melden sich alleine an. Wir matchen dich dann mit einem anderen Single zu einem Kochteam. So lernst du direkt noch mehr Leute kennen!"),
        ("Was ist mit Allergien oder vegetarisch/vegan?",
         "Bei der Anmeldung kannst du alle Allergien und Präferenzen angeben. Wir berücksichtigen das beim Matching und informieren deine Gastgeber. Vegetarische und vegane Optionen sind mittlerweile Standard!"),
        ("Wie viel kostet die Teilnahme?",
         "Die Teilnahmegebühr variiert je nach Stadt, liegt aber meist zwischen 3-5€. Das deckt die Organisationskosten und manchmal einen Welcome-Drink bei der After-Party."),
        ("Ist das sicher?",
         "Ja! Alle Teilnehmer sind verifizierte Studierende. Du bekommst die Adressen erst kurz vorher und gehst nie alleine zu einem Haus. Bei Problemen ist das Orga-Team immer erreichbar.")
    ]
    
    return Section(
        Div(
            H2("Häufige Fragen", cls="section-title"),
            Div(
                *[FAQItem(q, a, f"faq-{i}") for i, (q, a) in enumerate(faqs)],
                style="max-width: 800px; margin: 0 auto;"
            ),
            cls="container"
        ),
        cls="section bg-gray"
    )

# CTA Section Component
def CTASection():
    return Div(
        H2("Bereit für dein erstes Running Dinner?"),
        P("Melde dich jetzt für das nächste Event an und erlebe einen unvergesslichen Abend voller neuer Freundschaften!"),
        Div(
            A("Event auswählen", href="#events", cls="cta-button-primary"),
            A("Noch Fragen?", href="#faq", cls="cta-button-secondary"),
            cls="cta-buttons"
        ),
        cls="cta-section"
    )

# Footer Component
def FooterSection():
    return Div(
        Div(
            Div(
                H3("Spinfood"),
                P("Running Dinner Events für Studenten in Deutschland."),
                Div(
                    A("📘 Facebook", href="#"),
                    A("📷 Instagram", href="#"),
                    cls="social-links"
                ),
                cls="footer-column"
            ),
            Div(
                H3("Events"),
                A("Berlin", href="#"),
                A("München", href="#"),
                A("Hamburg", href="#"),
                A("Köln", href="#"),
                cls="footer-column"
            ),
            Div(
                H3("Support"),
                A("FAQ", href="#faq"),
                A("Kontakt", href="#"),
                A("Hilfe", href="#"),
                cls="footer-column"
            ),
            Div(
                H3("Rechtliches"),
                A("Impressum", href="#"),
                A("Datenschutz", href="#"),
                A("AGB", href="#"),
                cls="footer-column"
            ),
            cls="footer-container"
        ),
        Div(
            P("© 2024 Spinfood. Made with ❤️ in Germany"),
            cls="footer-bottom"
        ),
        cls="footer-section"
    )

# Main route
@rt("/")
def get():
    return Title("Spinfood - Running Dinner für Studierende"), \
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"), \
        Meta(name="description", content="Triff 6-12 neue Leute an einem Abend beim Running Dinner in deiner Uni-Stadt. Food, Fun & Friends - Jetzt anmelden!"), \
        Style(custom_css), \
        Script(js_code), \
        HeroSection(), \
        ProblemSection(), \
        HowItWorksSection(), \
        BenefitsSection(), \
        EventsSection(), \
        TestimonialsSection(), \
        FAQSection(), \
        CTASection(), \
        FooterSection()

# Serve the app
serve()