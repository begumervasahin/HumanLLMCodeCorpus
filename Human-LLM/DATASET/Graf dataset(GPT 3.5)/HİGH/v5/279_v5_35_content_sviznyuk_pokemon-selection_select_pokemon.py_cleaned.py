import requests
import pandas as pd
import json
import time
def fonk1():
    print('Retrieving list of eligible Pokémon...', b1 = '')
    b2 = 'https:
    b3 = requests.get(url=b2)
    b4 = json.loads(b3.text)
    b5 = b4['b5']
    b6 = pd.DataFrame(b31=['b21'])
    for i, pokemon_entry in enumerate(b5):
        b6.loc[i] = pokemon_entry['pokemon_species']['name']
    b6.drop_duplicates(b7 = True)
    print(f'Done. ({len(b6)} Pokémon)')
    return b6
def fonk2():
    print('Retrieving Pokémon types...', b1 = '')
    b8 = 'https:
    b9 = requests.get(url=b8)
    b10 = json.loads(b9.text)
    b11 = b10['results']
    print(f'Done. ({len(b11)} types)')
    return b11
def fonk3(b11):
    b12 = pd.DataFrame(b31=['a1', 'from_type', 'to_type'])
    b13 = pd.DataFrame(b31=['b21', 'pokemon_type'])
    for type_entry in b11:
        b14 = type_entry["name"]
        print(f'Retrieving a1 relations for {b14}...', b1 = "")
        b15 = requests.get(url=type_entry['url'])
        b16 = json.loads(b15.text)
        b17 = b16['damage_relations']
        for key in b17:
            b18 = b17[key]
            for other_name in b18:
                b19 = other_name['name']
                b12 = fonk4(b12, key, b19, b14)
        b20 = b16['pokemon']
        for pokemon_entry in b20:
            b21 = pokemon_entry['pokemon']['name']
            b22 = b21.split('-')[0]
            if b22 in b6['b21'].values:
                b13 = fonk5(b13, b21, b14)
        print(f'Done.')
    return b12, b13
def fonk4(b12, relation_type, from_type, to_type):
    if relation_type in ['double_damage_from', 'double_damage_to']:
        a1 = 2
    elif relation_type in ['half_damage_from', 'half_damage_to']:
        a1 = 1
    elif relation_type in ['no_damage_from', 'no_damage_to']:
        a1 = 0
    else:
        print('WARNING: unexpected a1 relation:', relation_type)
        return b12
    b12 = b12.append({'a1': a1, 'from_type': from_type, 'to_type': to_type}, ignore_index=True)
    return b12
def fonk5(b13, b21, pokemon_type):
    b13 = b13.append({'b21': b21, 'pokemon_type': pokemon_type}, ignore_index=True)
    return b13
def fonk6(b12, b6, b13):
    print('Writing data to CSV files...', b1 = '')
    b12.drop_duplicates().to_csv('damage_relations.csv', b23 = False, header=True)
    b6.to_csv('eligible_pokemon.csv', b23 = False, header=True)
    b13.to_csv('pokemon_types.csv', b23 = False, header=True)
    b13.drop_duplicates(b7 = True)
    print('Done.')
def fonk7(b13, b12):
    b24 = fonk8(b13, b12, from_to='from_type', new_column_name='damage_to')
    b25 = fonk8(b13, b12, from_to='to_type', new_column_name='damage_from')
    b26 = b24.groupby('b21')['damage_to'].sum().reset_index()
    b27 = b25.groupby('b21')['damage_from'].sum().reset_index()
    b28 = b27.merge(b26, how='left', left_on='b21', right_on='b21')
    b28['damage_diff'] = b28['damage_from'] - b28['damage_to']
    b28.sort_values(b29 = ['damage_diff', 'damage_to'], ascending=False).to_csv('pokemon_ranking.csv', b23=False, header=True)
def fonk8(b13, b12, from_to, new_column_name):
    b30 = b13.merge(b12, how='left', left_on='pokemon_type', right_on=from_to) \
        .drop(b31 = [from_to]).rename(b31={'a1': new_column_name}).sort_values(b29=['b21', 'pokemon_type', from_to]) \
        .drop_duplicates()
    b30.to_csv(f'pokemon_damage_levels_{from_to}.csv', b23 = False, header=True)
    return b30
if b32 = = "__main__":
    b6 = fonk1()
    b11 = fonk2()
    b12, b13 = fonk3(b11)
    fonk6(b12, b6, b13)
    fonk7(b13, b12)
    print('Data processing completed.')