import asyncio
from aiohttp import ClientSession


async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json()
    return character


async def request_poke() -> object:
    """
    :return: Pokeapi pokemon information in JSON
    """
    async with ClientSession() as session:
        url = 'https://pokeapi.co/api/v2/pokemon/3'
        character = await get_character(session, url=url)
        return character


def get_poke():
    return asyncio.run(request_poke())

