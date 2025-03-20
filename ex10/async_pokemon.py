import aiohttp
import asyncio
import os
import aiofiles
from pathlib import Path

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"
NUM_POKEMONS = 5  # Number of Pokemon to fetch

async def fetch_pokemon(session, pokemon_id):
    """Fetch Pokemon data asynchronously from the API."""
    url = f"{POKEMON_API_URL}{pokemon_id}"
    async with session.get(url) as response:
        return await response.json()

async def download_sprite(session, url, save_path):
    """Download sprite image asynchronously and save it."""
    async with session.get(url) as response:
        if response.status == 200:
            async with aiofiles.open(save_path, mode="wb") as f:
                await f.write(await response.read())

async def process_pokemon(pokemon_id):
    """Fetch Pokemon data, create directory, and download sprites."""
    async with aiohttp.ClientSession() as session:
        data = await fetch_pokemon(session, pokemon_id)
        name = data["name"]
        sprites = data["sprites"]
        
        # Create directory for Pokemon
        pokemon_dir = Path(name)
        pokemon_dir.mkdir(exist_ok=True)
        
        # Download all available sprites
        tasks = []
        for key, url in sprites.items():
            if isinstance(url, str):  # Ensure it's a valid URL
                save_path = pokemon_dir / f"{key}.png"
                tasks.append(download_sprite(session, url, save_path))
        
        await asyncio.gather(*tasks)
        print(f"Downloaded sprites for {name}")

async def main():
    """Run async tasks for multiple Pokemons."""
    pokemon_ids = [i for i in range(1, NUM_POKEMONS + 1)]
    await asyncio.gather(*(process_pokemon(p_id) for p_id in pokemon_ids))

if __name__ == "__main__":
    asyncio.run(main())
