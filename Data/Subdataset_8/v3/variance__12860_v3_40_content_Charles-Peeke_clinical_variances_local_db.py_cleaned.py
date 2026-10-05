from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
conn = None
def load_environment_variables():
    load_dotenv()
    global hostname, database, username, password
    hostname = os.getenv('hostname')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def connect_to_database():
    global conn
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
def retrieve_studies_data():
    return pd.read_sql('SELECT * FROM ctgov.studies', con=conn)
def retrieve_keywords_data():
    return pd.read_sql('SELECT * FROM ctgov.keywords', con=conn)
def join_tables(first_table_name, second_table_name):
    return pd.read_sql(f'''
        SELECT *
        FROM {first_table_name}
        RIGHT JOIN {second_table_name}
        ON {first_table_name}.nct_id = {second_table_name}.nct_id
    ''', con=conn)
def main():
    load_environment_variables()
    connect_to_database()
    start_time = time.time()
    results = join_tables('ctgov.studies', 'ctgov.keywords')
    end_time = time.time()
    print("Time taken for joining tables:", end_time - start_time)
    start_time = time.time()
    pd.read_sql('SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.nct_id = ctgov.keywords.nct_id', con=conn)
    end_time = time.time()
    print("Time taken for joining tables (direct query):", end_time - start_time)
if __name__ == '__main__':
    main()