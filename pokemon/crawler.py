import asyncio
import requests
from aiohttp import ClientSession


async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json()
    return character


async def request_poke() -> object:
    """
    :return: Pokeapi pokemon information in JSON
    """
    BASE = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(BASE)
    if response.status_code != 200:
        return None
    total_data = response.json()
    total_count = total_data['count']
    async for id_count in total_count:
        async with ClientSession() as session:
            id_count = id_count + 1
            url = f'https://pokeapi.co/api/v2/pokemon/{id_count}'
            print(id_count)
            character = await get_character(session, url=url)
            return character


def get_poke():
    return asyncio.run(request_poke())
