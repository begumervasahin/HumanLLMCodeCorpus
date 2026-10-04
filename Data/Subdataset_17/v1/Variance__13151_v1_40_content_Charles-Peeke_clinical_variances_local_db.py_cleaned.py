from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
def load_env_vars():
    load_dotenv()
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def create_connection():
    return psycopg2.connect(host=hostname, port=port, database=database, user=username, password=password)
def fetch_studies(conn):
    return pd.read_sql('SELECT * FROM ctgov.studies', con=conn)
def fetch_keywords(conn):
    return pd.read_sql('SELECT * FROM ctgov.keywords', con=conn)
def fetch_sponsors(conn):
    return pd.read_sql('SELECT * FROM ctgov.sponsors', con=conn)
def join_tables(conn, first_table_name, second_table_name):
    query = f
    return pd.read_sql(query, con=conn)
if __name__ == '__main__':
    load_env_vars()
    conn = create_connection()
    start_time = time.time()
    joined_results = join_tables(conn, 'ctgov.studies', 'ctgov.keywords')
    end_time = time.time()
    print("Join operation time:", end_time - start_time)
    start_time = time.time()
    pd.read_sql('SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.nct_id = ctgov.keywords.nct_id', con=conn)
    end_time = time.time()
    print("Raw SQL query time:", end_time - start_time)
    conn.close()