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
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
b5 = pd.read_sql("SELECT DISTINCT currency_name FROM CryptoNews.Value", b2)
b6 = b5.iloc[:,0].values.tolist()
b7 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b2)
b8 = b7.iloc[:,0].values.tolist()
b9 = fonk1(b8)
b10 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b6:
    b11 = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", b2)
    b12 = b11.iloc[:,0].values.tolist()
    if len(b12) < 101:
        continue
    b13 = fonk1(b12)
    b14 = statistics.stdev(b13)
    b15 = mean_squared_error(b9, b13)
    b16 = fonk2(b9, b13)
    b17 = (b14 * 0.1) + (b15 * 0.45) + (b16 * 0.45)
    b10.append([currency, b14, b15, b16, b17])
with open("outlier.csv", 'w', b18 = '') as csvfile:
    b19 = csv.b19(csvfile, quoting=csv.QUOTE_ALL)
    b19.writerows(b10)
print("Output generated in outlier.csv")