# Design System Specification — IIT Patna CET Replica

This document defines the visual design system, CSS custom properties, typography scale, component patterns, and responsive behavior extracted directly from `https://cet.iitp.ac.in/`.

---

## 1. Color Palette & Tokens

### 1.1 Brand Palette

| Token Name | CSS Custom Property | Hex / RGB Value | Usage |
| :--- | :--- | :--- | :--- |
| **Brand Primary Navy** | `--color-brand-primary` | `#003360` (`rgb(0, 51, 96)`) | Main header bar, top bar background, deep contrast accents |
| **Brand Deep Blue** | `--color-brand-navy-dark` | `#042c53` (`rgb(4, 44, 83)`) | Hero gradient base, headings, filter text |
| **Brand Secondary Blue** | `--color-brand-secondary` | `#095aa3` (`rgb(9, 90, 163)`) | Dropdown menus, sub-navigation, footer background |
| **Brand Accent Blue** | `--color-brand-accent` | `#185fa5` (`rgb(24, 95, 165)`) | Statistics numbers (9+, 2, 2×), section highlights, links |
| **Brand Accent Orange** | `--color-accent-orange` | `#fb7906` (`rgb(251, 121, 6)`) | Active nav pill ("Home"), Back-to-top floating button |
| **Alert / Ticker Red** | `--color-alert-maroon` | `#8B0000` / `#990000` | Announcement ticker bar background, "NEW" blinking tag |
| **Active Pill Filter Bg** | `--color-filter-active-bg`| `#E6F1FB` | Active program filter button background |
| **Active Pill Filter Border**| `--color-filter-active-border`| `#378ADD` | Active program filter button border |

### 1.2 Neutral & Surface Palette

| Token Name | CSS Custom Property | Hex / Value | Usage |
| :--- | :--- | :--- | :--- |
| **Background Body** | `--color-bg-body` | `#ffffff` | Primary document background |
| **Surface Light** | `--color-surface-light` | `#F4F6FB` | Stat cards, feature boxes, notice strip |
| **Card Surface** | `--color-surface-card` | `#ffffff` | Degree program cards, modal sheets |
| **Border Soft** | `--color-border-soft` | `#e2e8f0` / `#dee2e6` | Card borders, dividers, table grid lines |
| **Text Primary** | `--color-text-primary` | `#212529` | Main body copy, table text, headers |
| **Text Muted** | `--color-text-muted` | `#64748b` / `#6c757d`| Subtitles, timestamps, metadata |
| **Text On Dark** | `--color-text-white` | `#ffffff` | Navbar links, footer text, hero text |

---

## 2. Typography Hierarchy

### 2.1 Font Family
- **Primary Typeface**: Google Fonts `'Source Sans Pro', sans-serif`
- **Fallback Stack**: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`

### 2.2 Scale & Weights

| Level | Size (Desktop) | Size (Mobile) | Weight | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Title (H1)** | `38px / 2.375rem` | `28px / 1.75rem` | `800` (Extra Bold) | `1.2` | `-0.02em` |
| **Section Title (H2)** | `28px / 1.75rem` | `24px / 1.5rem` | `700` (Bold) | `1.3` | `-0.01em` |
| **Card / Subsection (H3)** | `20px / 1.25rem` | `18px / 1.125rem` | `600` (Semi Bold) | `1.4` | `normal` |
| **Subheadings (H4-H6)** | `15px - 17px` | `14px - 15px` | `600` | `1.4` | `normal` |
| **Stat Numbers** | `26px / 1.625rem` | `24px / 1.5rem` | `800` | `1.0` | `normal` |
| **Body Regular** | `15px / 0.9375rem` | `14px / 0.875rem` | `400` (Regular) | `1.6` | `normal` |
| **Navigation Links** | `14px / 0.875rem` | `15px / 0.9375rem` | `600` | `1.0` | `0.01em` |
| **Badge / Filter Text**| `13px / 0.8125rem` | `12px / 0.75rem` | `600` | `1.0` | `normal` |

---

## 3. Spacing & Container Scale

```css
:root {
  --container-max-width: 1320px;
  --container-padding: 1.25rem;
  
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2.5rem;    /* 40px */
  --space-xxl: 4rem;     /* 64px */

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-pill: 9999px;

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.12);
  --shadow-glass: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
}
```

---

## 4. Component Patterns

### 4.1 Header & Brand Bar
- Top bar with deep navy (`#003360`) backdrop.
- Logo container accommodating the bilingual IIT Patna + CET emblem.
- Navbar menu items with hover indicators and clear arrow icons (`caret-down`).
- Active link marked with orange rounded pill (`#fb7906`).

