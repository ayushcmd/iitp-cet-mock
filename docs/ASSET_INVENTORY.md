# Asset Inventory — IIT Patna CET Website Replica

This document catalogs all visual, document, and font assets discovered on `https://cet.iitp.ac.in/`, their source URLs, purpose, local replication status, and permitted educational use.

---

## 1. Image Assets

| S.No. | Asset Name | Original URL | Local Mock Path | Status | Format | Source & Usage Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **CET & IITP Emblem (Header)** | `https://cet.iitp.ac.in/images/mobile-new-logo.png` | `assets/images/logo.png` | **Downloaded** | PNG (33.5 KB) | Official public header branding (bilingual IIT Patna crest & CET title). Used strictly under fair educational replica guidelines. |
| 2 | **IITP Seal (Favicon & Preloader)** | Authentic circular IIT Patna crest | `assets/images/iitp-seal.png`, `favicon.ico` | **Implemented** | PNG (256x256) & multi-size ICO | Official circular seal of IIT Patna. Used for site-wide browser tab favicon and authentic preloader animation. |
| 3 | **Footer Logo** | `https://cet.iitp.ac.in/images/footer-logo.png` | `assets/images/footer-logo.png` | **Downloaded** | PNG (19.0 KB) | High-contrast monochrome emblem for dark navy footer. |
| 4 | **Hero Background** | Direct gradient in live CSS (`linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)`) | Recreated natively in CSS (`--gradient-hero`) | **Implemented via CSS** | CSS3 | The live template uses a pure CSS linear gradient rather than a standalone raster image. This eliminates heavy network overhead and ensures crisp rendering across all screen densities. |
| 5 | **Faculty Portraits** | `https://cet.iitp.ac.in/images/faculty/...` | `assets/images/faculty/` | **Documented** | SVG / WebP Avatar placeholders | Neutral academic profile silhouettes / placeholders to avoid unlicensed third-party photo redistribution. |
| 6 | **Promotional Flyers & Clippings** | `https://cet.iitp.ac.in/images/announcements/...` | `assets/images/announcements/` | **Documented** | SVG / CSS cards | High-fidelity card layout representations in pure CSS/SVG rather than copyrighted newspaper scan bitmaps. |

---

## 2. Iconography

- **FontAwesome 6 Free** & **Bootstrap Icons**:
  - Embedded via lightweight SVG sprite definitions in `assets/icons/icons.svg` or standard SVG inline symbols:
    - Search (`fa-search`)
    - Dropdown carets (`fa-chevron-down`)
    - Mobile hamburger (`fa-bars`)
    - Mobile close button (`fa-times`)
    - Calendar (`fa-calendar-days`)
    - Clock (`fa-clock`)
    - Document download (`fa-file-pdf`)
    - Location pin (`fa-location-dot`)
    - Email envelope (`fa-envelope`)
    - External link (`fa-arrow-up-right-from-square`)
    - Up arrow (`fa-arrow-up`) for Back-to-Top
- **Unicode Emoji Badges (Native to browser/OS)**:
  - 🎓 Degree / Admission
  - 🚀 Apply / Launch
  - 📚 Programs / Books
  - 📢 Announcements
  - 🗓️ Calendar / Dates
  - ⚡ Hands-on Training
  - 🕐 Schedule Flexibility
  - 🎉 NEP 2020 Aligned
  - 📅 2 Intakes Yearly

---

## 3. Official Documents & Academic Schedules (PDFs)

All official downloadable academic schedules are linked directly to their public institutional URLs to maintain factual authenticity without unauthorized document alteration:

1. **UG Academic Calendar Autumn 2024**: `https://cet.iitp.ac.in/images/pdf/UGAC24.pdf`
2. **UG Academic Calendar Spring 2025**: `https://cet.iitp.ac.in/images/199.pdf`
3. **UG Academic Calendar Autumn 2025**: `https://cet.iitp.ac.in/images/pdf/1000.pdf`
4. **UG Academic Calendar Spring 2026**: `https://cet.iitp.ac.in/images/pdf/2000.pdf`
5. **UG Academic Calendar Autumn 2026**: `https://cet.iitp.ac.in/images/pdf/20262.pdf`
6. **Moodle SOP Guidelines**: `https://cet.iitp.ac.in/images/SOP.pdf`

---

## 4. Typography & Fonts

- **Family**: `Source Sans Pro`
- **Source**: Google Fonts (`https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&display=swap`)
- **System Fallback Stack**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
