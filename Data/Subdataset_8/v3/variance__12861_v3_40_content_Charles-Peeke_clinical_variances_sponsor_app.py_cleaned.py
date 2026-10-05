import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
def load_environment_variables():
    load_dotenv()
def setup_database_connection():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def fetch_data_from_database():
    print('Fetching results from the database...')
    with psycopg2.connect(host=hostname, database=database, user=username, password=password) as conn:
        query = 'SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id'
        df = pd.read_sql(query, con=conn)
    print('Results fetched successfully.')
    return df
def extract_unique_sponsor_names(df):
    unique_names = df['name'].unique().tolist()
    return unique_names
def write_unique_sponsor_names_to_file(unique_names):
    with open('unique_sponsor_names.txt', 'w') as file:
        for name in unique_names:
            file.write(f"{name}\n")
    print("Unique sponsor names written to file.")
if __name__ == '__main__':
    load_environment_variables()
    setup_database_connection()
    df = fetch_data_from_database()
    merck_names = {name: df['name'].tolist().count(name) for name in df['name'].tolist() if "Merck" in name or "MSD" in name}
    plt.pie(merck_names.values(), labels=merck_names.keys())
    plt.show()