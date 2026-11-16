import glob
import re

files = sorted(glob.glob('*.html') + glob.glob('pages/**/*.html', recursive=True))
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    p_ids = re.findall(r'id=["\']([^"\']*(?:preloader|backtotop|backToTop)[^"\']*)["\']', c, re.IGNORECASE)
    print(f"{f}: {p_ids}")
