import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
conn = None
def load_env_vars():
    load_dotenv()
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def connect_to_db():
    return psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password
    )
def fetch_table_data(query):
    return pd.read_sql(query, con=conn)
def get_studies_table():
    return fetch_table_data('SELECT * FROM studies')
def get_sponsors_table():
    return fetch_table_data('SELECT * FROM sponsors')
def get_keywords_table():
    return fetch_table_data('SELECT * FROM keywords')
def get_sponsors_studies():
    query =
    return fetch_table_data(query)
def get_keywords_studies():
    query =
    return fetch_table_data(query)
if __name__ == '__main__':
    load_env_vars()
    conn = connect_to_db()
    start_time = time.time()
    studies_df = get_studies_table()
    keywords_df = get_keywords_table()
    merge_result = pd.merge(studies_df, keywords_df, how='right', on='nct_id')
    end_time = time.time()
    print("Time taken:", end_time - start_time)
    print(merge_result)