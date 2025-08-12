from fasthtml.common import *

# CSS styles
css = """
:root {
    --spinfood-pink: #E91E63;
    --spinfood-green: #4CAF50;
    --spinfood-dark: #2D3748;
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

.gradient-bg {
    background: linear-gradient(135deg, var(--spinfood-pink) 0%, var(--spinfood-green) 100%);
}

.text-gradient {
    background: linear-gradient(135deg, var(--spinfood-pink), var(--spinfood-green));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.smooth-scroll {
    scroll-behavior: smooth;
}

.fade-in {
    animation: fadeIn 0.6s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.hover-scale {
    transition: transform 0.3s ease;
}

.hover-scale:hover {
    transform: scale(1.05);
}

.btn-primary {
    background: var(--spinfood-pink) !important;
    color: white !important;
    padding: 16px 32px !important;
    border-radius: 50px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    display: inline-block !important;
    transition: all 0.3s ease !important;
    border: none !important;
    cursor: pointer !important;
    font-size: 18px !important;
    text-align: center !important;
    min-width: 200px !important;
}

.btn-primary:hover {
    background: #C2185B;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(233, 30, 99, 0.3);
}

.btn-secondary {
    background: transparent;
    color: var(--spinfood-green);
    border: 2px solid var(--spinfood-green);
    padding: 14px 30px;
    border-radius: 50px;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
}

.btn-secondary:hover {
    background: var(--spinfood-green);
    color: white;
}

.card {
    background: white !important;
    border-radius: 20px !important;
    padding: 32px !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1) !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    margin: 16px 8px !important;
    border: 1px solid #f0f0f0 !important;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.15);
}

.icon-circle {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: 0 auto 24px;
}

.faq-item {
    border-bottom: 1px solid #E2E8F0;
    padding: 24px 0;
}

.faq-question {
    font-weight: 600;
    color: var(--spinfood-dark);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    color: #64748B;
    line-height: 1.6;
}

.faq-answer.open {
    max-height: 200px;
    padding-top: 16px;
}

.event-card {
    background: white !important;
    border-radius: 16px !important;
    padding: 24px !important;
    border-left: 4px solid var(--spinfood-pink) !important;
    margin-bottom: 16px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
}

.container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    padding: 0 24px !important;
}

.text-center {
    text-align: center !important;
}

.grid {
    display: grid !important;
}

.gap-8 {
    gap: 2rem !important;
}

.gap-12 {
    gap: 3rem !important;
}

@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 2.5rem;
    }
    
    .btn-primary, .btn-secondary {
        display: block;
        text-align: center;
        margin: 8px 0;
    }
}
"""

# JavaScript for interactivity
js = """
function toggleFaq(element) {
    const answer = element.nextElementSibling;
    const icon = element.querySelector('span:last-child');
    
    if (answer.classList.contains('open')) {
        answer.classList.remove('open');
        icon.textContent = '+';
    } else {
        document.querySelectorAll('.faq-answer.open').forEach(item => {
            item.classList.remove('open');
            item.previousElementSibling.querySelector('span:last-child').textContent = '+';
        });
        
        answer.classList.add('open');
        icon.textContent = '−';
    }
}

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

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
});
"""

# Initialize FastHTML app
app, rt = fast_app()

def hero_section():
    return Section(
        Div(
            Div(
                Div(
                    H1("Neue Freunde beim ", Span("Running Dinner", cls="text-yellow-300"), 
                       cls="text-5xl lg:text-6xl font-bold mb-6 leading-tight text-white"),
                    P("Koche einen Gang, besuche zwei Häuser und lerne 6-12 neue Leute bei einem unvergesslichen Abend kennen.",
                      cls="text-xl mb-8 opacity-90 leading-relaxed text-white"),
                    Div(
                        A("Nächstes Event finden 🍽️", href="#events", cls="btn-primary"),
                        A("Wie es funktioniert", href="#how-it-works", cls="btn-secondary"),
                        cls="flex flex-col sm:flex-row gap-4"
                    ),
                    cls="hero-content fade-in"
                ),
                Div(
                    Div(
                        Img(src="https://images.unsplash.com/photo-1544717297-fa95b6ee9643?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
                            alt="Studenten beim gemeinsamen Kochen",
                            cls="rounded-2xl w-full h-80 object-cover"),
                        cls="bg-white bg-opacity-20 backdrop-blur-lg rounded-3xl p-8"
                    ),
                    cls="fade-in"
                ),
                cls="grid lg:grid-cols-2 gap-12 items-center"
            ),
            cls="container mx-auto px-6 py-20"
        ),
        cls="gradient-bg min-h-screen flex items-center relative overflow-hidden"
    )

