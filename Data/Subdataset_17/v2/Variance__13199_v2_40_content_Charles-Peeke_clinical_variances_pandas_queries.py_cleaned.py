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
def fetch_table_data(query):
    return pd.read_sql(query, con=conn)
def main():
    load_dotenv()
    load_environment_variables()
    connect_to_database()
    start_time = time.time()
    studies_df = fetch_table_data('SELECT * FROM studies')
    keywords_df = fetch_table_data('SELECT * FROM keywords')
    merged_result = pd.merge(studies_df, keywords_df, how='right', on='nct_id')
    select_time = time.time()
    elapsed_time = select_time - start_time
    print(f"Time taken: {elapsed_time} seconds")
    print(merged_result)
if __name__ == '__main__':
    main()