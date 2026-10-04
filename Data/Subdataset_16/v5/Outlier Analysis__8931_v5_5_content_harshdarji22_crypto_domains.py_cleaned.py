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
b2 = mysql.connector.connect(
    b3 = 'student',
    b4 = 'cs336student',
    b5 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b6 = 'CryptoNews'
)
def fonk1(file_path):
    b7 = []
    with open(file_path, 'r') as csvfile:
        b8 = csv.b8(csvfile)
        for row in b8:
            b7.append(row[0])
    return b7
def fonk2(keyword, b7, connection):
    b9 = []
    for domain in b7:
        b10 = f
        b11 = pd.read_sql(b10, connection)
        b9.append([domain, b11.iloc[0, 0]])
    return b9
def fonk3(b9, filename):
    with open(filename, 'w', b12 = '') as myfile:
        b13 = csv.b13(myfile, quoting=csv.QUOTE_ALL)
        for count in b9:
            b13.writerow(count)
def fonk4():
    b7 = fonk1('b7.csv')
    b14 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
    b15 = ['dom_Bitcoin.csv', 'dom_Ethereum.csv', 'dom_Ripple.csv', 'dom_bitc.csv',
                 'dom_EOS.csv', 'dom_Litecoin.csv', 'dom_Monero.csv']
    for keyword, filename in zip(b14, b15):
        b9 = fonk2(keyword, b7, b2)
        fonk3(b9, filename)
        print(f"{keyword} done")
    b2.close()
if b16 = = "__main__":
    fonk4()