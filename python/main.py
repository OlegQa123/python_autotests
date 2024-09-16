import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c0e3a0fe10caa2c11f26e39b59a586cb'
HEADER =  {'Content-type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "dima1@mail.ru",
    "password": "Iloveqa1234"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "TykTyk",
    "photo_id" : 1
}

body_change = {

    "pokemon_id": "71048",
    "name": "maksii",
}

body_pokeball = {
    
    "pokemon_id": "71048"
}



'''response_registration = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response_registration.text)'''


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.patch(url= f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_cange.text)'''

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
