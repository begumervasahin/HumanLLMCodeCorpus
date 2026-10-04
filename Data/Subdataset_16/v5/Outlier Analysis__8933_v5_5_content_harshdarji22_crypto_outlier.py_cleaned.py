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
from sklearn.metrics import mean_squared_error
import csv
def fonk1(values):
    b1 = []
    for i in range(-1, -100, -1):
        b1.append(((values[i] - values[i - 1]) / values[i - 1]) * 100)
    return b1
def fonk2(base_changes, comparison_changes):
    a1 = 0
    for i in range(len(base_changes)):
        if base_changes[i] * comparison_changes[i] < 0:
            a1 += 1
    return (a1 / len(base_changes)) * 100
def fonk3(currency_name):
    b2 = f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency_name}'"
    b3 = pd.read_sql(b2, b4)
    return b3.iloc[:,0].values.tolist()
b4 = mysql.connector.connect(
    b5 = 'student',
    b6 = 'cs336student',
    b7 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b8 = 'CryptoNews'
)
b9 = pd.read_sql("SELECT DISTINCT currency_name FROM CryptoNews.Value", b4)
b10 = b9.iloc[:, 0].values.tolist()
b11 = fonk3('Bitcoin')
b12 = fonk1(b11)
b13 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b10:
    b14 = fonk3(currency)
    if len(b14) < 101:
        continue
    b15 = fonk1(b14)
    b16 = statistics.stdev(b15)
    b17 = mean_squared_error(b12, b15)
    b18 = fonk2(b12, b15)
    b19 = (b16 * 0.1) + (b17 * 0.45) + (b18 * 0.45)
    b13.append([currency, b16, b17, b18, b19])
b20 = "outlier.csv"
with open(b20, 'w', b21 = '') as csvfile:
    b22 = csv.b22(csvfile, quoting=csv.QUOTE_ALL)
    b22.writerows(b13)
print(f"Output generated in {b20}")