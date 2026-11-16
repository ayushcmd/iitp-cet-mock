# Website Audit — Centre for Educational Technology (CET), IIT Patna

## 1. Executive Summary & Context

The official website of the **Centre for Educational Technology (CET)** at the **Indian Institute of Technology Patna (IIT Patna)** (`https://cet.iitp.ac.in/`) serves as the official digital gateway for CET's academic programs, NEP-2020 aligned degree courses, semester timetables, academic calendars, notifications, examination schedules, fee structures, and learning portal (Moodle) integrations.

This audit provides an evidence-based reverse-engineering analysis of the live website, evaluating its technical architecture, visual layout, navigation system, responsive adaptations, page hierarchy, and assets.

> [!IMPORTANT]
> **Project Disclaimer**: This project is strictly an unofficial personal educational replica created for frontend engineering and UI reverse-engineering learning. It is not affiliated with, endorsed by, or representing IIT Patna. Official information is hosted exclusively at `https://cet.iitp.ac.in/`.

---

## 2. Technical Stack and Infrastructure

Through live inspection of HTTP headers, DOM structure, and linked assets, the technical stack of `https://cet.iitp.ac.in/` was identified:

- **Content Management System (CMS)**: Joomla! 4.x / 5.x CMS
- **Template Framework**: Astroid Framework (Template Zero v2.6.5 / 3.x)
- **CSS Framework**: Bootstrap 5.3 customized with Astroid SCSS variables, utilities, and direct inline element styling.
- **Color Gradients**: Hero backdrop uses an established linear gradient: `linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)`.
- **Web Fonts**: Google Fonts `Source Sans Pro` (weights: 200, 300, 400, 600, 700, 900), with system fallback stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`).
- **Iconography**: FontAwesome 6 Free (`all.css`), Joomla FontAwesome (`joomla-fontawesome.css`), and Bootstrap Icons (`bi`), enriched with modern Unicode emoji badges (🎓, 🚀, 📚, 📢, 🗓️, ⚡, 🕐, 🎉, 📅).
- **Analytics & Tracking**: Google Analytics 4 (`G-68TLSNH0ZD`) — *omitted in replica*.
- **Hosting Strategy**: Target deployment on **Vercel** as a static website (preset: "Other") at the domain root, with source control hosted at GitHub (`https://github.com/ayushcmd/iitp-cet-mock.git`).

---

## 3. Visual and Structural Architecture

### 3.1 Header and Navigation
- **Preloader**: Full-screen white overlay with a spinning circular IIT Patna seal (`assets/images/iitp-seal.png` / `footer-logo.png`), fading smoothly upon `domcontentloaded`.
- **Top Branding Bar**:
  - Left: IIT Patna official emblem paired with bilingual English and Hindi typography: "भारतीय प्रौद्योगिकी संस्थान पटना | Indian Institute of Technology Patna" and "शैक्षणिक प्रौद्योगिकी केंद्र | Centre for Educational Technology" (`assets/images/logo.png`).
  - Desktop view width: Fluid with inner container bounded to `1320px` max-width.
  - Background color: Deep Navy Blue (`#003360` / `rgb(0, 51, 96)`).
- **Navigation Bar**:
  - Horizontal menu bar attached to header with active status indicators (e.g. orange pill for "Home" `#fb7906`).
  - Multi-level hover menus for "Announcements", "Admissions", and "Academics" (which features a nested flyout submenu for "Program").
  - Quick action call-to-action button: "Apply Now" (`https://registrations.iitp-cep.in`).

### 3.2 Homepage Component Anatomy
1. **Hero Section**:
   - Background: Deep navy royal gradient `linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)`.
   - Glassmorphic Hero Card: Semi-transparent backdrop with `rgba(255, 255, 255, 0.08)`, `backdrop-filter: blur(16px)`, rounded corners (`border-radius: 16px`).
   - Callouts:
     - Heading: "Centre for Educational Technology"
     - Subheading: "Empowering Education through Technology @ IIT Patna"
     - CTA Pills: `🎓 Admission Open For Autumn 2026 Session` and `🎓 Academic Calendar for Autumn 2026 NEW` (with an animated CSS blinking badge).
