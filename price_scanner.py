import requests
import re

URL = "https://www.futwiz.com/fc27/player/kylian-mbappe/27"

print("FC 27 FUTWIZ Price Test")
print("Checking Mbappé...")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
}

response = requests.get(URL, headers=headers, timeout=30)

print("HTTP status:", response.status_code)

if response.status_code != 200:
    raise Exception(f"FUTWIZ returned HTTP {response.status_code}")

html = response.text

print("Successfully downloaded FUTWIZ page")
print("Page length:", len(html))

# Look for the exact wording FUTWIZ uses for console prices.
patterns = [
    r"price on the (?:Xbox and )?PlayStation console market is\s*([0-9,.]+)",
    r"playstation[^<]{0,300}?([0-9,.]+)\s*coins",
    r"console[^<]{0,300}?([0-9,.]+)\s*coins",
]

price = None

for pattern in patterns:
    match = re.search(pattern, html, re.IGNORECASE)
    if match:
        price = match.group(1)
        print("Matched pattern:", pattern)
        break

if price:
    print("Mbappé PlayStation/Console price:", price, "coins")
else:
    print("PRICE NOT FOUND IN RAW HTML")

    # Show snippets containing likely price-related data
    for word in ["playstation", "console", "price"]:
        position = html.lower().find(word)

        if position != -1:
            print(f"\nRAW HTML around '{word}':")
            print(html[max(0, position - 300):position + 1000])
            break

print("\nFUTWIZ price extraction test complete.")
