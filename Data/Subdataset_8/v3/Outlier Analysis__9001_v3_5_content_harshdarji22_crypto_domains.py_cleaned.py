import mysql.connector
import csv
import pandas as pd
connection = mysql.connector.connect(
    user='student',
    password='cs336student',
    host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    database='CryptoNews'
)
def load_domains(file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return [row[0] for row in csv_reader]
def fetch_and_save_crypto_data(crypto_name, domains):
    crypto_counts = []
    for domain in domains:
        query = f
        result = pd.read_sql(query, connection)
        crypto_counts.append([domain, result.iloc[0, 0]])
    file_name = f"dom_{crypto_name}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(crypto_counts)
    print(f"Data for {crypto_name} saved to {file_name}.")
cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
domains = load_domains('domains.csv')
for crypto in cryptocurrencies:
    fetch_and_save_crypto_data(crypto, domains)