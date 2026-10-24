import requests
import re

URL = "https://www.futwiz.com/fc27/player/kylian-mbappe/27"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9",
}

print("FC 27 FUTWIZ Price Diagnostic")
print("Checking Mbappé...")

response = requests.get(URL, headers=headers, timeout=30)

print("HTTP status:", response.status_code)
print("Page length:", len(response.text))

if response.status_code != 200:
    raise Exception(f"FUTWIZ returned HTTP {response.status_code}")

html = response.text

# Search the raw response for common price/data structures.
patterns = [
    r'"price"\s*:\s*([0-9]+)',
    r'"consolePrice"\s*:\s*([0-9]+)',
    r'"priceConsole"\s*:\s*([0-9]+)',
    r'"xboxPrice"\s*:\s*([0-9]+)',
    r'"psPrice"\s*:\s*([0-9]+)',
    r'"playstationPrice"\s*:\s*([0-9]+)',
    r'"currentPrice"\s*:\s*([0-9]+)',
]

found = []

for pattern in patterns:
    matches = re.findall(pattern, html, re.IGNORECASE)
    if matches:
        print("MATCH:", pattern)
        print("VALUES:", matches[:20])
        found.extend(matches[:20])

if not found:
    print("No obvious price JSON field found.")

    # Look for API-looking URLs inside the page.
    urls = re.findall(
        r'https?://[^"\']+',
        html,
        re.IGNORECASE
    )

    print("\nPossible API/data URLs:")

    count = 0
    for url in urls:
        if any(word in url.lower() for word in [
            "api", "price", "player", "market"
        ]):
            print(url[:500])
            count += 1

        if count >= 20:
            break

print("\nDiagnostic complete.")
