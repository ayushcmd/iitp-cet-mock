# Implementation Plan — IIT Patna CET Website Replica

## 1. Project Overview & Strategy

This implementation plan outlines the roadmap to recreate a high-fidelity, responsive, multi-page frontend replica of the official IIT Patna Centre for Educational Technology (CET) website (`https://cet.iitp.ac.in/`).

The replica is constructed using **semantic HTML5**, **modern CSS3**, and **vanilla JavaScript (ES6+)**, with zero runtime frameworks, zero build tools, and full compatibility for static deployment on **Vercel** (Framework preset: "Other") deployed at domain root, with source management at GitHub (`https://github.com/ayushcmd/iitp-cet-mock.git`).

---

## 2. Target Project Architecture

```text
iitp-cet-mock/
├── index.html                           # Full Homepage
├── pages/
│   ├── about.html                       # The Institute & About CET
│   ├── faculty.html                     # Faculty & Mentors Directory
│   ├── academic-service-charges.html    # Academic Service Charges Table
│   ├── online-classes.html              # Moodle & Online LMS Portal Guide
│   ├── bonafide-application.html        # Bonafide Application Portal (Read-only Informational Mock)
│   ├── admission-notice.html            # Admission Notices Archive
│   ├── e-gymkhana.html                  # E-Gymkhana Portal ("Coming Soon")
│   ├── admissions/
│   │   └── eligibility.html             # Eligibility Criteria & Evaluation
│   ├── academics/
│   │   ├── academic-calendar.html       # Academic Calendars & PDF Downloads
│   │   ├── holiday-list.html            # Institute Holidays 2025/2026
│   │   ├── time-table.html              # Semester Lecture Timetables
│   │   ├── evaluation-scheme.html       # Evaluation & Grading Scheme
│   │   ├── re-exam-schedule.html        # Re-Exam & Supplementary Schedule
│   │   └── programs.html                # Degree Programs Detail Catalog
│   └── announcements/
│       ├── flyer.html                   # Course Flyers & Admission Brochure
│       ├── news.html                    # CET in Media & Press Releases
│       └── placement.html               # Tech Club & Placement Cell
├── assets/
│   ├── images/                          # Official logos (logo.png, iitp-seal.png, footer-logo.png)
│   └── icons/                           # Reusable SVG sprites
├── css/
│   ├── global.css                       # CSS variables, typography, reset, disclaimer banner
│   ├── components.css                   # Header, navbar, cards, hero, ticker, buttons, tables, footer
│   └── responsive.css                   # Breakpoints (1200px, 992px, 768px, 480px)
├── js/
│   ├── navigation.js                    # Mobile drawer, dropdown hover/tap, active state
│   ├── programs.js                      # Program category filter tabs (UG/PG/PhD)
│   ├── ticker.js                        # Marquee ticker controls & pause on hover
│   └── main.js                          # Back-to-top button, preloader, shared utilities
├── docs/
│   ├── SITE_AUDIT.md                    # Live site reverse engineering audit
│   ├── PAGE_INVENTORY.md                # Page hierarchy, verification status, and routes
│   ├── DESIGN_SYSTEM.md                 # Visual design tokens & CSS rules
│   ├── ASSET_INVENTORY.md               # Asset sources and mapping
│   ├── IMPLEMENTATION_PLAN.md           # This document
│   └── TEST_REPORT.md                   # QA verification report (Phase 5)
├── README.md                            # Project documentation & local setup
└── .gitignore                           # Git ignore rules
```

---

## 3. Phased Implementation Roadmap

### Phase 1 — Discovery & Planning (Completed)
- [x] Inspect local workspace.
- [x] Analyze live CET website (`https://cet.iitp.ac.in/`) using browser automation and DOM extraction.
- [x] Extract design tokens, typography, colors, and layout metrics.
- [x] Create comprehensive planning documentation (`SITE_AUDIT.md`, `PAGE_INVENTORY.md`, `DESIGN_SYSTEM.md`, `ASSET_INVENTORY.md`, `IMPLEMENTATION_PLAN.md`).
- [x] Checkpoint 1 approved with Vercel hosting & scope updates.

