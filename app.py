#!/usr/bin/env python3
"""
Spinfood Landing Page
======================
A FastHTML-based landing page for Spinfood - a platform for organizing
Running Dinner events at German universities.

This is the main application entry point. All components and configuration
are imported from their respective modules.
"""

import logging

from fasthtml.common import fast_app, serve, Title, Meta, Link, Script
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse

from config import APP_TITLE, APP_DESCRIPTION
from components import (
    NavigationBar, HeroSection, ProblemSection, SolutionSection,
    HowItWorksSection, BenefitsSection, EventsSection, OrganizerSection,
    TestimonialsSection, FAQSection, CTASection, TeamSection, PartnerSection,
    SponsorsSection, FooterSection, ContactModal,
    AGBNavigation, AGBPageContent, ImpressumPageContent, DatenschutzPageContent,
    UeberUnsPageContent
)

# =============================================================================
# Logging Configuration
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# =============================================================================
# Application Setup
# =============================================================================

app, rt = fast_app()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

logger.info("Application initialized")

# =============================================================================
# Routes
# =============================================================================

@rt("/favicon.ico")
def favicon():
    """Serve favicon from logo image."""
    return FileResponse("images/intern/logo.png", media_type="image/png")


@rt("/")
def get():
    """
    Main route handler for the landing page.
    Assembles all components in the correct order.
    """
    logger.info("Serving landing page")

    return (
        # Page metadata
        Title(APP_TITLE),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content=APP_DESCRIPTION),

        # External CSS and JS
        Link(rel="icon", type="image/png", href="/images/intern/logo.png"),
        Link(rel="stylesheet", href="/static/css/styles.css"),
        Script(src="/static/js/main.js", defer=True),

        # Page components
        NavigationBar(),
        HeroSection(),
        ProblemSection(),          # 1) Kennst du das?
        SolutionSection(),         # 2) Running Dinner in deiner Stadt
        BenefitsSection(),         # 3) Was ist ein Running Dinner Event
        HowItWorksSection(),       # 4) So funktioniert's
        EventsSection(),
        OrganizerSection(),
        TestimonialsSection(),
        FAQSection(),
        CTASection(),
        TeamSection(),
        PartnerSection(),
        SponsorsSection(),
        FooterSection(),
        ContactModal()
    )


@rt("/agb")
def get_agb():
    """
    Route handler for the AGB (Terms & Conditions) page.
    Displays all terms and conditions in a clean, readable format.
    """
    logger.info("Serving AGB page")

    return (
        # Page metadata
        Title("AGB - Spinfood"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Allgemeine Geschäftsbedingungen für Spinfood"),

        # External CSS and JS
        Link(rel="icon", type="image/png", href="/images/intern/logo.png"),
        Link(rel="stylesheet", href="/static/css/styles.css"),

        # Page components
        AGBNavigation(),
        AGBPageContent(),
        FooterSection()
    )


@rt("/impressum")
def get_impressum():
    """
    Route handler for the Impressum (Legal Notice) page.
    Displays all legal information required by German law (§ 5 TMG).
    """
    logger.info("Serving Impressum page")

    return (
        # Page metadata
        Title("Impressum - Spinfood"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Impressum und rechtliche Angaben von Spinfood"),

        # External CSS and JS
        Link(rel="icon", type="image/png", href="/images/intern/logo.png"),
        Link(rel="stylesheet", href="/static/css/styles.css"),

        # Page components
        AGBNavigation(),
        ImpressumPageContent(),
        FooterSection()
    )


@rt("/datenschutz")
def get_datenschutz():
    """
    Route handler for the Datenschutz (Privacy Policy) page.
    Displays all privacy information according to DSGVO and BDSG.
    """
    logger.info("Serving Datenschutz page")

    return (
        # Page metadata
        Title("Datenschutz - Spinfood"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Datenschutzerklärung von Spinfood gemäß DSGVO"),

        # External CSS and JS
        Link(rel="icon", type="image/png", href="/images/intern/logo.png"),
        Link(rel="stylesheet", href="/static/css/styles.css"),

        # Page components
        AGBNavigation(),
        DatenschutzPageContent(),
        FooterSection()
    )


@rt("/ueber-uns")
def get_ueber_uns():
    """
    Route handler for the Über uns (About) page.
    Presents the team, philosophy, and partnership information.
    """
    logger.info("Serving Über uns page")

    return (
        # Page metadata
        Title("Über uns - Spinfood"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Lerne das Team hinter Spinfood kennen"),

        # External CSS and JS
        Link(rel="icon", type="image/png", href="/images/intern/logo.png"),
        Link(rel="stylesheet", href="/static/css/styles.css"),
        Script(src="/static/js/main.js", defer=True),

        # Page components
        AGBNavigation(),
        UeberUnsPageContent(),
        FooterSection(),
        ContactModal()
    )


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    logger.info("Starting Spinfood Landing Page server")
    serve()
