import os
import requests

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def main():
    if not WEBHOOK:
        print("Discord webhook secret is missing.")
        return

    message = (
        "⚽ FC 27 Icon Price Alert Bot is connected!\n"
        "Discord notifications are working."
    )

    response = requests.post(
        WEBHOOK,
        json={"content": message},
        timeout=15
    )
    response.raise_for_status()
    print("Discord test notification sent.")

if __name__ == "__main__":
    main()
