# IIT Patna CET Website Replica — Visual Fidelity Audit Report

**Date:** November 17, 2026  
**Auditor:** Senior Frontend QA & UI Reverse-Engineering Specialist  
**Reference Portal:** `https://cet.iitp.ac.in/`  
**Mock Repository:** `https://github.com/ayushcmd/iitp-cet-mock.git`  
**Deployment Target:** Vercel Static Hosting (Root Domain)  
**Evaluated Branch:** `fix/post-qa-verification`

---

## 1. Executive Summary

This Visual Fidelity Audit evaluates all 18 pages of the unofficial educational replica against the live production portal of the Centre for Educational Technology (CET) at IIT Patna. The evaluation was conducted across 6 standardized viewports (1920×1080, 1440×900, 1024×768, 768×1024, 390×844, and 320×568) comparing typography, container widths, color palettes, heading hierarchies, grid structures, table formatting, and mobile responsiveness.

---

## 2. Core Visual Systems Comparison

### 2.1 Institute Branding & Header
- **Original Site**: Displays bilingual IIT Patna brand emblem (`logo.png`) featuring Devanagari "भारतीय प्रौद्योगिकी संस्थान पटना" and English "Indian Institute of Technology Patna" with Centre for Educational Technology typography.
- **Replica Implementation**: Uses identical asset dimensions (`width="320" height="60"`) positioned in a flexbox header container with deep navy background (`#003360`).
- **Discrepancy / Alignment**: The original site has no top educational disclaimer. The replica includes a high-contrast amber disclaimer banner (`#fffbeb`, border `#fef3c7`, text `#92400e`) pinned at the top to fulfill ethical reproduction standards without shifting header layout.

### 2.2 Navigation Architecture
- **Desktop Nav**:
  - Horizontal menu bar with hover/focus-within dropdown menus.
  - Two-tier nested flyouts (`Academics -> Program ▶ -> B.Tech / M.Tech / BBA`).
  - Active route pill indicator (`#fb7906` orange background with high-contrast `#002147` deep navy text for active page to meet WCAG 2.2 AA 5.99:1 contrast).
  - External links marked with `↗` glyphs.
- **Mobile Navigation**:
  - Offcanvas drawer sliding in from left (`width: 320px; max-width: 85vw; background: #003360`).
  - Submenu accordion toggles with rotating chevron icons (180deg smooth CSS rotation).
  - Backdrop blur filter (`backdrop-filter: blur(4px); background: rgba(0,0,0,0.55)`).

### 2.3 Typography & Hierarchy
- **Font Family**: Google Fonts `Source Sans Pro` loaded with weights 300, 400, 600, 700, 800, 900.
- **Headings**:
  - H1 Page Titles: `1.85rem` (29.6px) – `2.25rem` (36px), font-weight 700/800, deep navy (`#042c53`).
  - H2 Section Titles: `1.4rem` – `1.65rem`, font-weight 700.
  - H3 Card Titles: `1.15rem` – `1.3rem`, font-weight 600/700.
  - Body Text: `0.9375rem` (15px) base size, line-height `1.65`, color `#212529` / `#334155`.
- **Text Wrapping & Contrast**:
  - Headers preserve proper word breaks. Long email IDs and URLs utilize `word-break: break-all` to prevent layout overflow on narrow mobile screens.

### 2.4 Color Palette & Gradients
| Token | Hex Value | Role in Design |
| :--- | :--- | :--- |
| `--color-brand-primary` | `#003360` | Site header, mobile drawer base, primary buttons |
| `--color-brand-navy-dark` | `#042c53` | Section headings, card titles, hero gradient start |
| `--color-brand-secondary` | `#095aa3` | Dropdown menus, submenus, footer background |
| `--color-brand-accent` | `#185fa5` | Counter metrics, links, sidebar active text |
| `--color-accent-orange` | `#fb7906` | Active menu pill, back-to-top floating button |
| `--color-accent-yellow` | `#f9c74f` | Menu link hover state |
| `--color-alert-maroon` | `#8B0000` | Announcement marquee ticker bar |
| `--color-alert-red` | `#dc2626` | Pulsing "NEW" notifications and alert badges |
| `--color-surface-light` | `#F4F6FB` | Stat cards, feature highlight callout boxes |
| `--gradient-hero` | `linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)` | Homepage hero background |

