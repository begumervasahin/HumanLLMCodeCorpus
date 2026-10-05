import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
conn = None
df = None
load_dotenv()
def create_variables():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def compute_results():
    print('Computing results...')
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
    df = pd.read_sql('SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=conn)
    print('Done.')
    return df
def get_unique_sponsor_names(df):
    unique_names = set(df['name'].tolist())
    return list(unique_names)
def write_list_to_file(names_list):
    with open('unique_sponsor_names.txt', 'w') as f:
        for name in names_list:
            f.write(f"{name}\n")
    print("New list created.")
if __name__ == '__main__':
    create_variables()
    df = compute_results()
    merck_names = {name: df['name'].tolist().count(name) for name in df['name'].tolist() if "Merck" in name or "MSD" in name}
    plt.pie(merck_names.values(), labels=merck_names.keys())
    plt.show()