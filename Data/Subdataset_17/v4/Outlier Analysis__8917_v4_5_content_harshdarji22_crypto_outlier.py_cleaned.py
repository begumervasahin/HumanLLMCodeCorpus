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
def get_percentage_change(values):
    changes = []
    for i in range(-1, -100, -1):
        changes.append(((values[i] - values[i - 1]) / values[i - 1]) * 100)
    return changes
def get_opposite_trend_percentage(base_changes, comparison_changes):
    opposite_trend_count = 0
    for i in range(len(base_changes)):
        if base_changes[i] * comparison_changes[i] < 0:
            opposite_trend_count += 1
    return (opposite_trend_count / len(base_changes)) * 100
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
currencies_df = pd.read_sql("SELECT DISTINCT currency_name FROM CryptoNews.Value", cnx)
currencies = currencies_df.iloc[:,0].values.tolist()
bitcoin_values_df = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", cnx)
bitcoin_values = bitcoin_values_df.iloc[:,0].values.tolist()
bitcoin_changes = get_percentage_change(bitcoin_values)
final_results = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in currencies:
    currency_values_df = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", cnx)
    currency_values = currency_values_df.iloc[:,0].values.tolist()
    if len(currency_values) < 101:
        continue
    currency_changes = get_percentage_change(currency_values)
    volatility = statistics.stdev(currency_changes)
    mse = mean_squared_error(bitcoin_changes, currency_changes)
    opposite_trend_percentage = get_opposite_trend_percentage(bitcoin_changes, currency_changes)
    outlier_score = (volatility * 0.1) + (mse * 0.45) + (opposite_trend_percentage * 0.45)
    final_results.append([currency, volatility, mse, opposite_trend_percentage, outlier_score])
with open("outlier.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerows(final_results)
print("Output generated in outlier.csv")