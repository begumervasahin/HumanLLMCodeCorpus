import requests
import pandas as pd
import json
import time
def retrieve_pokemon_data():
    print('Retrieving list of eligible Pokémon...', end='')
    pokemon_url = 'https:
    pokemon_resp = requests.get(url=pokemon_url)
    pokemon_entries_dict = json.loads(pokemon_resp.text)
    pokemon_entries = pokemon_entries_dict['pokemon_entries']
    pokemon_df = pd.DataFrame(columns=['pokemon_name'])
    for i, pokemon_entry in enumerate(pokemon_entries):
        pokemon_df.loc[i] = pokemon_entry['pokemon_species']['name']
    pokemon_df.drop_duplicates(inplace=True)
    print(f'Done. ({len(pokemon_df)} Pokémon)')
    return pokemon_df
def retrieve_pokemon_types():
    print('Retrieving Pokémon types...', end='')
    types_url = 'https:
    types_resp = requests.get(url=types_url)
    types_dict = json.loads(types_resp.text)
    type_entries_list = types_dict['results']
    print(f'Done. ({len(type_entries_list)} types)')
    return type_entries_list
def fetch_damage_relations_and_pokemon_types(type_entries_list):
    damage_relations_df = pd.DataFrame(columns=['damage', 'from_type', 'to_type'])
    pokemon_type_df = pd.DataFrame(columns=['pokemon_name', 'pokemon_type'])
    for type_entry in type_entries_list:
        type_name = type_entry["name"]
        print(f'Retrieving damage relations for {type_name}...', end="")
        damage_relation_resp = requests.get(url=type_entry['url'])
        damage_relation_dict = json.loads(damage_relation_resp.text)
        damage_relation = damage_relation_dict['damage_relations']
        for key in damage_relation:
            damage_relation_names = damage_relation[key]
            for other_name in damage_relation_names:
                other_name_name = other_name['name']
                damage_relations_df = append_damage_relation(damage_relations_df, key, other_name_name, type_name)
        pokemon_list = damage_relation_dict['pokemon']
        for pokemon_entry in pokemon_list:
            pokemon_name = pokemon_entry['pokemon']['name']
            pokemon_short = pokemon_name.split('-')[0]
            if pokemon_short in pokemon_df['pokemon_name'].values:
                pokemon_type_df = append_pokemon_type(pokemon_type_df, pokemon_name, type_name)
        print(f'Done.')
    return damage_relations_df, pokemon_type_df
def append_damage_relation(damage_relations_df, relation_type, from_type, to_type):
    if relation_type in ['double_damage_from', 'double_damage_to']:
        damage = 2
    elif relation_type in ['half_damage_from', 'half_damage_to']:
        damage = 1
    elif relation_type in ['no_damage_from', 'no_damage_to']:
        damage = 0
    else:
        print('WARNING: unexpected damage relation:', relation_type)
        return damage_relations_df
    damage_relations_df = damage_relations_df.append({'damage': damage, 'from_type': from_type, 'to_type': to_type}, ignore_index=True)
    return damage_relations_df
def append_pokemon_type(pokemon_type_df, pokemon_name, pokemon_type):
    pokemon_type_df = pokemon_type_df.append({'pokemon_name': pokemon_name, 'pokemon_type': pokemon_type}, ignore_index=True)
    return pokemon_type_df
def write_to_csv(damage_relations_df, pokemon_df, pokemon_type_df):
    print('Writing data to CSV files...', end='')
    damage_relations_df.drop_duplicates().to_csv('damage_relations.csv', index=False, header=True)
    pokemon_df.to_csv('eligible_pokemon.csv', index=False, header=True)
    pokemon_type_df.to_csv('pokemon_types.csv', index=False, header=True)
    pokemon_type_df.drop_duplicates(inplace=True)
    print('Done.')
def calculate_additional_statistics(pokemon_type_df, damage_relations_df):
    df1 = merge_and_sort(pokemon_type_df, damage_relations_df, from_to='from_type', new_column_name='damage_to')
    df2 = merge_and_sort(pokemon_type_df, damage_relations_df, from_to='to_type', new_column_name='damage_from')
    df3 = df1.groupby('pokemon_name')['damage_to'].sum().reset_index()
    df4 = df2.groupby('pokemon_name')['damage_from'].sum().reset_index()
    df5 = df4.merge(df3, how='left', left_on='pokemon_name', right_on='pokemon_name')
    df5['damage_diff'] = df5['damage_from'] - df5['damage_to']
    df5.sort_values(by=['damage_diff', 'damage_to'], ascending=False).to_csv('pokemon_ranking.csv', index=False, header=True)
def merge_and_sort(pokemon_type_df, damage_relations_df, from_to, new_column_name):
    df = pokemon_type_df.merge(damage_relations_df, how='left', left_on='pokemon_type', right_on=from_to) \
        .drop(columns=[from_to]).rename(columns={'damage': new_column_name}).sort_values(by=['pokemon_name', 'pokemon_type', from_to]) \
        .drop_duplicates()
    df.to_csv(f'pokemon_damage_levels_{from_to}.csv', index=False, header=True)
    return df
if __name__ == "__main__":
    pokemon_df = retrieve_pokemon_data()
    type_entries_list = retrieve_pokemon_types()
    damage_relations_df, pokemon_type_df = fetch_damage_relations_and_pokemon_types(type_entries_list)
    write_to_csv(damage_relations_df, pokemon_df, pokemon_type_df)
    calculate_additional_statistics(pokemon_type_df, damage_relations_df)
    print('Data processing completed.')