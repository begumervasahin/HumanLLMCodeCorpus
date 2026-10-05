import os
import time
import pandas as pd
import psycopg2
from dotenv import load_dotenv
conn = None
df = None
df_keywords = None
df_nct = None
def load_env_variables():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def connect_to_database():
    global conn
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
def execute_query(query):
    return pd.read_sql(query, con=conn)
def get_studies():
    query = 'SELECT * FROM ctgov.studies'
    return execute_query(query)
def get_keywords():
    query = 'SELECT * FROM ctgov.keywords'
    return execute_query(query)
def get_sponsors():
    query = 'SELECT * FROM ctgov.sponsors'
    return execute_query(query)
def join_tables(first_table_name, second_table_name):
    query = f
    return execute_query(query)
if __name__ == '__main__':
    load_dotenv()
    load_env_variables()
    connect_to_database()
    start_time = time.time()
    results = join_tables('ctgov.studies', 'ctgov.keywords')
    end_time = time.time()
    print("Time taken for joining tables:", end_time - start_time)
    start_time = time.time()
    query =
    execute_query(query)
    end_time = time.time()
    print("Time taken for another query:", end_time - start_time)