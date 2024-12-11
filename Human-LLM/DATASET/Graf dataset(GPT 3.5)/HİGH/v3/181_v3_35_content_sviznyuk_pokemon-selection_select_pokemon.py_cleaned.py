import requests
import pandas as pd
import json
import time
from prettytable import PrettyTable
import sys
sys.setrecursionlimit(9000)
def fonk1(url, key_name, b12, name_column):
    print(f'Retrieving {key_name} in ', b1 = '')
    b2 = requests.get(url=url, headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
    b3 = json.loads(b2.text)
    b4 = b3['results']
    b12[name_column] = [entry["name"] for entry in b4]
    b12.drop_duplicates(b5 = True)
    print(f"{round(time.perf_counter() - b17, 3)} s")
    return b12
def fonk2(url, b12):
    print('Retrieving damage relations in ', b1 = "")
    b2 = requests.get(url=url, headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
    b3 = json.loads(b2.text)
    for type_entry in b3['results']:
        b6 = type_entry["name"]
        b7 = requests.get(url=type_entry['url'], headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
        b8 = json.loads(b7.text)
        b9 = b8['damage_relations']
        for key in b9.keys():
            b10 = b9[key]
            for other_name in b10:
                b11 = other_name['name']
                if key in ['double_damage_from', 'double_damage_to', 'half_damage_from', 'half_damage_to', 'no_damage_from', 'no_damage_to']:
                    b12 = b12.append({'damage': 2 if key.startswith('double') else 1 if key.startswith('half') else 0,
                                                  'from_type': b11 if key.endswith('from') else b6,
                                                  'to_type': b6 if key.endswith('to') else b11}, b13 = True)
        for pokemon_entry in b8['pokemon']:
            b14 = pokemon_entry['pokemon']['name']
            b15 = b14.find('-')
            b16 = b14 if b15 == -1 else b14[0:b15]
            if b16 in b12['b14'].values:
                b12 = b12.append({'b14': b14, 'pokemon_type': b6}, b13=True)
    print(f"{round(time.perf_counter() - b17, 3)} s")
    return b12
b17 = time.perf_counter()
b18 = pd.DataFrame(columns=['b14'])
b18 = fonk1('https:
b19 = pd.DataFrame(columns=['b6'])
b19 = fonk1('https:
b20 = pd.DataFrame(columns=['damage', 'from_type', 'to_type'])
b21 = pd.DataFrame(columns=['b14', 'pokemon_type'])
b20 = fonk2('https:
b21 = fonk2('https:
b20.drop_duplicates().to_csv('damage_relations.csv', b22 = False, header=True)
b18.to_csv('eligible_pokemon.csv', b22 = False, header=True)
b21.to_csv('pokemon_types.csv', b22 = False, header=True)
b23 = b21.merge(b20, how='left', left_on='pokemon_type', right_on='from_type').drop(columns=['from_type']).rename(columns={'damage': 'damage_to'}).sort_values(b28=['b14', 'pokemon_type', 'to_type']).drop_duplicates()
b24 = b21.merge(b20, how='left', left_on='pokemon_type', right_on='to_type').drop(columns=['to_type']).rename(columns={'damage': 'damage_from'}).sort_values(b28=['b14', 'pokemon_type', 'from_type']).drop_duplicates()
b23.to_csv('pokemon_damage_levels_to.csv', b22 = False, header=True)
b24.to_csv('pokemon_damage_levels_from.csv', b22 = False, header=True)
b25 = b23.groupby('b14')['damage_to'].sum().reset_index()
b26 = b24.groupby('b14')['damage_from'].sum().reset_index()
b27 = b26.merge(b25, how='left', left_on='b14', right_on='b14')
b27['damage_diff'] = b27['damage_from'] - b27['damage_to']
b27.sort_values(b28 = ['damage_diff', 'damage_to'], ascending=False).to_csv('pokemon_ranking.csv', b22=False, header=True)
b29 = time.perf_counter()
print(f"{round(b29 - b17, 3)} s")
print('Total runtime', round(b29 - time0, 1), 's')