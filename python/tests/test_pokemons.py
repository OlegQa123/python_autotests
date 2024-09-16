import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c0e3a0fe10caa2c11f26e39b59a586cb'
HEADER =  {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '10210'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
         response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
         assert response_get.json()["data"][0]['trainer_name'] == 'Ara'
