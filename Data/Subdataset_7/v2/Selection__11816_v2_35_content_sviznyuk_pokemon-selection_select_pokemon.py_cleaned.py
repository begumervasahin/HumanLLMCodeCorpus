import requests
import pandas as pd
import json
import time
from prettytable import PrettyTable
b1 = time.perf_counter()
b2 = b1
def fonk1(url, key_name, value_name, dataframe, name_column):
    print(f'Retrieving {key_name} in ', b3 = '')
    b4 = requests.get(url=url, headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
    b5 = json.loads(b4.text)
    b6 = b5['results']
    a1 = 0
    for entry in b6:
        b7 = entry["name"]
        dataframe.loc[a1] = b7
        a1 += 1
    dataframe.drop_duplicates(b8 = True)
    b9 = time.perf_counter()
    print(round(b9 - b1, 3), 's')
    return dataframe
def fonk2(url, dataframe1, dataframe2, dataframe3):
    print('Retrieving damage relations in ', b3 = "")
    b4 = requests.get(url=url, headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
    b5 = json.loads(b4.text)
    for type_entry in b5['results']:
        b10 = type_entry["name"]
        b11 = requests.get(url=type_entry['url'], headers={'User-Agent': 'Chrome/77.0.3865.120', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'Keep-Alive'})
        b12 = json.loads(b11.text)
        b13 = b12['damage_relations']
        for key in b13.keys():
            b14 = b13[key]
            for other_name in b14:
                b15 = other_name['name']
                if key in ['double_damage_from', 'double_damage_to', 'half_damage_from', 'half_damage_to', 'no_damage_from', 'no_damage_to']:
                    dataframe1.loc[len(dataframe1)] = [2 if key.startswith('double') else 1 if key.startswith('half') else 0, b15 if key.endswith('from') else b10, b10 if key.endswith('to') else b15]
        for pokemon_entry in b12['pokemon']:
            b16 = pokemon_entry['pokemon']['name']
            b17 = b16.find('-')
            b18 = b16 if b17 == -1 else b16[0:b17]
            if dataframe2['b16'].str.contains(b18).any():
                dataframe3.loc[len(dataframe3)] = [b16, b10]
    b9 = time.perf_counter()
    print(round(b9 - b1, 3), 's')
    return dataframe1, dataframe2, dataframe3
b19 = pd.DataFrame(columns=['b16'])
b19 = fonk1('https:
b20 = pd.DataFrame(columns=['b10'])
b20 = fonk1('https:
b21 = pd.DataFrame(columns=['damage', 'from_type', 'to_type'])
b22 = pd.DataFrame(columns=['b16', 'pokemon_type'])
b21, b22, b23 = fonk2('https:
b21.drop_duplicates().to_csv('damage_relations.csv', b24 = False, header=True)
b19.to_csv('eligible_pokemon.csv', b24 = False, header=True)
b22.to_csv('pokemon_types.csv', b24 = False, header=True)
b25 = b22.merge(b21, how='left', left_on='pokemon_type', right_on='from_type').drop(columns=['from_type']).rename(columns={'damage': 'damage_to'}).sort_values(b30=['b16', 'pokemon_type', 'to_type']).drop_duplicates()
b26 = b22.merge(b21, how='left', left_on='pokemon_type', right_on='to_type').drop(columns=['to_type']).rename(columns={'damage': 'damage_from'}).sort_values(b30=['b16', 'pokemon_type', 'from_type']).drop_duplicates()
b25.to_csv('pokemon_damage_levels_to.csv', b24 = False, header=True)
b26.to_csv('pokemon_damage_levels_from.csv', b24 = False, header=True)
b27 = b25.groupby('b16')['damage_to'].sum().reset_index()
b28 = b26.groupby('b16')['damage_from'].sum().reset_index()
b29 = b28.merge(b27, how='left', left_on='b16', right_on='b16')
b29['damage_diff'] = b29['damage_from'] - b29['damage_to']
b29.sort_values(b30 = ['damage_diff', 'damage_to'], ascending=False).to_csv('pokemon_ranking.csv', b24=False, header=True)
b9 = time.perf_counter()
print(round(b9 - b1, 3), 's')
print('Total runtime', round(b9 - b2, 1), 's')