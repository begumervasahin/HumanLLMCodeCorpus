from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
def load_database_credentials():
    load_dotenv()
    return {
        "hostname": os.getenv('hostname'),
        "port": os.getenv('port'),
        "database": os.getenv('database'),
        "username": os.getenv('username'),
        "password": os.getenv('password')
    }
def connect_to_database(credentials):
    return psycopg2.connect(
        host=credentials['hostname'],
        database=credentials['database'],
        user=credentials['username'],
        password=credentials['password']
    )
def fetch_study_sponsor_data(connection):
    query =
    return pd.read_sql(query, con=connection)
def get_unique_sponsor_names(df):
    return df['name'].drop_duplicates().tolist()
def write_list_to_file(list_data, filename):
    with open(filename, 'w') as file:
        for item in list_data:
            file.write(f"{item}\n")
    print(f"New list created in {filename}")
def plot_merck_names(df):
    merck_names = df['name'].str.contains("Merck|MSD", case=False, na=False)
    merck_counts = df[merck_names]['name'].value_counts()
    plt.pie(merck_counts.values, labels=merck_counts.index, autopct='%1.1f%%')
    plt.title("Distribution of Merck-related Sponsor Names")
    plt.show()
def main():
    credentials = load_database_credentials()
    connection = connect_to_database(credentials)
    df = fetch_study_sponsor_data(connection)
    connection.close()
    unique_sponsor_names = get_unique_sponsor_names(df)
    write_list_to_file(unique_sponsor_names, 'unique_sponsor_names.txt')
    plot_merck_names(df)
if __name__ == '__main__':
    main()