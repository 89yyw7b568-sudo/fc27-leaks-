import requests
from bs4 import BeautifulSoup

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

print("Successfully connected to FUTWIZ")

soup = BeautifulSoup(response.text, "html.parser")

print("Page downloaded:", len(response.text), "characters")

# Show text containing possible price information
text = soup.get_text(" ", strip=True)

for keyword in ["Price", "Console", "PlayStation", "PS"]:
    if keyword.lower() in text.lower():
        print(f"Found '{keyword}' on page")

print("FUTWIZ connection test complete.")
