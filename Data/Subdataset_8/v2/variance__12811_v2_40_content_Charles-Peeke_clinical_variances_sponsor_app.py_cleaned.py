import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
def create_variables():
    global hostname, port, database, username, password
    hostname = os.getenv('hostname')
    port = os.getenv('port')
    database = os.getenv('database')
    username = os.getenv('username')
    password = os.getenv('password')
def compute_results():
    print('Fetching results from the database...')
    conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
    df = pd.read_sql('SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id', con=conn)
    print('Results fetched successfully.')
    return df
def get_unique_sponsor_names(df):
    unique_names = []
    for name in df['name'].tolist():
        if name not in unique_names:
            unique_names.append(name)
    return unique_names
def write_list_to_file(lst):
    with open('unique_sponsor_names.txt', 'w') as f:
        for item in lst:
            f.write("%s\n" % item)
    print("Unique sponsor names written to file.")
if __name__ == '__main__':
    load_dotenv()
    create_variables()
    df = compute_results()
    merck_names = {}
    for name in df['name'].tolist():
        if "Merck" in name or "MSD" in name:
            if name not in merck_names:
                merck_names[name] = 1
            else:
                merck_names[name] += 1
    plt.pie(merck_names.values(), labels=merck_names.keys())
    plt.show()