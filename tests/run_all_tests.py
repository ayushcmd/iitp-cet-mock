"""
IIT Patna - Centre for Educational Technology (CET) Replica
Site-Wide Quality Assurance & Test Suite Runner
Validates all 18 HTML pages, HTTP server status, asset resolution, accessibility primitives, and link integrity.
"""

import os
import re
import urllib.request
import urllib.error

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

PAGES = [
    'index.html',
    'pages/about.html',
    'pages/faculty.html',
    'pages/academic-service-charges.html',
    'pages/announcements/flyer.html',
    'pages/announcements/news.html',
    'pages/announcements/placement.html',
    'pages/admissions/eligibility.html',
    'pages/academics/academic-calendar.html',
    'pages/academics/evaluation-scheme.html',
    'pages/academics/holiday-list.html',
    'pages/academics/programs.html',
    'pages/academics/re-exam-schedule.html',
    'pages/academics/time-table.html',
    'pages/online-classes.html',
    'pages/bonafide-application.html',
    'pages/admission-notice.html',
    'pages/e-gymkhana.html'
]

def run_suite():
    print("================================================================================")
    print("      IIT PATNA CET REPLICA — CONSOLIDATED SITE-WIDE QA TEST SUITE              ")
    print("================================================================================\n")
    print(f"Project Workspace: {PROJECT_ROOT}")
    print(f"Total Configured Pages: {len(PAGES)}\n")

    suite_passed = True
    page_metrics = []

    total_internal_links = 0
    total_assets = 0
    total_broken_links = 0
    total_broken_assets = 0

    for rel_path in PAGES:
        abs_path = os.path.join(PROJECT_ROOT, os.path.normpath(rel_path))
        page_dir = os.path.dirname(abs_path)

        if not os.path.exists(abs_path):
            print(f"❌ [CRITICAL] File missing on disk: {rel_path}")
            suite_passed = False
            continue

        with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 1. HTTP 200 Status on local server
        url = f"http://localhost:3000/{rel_path.replace(os.sep, '/')}"
        http_code = None
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'CET-Test-Runner/1.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                http_code = resp.status
        except Exception as e:
            http_code = f"ERR: {e}"
            suite_passed = False

        # 2. Disclaimer & Meta Description
        has_disclaimer = 'replica-disclaimer' in content
        has_meta_replica = 'Unofficial educational replica' in content
        has_title = bool(re.search(r'<title>[^<]+</title>', content))

        # 3. Accessibility Primitives
        has_lang_en = '<html lang="en">' in content or "<html lang='en'>" in content
        has_banner = 'role="banner"' in content
        has_main = 'id="mainContent"' in content
        has_footer = 'role="contentinfo"' in content
        has_drawer = 'class="mobile-drawer"' in content
        has_skip_link = 'skip-link' in content and 'href="#mainContent"' in content
        has_h1 = bool(re.search(r'<h1[^>]*>.*?</h1>', content, re.IGNORECASE | re.DOTALL))

        # Check button accessible names
        buttons = re.findall(r'<button([^>]*)>(.*?)</button>', content, re.IGNORECASE | re.DOTALL)
        buttons_missing_name = []
        for attrs, inner in buttons:
            has_aria_label = 'aria-label=' in attrs or 'aria-labelledby=' in attrs
            has_inner_text = bool(re.sub(r'<[^>]+>', '', inner).strip())
            if not has_aria_label and not has_inner_text:
                buttons_missing_name.append(attrs)

        # 4. Check for broken image alts
        img_tags = re.findall(r'<img([^>]+)>', content, re.IGNORECASE)
        imgs_missing_alt = [img for img in img_tags if 'alt=' not in img]

        # 5. Check Table responsiveness
        tables = re.findall(r'<table', content, re.IGNORECASE)
        table_responsive_ok = True
        if tables:
            table_responsive_ok = 'table-responsive' in content

        # 6. Internal Link & Asset Resolution
        hrefs = re.findall(r'href="([^"]+)"', content)
        srcs = re.findall(r'src="([^"]+)"', content)

        broken_links_for_page = []
        for href in hrefs:
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:')):
                continue
            total_internal_links += 1
            clean_href = href.split('#')[0]
            if clean_href:
                target = os.path.normpath(os.path.join(page_dir, clean_href))
                if not os.path.exists(target):
                    broken_links_for_page.append((href, target))
                    total_broken_links += 1
                    suite_passed = False

        broken_assets_for_page = []
        for src in srcs:
            if src.startswith(('http://', 'https://', 'data:')):
                continue
            total_assets += 1
            target = os.path.normpath(os.path.join(page_dir, src))
            if not os.path.exists(target):
                broken_assets_for_page.append((src, target))
                total_broken_assets += 1
                suite_passed = False

        status_flag = "PASS" if (
            http_code == 200 and
            has_disclaimer and
            has_meta_replica and
            has_title and
            has_lang_en and
            has_banner and
            has_main and
            has_footer and
            has_drawer and
            has_skip_link and
            has_h1 and
            len(buttons_missing_name) == 0 and
            len(imgs_missing_alt) == 0 and
            table_responsive_ok and
            len(broken_links_for_page) == 0 and
            len(broken_assets_for_page) == 0
        ) else "FAIL"

        if status_flag == "FAIL":
            suite_passed = False

        page_metrics.append({
            'page': rel_path,
            'status': status_flag,
            'http': http_code,
            'disclaimer': has_disclaimer,
            'meta': has_meta_replica,
            'a11y_landmarks': (has_banner and has_main and has_footer and has_skip_link and has_h1),
            'img_alt_ok': len(imgs_missing_alt) == 0,
            'buttons_ok': len(buttons_missing_name) == 0,
            'table_resp': table_responsive_ok,
            'broken_links': len(broken_links_for_page),
            'broken_assets': len(broken_assets_for_page)
        })

    print(f"{'Page':<38} | {'HTTP':<5} | {'Disc.':<5} | {'Meta':<5} | {'A11y':<5} | {'Assets':<6} | {'Status'}")
    print("-" * 80)
    for m in page_metrics:
        print(f"{m['page']:<38} | {str(m['http']):<5} | {'OK' if m['disclaimer'] else 'FAIL':<5} | {'OK' if m['meta'] else 'FAIL':<5} | {'OK' if m['a11y_landmarks'] else 'FAIL':<5} | {'OK' if m['broken_assets']==0 else 'FAIL':<6} | {m['status']}")

    print("\n--------------------------------------------------------------------------------")
    print("                              METRICS SUMMARY                                   ")
    print("--------------------------------------------------------------------------------")
    print(f"Total HTML Pages Audited:       {len(page_metrics)}")
    print(f"Pages Passing All Checks:       {sum(1 for m in page_metrics if m['status'] == 'PASS')} / {len(page_metrics)}")
    print(f"Total Internal Links Verified:  {total_internal_links} (Broken: {total_broken_links})")
    print(f"Total Static Assets Verified:   {total_assets} (Broken: {total_broken_assets})")
    print("--------------------------------------------------------------------------------")

    # 7. Mathematical Color Contrast Verification (WCAG 2.2 AA)
    print("\n================================================================================")
    print("       WCAG 2.2 AA MATHEMATICAL CONTRAST VERIFICATION (MINIMUM 4.5:1)           ")
    print("================================================================================\n")
    contrast_passed = run_contrast_checks()
    if not contrast_passed:
        suite_passed = False

    # 8. Live Vercel Production Deployment Check
    print("\n================================================================================")
    print("       LIVE VERCEL PRODUCTION DEPLOYMENT VALIDATION                             ")
    print("================================================================================\n")
    vercel_passed = run_vercel_checks()
    if not vercel_passed:
        suite_passed = False

    if suite_passed:
        print("\n🎉 ALL SITE-WIDE TESTS PASSED SUCCESSFULLY (100% HEALTH INDEX)")
    else:
        print("\n❌ SITE-WIDE TESTS REPORTED ONE OR MORE FAILURES")
    print("================================================================================\n")
    return suite_passed

