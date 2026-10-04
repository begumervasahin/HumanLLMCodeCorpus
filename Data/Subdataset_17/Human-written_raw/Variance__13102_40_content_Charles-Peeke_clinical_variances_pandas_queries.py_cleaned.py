from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import time
import numpy as np
conn = None
df = None
df_keywords = None
df_kw_studies = None
df_sp_studies = None
def create_env_vars():
    global hostname, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def get_studies_table():
    df = pd.read_sql('SELECT * FROM studies', con=conn)
    return df
def get_sponsors_table():
    df = pd.read_sql('SELECT * FROM sponsors', con=conn)
    return df
def get_keywords_table():
    df_keywords = pd.read_sql('SELECT * FROM keywords', con=conn)
    return df_keywords
def get_sponsors_studies():
    df_sp_studies = pd.read_sql('SELECT * FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=conn)
    return df_sp_studies
def get_keywords_studies():
    df_kw_studies = pd.read_sql('SELECT * FROM studies RIGHT JOIN keywords ON studies.nct_id = keywords.nct_id', con=conn)
    return df_kw_studies
if __name__ == '__main__':
    sponsor_diffs = []
    keywords_diffs = []
    sponsor_join_diffs = []
    keywords_join_diffs = []
    load_dotenv()
    create_env_vars()
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
    start_time = time.time()
    studies_results = get_studies_table()
    sponsor_results = get_keywords_table()
    merge_result = pd.merge(studies_results, sponsor_results, how='right', on='nct_id')
    select_time = time.time()
    print(select_time - start_time)
    print(merge_result)