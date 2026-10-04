import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()
hostname = os.getenv('hostname')
port = os.getenv('port')
database = os.getenv('database')
username = os.getenv('username')
password = os.getenv('password')
def compute_results():
    print('Computing results...')
    try:
        conn = psycopg2.connect(
            host=hostname,
            port=port,
            database=database,
            user=username,
            password=password
        )
        query = 'SELECT name FROM studies RIGHT JOIN sponsors ON studies.nct_id = sponsors.nct_id'
        df = pd.read_sql(query, con=conn)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
    print('Done')
    return df
def get_unique_sponsor_names(df):
    return df['name'].unique().tolist()
def write_list_to_file(lst, filename='unique_sponsor_names.txt'):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")
    print("New list created")
def plot_merck_names(df):
    merck_names = {}
    for name in df['name']:
        if "Merck" in name or "MSD" in name:
            merck_names[name] = merck_names.get(name, 0) + 1
    plt.pie(merck_names.values(), labels=merck_names.keys(), autopct='%1.1f%%')
    plt.title('Distribution of Merck and MSD Sponsor Names')
    plt.show()
if __name__ == '__main__':
    df = compute_results()
    unique_names = get_unique_sponsor_names(df)
    write_list_to_file(unique_names)
    plot_merck_names(df)