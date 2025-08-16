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
    font-size: 18px;
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
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    text-align: center;
    color: var(--text-dark);
}

.section-subtitle {
    font-size: 1.6rem;
    color: var(--text-light);
    text-align: center;
    max-width: 900px;
    margin: 0 auto 3rem;
    line-height: 1.8;
}

.hero {
    min-height: 100vh;
    background: linear-gradient(135deg, #E91E63 0%, #4CAF50 100%);
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
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.hero-title .highlight {
    color: #FFEB3B;
    display: block;
    text-shadow: 0 2px 15px rgba(255,235,59,0.3);
}

.hero-subtitle {
    font-size: 1.5rem;
    color: rgba(255,255,255,0.95);
    margin-bottom: 3rem;
    line-height: 1.6;
    font-weight: 400;
    text-shadow: 0 1px 5px rgba(0,0,0,0.15);
}

.hero-buttons {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.hero-cta-primary {
    background: #E91E63;
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
    box-shadow: 0 6px 25px rgba(233,30,99,0.4);
    text-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.hero-cta-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(233,30,99,0.5);
    background: #C2185B;
}

.hero-cta-secondary {
    background: rgba(255,255,255,0.15);
    color: white;
    padding: 1.2rem 2.8rem;
    font-size: 1.2rem;
    border: 2px solid rgba(255,255,255,0.9);
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
    backdrop-filter: blur(10px);
    text-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.hero-cta-secondary:hover {
    background: rgba(255,255,255,0.25);
    border-color: white;
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(255,255,255,0.2);
}

.hero-image {
    position: relative;
    height: 600px;
    border-radius: 20px;
    overflow: hidden;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(20px);
    box-shadow: 0 25px 70px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.2);
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
    background: linear-gradient(135deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.15) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: white;
    font-size: 1.2rem;
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.hero-image-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.2));
}

.logo {
    font-size: 2rem;
    font-weight: bold;
    color: white;
    margin-bottom: 3rem;
    letter-spacing: -1px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.tagline {
    color: rgba(255,255,255,0.9);
    font-size: 1rem;
    margin-top: -2.5rem;
    margin-bottom: 2rem;
    text-shadow: 0 1px 4px rgba(0,0,0,0.15);
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
        font-size: 3rem;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
    }
    
    .section-title {
        font-size: 2.5rem;
    }
    
    .section-subtitle {
        font-size: 1.3rem;
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
    font-size: 1.8rem;
    margin-bottom: 0.8rem;
}

.step-card p {
    font-size: 1.3rem;
    line-height: 1.7;
}

.step-number {
    display: inline-block;
    width: 60px;
    height: 60px;
    line-height: 60px;
    background: var(--primary-teal);
    color: white;
    border-radius: 50%;
    font-size: 1.8rem;
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
    padding: 2.5rem;
    border-radius: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
    border-left: 6px solid var(--primary-teal);
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    min-height: 140px;
}

.event-card:hover {
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    transform: translateX(10px);
}

.event-date {
    background: var(--light-teal);
    color: var(--dark-teal);
    padding: 0.6rem 1.3rem;
    border-radius: 25px;
    font-size: 1.1rem;
    display: inline-block;
    margin-bottom: 1rem;
    font-weight: 600;
}

.event-card h3 {
    font-size: 1.8rem;
    margin-bottom: 0.6rem;
}

.event-card p {
    font-size: 1.3rem;
}

.event-cta {
    background: var(--text-dark);
    color: white;
    padding: 0.9rem 2rem;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    font-weight: 600;
    white-space: nowrap;
    font-size: 1.3rem;
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
    font-size: 1.4rem;
}

.testimonial-card p:first-child {
    font-size: 1.5rem;
    line-height: 1.8;
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
    grid-template-columns: 2fr 1fr 1fr;
    gap: 3rem;
}

.footer-column h3 {
    color: var(--primary-pink);
    margin-bottom: 1.2rem;
    font-size: 1.6rem;
}

.footer-column p {
    margin-bottom: 1.2rem;
    opacity: 0.9;
    line-height: 1.7;
    font-size: 1.2rem;
}

.footer-column a {
    color: white;
    text-decoration: none;
    display: block;
    margin-bottom: 1rem;
    transition: color 0.3s ease;
    opacity: 0.9;
    font-size: 1.2rem;
}

.footer-bottom {
    text-align: center;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    opacity: 0.7;
    font-size: 1.1rem;
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

/* Navigation Bar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    z-index: 999;
    padding: 1rem 0;
}

.navbar-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar-logo {
    font-size: 1.8rem;
    font-weight: bold;
    color: var(--primary-pink);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.navbar-menu {
    display: flex;
    gap: 1.5rem; /* Gap between menu items */
    align-items: center;
    margin-left: 3rem; /* Add left margin to create space from logo */
}

.navbar-link {
    color: var(--text-dark);
    text-decoration: none;
    font-weight: 500;
    font-size: 1.1rem;
    transition: color 0.3s ease;
    padding: 0.5rem 1rem;
    border-radius: 25px;
}

.navbar-link:hover {
    color: var(--primary-pink);
}

.navbar-link.active {
    background: var(--light-pink);
    color: var(--primary-pink);
}

.navbar-cta {
    background: var(--primary-teal);
    color: white;
    padding: 0.7rem 1.5rem;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

.navbar-cta:hover {
    background: var(--dark-teal);
    transform: translateY(-2px);
}

/* Partner Section */
.partner-section {
    background: white;
    padding: 80px 20px;
    border-top: 1px solid #E0E0E0;
}

.partner-container {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
}

.partner-label {
    font-size: 2.5rem;
    color: var(--text-dark);
    font-weight: 700;
    margin-bottom: 1rem;
}

.partner-subtitle {
    font-size: 1.3rem;
    color: var(--text-light);
    margin-bottom: 3rem;
}

.partner-logos {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4rem;
    flex-wrap: wrap;
}

.partner-logo-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.partner-logo {
    width: 180px;
    height: 80px;
    background: #F5F5F5;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: #999;
    transition: all 0.3s ease;
    border: 2px solid transparent;
}

.partner-logo:hover {
    border-color: var(--primary-teal);
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.partner-name {
    font-size: 1.1rem;
    color: var(--text-light);
    font-weight: 500;
}

/* Team/About Section */
.team-section {
    background: linear-gradient(135deg, #FFF5F7 0%, #F0FFF4 100%);
    padding: 100px 20px;
    position: relative;
    overflow: hidden;
}

.team-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 80px;
    align-items: center;
}

.team-image-wrapper {
    position: relative;
}

.team-image {
    width: 100%;
    max-width: 450px;
    height: 450px;
    background: linear-gradient(135deg, var(--primary-pink), var(--primary-teal));
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.team-image::before {
    content: '';
    position: absolute;
    top: -20px;
    left: -20px;
    right: -20px;
    bottom: -20px;
    background: linear-gradient(135deg, var(--primary-pink), var(--primary-teal));
    opacity: 0.1;
    border-radius: 30px;
    z-index: -1;
}

.team-photo-placeholder {
    font-size: 8rem;
    color: white;
    opacity: 0.9;
}

.team-content {
    padding-left: 2rem;
}

.team-content h2 {
    font-size: 3rem;
    color: var(--text-dark);
    margin-bottom: 1rem;
    font-weight: 700;
    line-height: 1.2;
}

.team-content h2 span {
    color: var(--primary-pink);
}

.team-divider {
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, var(--primary-pink), var(--primary-teal));
    margin: 2rem 0;
    border-radius: 2px;
}

.team-description {
    font-size: 1.4rem;
    color: var(--text-dark);
    line-height: 1.8;
    margin-bottom: 2rem;
}

.team-highlight {
    font-size: 1.3rem;
    color: var(--text-light);
    font-style: italic;
    margin-bottom: 3rem;
}

.team-buttons {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.team-btn-primary {
    background: var(--text-dark);
    color: white;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.team-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    background: #1a1a1a;
}

.team-btn-secondary {
    background: transparent;
    color: var(--text-dark);
    padding: 1rem 2.5rem;
    border: 2px solid var(--text-dark);
    border-radius: 50px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.team-btn-secondary:hover {
    background: var(--text-dark);
    color: white;
    transform: translateY(-2px);
}

.team-locations {
    display: flex;
    gap: 2rem;
    margin-top: 3rem;
    flex-wrap: wrap;
}

.team-location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
    color: var(--text-light);
}

.team-location span {
    font-weight: 600;
    color: var(--text-dark);
}

@media (max-width: 968px) {
    .team-container {
        grid-template-columns: 1fr;
        gap: 40px;
        text-align: center;
    }
    
    .team-content {
        padding-left: 0;
    }
    
    .team-image {
        margin: 0 auto;
        max-width: 350px;
        height: 350px;
    }
    
    .team-content h2 {
        font-size: 2.5rem;
    }
    
    .team-divider {
        margin: 2rem auto;
    }
    
    .team-buttons {
        justify-content: center;
    }
    
    .team-locations {
        justify-content: center;
    }
    
    .partner-logos {
        gap: 2rem;
    }
    
    .partner-logo {
        width: 150px;
        height: 70px;
    }
    
    .partner-label {
        font-size: 2rem;
    }
}

/* Adjust hero for navbar only */
.hero {
    min-height: 100vh;
    background: linear-gradient(135deg, #E91E63 0%, #4CAF50 100%);
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    padding: 0;
    margin-top: 70px; /* Space for fixed navbar */
}

/* Organizer Section - IMPROVED */
.organizer-section {
    padding: 100px 20px;
    background: linear-gradient(135deg, var(--light-teal) 0%, var(--light-pink) 100%);
}

.organizer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

/* IMPROVED: Better contrast and readability for the title */
.organizer-text h2 {
    font-size: 3.5rem; /* Increased from 3rem */
    color: var(--text-dark);
    margin-bottom: 1.5rem;
    font-weight: 800; /* Increased weight for better visibility */
    line-height: 1.2;
    text-shadow: 0 2px 4px rgba(0,0,0,0.05); /* Subtle shadow for better readability */
}

.organizer-text h2 span {
    color: var(--primary-teal);
    display: block; /* Makes "veranstalten" appear on its own line */
    margin-top: 0.2rem;
}

/* IMPROVED: Increased font sizes in organizer section */
.organizer-text p {
    font-size: 1.4rem; /* Increased from 1.3rem */
    color: var(--text-light);
    margin-bottom: 2rem;
    line-height: 1.7;
}

.organizer-benefits {
    list-style: none;
    margin-bottom: 2rem;
}

.organizer-benefits li {
    padding: 0.8rem 0;
    font-size: 1.3rem; /* Increased from 1.2rem */
    color: var(--text-dark);
    display: flex;
    align-items: center;
    gap: 1rem;
    list-style: none;
}

.organizer-benefits li::before {
    content: "✓";
    color: var(--primary-teal);
    font-weight: bold;
    font-size: 1.8rem;
    display: inline-block;
    width: 25px;
}

.organizer-cta {
    background: var(--primary-teal);
    color: white;
    padding: 1.2rem 2.5rem;
    font-size: 1.4rem; /* Increased from 1.3rem */
    border-radius: 50px;
    text-decoration: none;
    display: inline-block;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.organizer-cta:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
}

.organizer-image {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
}

.organizer-image h3 {
    font-size: 1.9rem; /* Increased font size */
}

.organizer-image p {
    font-size: 1.3rem; /* Increased font size */
    line-height: 1.7;
    color: #495057; /* Darker gray for better contrast */
}

.organizer-image p:first-of-type {
    color: #6c757d; /* Slightly lighter for the first paragraph */
}

.organizer-image p:last-of-type {
    color: #343a40; /* Darker for emphasis on the last paragraph */
    font-weight: 500;
}

@media (max-width: 968px) {
    .navbar-menu {
        flex-direction: column;
        gap: 1rem;
    }
    
    .organizer-content {
        grid-template-columns: 1fr;
        text-align: center;
    }
    
    .organizer-text h2 {
        font-size: 2.5rem; /* Adjusted for mobile */
    }
    
    .organizer-text h2 span {
        display: inline; /* On mobile, keep it inline */
        margin-left: 0.3rem;
    }
}

.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    animation: fadeIn 0.3s ease;
}

.modal.show {
    display: flex;
    align-items: center;
    justify-content: center;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.modal-content {
    background-color: white;
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    max-width: 500px;
    margin: 20px;
    position: relative;
    animation: slideUp 0.3s ease;
    text-align: center;
}

@keyframes slideUp {
    from {
        transform: translateY(30px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 2rem;
    font-weight: bold;
    color: var(--text-light);
    cursor: pointer;
    background: none;
    border: none;
    transition: color 0.3s ease;
}

.modal-close:hover {
    color: var(--primary-pink);
}

.modal-content h3 {
    color: var(--primary-pink);
    margin-bottom: 1.5rem;
    font-size: 2rem;
}

.modal-content p {
    font-size: 1.3rem;
    line-height: 1.7;
    color: var(--text-dark);
    margin-bottom: 1rem;
}

.modal-email {
    color: var(--primary-teal);
    font-weight: 600;
    font-size: 1.4rem;
    text-decoration: none;
    transition: color 0.3s ease;
}

.modal-email:hover {
    color: var(--primary-pink);
    text-decoration: underline;
}

@media (max-width: 768px) {
    .modal-content {
        padding: 2rem;
        margin: 15px;
    }
    
    .modal-content h3 {
        font-size: 1.6rem;
    }
    
    .modal-content p {
        font-size: 1.1rem;
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

.expandable {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
}

.expandable.show {
    max-height: 500px;
}

.bg-white { 
    background: white;
    border: none;
}

.bg-gray { 
    background: #F8F9FA;
    border: none;
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

// Modal functionality
function showContactModal() {
    document.getElementById('contactModal').classList.add('show');
}

function closeContactModal() {
    document.getElementById('contactModal').classList.remove('show');
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    // Get all links that start with #
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Close modal when clicking outside
    window.onclick = function(event) {
        const modal = document.getElementById('contactModal');
        if (event.target === modal) {
            closeContactModal();
        }
    }
});
"""

# Initialize FastHTML app
app, rt = fast_app()

# Navigation Bar Component - IMPROVED with better spacing
def NavigationBar():
    return Nav(
        Div(
            A("🍝 SPINFOOD", href="#", cls="navbar-logo"),
            Div(
                A("Für Teilnehmer", href="#", cls="navbar-link active"),
                A("Für Veranstalter", href="#organizer", cls="navbar-link"),
                A("Event finden", href="#events", cls="navbar-cta"),
                cls="navbar-menu"
            ),
            cls="navbar-container"
        ),
        cls="navbar"
    )

# Partner Section Component
def PartnerSection():
    return Div(
        Div(
            H2("Vertraut von führenden Universitäten", cls="partner-label"),
            P("Tausende Studierende haben bereits an unseren Events teilgenommen", cls="partner-subtitle"),
            Div(
                Div(
                    # Placeholder for Uni Gießen logo
                    Div("🎓", cls="partner-logo"),
                    Span("Universität Gießen", cls="partner-name"),
                    cls="partner-logo-item"
                ),
                Div(
                    # Placeholder for Uni Erlangen logo
                    Div("🏛️", cls="partner-logo"),
                    Span("Universität Erlangen", cls="partner-name"),
                    cls="partner-logo-item"
                ),
                cls="partner-logos"
            ),
            cls="partner-container"
        ),
        cls="partner-section"
    )

# Team/About Section Component
def TeamSection():
    return Div(
        Div(
            Div(
                Div(
                    # Placeholder for team photo - in production, use Img()
                    Div("👥", cls="team-photo-placeholder"),
                    cls="team-image"
                ),
                cls="team-image-wrapper"
            ),
            Div(
                H2(
                    "Und wer steckt hinter ",
                    Span("Spinfood?"),
                    cls="team-title"
                ),
                Div(cls="team-divider"),
                P(
                    "Wir sind drei Hobby-Köche aus Berlin, Dresden und Nürnberg und arbeiten in unserer Freizeit an diesem Projekt. Wenn du Fragen oder Anregungen hast, melde dich gerne bei uns. Wir wollen Spinfood kontinuierlich verbessern!",
                    cls="team-description"
                ),
                P(
                    "Unser Ziel: Running Dinner Events in jeder deutschen Uni-Stadt etablieren.",
                    cls="team-highlight"
                ),
                Div(
                    Button("✉️ Schreib uns", onclick="showContactModal()", cls="team-btn-primary"),
                    A("💡 Mehr über uns", href="#", cls="team-btn-secondary"),
                    cls="team-buttons"
                ),
                Div(
                    Div("📍", Span("Berlin"), cls="team-location"),
                    Div("📍", Span("Dresden"), cls="team-location"),
                    Div("📍", Span("Nürnberg"), cls="team-location"),
                    cls="team-locations"
                ),
                cls="team-content"
            ),
            cls="team-container"
        ),
        cls="team-section"
    )

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
                        "🎓 Event organisieren",
                        href="#organizer",
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
                    "Anmelden & Matchen",
                    "Melde dich online an und werde einem Kochteam zugeteilt.",
                    "Du meldest dich als 2er-Team oder alleine an. Wir teilen dich einem Gang zu (Vorspeise, Hauptgang oder Dessert) und matchen dich mit anderen Teilnehmern. Keine Sorge - auch Kochanfänger sind willkommen!"
                ),
                StepCard(
                    2, "🍽️",
                    "Kochen & Besuchen",
                    "Koche einen Gang zuhause und besuche zwei andere Teams.",
                    "Du kochst nur einen Gang für 4-6 Personen bei dir zuhause. Die anderen beiden Gänge genießt du bei anderen Teilnehmern. So lernst du verschiedene Wohnungen und Stadtteile kennen!"
                ),
                StepCard(
                    3, "🎉",
                    "After Party",
                    "Triff alle Teilnehmer bei der gemeinsamen Party.",
                    "Nach dem Dinner treffen sich alle Teilnehmer zur After-Party. Hier kannst du die Leute wiedertreffen und neue Kontakte knüpfen. Die Party geht oft bis in die Nacht!"
                ),
                cls="cards-grid"
            ),
            cls="container"
        ),
        id="how",
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
                BenefitCard("👥", "Friends", "Echte Verbindungen entstehen beim gemeinsamen Kochen und Essen. Nicht oberflächlich, sondern echt!"),
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
            Button("Noch Fragen?", onclick="showContactModal()", cls="cta-button-secondary"),
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
                    A("📺 YouTube", href="#"),
                    A("📷 Instagram", href="#"),
                    cls="social-links"
                ),
                cls="footer-column"
            ),
            Div(
                H3("Support"),
                A("Kontakt", href="#", onclick="showContactModal(); return false;"),
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
            P("© 2025 Spinfood. Made with ❤️ in Germany"),
            cls="footer-bottom"
        ),
        cls="footer-section"
    )

# Organizer Section Component - IMPROVED
def OrganizerSection():
    return Div(
        Div(
            Div(
                H2(
                    "Running Dinner Events",
                    Span("veranstalten", cls="organizer-highlight"),
                    cls="organizer-text"
                ),
                P("Spinfood ist die Plattform für Running Dinner Events in deutschen Universitätsstädten. Wir übernehmen die komplette technische Abwicklung für deine Organisation."),
                Ul(
                    Li("Vollautomatische Organisation"),
                    Li("Intelligentes Pärchen-Matching"),
                    Li("Nie den Überblick verlieren"),
                    Li("Integriertes Zahlungssystem"),
                    Li("Erfahrene Ansprechpartner"),
                    cls="organizer-benefits"
                ),
                P("Keine mühsame Handarbeit bei der Planung. Wir stellen das System - ihr organisiert das Event!", 
                  style="font-size: 1.3rem; color: var(--text-dark); font-weight: 500; margin-bottom: 2rem;"),
                Button("Jetzt Kontakt aufnehmen", onclick="showContactModal()", cls="organizer-cta"),
                cls="organizer-text"
            ),
            Div(
                H3("Was ist Spinfood?", style="color: var(--primary-pink); margin-bottom: 1rem; font-size: 1.9rem;"),
                P("Spinfood ist eine Plattform für Running Dinner Events in deutschen Universitätsstädten. Wir organisieren die komplette Logistik: von der Anmeldung über die automatische Teamzuteilung bis hin zur Erstellung individueller Dinner-Routen.",
                  style="margin-bottom: 1.5rem; font-size: 1.3rem; line-height: 1.7;"),
                P("Wir übernehmen den kompletten technischen Part, damit ihr euch auf das Wesentliche konzentrieren könnt: die Organisation des Events und das Marketing.",
                  style="font-weight: 500; font-size: 1.3rem; line-height: 1.7;"),
                cls="organizer-image"
            ),
            cls="organizer-content"
        ),
        id="organizer",
        cls="organizer-section"
    )

# Contact Modal Component
def ContactModal():
    return Div(
        Div(
            Button("×", onclick="closeContactModal()", cls="modal-close"),
            H3("Kontakt 📬"),
            P("Wenn Du weitere Fragen, Anregungen oder Wünsche hast, kannst du uns jeder Zeit eine Email schicken an"),
            A("hi@spinfood.de", href="mailto:hi@spinfood.de", cls="modal-email"),
            cls="modal-content"
        ),
        id="contactModal",
        cls="modal"
    )

# Main route
@rt("/")
def get():
    return Title("Spinfood - Running Dinner für Studierende"), \
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"), \
        Meta(name="description", content="Triff 6-12 neue Leute an einem Abend beim Running Dinner in deiner Uni-Stadt. Food, Fun & Friends - Jetzt anmelden!"), \
        Style(custom_css), \
        Script(js_code), \
        NavigationBar(), \
        HeroSection(), \
        ProblemSection(), \
        HowItWorksSection(), \
        BenefitsSection(), \
        EventsSection(), \
        OrganizerSection(), \
        TestimonialsSection(), \
        FAQSection(), \
        CTASection(), \
        TeamSection(), \
        PartnerSection(), \
        FooterSection(), \
        ContactModal()

# Serve the app
serve()