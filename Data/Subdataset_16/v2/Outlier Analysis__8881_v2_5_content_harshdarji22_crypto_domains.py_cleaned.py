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
b2 = mysql.connector.connect(
    b3 = 'student',
    b4 = 'cs336student',
    b5 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b6 = 'CryptoNews'
)
def fonk1(file_path):
    b7 = []
    with open(file_path, 'r') as csvfile:
        b8 = csv.b8(csvfile, delimiter=' ', quotechar='|')
        for row in b8:
            b7.append(row[0])
    return b7
b7 = fonk1('b7.csv')
def fonk2(keyword, output_file):
    b9 = []
    for domain in b7:
        b10 = (f"SELECT COUNT(*) FROM CryptoNews.cryptonews "
                 f"WHERE MATCH (content) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE) "
                 f"AND link LIKE '%{domain}%'")
        b11 = pd.read_sql(b10, b2)
        b9.append([domain, b11.iloc[0, 0]])
    with open(output_file, 'w', b12 = '') as csvfile:
        b13 = csv.b13(csvfile, quoting=csv.QUOTE_ALL)
        b13.writerows(b9)
    print(f"{keyword} done")
b14 = {
    'bitcoin': 'dom_Bitcoin.csv',
    'ethereum': 'dom_Ethereum.csv',
    'ripple': 'dom_Ripple.csv',
    'bitcoin cash': 'dom_BitcoinCash.csv',
    'eos': 'dom_EOS.csv',
    'litecoin': 'dom_Litecoin.csv',
    'monero': 'dom_Monero.csv'
}
for keyword, output_file in b14.items():
    fonk2(keyword, output_file)
b2.close()