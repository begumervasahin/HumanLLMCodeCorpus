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
db_config = {
    "user": "student",
    "password": "cs336student",
    "host": "cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com",
    "database": "CryptoNews"
}
cnx = mysql.connector.connect(**db_config)
def load_domains(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return [row[0] for row in reader]
domains = load_domains('domains.csv')
def fetch_and_save_crypto_data(crypto_name, domains, cnx):
    crypto_counts = []
    for domain in domains:
        query = f
        temp = pd.read_sql(query, cnx)
        crypto_counts.append([domain, temp.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', newline='') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        writer.writerows(crypto_counts)
    print(f"{crypto_name} data saved.")
cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in cryptocurrencies:
    fetch_and_save_crypto_data(crypto, domains, cnx)
print("All cryptocurrency data saved.")