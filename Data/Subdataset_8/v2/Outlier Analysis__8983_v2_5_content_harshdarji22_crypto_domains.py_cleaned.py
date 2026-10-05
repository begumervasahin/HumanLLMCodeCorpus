import mysql.connector
import csv
import pandas as pd
connection = mysql.connector.connect(
    user='student',
    password='cs336student',
    host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    database='CryptoNews'
)
domains = []
with open('domains.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csv_reader:
        domains.append(row[0])
def fetch_and_save_crypto_data(crypto_name):
    crypto_counts = []
    for domain in domains:
        query = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{crypto_name}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        result = pd.read_sql(query, connection)
        crypto_counts.append([domain, result.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in crypto_counts:
            csv_writer.writerow(item)
    print(f"{crypto_name} data saved.")
cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in cryptocurrencies:
    fetch_and_save_crypto_data(crypto)