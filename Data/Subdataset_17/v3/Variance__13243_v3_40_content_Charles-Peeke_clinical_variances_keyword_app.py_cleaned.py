import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import psycopg2
def load_environment_variables():
    load_dotenv()
    return {
        'hostname': os.getenv('hostname'),
        'port': os.getenv('port'),
        'database': os.getenv('database'),
        'username': os.getenv('username'),
        'password': os.getenv('password')
    }
def connect_to_database(env_vars):
    return psycopg2.connect(
        host=env_vars['hostname'],
        port=env_vars['port'],
        database=env_vars['database'],
        user=env_vars['username'],
        password=env_vars['password']
    )
def fetch_keywords(conn):
    print('Fetching keywords...')
    start_time = time.time()
    query = '''
        SELECT studies.nct_id, downcase_name
        FROM studies
        RIGHT JOIN keywords ON studies.nct_id = keywords.nct_id
    '''
    df_keywords = pd.read_sql(query, con=conn)
    elapsed_time = time.time() - start_time
    print(f'Keywords fetched in {elapsed_time:.2f} seconds')
    return df_keywords
def calculate_keyword_variances(df_keywords):
    print('Calculating keyword variances...')
    start_time = time.time()
    key_dict = {}
    for nct_id in df_keywords['nct_id']:
        key_dict[nct_id] = key_dict.get(nct_id, 0) + 1
    elapsed_time = time.time() - start_time
    print(f'Keyword variances calculated in {elapsed_time:.2f} seconds')
    return key_dict
def plot_keyword_variances(key_dict):
    ids, counts = zip(*key_dict.items())
    plt.figure(figsize=(10, 6))
    plt.bar(ids, counts)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances by NCT ID')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
def main():
    env_vars = load_environment_variables()
    with connect_to_database(env_vars) as conn:
        df_keywords = fetch_keywords(conn)
        key_dict = calculate_keyword_variances(df_keywords)
        plot_keyword_variances(key_dict)
if __name__ == '__main__':
    main()