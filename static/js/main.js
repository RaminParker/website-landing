/**
 * Spinfood Landing Page - JavaScript
 * ==================================
 * Handles interactive elements: expandable content, FAQ toggles, and modal.
 */

// =============================================================================
// Step Card Expansion
// =============================================================================

/**
 * Toggle expandable content in step cards.
 * @param {string} id - The element ID to toggle
 */
function toggleExpand(id) {
    const element = document.getElementById(id);
    if (!element) return;

    element.classList.toggle('show');
    const button = element.previousElementSibling;

    // Update button text based on state
    if (element.classList.contains('show')) {
        button.textContent = 'Weniger \u2191';
    } else {
        button.textContent = 'Mehr erfahren \u2193';
    }
}

// =============================================================================
// FAQ Accordion
// =============================================================================

/**
 * Toggle FAQ item visibility.
 * @param {string} id - The FAQ item ID to toggle
 */
function toggleFAQ(id) {
    const faqItem = document.getElementById(id);
    if (!faqItem) return;

    faqItem.classList.toggle('active');
    const answer = document.getElementById('faq-answer-' + id);

    // Show/hide answer based on active state
    if (faqItem.classList.contains('active')) {
        answer.style.display = 'block';
    } else {
        answer.style.display = 'none';
    }
}

// =============================================================================
// Contact Modal
// =============================================================================

/**
 * Show the contact modal.
 */
function showContactModal() {
    const modal = document.getElementById('contactModal');
    if (modal) {
        modal.classList.add('show');
    }
}

/**
 * Close the contact modal.
 */
function closeContactModal() {
    const modal = document.getElementById('contactModal');
    if (modal) {
        modal.classList.remove('show');
    }
}

// =============================================================================
// Page Initialization
// =============================================================================

/**
 * Initialize page functionality when DOM is ready.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    initSmoothScrolling();

    // Close modal when clicking outside
    initModalClickOutside();
});

/**
 * Initialize smooth scrolling for anchor links.
 */
function initSmoothScrolling() {
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
}

/**
 * Initialize modal click-outside-to-close behavior.
 */
function initModalClickOutside() {
    window.onclick = function(event) {
        const modal = document.getElementById('contactModal');
        if (event.target === modal) {
            closeContactModal();
        }
    };
}
