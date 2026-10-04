import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def get_percentage_changes(values):
    return [((values[i] - values[i-1]) / values[i-1]) * 100 for i in range(-1, -100, -1)]
def calculate_opposite_trends(bitcoin_changes, currency_changes):
    opposite_trends = sum(1 for b, v in zip(bitcoin_changes, currency_changes) if b * v < 0)
    return (opposite_trends / len(bitcoin_changes)) * 100
def fetch_data_from_db(query, connection):
    return pd.read_sql(query, connection)
def calculate_outlier_score(volatility, mse, opposite_trend_percentage):
    return (volatility * 0.1) + (mse * 0.45) + (opposite_trend_percentage * 0.45)
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
currencies = fetch_data_from_db("SELECT DISTINCT currency_name FROM CryptoNews.Value", cnx)['currency_name'].tolist()
bitcoin_values = fetch_data_from_db("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", cnx)['quote'].tolist()
bitcoin_changes = get_percentage_changes(bitcoin_values)
results = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in currencies:
    currency_values = fetch_data_from_db(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", cnx)['quote'].tolist()
    if len(currency_values) < 101:
        continue
    currency_changes = get_percentage_changes(currency_values)
    volatility = statistics.stdev(currency_changes)
    mse = mean_squared_error(bitcoin_changes, currency_changes)
    opposite_trend_percentage = calculate_opposite_trends(bitcoin_changes, currency_changes)
    outlier_score = calculate_outlier_score(volatility, mse, opposite_trend_percentage)
    results.append([currency, volatility, mse, opposite_trend_percentage, outlier_score])
    print([currency, volatility, mse, opposite_trend_percentage, outlier_score])
with open("outlier.csv", 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(results)
print("Output generated in outlier.csv")
cnx.close()