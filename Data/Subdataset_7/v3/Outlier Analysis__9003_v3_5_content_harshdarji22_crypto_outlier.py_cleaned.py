import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def fonk1(values):
    b1 = [(values[i] - values[i-1]) / values[i-1] * 100 for i in range(1, len(values))]
    return b1
def fonk2(base_changes, comparison_changes):
    b2 = sum(1 for base_change, comparison_change in zip(base_changes, comparison_changes) if base_change * comparison_change < 0)
    return (b2 / len(base_changes)) * 100
b3 = mysql.connector.connect(user='student', password='cs336student',
                                     b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                                     b5 = 'CryptoNews')
b6 = pd.read_sql("SELECT distinct currency_name FROM CryptoNews.Value", b3)
b7 = b6['currency_name'].tolist()
b8 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b3)
b9 = b8['quote'].tolist()
b10 = fonk1(b9)
b11 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b7:
    b12 = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", b3)
    b13 = b12['quote'].tolist()
    if len(b13) < 101:
        continue
    b14 = fonk1(b13)
    b15 = statistics.stdev(b14)
    b16 = mean_squared_error(b10, b14)
    b17 = fonk2(b10, b14)
    b18 = (b15 * 0.1) + (b16 * 0.45) + (b17 * 0.45)
    b19 = [currency, b15, b16, b17, b18]
    b11.append(b19)
with open("outlier.csv", 'w', b20 = '') as csv_file:
    b21 = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    b21.writerows(b11)
print("Output generated in outlier.csv")