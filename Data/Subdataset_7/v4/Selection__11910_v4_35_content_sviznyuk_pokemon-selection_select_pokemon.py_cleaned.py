import requests
import pandas as pd
import json
import time
b1 = time.perf_counter()
b2 = b1
print('Retrieving list of eligible Pokémon in ', b3 = '')
b4 = 'https:
b5 = requests.get(url=b4)
b6 = json.loads(b5.text)
b7 = b6['b7']
b8 = pd.DataFrame(b30=['b25'])
a1 = 0
for pokemon_entry in b7:
    b8.loc[a1] = pokemon_entry['pokemon_species']['name']
    a1 += 1
b8.drop_duplicates(b9 = True)
b10 = time.perf_counter()
print(round(b10 - b1, 3), 's')
b1 = b10
print('Retrieving Pokémon types in ', b3 = '')
b11 = 'https:
b12 = requests.get(url=b11)
b13 = json.loads(b12.text)
b14 = b13['results']
b10 = time.perf_counter()
print(round(b10 - b1, 3), 's')
b15 = pd.DataFrame(b30=['damage', 'from_type', 'to_type'])
b16 = pd.DataFrame(b30=['b25', 'pokemon_type'])
a2 = 0
a3 = 0
for type_entry in b14:
    b17 = type_entry["name"]
    print('Retrieving damage relations for ' + b17 + ' in ', b3 = "")
    b18 = requests.get(url=type_entry['url'])
    b19 = json.loads(b18.text)
    b20 = b19['damage_relations']
    for b23 in b20.keys():
        b21 = b20[b23]
        for other_name in b21:
            b22 = other_name['name']
            if b23 = = 'double_damage_from':
                b15.loc[a2] = [2, b22, b17]
            elif b23 = = 'double_damage_to':
                b15.loc[a2] = [2, b17, b22]
            elif b23 = = 'half_damage_from':
                b15.loc[a2] = [1, b22, b17]
            elif b23 = = 'half_damage_to':
                b15.loc[a2] = [1, b17, b22]
            elif b23 = = 'no_damage_from':
                b15.loc[a2] = [0, b22, b17]
            elif b23 = = 'no_damage_to':
                b15.loc[a2] = [0, b17, b22]
            else:
                print('WARNING: unexpected damage relation: ' + b23)
            a2 += 1
    b24 = b19['pokemon']
    for pokemon_entry in b24:
        b25 = pokemon_entry['pokemon']['name']
        b26 = b25.find('-')
        if b26 = = -1:
            b27 = b25
        else:
            b27 = b25[0:b26]
        if b8['b25'].str.contains(b27).any():
            b16.loc[a3] = [b25, b17]
            a3 += 1
    b10 = time.perf_counter()
    print(round(b10 - b1, 3), 's')
    b1 = b10
print('Reformatting and writing data in ', b3 = '')
b15.drop_duplicates().to_csv('damage_relations.csv', b28 = False, b36=True)
b8.to_csv('eligible_pokemon.csv', b28 = False, b36=True)
b16.to_csv('pokemon_types.csv', b28 = False, b36=True)
b16.drop_duplicates(b9 = True)
b29 = b16.merge(b15, how='left', left_on='pokemon_type', right_on='from_type') \
    .drop(b30 = ['from_type']).rename(b30={'damage': 'damage_to'}).sort_values(b35=['b25',
                                                                                          'pokemon_type',
                                                                                          'to_type']) \
    .drop_duplicates()
b31 = b16.merge(b15, how='left', left_on='pokemon_type', right_on='to_type') \
    .drop(b30 = ['to_type']).rename(b30={'damage': 'damage_from'}).sort_values(b35=['b25',
                                                                                          'pokemon_type',
                                                                                          'from_type']) \
    .drop_duplicates()
b29.to_csv('pokemon_damage_levels_to.csv', b28 = False, b36=True)
b31.to_csv('pokemon_damage_levels_from.csv', b28 = False, b36=True)
b32 = b29.groupby('b25')['damage_to'].sum().reset_index()
b33 = b31.groupby('b25')['damage_from'].sum().reset_index()
b34 = b33.merge(b32, how='left', left_on='b25', right_on='b25')
b34['damage_diff'] = b34['damage_from'] - b34['damage_to']
b34.sort_values(b35 = ['damage_diff', 'damage_to'], ascending=False).to_csv('pokemon_ranking.csv', b28=False,
                                                                         b36 = True)
b10 = time.perf_counter()
print(round(b10 - b1, 3), 's')
print('Total runtime', round(b10 - b2, 1), 's')