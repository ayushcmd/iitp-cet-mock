import glob
import os
import re
import urllib.parse

def audit_all_pages():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    expected_pages = [
        'index.html',
        'pages/about.html',
        'pages/academic-service-charges.html',
        'pages/admission-notice.html',
        'pages/bonafide-application.html',
        'pages/e-gymkhana.html',
        'pages/faculty.html',
        'pages/online-classes.html',
        'pages/academics/academic-calendar.html',
        'pages/academics/evaluation-scheme.html',
        'pages/academics/holiday-list.html',
        'pages/academics/programs.html',
        'pages/academics/re-exam-schedule.html',
        'pages/academics/time-table.html',
        'pages/admissions/eligibility.html',
        'pages/announcements/flyer.html',
        'pages/announcements/news.html',
        'pages/announcements/placement.html'
    ]
    
    print("=================================================================")
    print("     COMPREHENSIVE 18-PAGE CROSS-SITE NAVIGATION & LINK AUDIT    ")
    print("=================================================================\n")
    print(f"Total Expected Pages: {len(expected_pages)}")
    
    missing_pages = []
    for p in expected_pages:
        full_p = os.path.join(project_root, os.path.normpath(p))
        if not os.path.exists(full_p):
            missing_pages.append(p)
            
    if missing_pages:
        print(f"ERROR: Missing expected HTML pages: {missing_pages}")
        return False
    else:
        print("PASS: All 18 expected HTML pages exist on disk.\n")

    broken_links = []
    broken_assets = []
    broken_anchors = []
    
    stats = {
        'total_links_checked': 0,
        'total_assets_checked': 0,
        'external_links_count': 0
    }

    for page_rel in expected_pages:
        page_path = os.path.join(project_root, os.path.normpath(page_rel))
        page_dir = os.path.dirname(page_path)
        
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract all href and src
        hrefs = re.findall(r'href="([^"]+)"', content)
        srcs = re.findall(r'src="([^"]+)"', content)
        
        # Check href links
        for href in hrefs:
            stats['total_links_checked'] += 1
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                stats['external_links_count'] += 1
                continue
            if href == '#' or href.startswith('javascript:'):
                continue
                
            # Internal link
            parts = href.split('#')
            file_part = parts[0]
            anchor_part = parts[1] if len(parts) > 1 else None
            
            if file_part:
                target_file_path = os.path.normpath(os.path.join(page_dir, file_part))
                if not os.path.exists(target_file_path):
                    broken_links.append((page_rel, href, target_file_path))
                    continue
                else:
                    if anchor_part:
                        with open(target_file_path, 'r', encoding='utf-8') as tf:
                            target_content = tf.read()
                        if f'id="{anchor_part}"' not in target_content and f'name="{anchor_part}"' not in target_content:
                            broken_anchors.append((page_rel, href, anchor_part, target_file_path))
            else:
                # Same-page anchor
                if anchor_part:
                    if f'id="{anchor_part}"' not in content and f'name="{anchor_part}"' not in content:
                        broken_anchors.append((page_rel, href, anchor_part, page_rel))

        # Check src assets
        for src in srcs:
            stats['total_assets_checked'] += 1
            if src.startswith(('http://', 'https://', 'data:')):
                continue
            target_asset_path = os.path.normpath(os.path.join(page_dir, src))
            if not os.path.exists(target_asset_path):
                broken_assets.append((page_rel, src, target_asset_path))

    print(f"Total Links Checked: {stats['total_links_checked']}")
    print(f"Total External Links: {stats['external_links_count']}")
    print(f"Total Assets Checked: {stats['total_assets_checked']}\n")

    if broken_links:
        print(f"FAILED: Found {len(broken_links)} broken internal page links:")
        for source, link, target in broken_links:
            print(f"  In {source}: href='{link}' -> unresolved target: {target}")
    else:
        print("PASS: 100% of internal page links resolve correctly!")

    if broken_anchors:
        print(f"\nWARNING: Found {len(broken_anchors)} anchor targets not matching an id:")
        for source, link, anchor, target in broken_anchors:
            print(f"  In {source}: href='{link}' -> id='{anchor}' missing in {target}")
    else:
        print("PASS: All anchor targets resolve properly!")

    if broken_assets:
        print(f"\nFAILED: Found {len(broken_assets)} broken asset references:")
        for source, src, target in broken_assets:
            print(f"  In {source}: src='{src}' -> unresolved target: {target}")
    else:
        print("PASS: 100% of static asset references resolve correctly!")

    print("\n-----------------------------------------------------------------")
    all_clean = len(broken_links) == 0 and len(broken_assets) == 0
    if all_clean:
        print("AUDIT RESULT: ALL 18 PAGES ARE 100% HEALTHY AND CROSS-LINKED!")
    else:
        print("AUDIT RESULT: ISSUES DETECTED. PLEASE REVIEW LOG ABOVE.")
    print("-----------------------------------------------------------------")
    return all_clean

if __name__ == '__main__':
    audit_all_pages()
