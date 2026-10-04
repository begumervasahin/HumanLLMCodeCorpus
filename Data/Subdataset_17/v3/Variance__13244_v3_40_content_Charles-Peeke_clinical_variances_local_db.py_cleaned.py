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
    return psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password
    )
def fetch_data(conn, table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, con=conn)
def join_tables(conn, first_table_name, second_table_name):
    query = f
    return pd.read_sql(query, con=conn)
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time
if __name__ == '__main__':
    load_env_vars()
    conn = create_connection()
    joined_results, join_time_function = measure_time(join_tables, conn, 'ctgov.studies', 'ctgov.keywords')
    print("Join operation time using function:", join_time_function)
    query = 'SELECT * FROM ctgov.studies RIGHT JOIN ctgov.keywords ON ctgov.studies.nct_id = ctgov.keywords.nct_id'
    _, join_time_raw_sql = measure_time(pd.read_sql, query, conn)
    print("Join operation time using raw SQL:", join_time_raw_sql)
    conn.close()