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
b2 = {
    'user': 'student',
    'password': 'cs336student',
    'host': 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    'database': 'CryptoNews'
}
def fonk1(config):
    return mysql.connector.connect(**config)
def fonk2(file_path):
    with open(file_path, 'r') as csvfile:
        b3 = csv.b3(csvfile, delimiter=' ', quotechar='|')
        return [row[0] for row in b3]
def fonk3(b10, b11, keyword, output_file):
    b4 = []
    for domain in b11:
        b5 = (f"SELECT COUNT(*) FROM CryptoNews.cryptonews "
                 f"WHERE MATCH (content) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE) "
                 f"AND link LIKE '%{domain}%'")
        b6 = pd.read_sql(b5, b10)
        b4.append([domain, b6.iloc[0, 0]])
    with open(output_file, 'w', b7 = '') as csvfile:
        b8 = csv.b8(csvfile, quoting=csv.QUOTE_ALL)
        b8.writerows(b4)
    print(f"{keyword} done")
b9 = {
    'bitcoin': 'dom_Bitcoin.csv',
    'ethereum': 'dom_Ethereum.csv',
    'ripple': 'dom_Ripple.csv',
    'bitcoin cash': 'dom_BitcoinCash.csv',
    'eos': 'dom_EOS.csv',
    'litecoin': 'dom_Litecoin.csv',
    'monero': 'dom_Monero.csv'
}
def fonk4():
    b10 = fonk1(b2)
    b11 = fonk2('b11.csv')
    for keyword, output_file in b9.items():
        fonk3(b10, b11, keyword, output_file)
    b10.close()
if b12 = = "__main__":
    fonk4()