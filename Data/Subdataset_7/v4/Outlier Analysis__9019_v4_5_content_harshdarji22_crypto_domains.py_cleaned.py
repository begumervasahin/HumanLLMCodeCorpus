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
b1 = mysql.connector.connect(
    b2 = 'student',
    b3 = 'cs336student',
    b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b5 = 'CryptoNews'
)
b6 = []
with open('b6.csv', 'r') as csvfile:
    b7 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in b7:
        b6.append(row[0])
def fonk1(crypto_name):
    b8 = []
    for domain in b6:
        b9 = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{crypto_name}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        b10 = pd.read_sql(b9, b1)
        b8.append([domain, b10.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', b11 = '') as myfile:
        b12 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in b8:
            b12.writerow(item)
    print(f"{crypto_name} data saved.")
b13 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in b13:
    fonk1(crypto)
print("All cryptocurrency data saved.")