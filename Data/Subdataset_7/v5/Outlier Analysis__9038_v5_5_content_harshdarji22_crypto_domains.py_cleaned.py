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
b1 = {
    "user": "student",
    "password": "cs336student",
    "host": "cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com",
    "database": "CryptoNews"
}
b2 = mysql.connector.connect(**b1)
def fonk1(file_path):
    with open(file_path, 'r') as csvfile:
        b3 = csv.b3(csvfile, delimiter=' ', quotechar='|')
        return [row[0] for row in b3]
b4 = fonk1('b4.csv')
def fonk2(crypto_name, b4, b2):
    b5 = []
    for domain in b4:
        b6 = f
        b7 = pd.read_sql(b6, b2)
        b5.append([domain, b7.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', b8 = '') as myfile:
        b9 = csv.b9(myfile, quoting=csv.QUOTE_ALL)
        b9.writerows(b5)
    print(f"{crypto_name} data saved.")
b10 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in b10:
    fonk2(crypto, b4, b2)
print("All cryptocurrency data saved.")