---

## 3. Page-by-Page Visual Audit Matrix

| Page Path | Verified Layout | Visual Hierarchy & Components | Table / Grid Styling | Discrepancies & Adjustments Made |
| :--- | :--- | :--- | :--- | :--- |
| `index.html` | Hero + 8/4 Split + 3-Col Grids | Hero stats, marquee ticker, program category filter tabs, specialization tracks, NEP pathway, notice sidebar, footer | CSS grid `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` | Added landmark `<main id="mainContent">` and skip-to-content bypass link. |
| `pages/about.html` | 8/4 Grid with Sidebar | Institutional history, NEP-2020 mission cards, Director's address, notice sidebar | 2-column feature card grid, soft background panels | Verified verbatim content and typography alignment. |
| `pages/faculty.html` | 8/4 Grid with Sidebar | Chief Mentor card (Director IIT Patna), 3 Coordinator cards with verified photos, directory table | Responsive table + mentor profile grid | Verified 130×130px headshots (`tns.jpg`, `akt.jpg`, `nkt.jpg`), rounded borders, badge chips. |
| `pages/academic-service-charges.html` | 8/4 Grid with Sidebar | 10 verified service fee rows, currency symbols, urgent note callout, notice sidebar | Striped table with sticky headers on scroll | Verified verbatim fee structure and Rs. 5,500 semester exam fee rate. |
| `pages/announcements/flyer.html` | 8/4 Grid with Sidebar | Course flyers, PDF preview badges, admissions document list | 2-column card showcase grid | Verified external PDF asset links and responsive card reflow. |
| `pages/announcements/news.html` | 8/4 Grid with Sidebar | Press clippings, media coverage cards, verified thumbnail photos | 3-column media press grid | Verified authentic JPEG clippings (`news-1.jpeg`, `news-2.jpeg`, `news-3.jpeg`). |
| `pages/announcements/placement.html` | 8/4 Grid with Sidebar | Tech Club initiatives, training programs, selected candidate PDF circulars | Card and list layout with action links | Verified PDF download links to official CET server. |
| `pages/admissions/eligibility.html` | 8/4 Grid with Sidebar | Program tabs, qualifying score tables, 10+2 science criteria, national test ranks | Responsive multi-column table | Clarified PCM 60% requirement and JEE Main / CUET / SAT equivalencies. |
| `pages/academics/academic-calendar.html` | 8/4 Grid with Sidebar | Autumn 2024–Autumn 2026 session calendars, PDF download action buttons | Tabular download matrix | Verified all 6 official calendar PDF endpoints resolve to 200 OK. |
| `pages/academics/evaluation-scheme.html` | 8/4 Grid with Sidebar | Assessment mode percentages (20% quiz, 30% assignment, 50% end-sem), distinction callout | Badge-weighted list with progress chips | Verified verbatim 50/50 continuous vs summative weightage. |
| `pages/academics/holiday-list.html` | 8/4 Grid with Sidebar | 2025 gazetted and restricted holiday schedules, day-by-day dates | Multi-column tabular calendar | Full responsive wrapper `.table-responsive` prevents horizontal page overflow. |
| `pages/academics/programs.html` | Full-width Catalog | Degree catalog for B.Tech AI & DS, B.Tech CSE, Exec M.Tech, and BBA with curricula tabs | Multi-column grid with tag pills | Verified semester course breakdowns and credit allocations. |
| `pages/academics/re-exam-schedule.html` | 8/4 Grid with Sidebar | Supplementary examination schedule tables, time slots, course codes | Schedule table with date headers | Responsive wrapper verified across mobile viewports. |
| `pages/academics/time-table.html` | 8/4 Grid with Sidebar | Semester lecture schedules for CSDA, AICS, and BBA cohorts | Slot schedule tables | Responsive scroll container verified on compact screens. |
| `pages/online-classes.html` | 8/4 Grid with Sidebar | Moodle Hero card, 3 action cards, query notice box, 8-item FAQ accordion | 3-column action card row + FAQ accordion | FAQ accordion toggle verified; interactive expand/collapse fully operational without dependencies. |
| `pages/bonafide-application.html` | 8/4 Grid with Sidebar | Application instruction card, red status alert banner, documents required card | 2-column card presentation | Marked status notice with historical context; verified external Microsoft Forms link. |
| `pages/admission-notice.html` | 8/4 Grid with Sidebar | July 2025 seat deferral alert, Spring 2026 intake circular, notification archive | Banner alert + archived circular grid | Refactored active intake label to Historical Session Archive per Phase 5 guidelines. |
| `pages/e-gymkhana.html` | 8/4 Grid with Sidebar | Gradient hero box, "Coming Soon !!" badge, 4 council cards (Technical, Cultural, Sports, Welfare) | 4-column council grid | Verified authentic "Coming Soon !!" badge matching live portal status. |