def problem_section():
    return Section(
        Div(
            Div(
                H2("Kennst du das auch? 🤔", cls="text-4xl font-bold text-gray-800 mb-8"),
                Div(
                    Div(
                        Div("😔", cls="text-6xl mb-4"),
                        H3("Einsam im Studium", cls="text-xl font-semibold mb-4"),
                        P("Neue Stadt, neue Uni - aber wo sind die neuen Freunde?", cls="text-gray-600"),
                        cls="bg-white rounded-2xl p-8 shadow-lg"
                    ),
                    Div(
                        Div("🏠", cls="text-6xl mb-4"),
                        H3("Immer zuhause", cls="text-xl font-semibold mb-4"),
                        P("Netflix und Nudeln - jeden Abend das gleiche?", cls="text-gray-600"),
                        cls="bg-white rounded-2xl p-8 shadow-lg"
                    ),
                    Div(
                        Div("💭", cls="text-6xl mb-4"),
                        H3("Oberflächliche Kontakte", cls="text-xl font-semibold mb-4"),
                        P("Dating-Apps und Partys führen nur zu kurzen Begegnungen.", cls="text-gray-600"),
                        cls="bg-white rounded-2xl p-8 shadow-lg"
                    ),
                    cls="grid md:grid-cols-3 gap-8"
                ),
                cls="max-w-4xl mx-auto text-center"
            ),
            cls="container mx-auto px-6"
        ),
        cls="py-20 bg-gray-50"
    )

def solution_section():
    return Section(
        Div(
            Div(
                H2("So funktioniert's", cls="text-4xl font-bold text-gray-800 mb-4"),
                P("Ein Running Dinner ist dein Ticket zu echten Verbindungen und unvergesslichen Abenden.",
                  cls="text-xl text-gray-600 max-w-2xl mx-auto"),
                cls="text-center mb-16"
            ),
            Div(
                Div(
                    Div("👥", cls="icon-circle gradient-bg text-white"),
                    H3("1. Anmelden & Matchen", cls="text-2xl font-bold mb-4", style="color: var(--spinfood-pink)"),
                    P("Melde dich für das nächste Event an. Wir matchen dich mit anderen Teilnehmern in deiner Nähe.",
                      cls="text-gray-600 mb-6"),
                    Details(
                        Summary("Mehr erfahren", cls="cursor-pointer text-green-600 font-semibold"),
                        Div(
                            P("Du gibst deine Präferenzen an (vegetarisch, Allergien, etc.) und wir sorgen dafür, dass du mit passenden Leuten gematcht wirst. Jede Gruppe besteht aus 2-4 Personen.",
                              cls="text-sm text-gray-600"),
                            cls="mt-4 p-4 bg-gray-50 rounded-lg"
                        ),
                        cls="text-left"
                    ),
                    cls="text-center fade-in"
                ),
                Div(
                    Div("🍳", cls="icon-circle", style="background: var(--spinfood-green); color: white;"),
                    H3("2. Kochen & Besuchen", cls="text-2xl font-bold mb-4", style="color: var(--spinfood-green)"),
                    P("Koche eine Vorspeise, Hauptgang oder Dessert und besuche zwei andere Häuser für die anderen Gänge.",
                      cls="text-gray-600 mb-6"),
                    Details(
                        Summary("Mehr erfahren", cls="cursor-pointer text-green-600 font-semibold"),
                        Div(
                            P("Du bekommst einfache Rezepte und eine genaue Anleitung. Keine Sorge - du musst kein Profikoch sein! Jeder Gang dauert etwa 1,5 Stunden.",
                              cls="text-sm text-gray-600"),
                            cls="mt-4 p-4 bg-gray-50 rounded-lg"
                        ),
                        cls="text-left"
                    ),
                    cls="text-center fade-in"
                ),
                Div(
                    Div("🎉", cls="icon-circle text-white", style="background: var(--spinfood-pink);"),
                    H3("3. After-Party", cls="text-2xl font-bold mb-4", style="color: var(--spinfood-pink)"),
                    P("Alle Teilnehmer treffen sich zum Abschluss in einer Bar oder einem Café und feiern den gelungenen Abend.",
                      cls="text-gray-600 mb-6"),
                    Details(
                        Summary("Mehr erfahren", cls="cursor-pointer text-green-600 font-semibold"),
                        Div(
                            P("Bei der After-Party lernst du alle anderen Teilnehmer kennen und tauschst Kontakte aus. Hier entstehen oft die besten Freundschaften!",
                              cls="text-sm text-gray-600"),
                            cls="mt-4 p-4 bg-gray-50 rounded-lg"
                        ),
                        cls="text-left"
                    ),
                    cls="text-center fade-in"
                ),
                cls="grid md:grid-cols-3 gap-12 max-w-6xl mx-auto"
            ),
            cls="container mx-auto px-6"
        ),
        id="how-it-works",
        cls="py-20 bg-white"
    )

