import urllib.request
import re
import glob
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

external_urls = set()
for f in sorted(glob.glob('*.html') + glob.glob('pages/**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    links = re.findall(r'href=["\'](https?://[^"\']+)["\']', c)
    external_urls.update(links)

print(f"Auditing {len(external_urls)} unique external URLs:\n")
results = {}
for u in sorted(external_urls):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            results[u] = (resp.status, "Reachable")
    except Exception as e:
        results[u] = (str(e), "Unreachable/Blocked/Protected")

for u, (status, category) in results.items():
    print(f"[{category}] {u} -> Status: {status}")
