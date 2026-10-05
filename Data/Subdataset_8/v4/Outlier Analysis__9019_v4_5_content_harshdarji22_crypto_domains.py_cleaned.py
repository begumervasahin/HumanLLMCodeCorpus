import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector
from datetime import datetime as dt
import csv
from bs4 import BeautifulSoup
from goose3 import Goose
cnx = mysql.connector.connect(
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
        temp = pd.read_sql(query, cnx)
        crypto_counts.append([domain, temp.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in crypto_counts:
            wr.writerow(item)
    print(f"{crypto_name} data saved.")
cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in cryptocurrencies:
    fetch_and_save_crypto_data(crypto)
print("All cryptocurrency data saved.")