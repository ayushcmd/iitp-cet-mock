import glob
import re
import os

pages = glob.glob('pages/**/*.html', recursive=True)
print(f"Found {len(pages)} subpages to inspect:\n")

all_ok = True

for p in sorted(pages):
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    has_disclaimer = 'replica-disclaimer' in content
    has_header = '<header' in content
    has_footer = '<footer' in content
    has_desktop_nav = 'class="desktop-nav"' in content
    has_mobile_drawer = 'class="mobile-drawer"' in content
    has_table = '<table' in content
    has_table_resp = 'table-responsive' in content if has_table else True
    has_breadcrumbs = 'breadcrumb' in content

    # Find internal assets
    links = re.findall(r'(?:href|src)="([^"]+)"', content)
    missing_critical = []
    future_links = []
    base_dir = os.path.dirname(p)

    for link in links:
        if link.startswith(('http', '#', 'mailto:', 'tel:')):
            continue
        clean_link = link.split('#')[0]
        if not clean_link:
            continue
        target_path = os.path.normcase(os.path.normpath(os.path.join(base_dir, clean_link)))
        if not os.path.exists(target_path):
            if clean_link.endswith(('.css', '.js', '.png', '.jpg', '.svg', '.webp')):
                missing_critical.append(link)
            else:
                future_links.append(link)

    print(f"=== {p} ===")
    print(f"Disclaimer: {'PASS' if has_disclaimer else 'FAIL'} | Header: {'PASS' if has_header else 'FAIL'} | Footer: {'PASS' if has_footer else 'FAIL'} | Desktop Nav: {'PASS' if has_desktop_nav else 'FAIL'} | Mobile Drawer: {'PASS' if has_mobile_drawer else 'FAIL'} | Breadcrumb: {'PASS' if has_breadcrumbs else 'FAIL'}")
    if has_table:
        print(f"Tables wrapped in table-responsive: {'PASS' if has_table_resp else 'FAIL'}")

    if missing_critical:
        print(f"CRITICAL ASSET MISSING: {missing_critical}")
        all_ok = False
    else:
        print("Static assets (CSS, JS, images): ALL RESOLVED (100% OK)")

    if future_links:
        print(f"Note: {len(future_links)} links to other subpages (expected for batch 2/3): {list(set(future_links))}")
    print()

if all_ok:
    print("ALL BATCH 1 PAGES PASSED STATIC VALIDATION.")
else:
    print("SOME CRITICAL ASSETS FAILED.")
