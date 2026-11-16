import glob
import re
import os
import urllib.request

batch2_pages = [
    'pages/about.html',
    'pages/faculty.html',
    'pages/academic-service-charges.html',
    'pages/announcements/flyer.html',
    'pages/announcements/news.html',
    'pages/announcements/placement.html'
]

print(f"Validating {len(batch2_pages)} Batch 2 pages:\n")
all_ok = True

for p in batch2_pages:
    norm_p = os.path.normpath(p)
    if not os.path.exists(norm_p):
        print(f"FAILED: {p} does not exist!")
        all_ok = False
        continue

    with open(norm_p, 'r', encoding='utf-8') as f:
        content = f.read()

    has_disclaimer = 'replica-disclaimer' in content
    has_header = '<header' in content
    has_footer = '<footer' in content
    has_desktop_nav = 'class="desktop-nav"' in content
    has_mobile_drawer = 'class="mobile-drawer"' in content
    has_breadcrumbs = 'breadcrumb' in content
    has_table = '<table' in content
    has_table_resp = 'table-responsive' in content if has_table else True
    is_replica_meta = 'Unofficial educational replica' in content

    # Check local server HTTP status
    url = f"http://localhost:3000/{p.replace('\\', '/')}"
    http_status = None
    try:
        resp = urllib.request.urlopen(url)
        http_status = resp.status
    except Exception as e:
        http_status = str(e)
        all_ok = False

    # Check internal relative assets
    links = re.findall(r'(?:href|src)="([^"]+)"', content)
    missing_assets = []
    base_dir = os.path.dirname(norm_p)
    for link in links:
        if link.startswith(('http', '#', 'mailto:', 'tel:')):
            continue
        clean_link = link.split('#')[0]
        if not clean_link:
            continue
        target_path = os.path.normcase(os.path.normpath(os.path.join(base_dir, clean_link)))
        if clean_link.endswith(('.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.webp')):
            if not os.path.exists(target_path):
                missing_assets.append((link, target_path))

    print(f"=== {p} ===")
    print(f"HTTP Status: {http_status} | Disclaimer: {'PASS' if has_disclaimer else 'FAIL'} | Meta replica: {'PASS' if is_replica_meta else 'FAIL'}")
    print(f"Header: {'PASS' if has_header else 'FAIL'} | Footer: {'PASS' if has_footer else 'FAIL'} | Desktop Nav: {'PASS' if has_desktop_nav else 'FAIL'} | Mobile Drawer: {'PASS' if has_mobile_drawer else 'FAIL'} | Breadcrumb: {'PASS' if has_breadcrumbs else 'FAIL'}")
    if has_table:
        print(f"Table Responsive Wrapper: {'PASS' if has_table_resp else 'FAIL'}")
    if missing_assets:
        print(f"MISSING STATIC ASSETS: {missing_assets}")
        all_ok = False
    else:
        print("Static Assets: ALL RESOLVED (100% OK)")
    print()

if all_ok:
    print("ALL BATCH 2 PAGES PASSED VALIDATION.")
else:
    print("SOME PAGES FAILED VALIDATION.")