---

## 4. Multi-Viewport Layout Integrity

### 4.1 1920 × 1080 (Large Desktop)
- Container max-width constrained to `1320px` with centered auto-margins.
- Ample whitespace breathing room; zero horizontal distortion or pixel stretching.
- Background gradients render smoothly without banding.

### 4.2 1440 × 900 (Desktop)
- Standard laptop/desktop presentation.
- Main 8/4 grid maintains clean column separation (`gap: 2rem`).
- Desktop navigation menu renders on a single unbroken line.

### 4.3 1024 × 768 (Laptop / Tablet Landscape)
- Navigation transitions smoothly.
- 3-column grids adjust spacing to accommodate narrower content boundaries.
- No elements collide or truncate awkwardly.

### 4.4 768 × 1024 (Tablet Portrait)
- Breakpoint trigger: Desktop navigation hides; mobile hamburger toggle button appears.
- 8/4 column layout reflows into vertical stacking (main content above notice sidebar).
- Touch target sizes ensure ease of interaction on touchscreens.

### 4.5 390 × 844 (Mobile)
- Single-column flow with padding reduced to `1rem`.
- Action cards stack vertically.
- Academic schedule tables scroll cleanly inside `.table-responsive` containers with subtle scroll indicator hints.

### 4.6 320 × 568 (Narrow Mobile)
- Extreme narrow viewport test: `document.documentElement.scrollWidth` strictly equals client width.
- Zero horizontal window overflow on all 18 pages.
- Header logo scales proportionally without clipping.

---

## 5. Visual Discrepancies Cataloged & Remediated

1. **Homepage Semantic Landmark**:
   - *Observation*: `index.html` lacked `<main id="mainContent">` wrapping homepage sections.
   - *Fix*: Wrapped all 8 homepage sections in `<main id="mainContent">` and added `<a href="#mainContent" class="skip-link">Skip to Main Content</a>`.
2. **Historical Intake Labeling on Admission Notice**:
   - *Observation*: `admission-notice.html` displayed an "Active Intake Cycle" badge for Spring 2026 deferral.
   - *Fix*: Replaced with "Historical Session Archive" tag and added explicit explanatory notes stating active intake cycles are governed by official institute notifications.
3. **Bonafide Temporary Pause Notice**:
   - *Observation*: Verbatim text stated application resumption from 1st November 2025 without historical framing.
   - *Fix*: Appended historical archive annotation clarifying the announcement was made during Autumn 2025 and live form availability depends on official institutional access.
4. **Touch Targets on Mobile Controls**:
   - *Observation*: Hamburger button, drawer close button, and submenu toggle chevrons had computed touch targets around 34–38px.
   - *Fix*: Configured `min-width: 44px; min-height: 44px` on all mobile navigation control elements in `css/responsive.css`.

---

## 6. Visual Fidelity Conclusion
The 18-page website replica maintains high aesthetic and structural fidelity to the live IIT Patna CET portal, faithfully reproducing typography, color relationships, iconography, and responsive layouts while upholding safety standards and clear educational attribution.
