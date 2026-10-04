from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
conn = None
def load_environment_variables():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def connect_to_database():
    global conn
    conn = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password
    )
def fetch_table_data(table_name):
    query = f'SELECT * FROM {table_name}'
    return pd.read_sql(query, con=conn)
def merge_dataframes(df1, df2, key, how='right'):
    return pd.merge(df1, df2, how=how, on=key)
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Time taken: {elapsed_time} seconds")
        return result
    return wrapper
@measure_execution_time
def main():
    load_dotenv()
    load_environment_variables()
    connect_to_database()
    studies_df = fetch_table_data('studies')
    keywords_df = fetch_table_data('keywords')
    merged_result = merge_dataframes(studies_df, keywords_df, 'nct_id')
    print(merged_result)
if __name__ == '__main__':
    main()