2. **Announcement Marquee Ticker**:
   - Dark crimson / maroon bar (`#8B0000` / `#990000`) situated directly below the hero.
   - Fixed badge: `📢 Announcements:`
   - Continuous horizontal scrolling marquee with key updates (`🗓️ Academic Calendar for Autumn 2025`, `🚀 Applications Invited Year-Round | Apply Now`).
3. **Introduction & Quick Stats**:
   - Two-column split layout (8 cols main content + 4 cols sidebar on desktop):
     - Main column: Detailed introduction to CET's mission under NEP-2020, with action links `🚀 Apply for Autumn 2026` and `📚 Browse programs`.
     - Stats row (4 cards, `#F4F6FB` surface): `9+ Degree programs`, `2 Tech specializations`, `2× Intakes per year`, `IIT Senate approved`.
4. **Notice Board Sidebar**:
   - Prominent card with deep navy title header `Notice` and clean list group:
     - Academic Service Charges
     - Quiz - II Schedule (Autumn 2025 Session)
     - Admission Autumn 2026
     - Moodle Portal Information
     - Holidays List
5. **Programs Section (`#cet-programs`)**:
   - Section heading: "Programs — Modular, flexible pathways for undergraduate, postgraduate, and doctoral study."
   - Pill-shaped Category Filter Tabs:
     - `All programs` (active filter state with light blue background `#E6F1FB`, blue border `#378ADD`, dark blue text `#042c53`)
     - `Undergraduate`
     - `Postgraduate`
     - `Doctoral`
   - 9 Degree Program Cards (responsive grid):
     - BBA, BBA–MBA (Integrated), BS (AICS / CSDA), BS–MS (AICS / CSDA), MS (AICS / CSDA), MBA, MBA (Gen AI & PM), MTech (AI & DSE / CSE), PhD.
     - Each card displays degree title, duration, curriculum summary, eligibility snippet, and a distinct "Register →" button linking to the registration subdomain.
6. **Tech Specializations**:
   - Dual-track side-by-side comparative cards:
     - Track 1: **AICS** (Artificial Intelligence and Cyber Security)
     - Track 2: **CSDA** (Computer Science and Data Analytics)
7. **Modular Learning Pathway (NEP 2020 Multi-Exit)**:
   - Visual progress pathway demonstrating the 4-tier graduation architecture:
     - Certificate (2 semesters) -> Diploma (4 semesters) -> B.Sc. (6 semesters) -> B.S. (8 semesters).
8. **Why CET**:
   - Grid of 4 value proposition cards: Hands-on training, Flexible schedule, NEP 2020 aligned, 2 intakes yearly.
9. **Footer**:
   - Dark Royal Navy background (`#095aa3`).
   - Contact details, administrative office location, quick links, academic shortcuts, official copyright, and an interactive orange floating "Back to Top" button (`#fb7906`).

---

## 4. Responsive Viewport Analysis

### Desktop Viewport (1440px)
- Full expanded navbar with multi-level dropdowns.
- 8/4 grid layout for hero intro and notice sidebar.
- 5-column / 4-column adaptive layout for program cards.
- Content constrained to `1320px` container.

### Tablet Viewport (768px)
- Navbar collapses into hamburger toggle button.
- Notice board wraps under the main introduction column.
- Program grid shifts to 2 columns.
- Font sizes adjust smoothly.

### Mobile Viewport (390px)
- Top navbar collapses completely into a sticky top bar with brand emblem and hamburger button.
- Offcanvas slide-out drawer from left containing full menu navigation with accordion carets for submenus.
- Program cards stack in a single column.
- Hero action buttons stack vertically.
- Tables receive horizontal scroll containers to prevent page overflow.

---

## 5. Replica Scope & Safety Directives

As an **educational replica**:
1. **Disclaimer**: A prominent disclaimer bar will be integrated across all pages:
   *"Unofficial educational replica of the IIT Patna CET website. Created for personal learning. Not affiliated with or endorsed by IIT Patna. For official information, visit cet.iitp.ac.in."*
2. **Security & Privacy**: Zero collection, storage, or transmission of student personal data or credentials.
3. **Bonafide Application Handling**: Implemented strictly as an informational notice and read-only demonstrational mock, explicitly explaining application rules and redirecting official requests to the legitimate administrative section.
4. **External Services**: Admissions links point to the official external portal (`https://registrations.iitp-cep.in/`) and Moodle LMS points to `https://cet.iitp.ac.in/moodle/`.
