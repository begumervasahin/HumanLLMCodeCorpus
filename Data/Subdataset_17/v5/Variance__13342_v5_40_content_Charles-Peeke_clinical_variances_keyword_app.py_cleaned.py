import os
import time
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
conn = None
df_keywords = None
def load_environment_variables():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def fetch_keywords():
    print('Fetching keywords...')
    start_time = time.time()
    global df_keywords
    query = '''
    SELECT studies.nct_id, downcase_name
    FROM studies
    RIGHT JOIN keywords
    ON studies.nct_id = keywords.nct_id
    '''
    df_keywords = pd.read_sql(query, con=conn)
    elapsed_time = time.time() - start_time
    print(f'Keywords fetched in {elapsed_time:.2f} seconds')
def calculate_keyword_variances():
    print('Calculating keyword variances...')
    start_time = time.time()
    keyword_counts = df_keywords['nct_id'].value_counts()
    elapsed_time = time.time() - start_time
    print(f'Keyword variances calculated in {elapsed_time:.2f} seconds')
    plt.bar(keyword_counts.index, keyword_counts.values)
    plt.xlabel('NCT ID')
    plt.ylabel('Keyword Count')
    plt.title('Keyword Variances')
    plt.show()
def main():
    load_dotenv()
    load_environment_variables()
    global conn
    conn = psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password
    )
    fetch_keywords()
    calculate_keyword_variances()
if __name__ == '__main__':
    main()