def benefits_section():
    return Section(
        Div(
            Div(
                H2("Warum Running Dinner?", cls="text-4xl font-bold text-gray-800 mb-4"),
                cls="text-center mb-16"
            ),
            Div(
                Div(
                    Div("🍽️", cls="text-6xl mb-6"),
                    H3("Food", cls="text-2xl font-bold mb-4 text-gradient"),
                    P("Entdecke neue Gerichte und lerne kochen von anderen. Jeder Gang ist eine kulinarische Überraschung!",
                      cls="text-gray-600"),
                    cls="card text-center hover-scale"
                ),
                Div(
                    Div("🎊", cls="text-6xl mb-6"),
                    H3("Fun", cls="text-2xl font-bold mb-4 text-gradient"),
                    P("Vergiss langweilige Partys! Bei uns erlebst du authentische Momente in gemütlicher Atmosphäre.",
                      cls="text-gray-600"),
                    cls="card text-center hover-scale"
                ),
                Div(
                    Div("👫", cls="text-6xl mb-6"),
                    H3("Friends", cls="text-2xl font-bold mb-4 text-gradient"),
                    P("Echte Verbindungen entstehen beim gemeinsamen Kochen und Essen. Nicht oberflächlich, sondern echt!",
                      cls="text-gray-600"),
                    cls="card text-center hover-scale"
                ),
                cls="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto"
            ),
            cls="container mx-auto px-6"
        ),
        cls="py-20 bg-gray-50"
    )

def events_section():
    return Section(
        Div(
            Div(
                H2("Nächste Events", cls="text-4xl font-bold text-gray-800 mb-4"),
                P("Melde dich jetzt für das nächste Running Dinner in deiner Stadt an!",
                  cls="text-xl text-gray-600"),
                cls="text-center mb-16"
            ),
            Div(
                Div(
                    Div(
                        Div(
                            H3("Berlin - Mitte", cls="text-2xl font-bold text-gray-800 mb-2"),
                            P("📅 Samstag, 24. August 2025 | 18:00 Uhr", cls="text-gray-600 mb-2"),
                            P("Noch 8 Plätze frei", cls="text-sm text-gray-500"),
                            cls="mb-4 md:mb-0"
                        ),
                        A("Jetzt anmelden - 25€", href="#signup", cls="btn-primary"),
                        cls="flex flex-col md:flex-row justify-between items-start md:items-center"
                    ),
                    cls="event-card"
                ),
                Div(
                    Div(
                        Div(
                            H3("München - Maxvorstadt", cls="text-2xl font-bold text-gray-800 mb-2"),
                            P("📅 Sonntag, 25. August 2025 | 17:30 Uhr", cls="text-gray-600 mb-2"),
                            P("Noch 12 Plätze frei", cls="text-sm text-gray-500"),
                            cls="mb-4 md:mb-0"
                        ),
                        A("Jetzt anmelden - 25€", href="#signup", cls="btn-primary"),
                        cls="flex flex-col md:flex-row justify-between items-start md:items-center"
                    ),
                    cls="event-card"
                ),
                Div(
                    Div(
                        Div(
                            H3("Hamburg - Sternschanze", cls="text-2xl font-bold text-gray-800 mb-2"),
                            P("📅 Freitag, 30. August 2025 | 18:30 Uhr", cls="text-gray-600 mb-2"),
                            P("⚡ Nur noch 3 Plätze!", cls="text-sm text-red-500"),
                            cls="mb-4 md:mb-0"
                        ),
                        A("Jetzt anmelden - 25€", href="#signup", cls="btn-primary"),
                        cls="flex flex-col md:flex-row justify-between items-start md:items-center"
                    ),
                    cls="event-card"
                ),
                cls="max-w-4xl mx-auto"
            ),
            cls="container mx-auto px-6"
        ),
        id="events",
        cls="py-20 bg-white"
    )

