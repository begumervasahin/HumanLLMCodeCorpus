import os
import time
import psycopg2
import pandas as pd
from dotenv import load_dotenv
conn = None
def load_environment_variables():
    load_dotenv()
    env_vars = {
        "hostname": os.getenv('hostname'),
        "port": os.getenv('port'),
        "database": os.getenv('database'),
        "username": os.getenv('username'),
        "password": os.getenv('password')
    }
    return env_vars
def connect_to_database(env_vars):
    connection = psycopg2.connect(
        host=env_vars["hostname"],
        port=env_vars["port"],
        database=env_vars["database"],
        user=env_vars["username"],
        password=env_vars["password"]
    )
    return connection
def get_data_from_table(table_name):
    query = f'SELECT * FROM {table_name}'
    data = pd.read_sql(query, con=conn)
    return data
def join_tables(table1, table2):
    query = f
    joined_data = pd.read_sql(query, con=conn)
    return joined_data
def measure_query_time(query_function, *args):
    start_time = time.time()
    query_function(*args)
    end_time = time.time()
    return end_time - start_time
def main():
    env_vars = load_environment_variables()
    global conn
    conn = connect_to_database(env_vars)
    join_time = measure_query_time(join_tables, 'ctgov.studies', 'ctgov.keywords')
    print(f"Join operation time: {join_time:.4f} seconds")
    raw_sql_time = measure_query_time(pd.read_sql, , con=conn)
    print(f"Raw SQL join query time: {raw_sql_time:.4f} seconds")
    conn.close()
if __name__ == '__main__':
    main()