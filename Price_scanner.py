
import asyncio
from futbin_sdk import FutbinClient

async def main():
    print("FC 27 Console Price Scanner")
    
    async with FutbinClient() as client:
        print("\nChecking popular players...")
        players = await client.get_popular_players()

        for player in players[:10]:
            price = getattr(player, "price_ps", None)
            if price:
                print(f"{player.name}: {price:,} coins")

        print("\nChecking Team of the Week...")
        totw = await client.get_totw()
        print(f"TOTW cards returned: {len(totw)}")

if __name__ == "__main__":
    asyncio.run(main())
