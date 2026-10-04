import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
def load_env_vars():
    load_dotenv()
    env_vars = {
        'hostname': os.getenv('hostname'),
        'port': os.getenv('port'),
        'database': os.getenv('database'),
        'username': os.getenv('username'),
        'password': os.getenv('password')
    }
    return env_vars
def connect_to_db(env_vars):
    return psycopg2.connect(
        host=env_vars['hostname'],
        port=env_vars['port'],
        database=env_vars['database'],
        user=env_vars['username'],
        password=env_vars['password']
    )
def fetch_table_data(query, connection):
    return pd.read_sql(query, con=connection)
def get_studies_table(connection):
    return fetch_table_data('SELECT * FROM studies', connection)
def get_sponsors_table(connection):
    return fetch_table_data('SELECT * FROM sponsors', connection)
def get_keywords_table(connection):
    return fetch_table_data('SELECT * FROM keywords', connection)
def get_sponsors_studies(connection):
    query =
    return fetch_table_data(query, connection)
def get_keywords_studies(connection):
    query =
    return fetch_table_data(query, connection)
def main():
    env_vars = load_env_vars()
    connection = connect_to_db(env_vars)
    start_time = time.time()
    studies_df = get_studies_table(connection)
    keywords_df = get_keywords_table(connection)
    merge_result = pd.merge(studies_df, keywords_df, how='right', on='nct_id')
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(merge_result)
if __name__ == '__main__':
    main()