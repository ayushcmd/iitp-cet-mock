/**
 * IIT Patna - Centre for Educational Technology (CET) Replica
 * Programs Filtering Script: Interactive category tab filtering (All, UG, PG, Doctoral)
 */

document.addEventListener('DOMContentLoaded', () => {
  initProgramFilters();
});

/**
 * Initializes program category filter buttons and updates card visibility dynamically.
 */
function initProgramFilters() {
  const filterButtons = document.querySelectorAll('.program-filter-bar .filter-btn');
  const programCards = document.querySelectorAll('.programs-grid .program-card');

  if (!filterButtons.length || !programCards.length) return;

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      // 1. Update active tab UI state
      filterButtons.forEach((btn) => {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      });
      button.classList.add('active');
      button.setAttribute('aria-pressed', 'true');

      // 2. Determine selected category
      const selectedCategory = button.getAttribute('data-filter') || 'all';

      // 3. Filter cards with smooth fade/scale transition
      programCards.forEach((card) => {
        const cardCategory = card.getAttribute('data-category') || '';
        const categories = cardCategory.split(' ');

        if (selectedCategory === 'all' || categories.includes(selectedCategory)) {
          card.style.display = 'flex';
          // Trigger slight reflow for smooth animation
          requestAnimationFrame(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0) scale(1)';
          });
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px) scale(0.98)';
          setTimeout(() => {
            if (!card.parentElement.querySelector(`.filter-btn.active[data-filter="${selectedCategory}"]`)) return;
            card.style.display = 'none';
          }, 200);
        }
      });
    });

    // Keyboard navigation support for filter tabs (Arrow keys)
    button.addEventListener('keydown', (e) => {
      let targetButton = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        targetButton = button.nextElementSibling || filterButtons[0];
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        targetButton = button.previousElementSibling || filterButtons[filterButtons.length - 1];
      }

      if (targetButton && targetButton.classList.contains('filter-btn')) {
        targetButton.focus();
        targetButton.click();
      }
    });
  });
}