### 4.2 Hero Section & Glassmorphic Container
- Backdrop image with dark navy linear overlay.
- Glassmorphic card styling:
  ```css
  .hero-glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: var(--radius-lg);
    color: #ffffff;
    padding: var(--space-xl);
  }
  ```

### 4.3 Announcement Marquee Ticker
- Crimson bar (`#8B0000`).
- Bold badge `📢 Announcements:`.
- Continuous CSS keyframe marquee animation (`@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }`) with pause-on-hover capability.

### 4.4 Category Filter Tabs
- Horizontal pill-button list:
  ```css
  .filter-btn {
    font-size: 13px;
    padding: 6px 16px;
    border-radius: 20px;
    cursor: pointer;
    border: 1px solid #ccc;
    background: #fff;
    color: #555;
    font-weight: 500;
    transition: all 0.2s ease;
  }
  .filter-btn.active {
    border-color: #378ADD;
    background: #E6F1FB;
    color: #042c53;
    font-weight: 600;
  }
  ```

### 4.5 Degree Program Cards
- Clean card with white surface, `#e2e8f0` border, `12px` border radius.
- Top badge with degree abbreviation, program title, duration pill, curriculum highlights, and bottom "Register →" button.
- Hover effect: `transform: translateY(-4px)`, `box-shadow: 0 8px 20px rgba(0, 51, 96, 0.1)`.

### 4.6 Notice Board Widget
- Right sidebar card with dark blue header (`#003360`).
- White surface with clean divided links (`border-bottom: 1px solid #f1f5f9`).
- Left indicator accent or calendar icon with hover highlight (`#F4F6FB`).

### 4.7 Academic Tables
- Zebra striping (`tbody tr:nth-child(even) { background-color: #f8fafc; }`).
- Navy table header (`thead { background-color: #003360; color: #fff; }`).
- Responsive scroll container (`overflow-x: auto`) for mobile readability.

### 4.8 Reusable Disclaimer Banner
- Restrained, legible notice at the very top or bottom of every page:
  ```html
  <div class="replica-disclaimer">
    <span>⚠️ Unofficial educational replica of the IIT Patna CET website. Created for personal learning. Not affiliated with or endorsed by IIT Patna. For official information, visit <a href="https://cet.iitp.ac.in/" target="_blank" rel="noopener">cet.iitp.ac.in</a>.</span>
  </div>
  ```

---

## 5. Responsive Breakpoints

| Breakpoint | Width Trigger | Media Query | Key Layout Adaptation |
| :--- | :--- | :--- | :--- |
| **Desktop Extra Large** | `>= 1200px` | `@media (min-width: 1200px)` | Multi-column grid (5 cols programs), horizontal navbar with hover flyouts |
| **Desktop / Laptop** | `992px - 1199px` | `@media (min-width: 992px) and (max-width: 1199px)` | 4-column program grid, full navbar |
| **Tablet** | `768px - 991px` | `@media (min-width: 768px) and (max-width: 991px)` | Mobile hamburger toggle activates, 2-column program grid, sidebar stacks below |
| **Mobile** | `<= 767px` | `@media (max-width: 767px)` | Offcanvas sliding navigation drawer, 1-column cards, full-width buttons |
