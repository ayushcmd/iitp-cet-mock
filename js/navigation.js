/**
 * IIT Patna - Centre for Educational Technology (CET) Replica
 * Navigation Script: Mobile Drawer Toggle, Accordion Submenus, Active Route Highlighting
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileDrawer();
  initMobileAccordions();
  highlightActiveNav();
});

/**
 * Initializes the mobile offcanvas sliding drawer and backdrop.
 */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const closeBtn = document.querySelector('.mobile-drawer-close');
  const drawer = document.querySelector('.mobile-drawer');
  const backdrop = document.querySelector('.mobile-drawer-backdrop');

  if (!toggleBtn || !drawer || !backdrop) return;

  function openDrawer() {
    drawer.classList.add('open');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
    toggleBtn.setAttribute('aria-expanded', 'true');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
    toggleBtn.setAttribute('aria-expanded', 'false');
  }

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);

  // Close on Escape key press
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/**
 * Initializes mobile accordion dropdowns inside the offcanvas drawer.
 */
function initMobileAccordions() {
  const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');

  submenuToggles.forEach((toggle) => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const parentItem = toggle.closest('.mobile-nav-item');
      if (!parentItem) return;

      const isExpanded = parentItem.classList.contains('expanded');

      // Close sibling accordions for clean accordion behavior
      const siblings = parentItem.parentElement.querySelectorAll('.mobile-nav-item.expanded');
      siblings.forEach((sibling) => {
        if (sibling !== parentItem) {
          sibling.classList.remove('expanded');
          const siblingToggle = sibling.querySelector('.mobile-submenu-toggle');
          if (siblingToggle) siblingToggle.setAttribute('aria-expanded', 'false');
        }
      });

      parentItem.classList.toggle('expanded', !isExpanded);
      toggle.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
    });
  });
}

/**
 * Highlights the active menu item in the navbar based on the current URL.
 */
function highlightActiveNav() {
  const currentPath = window.location.pathname.toLowerCase();
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link, .dropdown-link');

  navLinks.forEach((link) => {
    const href = link.getAttribute('href');
    if (!href || href === '#' || href.startsWith('http')) return;

    // Normalize comparison
    const linkPath = href.toLowerCase().replace(/^\.?\.\//, '');
    const isHome = (currentPath === '/' || currentPath.endsWith('index.html') || currentPath === '') && (linkPath === 'index.html' || linkPath === './index.html' || linkPath === '/');

    if (isHome) {
      if (link.textContent.trim().toLowerCase() === 'home') {
        const parent = link.closest('.nav-item');
        if (parent) parent.classList.add('active');
      }
    } else if (currentPath.includes(linkPath.replace('.html', ''))) {
      const parent = link.closest('.nav-item');
      if (parent) parent.classList.add('active');
    }
  });
}
