/**
 * IIT Patna - Centre for Educational Technology (CET) Replica
 * Main Shared Script: Preloader, Back-to-Top Button, Global Utilities
 */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initBackToTop();
  initAccordions();
  logDisclaimer();
});

/**
 * Handles the animated preloader, smoothly fading it out once the page assets load.
 */
function initPreloader() {
  const preloader = document.getElementById('astroid-preloader') || document.getElementById('preloader');
  if (!preloader) return;

  function fadeOut() {
    preloader.classList.add('fade-out');
    setTimeout(() => {
      if (preloader.parentNode) {
        preloader.parentNode.removeChild(preloader);
      }
    }, 550);
  }

  // Fade out on window load, with a fallback safety timeout
  if (document.readyState === 'complete') {
    fadeOut();
  } else {
    window.addEventListener('load', fadeOut);
    setTimeout(fadeOut, 1200); // Safety fallback
  }
}

/**
 * Handles the floating Back-to-Top button behavior.
 */
function initBackToTop() {
  const backToTopBtn = document.getElementById('astroid-backtotop') || document.getElementById('backToTop');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 250) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * Handles interactive accordion collapses (used in Moodle FAQ and other collapsibles).
 */
function initAccordions() {
  const accordionButtons = document.querySelectorAll('.accordion-button');

  accordionButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetSelector = btn.getAttribute('data-bs-target') || btn.getAttribute('data-target');
      let targetCollapse = null;

      if (targetSelector) {
        targetCollapse = document.querySelector(targetSelector);
      } else {
        const item = btn.closest('.accordion-item');
        if (item) {
          targetCollapse = item.querySelector('.accordion-collapse');
        }
      }

      if (!targetCollapse) return;

      const isCurrentlyOpen = targetCollapse.classList.contains('show');
      const parentAccordion = btn.closest('.accordion');

      // If parent enforces single open item (accordion behavior)
      if (parentAccordion) {
        const openCollapses = parentAccordion.querySelectorAll('.accordion-collapse.show');
        const openButtons = parentAccordion.querySelectorAll('.accordion-button:not(.collapsed)');

        openCollapses.forEach((c) => {
          if (c !== targetCollapse) {
            c.classList.remove('show');
          }
        });
        openButtons.forEach((b) => {
          if (b !== btn) {
            b.classList.add('collapsed');
            b.setAttribute('aria-expanded', 'false');
          }
        });
      }

      if (isCurrentlyOpen) {
        targetCollapse.classList.remove('show');
        btn.classList.add('collapsed');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        targetCollapse.classList.add('show');
        btn.classList.remove('collapsed');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/**
 * Educational disclaimer notification in browser console.
 */
function logDisclaimer() {
  console.info(
    '%c [IIT Patna CET Mock] %c Unofficial educational replica created for personal learning. Not affiliated with or endorsed by IIT Patna. Official site: https://cet.iitp.ac.in/',
    'background: #003360; color: #ffffff; font-weight: bold; padding: 4px 8px; border-radius: 4px;',
    'color: #042c53; font-weight: 500;'
  );
}
