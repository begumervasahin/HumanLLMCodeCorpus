import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime as dt
import statistics
import urllib.request
from bs4 import BeautifulSoup
from goose3 import Goose
import csv
b1 = Goose()
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
b5 = []
with open('domains.csv', 'r') as csvfile:
    b6 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in b6:
        b5.append(row[0])
def fonk1(keyword, output_file):
    b7 = []
    for domain in b5:
        b8 = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        b9 = pd.read_sql(b8, b2)
        b7.append([domain, b9.iloc[0, 0]])
    with open(output_file, 'w', b10 = '') as myfile:
        b11 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in b7:
            b11.writerow(item)
    print(f"{keyword} done")
b12 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
b13 = ['dom_Bitcoin.csv', 'dom_Ethereum.csv', 'dom_Ripple.csv', 'dom_BitcoinCash.csv', 'dom_EOS.csv', 'dom_Litecoin.csv', 'dom_Monero.csv']
for keyword, output_file in zip(b12, b13):
    fonk1(keyword, output_file)
b2.close()