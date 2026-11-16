import glob
import re

files = sorted(glob.glob('*.html') + glob.glob('pages/**/*.html', recursive=True))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    metas = re.findall(r'<meta name="description" content="([^"]+)"', c)
    titles = re.findall(r'<title>([^<]+)</title>', c)
    print(f"File: {f}")
    print(f"  Title: {titles[0] if titles else 'NONE'}")
    print(f"  Meta Description: {metas[0] if metas else 'NONE'}")