### Phase 2 — Project Foundation (Current Phase)
- [x] Initialize Git repository locally; configure user name `ayushcmd` and user email `ayush_24a12res897@iitp.ac.in`.
- [x] Set remote URL to `https://github.com/ayushcmd/iitp-cet-mock.git`.
- [x] Download authentic public assets (`logo.png`, `iitp-seal.png`, `footer-logo.png`).
- [ ] Implement `css/global.css` with CSS custom properties, typography, reset, and site-wide disclaimer banner.
- [ ] Implement reusable components in `css/components.css` (header, multi-level dropdown navbar, footer, buttons, cards).
- [ ] Implement responsive styles in `css/responsive.css` (breakpoints: 1200px, 992px, 768px, 480px).
- [ ] Implement `js/navigation.js` and `js/main.js` (mobile offcanvas drawer, dropdown support, back-to-top, preloader).
- [ ] Create `README.md` and `.gitignore`.
- [ ] Perform local verification tests (using local HTTP server).
- [ ] **Approval Checkpoint 2**: Submit Phase 2 completion report and wait for approval before building the homepage.

### Phase 3 — Homepage Implementation
- Construct full `index.html`:
  - Official brand header with bilingual logo and topbar.
  - Desktop multi-level navigation and mobile slide-in drawer.
  - Glassmorphic Hero section with authentic CSS gradient backdrop (`linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)`).
  - Scrolling announcement marquee ticker bar.
  - 8/4 grid: Main mission overview + stats cards alongside Notice Board sidebar.
  - Programs section with client-side interactive category filter tabs (All, Undergraduate, Postgraduate, Doctoral) and 9 degree cards.
  - Tech Specializations comparative tracks (AICS & CSDA).
  - Modular qualification pathway step progress indicator (NEP-2020).
  - Value proposition blocks ("Why CET at IIT Patna?").
  - Admissions call-to-action banner.
  - Comprehensive footer with office location, quick links, and floating back-to-top button.
- Verify across desktop (1440px), tablet (768px), and mobile (390px).
- **Approval Checkpoint 3**: Present visual comparison and review homepage.

### Phase 4 — All Public Internal Pages
- **Batch 1 (Academic & Program Pages)**:
  - `pages/academics/academic-calendar.html`
  - `pages/academics/holiday-list.html`
  - `pages/academics/time-table.html`
  - `pages/academics/evaluation-scheme.html`
  - `pages/academics/re-exam-schedule.html`
  - `pages/academics/programs.html`
  - `pages/admissions/eligibility.html`
- **Batch 2 (Institutional & Announcements)**:
  - `pages/about.html`
  - `pages/faculty.html`
  - `pages/academic-service-charges.html`
  - `pages/announcements/flyer.html`
  - `pages/announcements/news.html`
  - `pages/announcements/placement.html`
- **Batch 3 (Portals & Student Services)**:
  - `pages/online-classes.html` (Moodle LMS)
  - `pages/bonafide-application.html` (Read-only informational mock)
  - `pages/admission-notice.html`
  - `pages/e-gymkhana.html`
- Verify relative link integrity across all pages.
- **Approval Checkpoint 4**: Review internal pages across batches.

### Phase 5 — Testing and Quality Assurance
- Responsive viewport audits (1440px, 768px, 390px).
- Interactive behaviors (mobile menu drawer toggle, program tab filters, marquee pause on hover, smooth scrolling, modal previews).
- Static path verification for local HTTP server and Vercel root deployment.
- Accessibility check (color contrast, alt texts, keyboard focus rings).
- Generate `docs/TEST_REPORT.md`.
- **Approval Checkpoint 5**: Review test report before deployment.

### Phase 6 — Vercel Deployment & Verification
- Review Git status, branch name, and staged files.
- Commit all assets and code with structured commit messages.
- Request user confirmation before pushing to remote repository (`ayushcmd/iitp-cet-mock`).
- Verify live deployment under Vercel at domain root.
- Provide summary report and technical mentoring walk-through.
