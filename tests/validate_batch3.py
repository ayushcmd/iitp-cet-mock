import glob
import re
import os
import urllib.request

batch3_pages = [
    'pages/online-classes.html',
    'pages/bonafide-application.html',
    'pages/admission-notice.html',
    'pages/e-gymkhana.html'
]

print(f"Validating {len(batch3_pages)} Batch 3 pages:\n")
all_ok = True

for p in batch3_pages:
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
    is_replica_meta = 'Unofficial educational replica' in content

    # Safety checks
    has_form = '<form' in content.lower()
    has_password_input = 'type="password"' in content.lower()

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
    print(f"Safety (No form/password collection): {'PASS' if (not has_form and not has_password_input) else 'FAIL'}")
    if missing_assets:
        print(f"MISSING STATIC ASSETS: {missing_assets}")
        all_ok = False
    else:
        print("Static Assets: ALL RESOLVED (100% OK)")
    print()

if all_ok:
    print("ALL BATCH 3 PAGES PASSED VALIDATION.")
else:
    print("SOME PAGES FAILED VALIDATION.")
