from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
conn = None
def create_env_vars():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def get_studies_table():
    return pd.read_sql('SELECT * FROM studies', con=conn)
def get_sponsors_table():
    return pd.read_sql('SELECT * FROM sponsors', con=conn)
def get_keywords_table():
    return pd.read_sql('SELECT * FROM keywords', con=conn)
def get_sponsors_studies():
    return pd.read_sql('SELECT * FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=conn)
def get_keywords_studies():
    return pd.read_sql('SELECT * FROM studies RIGHT JOIN keywords ON studies.nct_id = keywords.nct_id', con=conn)
def main():
    load_dotenv()
    create_env_vars()
    global conn
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
    start_time = time.time()
    studies_df = get_studies_table()
    keywords_df = get_keywords_table()
    merged_result = pd.merge(studies_df, keywords_df, how='right', on='nct_id')
    select_time = time.time()
    print(f"Time taken: {select_time - start_time} seconds")
    print(merged_result)
if __name__ == '__main__':
    main()