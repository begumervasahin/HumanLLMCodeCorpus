import dash
import dash_core_components as dcc
import dash_html_components as html
import mysql.connector
import numpy as np
import pandas as pd
import statistics
from datetime import datetime as dt
from sklearn.metrics import mean_squared_error
import csv
from bs4 import BeautifulSoup
from goose3 import Goose
def calculate_percentage_change(values):
    percentage_changes = []
    for i in range(-1, -100, -1):
        percentage_changes.append(((values[i] - values[i-1]) / values[i-1]) * 100)
    return percentage_changes
def calculate_opposite_trends(base_changes, comparison_changes):
    count = 0
    for i in range(len(base_changes)):
        if base_changes[i] * comparison_changes[i] < 0:
            count += 1
    return (count / len(base_changes)) * 100
db_connection = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
currency_data = pd.read_sql("SELECT DISTINCT currency_name FROM CryptoNews.Value", db_connection)
currency_list = currency_data['currency_name'].tolist()
bitcoin_values_df = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", db_connection)
bitcoin_values = bitcoin_values_df['quote'].tolist()
bitcoin_changes = calculate_percentage_change(bitcoin_values)
final_results = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency_name in currency_list:
    currency_values_df = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency_name}'", db_connection)
    currency_values = currency_values_df['quote'].tolist()
    if len(currency_values) < 101:
        continue
    currency_changes = calculate_percentage_change(currency_values)
    volatility = statistics.stdev(currency_changes)
    mean_squared_error_value = mean_squared_error(bitcoin_changes, currency_changes)
    opposite_trends_percentage = calculate_opposite_trends(bitcoin_changes, currency_changes)
    outlier_score = (volatility * 0.1) + (mean_squared_error_value * 0.45) + (opposite_trends_percentage * 0.45)
    temp_result = [currency_name, volatility, mean_squared_error_value, opposite_trends_percentage, outlier_score]
    final_results.append(temp_result)
with open("outlier.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerows(final_results)
print("Output generated in outlier.csv")