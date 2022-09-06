with open('Pokemon_file', 'w') as Pokemon_file:
from shutil import move
from typing import List

import requests

List['bulbasaur', 'ivysaur', 'charmander', 'squirtle', 'wartortle','butterfree']

list ['bulbasaur']


for Name in list:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(List)
    response = requests.get(url)
    Pokemon_names = response.json()
    list_name = []
    list_name.apend(Pokemon_names['name'])



    for Move in Pokemon_names:
        list_name.apend(move['move']['name'])

       pokemon_file.write(list_name,list)