def social_proof_section():
    return Section(
        Div(
            Div(
                H2("Das sagen unsere Teilnehmer", cls="text-4xl font-bold text-gray-800 mb-4"),
                cls="text-center mb-16"
            ),
            Div(
                Div(
                    Div(
                        Img(src="https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80",
                            alt="Sarah", cls="w-12 h-12 rounded-full mr-4"),
                        Div(
                            H4("Sarah, 22", cls="font-semibold"),
                            P("Medizinstudentin, Berlin", cls="text-sm text-gray-500"),
                        ),
                        cls="flex items-center mb-4"
                    ),
                    P("\"Ich war super nervös, aber alle waren so freundlich! Habe drei neue Freundinnen gefunden und wir treffen uns jetzt regelmäßig.\"",
                      cls="text-gray-600 italic"),
                    cls="bg-white rounded-2xl p-8 shadow-lg"
                ),
                Div(
                    Div(
                        Img(src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80",
                            alt="Marco", cls="w-12 h-12 rounded-full mr-4"),
                        Div(
                            H4("Marco, 24", cls="font-semibold"),
                            P("BWL-Student, München", cls="text-sm text-gray-500"),
                        ),
                        cls="flex items-center mb-4"
                    ),
                    P("\"Endlich mal was anderes als Bars und Clubs! Die Atmosphäre war entspannt und ich habe richtig coole Leute kennengelernt.\"",
                      cls="text-gray-600 italic"),
                    cls="bg-white rounded-2xl p-8 shadow-lg"
                ),
                Div(
                    Div(
                        Img(src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80",
                            alt="Lisa", cls="w-12 h-12 rounded-full mr-4"),
                        Div(
                            H4("Lisa, 21", cls="font-semibold"),
                            P("Psychologie, Hamburg", cls="text-sm text-gray-500"),
                        ),
                        cls="flex items-center mb-4"
                    ),
                    P("\"Ich kann gar nicht kochen, aber das war kein Problem! Alle haben sich gegenseitig geholfen und es war einfach lustig.\"",
                      cls="text-gray-600 italic"),
                    cls="bg-white rounded-2xl p-8 shadow-lg"
                ),
                cls="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto"
            ),
            Div(
                Div(
                    Div(
                        Div("2,500+", cls="text-3xl font-bold text-gradient"),
                        Div("Teilnehmer", cls="text-sm"),
                        cls="text-center"
                    ),
                    Div(
                        Div("180+", cls="text-3xl font-bold text-gradient"),
                        Div("Events", cls="text-sm"),
                        cls="text-center"
                    ),
                    Div(
                        Div("95%", cls="text-3xl font-bold text-gradient"),
                        Div("Weiterempfehlung", cls="text-sm"),
                        cls="text-center"
                    ),
                    cls="flex justify-center items-center space-x-8 text-gray-600"
                ),
                cls="text-center mt-12"
            ),
            cls="container mx-auto px-6"
        ),
        cls="py-20 bg-gray-50"
    )

def faq_section():
    return Section(
        Div(
            Div(
                H2("Häufige Fragen", cls="text-4xl font-bold text-gray-800 mb-4"),
                cls="text-center mb-16"
            ),
            Div(
                Div(
                    Div("Muss ich gut kochen können?", Span("+", cls="text-2xl"), 
                        cls="faq-question", onclick="toggleFaq(this)"),
                    Div(P("Nein! Du bekommst einfache Rezepte und Anleitungen. Es geht um den Spaß, nicht um Perfektion. Auch Anfänger sind herzlich willkommen!"),
                        cls="faq-answer"),
                    cls="faq-item"
                ),
                Div(
                    Div("Was kostet die Teilnahme?", Span("+", cls="text-2xl"), 
                        cls="faq-question", onclick="toggleFaq(this)"),
                    Div(P("Die Teilnahme kostet 25€. Darin enthalten sind die Organisation, Rezepte, ein kleines Starter-Kit und der Eintritt zur After-Party."),
                        cls="faq-answer"),
                    cls="faq-item"
                ),
                Div(
                    Div("Ist das sicher?", Span("+", cls="text-2xl"), 
                        cls="faq-question", onclick="toggleFaq(this)"),
                    Div(P("Ja! Alle Teilnehmer werden verifiziert und wir haben ein Support-Team, das während des Events erreichbar ist. Du bekommst vorher alle Kontaktdaten."),
                        cls="faq-answer"),
                    cls="faq-item"
                ),
                Div(
                    Div("Was ist mit Allergien und Unverträglichkeiten?", Span("+", cls="text-2xl"), 
                        cls="faq-question", onclick="toggleFaq(this)"),
                    Div(P("Gib deine Allergien und Ernährungsgewohnheiten bei der Anmeldung an. Wir matchen dich entsprechend und stellen passende Rezepte zur Verfügung."),
                        cls="faq-answer"),
                    cls="faq-item"
                ),
                Div(
                    Div("Kann ich mich auch mit Freunden anmelden?", Span("+", cls="text-2xl"), 
                        cls="faq-question", onclick="toggleFaq(this)"),
                    Div(P("Klar! Du kannst dich mit bis zu 3 Freunden als Gruppe anmelden. Ihr werdet dann gemeinsam gematcht und kocht zusammen."),
                        cls="faq-answer"),
                    cls="faq-item"
                ),
                cls="max-w-3xl mx-auto"
            ),
            cls="container mx-auto px-6"
        ),
        cls="py-20 bg-white"
    )

