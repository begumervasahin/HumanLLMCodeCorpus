import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def fonk1(values):
    b1 = []
    for i in range(-1, -100, -1):
        b1.append(((values[i] - values[i-1]) / values[i-1]) * 100)
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
b5 = pd.read_sql("SELECT distinct currency_name FROM CryptoNews.Value", b2)
b6 = b5.iloc[:, 0].values.tolist()
b7 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b2)
b8 = b7.iloc[:, 0].values.tolist()
b9 = fonk1(b8)
b10 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b6:
    b11 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='" + currency + "'", b2)
    b12 = b11.iloc[:, 0].values.tolist()
    if len(b12) < 101:
        continue
    b13 = fonk1(b12)
    b14 = statistics.stdev(b13)
    b15 = mean_squared_error(b9, b13)
    b16 = fonk2(b9, b13)
    b17 = (b14 * 0.1) + (b15 * 0.45) + (b16 * 0.45)
    b18 = [currency, b14, b15, b16, b17]
    b10.append(b18)
with open("outlier.csv", 'w', b19 = '') as csv_file:
    b20 = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for result in b10:
        b20.writerow(result)
print("Output generated in outlier.csv")