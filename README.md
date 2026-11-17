# IIT Patna — Centre for Educational Technology (CET) Website Replica

> [!IMPORTANT]
> **LEGAL & INSTITUTIONAL DISCLAIMER**:
> This repository contains an **unofficial educational replica** of the public-facing website of the **Centre for Educational Technology (CET) at the Indian Institute of Technology Patna (IIT Patna)** (`https://cet.iitp.ac.in/`).
> This project was developed strictly for personal learning, frontend engineering research, and UI reverse-engineering. It is **not affiliated with, endorsed by, or authorized by IIT Patna**.
> For official academic information, admissions, schedules, circulars, and services, visit the official portal at **[cet.iitp.ac.in](https://cet.iitp.ac.in/)**.

---

## 1. Technical Stack & Philosophy

This project strictly adheres to zero-framework, standards-compliant web engineering:

- **HTML5**: Semantic tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<table>`).
- **CSS3**: Pure CSS custom properties (design tokens), flexbox, grid, glassmorphic filters (`backdrop-filter`), keyframe animations, media query breakpoints (`1200px`, `992px`, `768px`, `480px`). Zero CSS frameworks (no Tailwind, Bootstrap CSS, or Sass compilation required).
- **Vanilla JavaScript (ES6+)**: Modular scripts handling mobile drawer toggle, accordion menus, smooth scrolling, active route detection, and category filtering. Zero runtime dependencies (no React, Vue, jQuery, or Node.js runtime required).
- **Target Deployment Platform**: **Vercel** (Framework preset: `Other`, deployed at domain root).
- **Source Control**: GitHub (`https://github.com/ayushcmd/iitp-cet-mock.git`).

---

## 2. Project Architecture

```text
iitp-cet-mock/
├── index.html                           # Complete Homepage (Hero, programs, notices, stats)
├── pages/                               # 17 Categorized Internal Pages
│   ├── about.html                       # About CET & The Institute
│   ├── faculty.html                     # Faculty & Mentors Directory
│   ├── academic-service-charges.html    # Academic Service Charges Table
│   ├── online-classes.html              # Moodle & Online LMS Portal Guide
│   ├── bonafide-application.html        # Bonafide Application Portal (Read-only Mock)
│   ├── admission-notice.html            # Admission Notices Archive
│   ├── e-gymkhana.html                  # E-Gymkhana Portal
│   ├── admissions/
│   │   └── eligibility.html             # Detailed Eligibility Criteria
│   ├── academics/
│   │   ├── academic-calendar.html       # Academic Calendars (PDF downloads)
│   │   ├── holiday-list.html            # Institute Holidays 2025/2026
│   │   ├── time-table.html              # Semester Lecture Timetables
│   │   ├── evaluation-scheme.html       # Evaluation & Grading Scheme
│   │   ├── re-exam-schedule.html        # Re-Exam & Supplementary Schedule
│   │   └── programs.html                # Degree Programs Detail Catalog
│   └── announcements/
│       ├── flyer.html                   # Course Flyers & Brochure
│       ├── news.html                    # CET in Media & Press Releases
│       └── placement.html               # Tech Club & Placement Cell
├── assets/
│   ├── images/                          # Official logos (logo.png, iitp-seal.png, footer-logo.png)
│   └── icons/                           # Reusable SVG assets
├── css/
│   ├── global.css                       # Variables, typography, reset, disclaimer banner
│   ├── components.css                   # Header, navbar, cards, tables, footer
│   └── responsive.css                   # Responsive layout & mobile drawer
├── js/
│   ├── navigation.js                    # Mobile drawer, dropdown hover/tap, active route
│   ├── programs.js                      # Program tab filter logic (UG/PG/Doctoral)
│   ├── ticker.js                        # Marquee ticker controls & pause on hover
│   └── main.js                          # Back-to-top button, preloader, disclaimer
├── docs/                                # Reverse-engineering audit & design system specifications
│   ├── SITE_AUDIT.md
│   ├── PAGE_INVENTORY.md
│   ├── DESIGN_SYSTEM.md
│   ├── ASSET_INVENTORY.md
│   └── IMPLEMENTATION_PLAN.md
├── README.md
└── .gitignore
```

---

## 3. Local Development & Testing

Because this project is built entirely on native web standards with zero build pipelines, you can run and test it locally using any lightweight static web server:

### Option A: Python Built-in HTTP Server (Recommended)
```bash
# In the project root (C:\Projects\AYUSHCMD-GITHUB\iitp-cet-mock)
python -m http.server 3000
```
Then navigate to: `http://localhost:3000`

### Option B: Node.js `serve` / `npx http-server`
```bash
npx serve .
# or
npx http-server -p 3000
```

---

## 4. Vercel Deployment Instructions

1. **Connect Repository**: Import `https://github.com/ayushcmd/iitp-cet-mock` in the Vercel Dashboard.
2. **Framework Preset**: Select **Other**.
3. **Build & Development Settings**:
   - Build Command: *(Leave blank)*
   - Output Directory: `.` *(Root directory)*
   - Install Command: *(Leave blank)*
4. **Deploy**: Click Deploy. Vercel automatically serves the static assets at your custom domain or `*.vercel.app` domain root.

---

## 5. Development Phases

- **Phase 1: Discovery & Planning** — *Completed & Approved*
- **Phase 2: Project Foundation & Shared Components** — *Completed & Approved*
- **Phase 3: Homepage Implementation** — *Completed & Merged to Master*
- **Phase 4: Public Internal Pages Implementation** — *Completed & Verified (Batches 1, 2, and 3: All 18 Pages Fully Implemented & Audited)*
- **Phase 5: Testing & Quality Assurance** — *Completed & Verified (18/18 Pages Audited, WCAG 2.2 AA Compliant, 100% Health Index)*
- **Phase 6: Vercel Production Deployment** — *Pending Final Approval*
