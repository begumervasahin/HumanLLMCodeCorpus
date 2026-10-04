import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
conn = None
def load_environment_variables():
    load_dotenv()
    return {
        "hostname": os.getenv('hostname'),
        "port": os.getenv('port'),
        "database": os.getenv('database'),
        "username": os.getenv('username'),
        "password": os.getenv('password')
    }
def connect_to_database(env_vars):
    return psycopg2.connect(
        host=env_vars["hostname"],
        port=env_vars["port"],
        database=env_vars["database"],
        user=env_vars["username"],
        password=env_vars["password"]
    )
def get_data_from_table(table_name):
    return pd.read_sql(f'SELECT * FROM {table_name}', con=conn)
def join_tables(table1, table2):
    query = f
    return pd.read_sql(query, con=conn)
if __name__ == '__main__':
    env_vars = load_environment_variables()
    conn = connect_to_database(env_vars)
    start_time = time.time()
    results = join_tables('ctgov.studies', 'ctgov.keywords')
    end_time = time.time()
    print(f"Join operation time: {end_time - start_time} seconds")
    start_time = time.time()
    pd.read_sql(, con=conn)
    end_time = time.time()
    print(f"Raw SQL join query time: {end_time - start_time} seconds")
    conn.close()