def srgb_to_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminance(r, g, b):
    return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)

def contrast(c1, c2):
    l1 = luminance(*c1)
    l2 = luminance(*c2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def run_contrast_checks():
    color_pairs = [
        ("Deep Navy (#002147) on Active Orange (#fb7906)", (0, 33, 71), (251, 121, 6), 4.5),
        ("Deep Navy (#002147) on Hover Orange (#e06c00)", (0, 33, 71), (224, 108, 0), 4.5),
        ("White (#ffffff) on Dark Navy Header (#003360)", (255, 255, 255), (0, 51, 96), 4.5),
        ("White (#ffffff) on Accessible CTA Blue (#1d68bd)", (255, 255, 255), (29, 104, 189), 4.5),
        ("White (#ffffff) on Alert Maroon Ticker (#8B0000)", (255, 255, 255), (139, 0, 0), 4.5),
        ("Primary Text (#212529) on Surface White (#ffffff)", (33, 37, 41), (255, 255, 255), 4.5),
        ("Secondary Text (#334155) on Surface White (#ffffff)", (51, 65, 85), (255, 255, 255), 4.5),
        ("Headings Navy (#042c53) on Surface White (#ffffff)", (4, 44, 83), (255, 255, 255), 4.5),
    ]

    print(f"{'UI Element / Color Pair':<52} | {'Ratio':<8} | {'Threshold':<9} | {'Status'}")
    print("-" * 80)
    all_ok = True
    for label, c1, c2, threshold in color_pairs:
        ratio = contrast(c1, c2)
        passed = ratio >= threshold
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_ok = False
        print(f"{label:<52} | {ratio:>5.2f}:1  | >={threshold:.1f}:1    | {status}")
    return all_ok

def run_vercel_checks():
    base_url = "https://iitp-cet-mock.vercel.app"
    print(f"Target Origin: {base_url}\n")
    print(f"{'Page Route':<42} | {'HTTP Code':<10} | {'Status'}")
    print("-" * 65)

    all_ok = True
    for rel_path in PAGES:
        u = f"{base_url}/{rel_path.replace(os.sep, '/')}"
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=8) as resp:
                code = resp.status
                passed = (code == 200)
        except Exception as e:
            code = f"ERR: {e}"
            passed = False

        if not passed:
            all_ok = False
        status_label = "PASS" if passed else "FAIL"
        print(f"{rel_path:<42} | {str(code):<10} | {status_label}")

    return all_ok

if __name__ == '__main__':
    run_suite()