def cta_section():
    return Section(
        Div(
            H2("Bereit für dein erstes Running Dinner?", cls="text-4xl lg:text-5xl font-bold text-white mb-6"),
            P("Melde dich jetzt für das nächste Event an und erlebe einen unvergesslichen Abend voller neuer Freundschaften!",
              cls="text-xl text-white opacity-90 mb-8 max-w-2xl mx-auto"),
            Div(
                A("Event auswählen", href="#events", cls="btn-primary bg-white text-pink-600 hover:bg-gray-100"),
                A("Noch Fragen?", href="#how-it-works", cls="btn-secondary border-white text-white hover:bg-white hover:text-pink-600"),
                cls="flex flex-col sm:flex-row gap-4 justify-center"
            ),
            cls="container mx-auto px-6 text-center"
        ),
        id="signup",
        cls="py-20 gradient-bg"
    )

def footer_section():
    return Footer(
        Div(
            Div(
                Div(
                    H3("Spinfood", cls="text-2xl font-bold mb-4 text-gradient"),
                    P("Running Dinner Events für Studenten in Deutschland.", cls="text-gray-400 mb-4"),
                    Div(
                        A("📘 Facebook", href="#", cls="text-gray-400 hover:text-white"),
                        A("📷 Instagram", href="#", cls="text-gray-400 hover:text-white"),
                        cls="flex space-x-4"
                    )
                ),
                Div(
                    H4("Events", cls="font-semibold mb-4"),
                    Ul(
                        Li(A("Berlin", href="#", cls="hover:text-white")),
                        Li(A("München", href="#", cls="hover:text-white")),
                        Li(A("Hamburg", href="#", cls="hover:text-white")),
                        Li(A("Köln", href="#", cls="hover:text-white")),
                        cls="space-y-2 text-gray-400"
                    )
                ),
                Div(
                    H4("Support", cls="font-semibold mb-4"),
                    Ul(
                        Li(A("FAQ", href="#", cls="hover:text-white")),
                        Li(A("Kontakt", href="#", cls="hover:text-white")),
                        Li(A("Hilfe", href="#", cls="hover:text-white")),
                        cls="space-y-2 text-gray-400"
                    )
                ),
                Div(
                    H4("Rechtliches", cls="font-semibold mb-4"),
                    Ul(
                        Li(A("Impressum", href="#", cls="hover:text-white")),
                        Li(A("Datenschutz", href="#", cls="hover:text-white")),
                        Li(A("AGB", href="#", cls="hover:text-white")),
                        cls="space-y-2 text-gray-400"
                    )
                ),
                cls="grid md:grid-cols-4 gap-8"
            ),
            Div(
                P("© 2025 Spinfood. Alle Rechte vorbehalten.", cls="text-center text-gray-400"),
                cls="border-t border-gray-700 mt-12 pt-8"
            ),
            cls="container mx-auto px-6"
        ),
        cls="bg-gray-800 text-white py-16"
    )

@rt("/")
def get():
    return Html(
        Head(
            Title("Spinfood - Running Dinner Events für Studenten"),
            Meta(name="description", content="Lerne neue Leute bei Running Dinner Events kennen. Koche, esse und feiere mit anderen Studenten in deiner Stadt."),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(charset="UTF-8"),
            Link(rel="stylesheet", href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"),
            Style(css),
            Script(js)
        ),
        Body(
            hero_section(),
            problem_section(),
            solution_section(),
            benefits_section(),
            events_section(),
            social_proof_section(),
            faq_section(),
            cta_section(),
            footer_section(),
            cls="smooth-scroll"
        ),
        lang="de"
    )

# Additional routes for form handling
@rt("/signup")
def post(name: str, email: str, event: str):
    return Div(
        H2("Anmeldung erhalten!", cls="text-2xl font-bold text-green-600 mb-4"),
        P(f"Danke {name}! Wir haben deine Anmeldung für {event} erhalten."),
        P(f"Eine Bestätigungsmail wurde an {email} gesendet."),
        A("Zurück zur Startseite", href="/", cls="btn-primary mt-4"),
        cls="container mx-auto px-6 py-20 text-center"
    )

if __name__ == "__main__":
    serve()