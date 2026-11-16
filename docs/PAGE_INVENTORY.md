# Page Inventory — IIT Patna CET Website Replica

This document records all public-facing pages discovered on `https://cet.iitp.ac.in/`, their corresponding mock site routes, page types, layout patterns, verification status, and implementation complexities.

---

## Complete Navigation Tree & Information Architecture

```text
├── [Home] (index.html) -> Verified
├── [About] (pages/about.html) -> Verified
├── [Announcements] (Dropdown)
│   ├── Flyer (pages/announcements/flyer.html) -> Verified
│   ├── News (pages/announcements/news.html) -> Verified
│   └── Technology Club & Internship - Placement Cell (pages/announcements/placement.html) -> Verified
├── [Admissions] (Dropdown)
│   ├── Eligibility (pages/admissions/eligibility.html) -> Verified
│   └── Apply Form (External: https://registrations.iitp-cep.in/) -> Verified
├── [Academics] (Dropdown)
│   ├── Academic Calendar (pages/academics/academic-calendar.html) -> Verified
│   ├── Evaluation Scheme (pages/academics/evaluation-scheme.html) -> Verified
│   ├── Holiday List (pages/academics/holiday-list.html) -> Verified
│   ├── Program (Nested Flyout Submenu)
│   │   ├── B.Tech Artificial Intelligence and Data Science (pages/academics/programs.html#btech-aids) -> Verified
│   │   ├── B.Tech Computer Science and Engineering (pages/academics/programs.html#btech-cse) -> Verified
│   │   ├── Executive M.Tech in AI & DSE (pages/academics/programs.html#mtech-aidse) -> Verified
│   │   └── BBA (pages/academics/programs.html#bba) -> Verified
│   ├── Time Table (pages/academics/time-table.html) -> Verified
│   ├── UG - Re - Exam Schedule (pages/academics/re-exam-schedule.html) -> Verified
│   └── Institute Holidays for Year 2025 (pages/academics/holiday-list.html#2025) -> Verified
├── [Faculty] (pages/faculty.html) -> Verified
├── [MOODLE] (pages/online-classes.html / External: https://cet.iitp.ac.in/moodle/) -> Verified
├── [Apply Now] (External: https://registrations.iitp-cep.in/) -> Verified
├── [E-Gymkhana] (pages/e-gymkhana.html) -> Verified ("Coming Soon !!")
├── [admission notice] (pages/admission-notice.html) -> Verified
└── [Bonafide Application] (pages/bonafide-application.html) -> Verified (Read-only informational mock)
```

---

## Detailed Page Mapping Matrix

