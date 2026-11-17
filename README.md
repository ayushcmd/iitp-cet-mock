# IIT Patna — Centre for Educational Technology (CET) Website Replica

> [!IMPORTANT]
> **LEGAL & INSTITUTIONAL DISCLAIMER**:
> This repository contains an **unofficial educational replica** of the public-facing website of the **Centre for Educational Technology (CET) at the Indian Institute of Technology Patna (IIT Patna)** (`https://cet.iitp.ac.in/`).
> This project was developed strictly for personal learning, frontend engineering research, accessibility analysis, and UI reverse-engineering. It is **not affiliated with, endorsed by, or authorized by IIT Patna**.
> For official academic information, admissions, schedules, circulars, and services, visit the official portal at **[cet.iitp.ac.in](https://cet.iitp.ac.in/)**.

---

## 1. Project Overview & Production URL

- **Production Deployment URL**: **[https://iitp-cet-mock.vercel.app/](https://iitp-cet-mock.vercel.app/)**
- **GitHub Repository**: **[https://github.com/ayushcmd/iitp-cet-mock](https://github.com/ayushcmd/iitp-cet-mock)**
- **Official Institutional Portal**: **[https://cet.iitp.ac.in/](https://cet.iitp.ac.in/)**
- **Hosting Target**: Vercel Static Hosting (Edge Network at Root Domain)
- **Framework Preset**: "Other" (Zero-framework, static site)
- **Primary Branch**: `master`

---

## 2. Technical Philosophy & Stack

This project strictly adheres to native, zero-framework, standards-compliant web engineering principles:

- **HTML5**: Semantic tags (`<header>`, `<nav>`, `<main id="mainContent">`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<table>`, `<th scope="col">`). Includes accessible skip-navigation links across all 18 pages.
- **CSS3**: Pure CSS custom properties (design tokens), modern CSS Grid, Flexbox, glassmorphic filters (`backdrop-filter`), keyframe animations, and responsive media queries (`1200px`, `992px`, `768px`, `480px`, `320px`). Zero CSS frameworks (no Tailwind, Bootstrap, or Sass compilation required).
- **Vanilla JavaScript (ES6+)**: Pure client-side scripts handling mobile offcanvas drawer navigation, keyboard focus trapping, accessible accordion toggles, hero carousels with pause-on-hover/touch/reduced-motion, dynamic category filtering, and preloader lifecycle. Zero runtime dependencies (no React, Vue, jQuery, or Node.js runtime required).
- **Security & Caching**: Custom `vercel.json` injecting HTTP security headers (`Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`) and long-term immutable caching headers for static assets.

---

## 3. Project Architecture & Complete Page Inventory

```text
iitp-cet-mock/
├── index.html                           # Complete Homepage (Hero, programs, notices, stats)
├── favicon.ico                          # 32x32 Institutional Favicon (ICO format)
├── robots.txt                           # Web crawler instructions & sitemap link
├── sitemap.xml                          # Canonical XML sitemap indexing all 18 routes
├── vercel.json                          # Vercel static routing, caching & security headers
├── pages/                               # 17 Categorized Internal Pages
│   ├── about.html                       # About CET & The Institute (NEP-2020 alignment)
│   ├── faculty.html                     # Faculty Directory & Department Filter
│   ├── academic-service-charges.html    # Academic Charges Schedule (Responsive Table)
│   ├── online-classes.html              # Moodle & Online LMS Portal Guide
│   ├── bonafide-application.html        # Bonafide Application Portal (Read-only Mock)
│   ├── admission-notice.html            # Admission Notices & Historical Session Archive
│   ├── e-gymkhana.html                  # E-Gymkhana Portal (Student Life Notice)
│   ├── admissions/
│   │   └── eligibility.html             # Detailed Eligibility Criteria & Matrices
│   ├── academics/
│   │   ├── academic-calendar.html       # Academic Calendars (Official PDF links)
│   │   ├── holiday-list.html            # Institute Holidays 2025/2026 Schedule Table
│   │   ├── time-table.html              # Semester Lecture Timetable Matrices
│   │   ├── evaluation-scheme.html       # Evaluation, Quiz & Grading Scheme
│   │   ├── re-exam-schedule.html        # Supplementary & Re-Exam Schedules
│   │   └── programs.html                # Degree Programs Detail Catalog (Curricula)
│   └── announcements/
│       ├── flyer.html                   # Course Flyers & Brochure Repository
│       ├── news.html                    # CET in Media & Press Clipping Archive
│       └── placement.html               # Tech Club & Selected Candidates
├── assets/
│   ├── images/                          # Authentic logos (logo.png, iitp-seal.png, footer-logo.png)
│   │   ├── faculty/                     # Faculty headshots (tns.jpg, akt.jpg, nkt.jpg)
│   │   └── news/                        # Newspaper media clippings (news-1, news-2, news-3)
│   └── icons/                           # Reusable SVG assets
├── css/
│   ├── global.css                       # Variables, typography, reset, skip-link, focus rings
│   ├── components.css                   # Header, navbar, cards, tables, accordions, footer
│   └── responsive.css                   # Breakpoints, mobile drawer, responsive table wrappers
├── js/
│   ├── navigation.js                    # Mobile drawer, focus trap, dropdown hover/tap, active route
│   ├── programs.js                      # Program tab filter logic (UG/PG/Doctoral)
│   └── main.js                          # Back-to-top button, preloader, disclaimer, modal
├── tests/
│   ├── run_all_tests.py                 # Site-wide test suite (HTTP, a11y, links, contrast, Vercel)
│   └── check_external_urls.py           # Network audit of external endpoints & documents
├── docs/                                # Reverse-engineering documentation & audits
│   ├── SITE_AUDIT.md                    # Initial discovery & competitive audit
│   ├── PAGE_INVENTORY.md                # 18-page navigation tree & mapping matrix
│   ├── DESIGN_SYSTEM.md                 # Design tokens, typography, and palette specs
│   ├── ASSET_INVENTORY.md               # Asset provenance & dimensions inventory
│   ├── IMPLEMENTATION_PLAN.md           # Phased development roadmap
│   ├── QA_REPORT.md                     # Consolidated quality assurance report
│   ├── VISUAL_AUDIT.md                  # Visual parity & component comparison
│   ├── ACCESSIBILITY_AUDIT.md           # WCAG 2.2 AA evaluation & contrast analysis
│   ├── PERFORMANCE_AUDIT.md             # Payload metrics & Core Web Vitals analysis
│   └── PRODUCTION_RELEASE.md            # Final release verification & DNS assessment
└── README.md
```

---

## 4. Local Development & Testing Instructions

Because this project is built entirely on native web standards with zero build steps or bundlers, it can be tested locally using any standard static HTTP server:

### Option A: Python Built-in HTTP Server (Recommended)
```bash
# In the repository root (C:\Projects\AYUSHCMD-GITHUB\iitp-cet-mock)
python -m http.server 3000
```
Then open your browser at: `http://localhost:3000`

### Option B: Node.js `serve` / `http-server`
```bash
npx serve .
# or
npx http-server -p 3000
```

### Running Automated Test Suites
```bash
# Run comprehensive site-wide QA & Vercel live check:
python tests/run_all_tests.py

# Audit all 44 external links over the network:
python tests/check_external_urls.py
```

---

## 5. Vercel Production Deployment Instructions

1. **Connect Repository**: Import `https://github.com/ayushcmd/iitp-cet-mock` in your Vercel Dashboard.
2. **Framework Preset**: Select **Other**.
3. **Build & Output Settings**:
   - Build Command: *(Leave empty)*
   - Output Directory: `.` *(Root directory)*
   - Install Command: *(Leave empty)*
4. **Deploy**: Click Deploy. Vercel automatically deploys the static files to its global Edge Network at `https://iitp-cet-mock.vercel.app/`.

---

## 6. Git Workflow & Branching Strategy

This project enforces strict Git hygiene to protect production stability:
- **Default Branch**: `master` (protected; no direct commits).
- **Feature Branches**: Every task develops on a dedicated branch (e.g., `feat/academic-pages`, `fix/navigation-contrast`, `chore/production-release`).
- **Conventional Commits**: Commit messages follow the Conventional Commits specification:
  - `feat: add academic programs page`
  - `fix: improve navigation text contrast`
  - `test: strengthen accessibility checks`
  - `docs: finalize production release verification`
- **Pull Requests**: Changes are merged into `master` exclusively via Pull Requests following thorough testing and approval.

---

## 7. Known Limitations & Content Safety

1. **Bonafide Application Portal (Specimen Only)**:
   - In compliance with student data privacy, `pages/bonafide-application.html` is an unmistakable **read-only informational mock**. It does NOT collect, store, or transmit personal student information.
   - For official applications, students are routed via external links to the verified institutional Microsoft Forms link.
2. **Online LMS & Admissions Portals**:
   - The Moodle portal (`https://cet.iitp.ac.in/moodle/`) and CEP Registration portal (`https://registrations.iitp-cep.in/`) are external institutional systems. The mock site provides user guides and direct links to these official endpoints with `target="_blank" rel="noopener noreferrer"`.
3. **Historical Circulars & Notices**:
   - Notices (such as the Spring 2026 admission deferral notice and Autumn 2025 bonafide pause banner) reflect the authentic state of the source website at the time of archiving and are explicitly labeled as **Historical Session Archives**.

---

## 8. Development Phases & Completion Record

- [x] **Phase 1: Discovery & Planning** — Architectural audit, asset inventory, and page mapping.
- [x] **Phase 2: Project Foundation & Shared Components** — CSS design tokens, responsive header, footer, navigation drawer, and test harness.
- [x] **Phase 3: High-Fidelity Homepage Implementation** — Root `index.html` with hero carousel, marquee ticker, program cards, and notice sidebar.
- [x] **Phase 4: Public Internal Pages Implementation** — All 17 internal pages implemented across three structured batches (Academics, Institutional, and Student Services).
- [x] **Phase 5: Site-Wide QA & Final Refinements** — Comprehensive multi-viewport testing, WCAG 2.2 AA contrast remediation, skip-navigation links, and performance benchmarking.
- [x] **Phase 6: Production Verification & Final Documentation** — Vercel edge deployment validation, TLS security verification, custom domain feasibility analysis, and final production release documentation.

---

## 9. Official Institutional Attribution

This project is dedicated to open educational frontend engineering and honors the academic leadership of **IIT Patna**:
- **Institute**: Indian Institute of Technology Patna (IIT Patna), Bihta, Patna, Bihar, India - 801106
- **Centre**: Centre for Educational Technology (CET)
- **Official Website**: [https://cet.iitp.ac.in/](https://cet.iitp.ac.in/)
- **Main Institute Portal**: [https://www.iitp.ac.in/](https://www.iitp.ac.in/)
