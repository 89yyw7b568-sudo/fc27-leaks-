import requests
from bs4 import BeautifulSoup
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

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(" ", strip=True)

print("Successfully downloaded FUTWIZ page")
print("Page length:", len(response.text))

# Look for the console price
patterns = [
    r"price on the Xbox and PlayStation console market is ([0-9,.]+)",
    r"Console.*?([0-9,.]+)\s*coins",
    r"PlayStation.*?([0-9,.]+)\s*coins",
]

price = None

for pattern in patterns:
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        price = match.group(1)
        break

if price:
    print("Mbappé PlayStation/Console price:", price, "coins")
else:
    print("Could not extract the price.")
    print("Searching page text for 'coins':")
    
    matches = re.findall(r".{0,100}coins.{0,100}", text, re.IGNORECASE)
    for match in matches[:10]:
        print(match)

print("FUTWIZ price extraction test complete.")