| S.No. | Page Title | Original URL | Mock Route | Category | Layout Type | Verification & Build Status | Mock Handling & Safety | Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Home** | `https://cet.iitp.ac.in/index.php` | `index.html` | Core | Hero + 8/4 Split + Grids | **Implemented & Verified** | Full replica with disclaimer, marquee ticker, program filters, and notice sidebar | High |
| 2 | **About / The Institute** | `https://cet.iitp.ac.in/index.php/the-institute` | `pages/about.html` | Institutional | Content with Sidebar | **Implemented & Verified** | Institute overview, NEP-2020 alignment, mission & vision | Medium |
| 3 | **Announcements - Flyer** | `https://cet.iitp.ac.in/index.php/announcements/flyer` | `pages/announcements/flyer.html` | Announcements | Card / Document Showcase | **Implemented & Verified** | Program flyers and admission brochure showcases | Low |
| 4 | **Announcements - News** | `https://cet.iitp.ac.in/index.php/announcements/news` | `pages/announcements/news.html` | Announcements | Media / Press Grid | **Implemented & Verified** | Authentic news clippings (3 articles) and media coverage | Medium |
| 5 | **Announcements - Tech Club & Placement** | `https://cet.iitp.ac.in/index.php/announcements/technology-club-internship-placement-cell` | `pages/announcements/placement.html` | Announcements | Info & List Layout | **Implemented & Verified** | Placement cell initiatives, selected candidate PDF links, and club info | Low |
| 6 | **Admissions - Eligibility** | `https://cet.iitp.ac.in/index.php/admissions/eligiblity` | `pages/admissions/eligibility.html` | Admissions | Tabbed / Accordion Tables | **Implemented & Verified** | Detailed 10+2 science & qualifying exam scores | Medium |
| 7 | **Academics - Academic Calendar** | `https://cet.iitp.ac.in/index.php/academics/academic-calendar` | `pages/academics/academic-calendar.html` | Academics | Document Table & Download Hub | **Implemented & Verified** | Session calendars (Autumn 2024 - Autumn 2026) with official PDF links | Medium |
| 8 | **Academics - Evaluation Scheme** | `https://cet.iitp.ac.in/index.php/academics/evaluation-scheme` | `pages/academics/evaluation-scheme.html` | Academics | Information & Policy | **Implemented & Verified** | Continuous grading, quiz weightage, end-semester evaluation | Medium |
| 9 | **Academics - Holiday List** | `https://cet.iitp.ac.in/index.php/academics/holiday-list` | `pages/academics/holiday-list.html` | Academics | Structured Calendar Table | **Implemented & Verified** | Official gazetted and restricted institute holidays | Low |
| 10 | **Academics - Time Table** | `https://cet.iitp.ac.in/index.php/academics/time-table` | `pages/academics/time-table.html` | Academics | Schedule Tables | **Implemented & Verified** | Slot timetable matrices for active semesters | Medium |
| 11 | **Academics - UG Re-Exam Schedule** | `https://cet.iitp.ac.in/index.php/academics/ug-re-exam-schedule` | `pages/academics/re-exam-schedule.html` | Academics | Schedule Table | **Implemented & Verified** | Supplementary and re-examination timetables | Low |
| 12 | **Academic Programs (Submenu)** | `https://cet.iitp.ac.in/index.php/academics/program/...` | `pages/academics/programs.html` | Academics | Program Detail Catalog | **Implemented & Verified** | Curricula for B.Tech AI & DS, B.Tech CSE, Exec M.Tech, and BBA | Medium |
| 13 | **Faculty Directory** | `https://cet.iitp.ac.in/index.php/faculty` | `pages/faculty.html` | People | Profile Card Grid | **Implemented & Verified** | Chief Mentor (Director IIT Patna), Coordinators, CSE, Math & Management faculty with authentic photos | Medium |
| 14 | **Moodle / Online Classes** | `https://cet.iitp.ac.in/index.php/online-classes` | `pages/online-classes.html` | Portal / LMS | Guide & Access Hub | **Implemented & Verified** | LMS instructions, SOP guide, link to official Moodle | Low |
| 15 | **Academic Service Charges** | `https://cet.iitp.ac.in/index.php?view=article&id=66:...` | `pages/academic-service-charges.html` | Information / Fee | Data Table | **Implemented & Verified** | 10 verified fee items (Marksheet, Transcripts, Bonafide, Exam fee) | Low |
| 16 | **Bonafide Application** | `https://cet.iitp.ac.in/index.php/bonafide-application` | `pages/bonafide-application.html` | Student Services | Informational / Mock Demo | **Implemented & Verified** | **Read-only informational mock**. Explains requirements, turnaround times, and official contacts. No personal information is collected. | Medium |
| 17 | **E-Gymkhana** | `https://cet.iitp.ac.in/index.php/e-gymkhana` | `pages/e-gymkhana.html` | Student Life | Notice Banner | **Implemented & Verified** | "Coming Soon !!" status notice | Low |
| 18 | **Admission Notice** | `https://cet.iitp.ac.in/index.php/admission-notice` | `pages/admission-notice.html` | Admissions | Circular / Notice Archive | **Implemented & Verified** | Admission circular archive and intake notifications | Low |

---

## External Integrated Systems (Official Endpoints Preserved)

1. **Registration & Application Portal**: `https://registrations.iitp-cep.in/` (Official external link with open-in-new-tab icon)
2. **Official Moodle LMS Portal**: `https://cet.iitp.ac.in/moodle/` (Official external link)
3. **Official IIT Patna Main Portal**: `https://www.iitp.ac.in/` (Official institutional link)
