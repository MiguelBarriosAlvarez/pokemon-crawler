import asyncio
import requests
from django.utils import timezone
from aiohttp import ClientSession
from pokemon.models import Name


def save_ddbb(character):
    data = {
        'id': character['id'],
        'name': character['name'],
        'characteristics': {
            'abilities': character['abilities'],
            'height': character['height'],
            'weight': character['weight']
        }
    }
    N = Name(
        id=data['id'],
        name=data['name'],
        height=data['characteristics']['height'],
        weight=data['characteristics']['weight'],
        date=timezone.now()
    )
    N.save()


async def get_character(session, url: str) -> object:
    response = await session.get(url)
    character = await response.json()
    save_ddbb(character)
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
    ids_count = total_data['count']
    async with ClientSession() as session:
        #character = asyncio.gather(*[get_character(session, id_count) for id_count in range(ids_count)])
        for id_count in range(ids_count):
            id_count = id_count + 1
            url = f'https://pokeapi.co/api/v2/pokemon/{id_count}'
            character = await get_character(session, url=url)
            return character


def crawler():
    return asyncio.run(request_poke())

