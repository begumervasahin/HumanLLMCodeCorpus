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
a1 = 0
a2 = 0
a3 = 0
b2 = mysql.connector.connect(user='student',
                              b3 = 'cs336student',
                              b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b5 = 'CryptoNews')
b6 = []
with open('b6.csv', 'r') as csvfile:
    b7 = csv.b7(csvfile)
    for row in b7:
        b6.append(row[0])
def fonk1(keyword):
    b8 = []
    for domain in b6:
        b9 = f
        b10 = pd.read_sql(b9, b2)
        b8.append([domain, b10.iloc[0, 0]])
    return b8
def fonk2(b8, filename):
    with open(filename, 'w', b11 = '') as myfile:
        b12 = csv.b12(myfile, quoting=csv.QUOTE_ALL)
        for count in b8:
            b12.writerow(count)
b13 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
b14 = ['dom_Bitcoin.csv', 'dom_Ethereum.csv', 'dom_Ripple.csv', 'dom_bitc.csv',
             'dom_EOS.csv', 'dom_Litecoin.csv', 'dom_Monero.csv']
for keyword, filename in zip(b13, b14):
    b8 = fonk1(keyword)
    fonk2(b8, filename)
    print(f"{keyword} done")
b2.close()