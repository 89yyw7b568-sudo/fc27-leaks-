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

# FUTWIZ format:
# "Player's price on the Xbox and PlayStation console market is 200 coins"

pattern = r"price on the Xbox and PlayStation console market is\s+([\d,.]+)\s+coins"

match = re.search(pattern, text, re.IGNORECASE)

if match:
    price = match.group(1)
    print("Mbappé PlayStation/Console price:", price, "coins")
else:
    print("Could not extract the price.")

    # Find the relevant section so we can diagnose it
    index = text.lower().find("playstation")

    if index != -1:
        print("FUTWIZ text around PlayStation:")
        print(text[max(0, index - 300):index + 500])
    else:
        print("No PlayStation text found.")

print("FUTWIZ price extraction test complete.")
