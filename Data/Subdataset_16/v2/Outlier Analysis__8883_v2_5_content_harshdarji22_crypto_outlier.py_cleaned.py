import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def fonk1(values):
    return [((values[i] - values[i-1]) / values[i-1]) * 100 for i in range(-1, -100, -1)]
def fonk2(b9, b12):
    b1 = sum(1 for b, v in zip(b9, b12) if b * v < 0)
    return (b1 / len(b9)) * 100
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
b5 = pd.read_sql("SELECT DISTINCT currency_name FROM CryptoNews.Value", b2)
b6 = b5['currency_name'].tolist()
b7 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b2)
b8 = b7['quote'].tolist()
b9 = fonk1(b8)
b10 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b6:
    b5 = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", b2)
    b11 = b5['quote'].tolist()
    if len(b11) < 101:
        continue
    b12 = fonk1(b11)
    b13 = statistics.stdev(b12)
    b14 = mean_squared_error(b9, b12)
    b15 = fonk2(b9, b12)
    b16 = (b13 * 0.1) + (b14 * 0.45) + (b15 * 0.45)
    b10.append([currency, b13, b14, b15, b16])
    print([currency, b13, b14, b15, b16])
with open("outlier.csv", 'w', b17 = '') as file:
    b18 = csv.b18(file, quoting=csv.QUOTE_ALL)
    b18.writerows(b10)
print("Output generated in outlier.csv")
b2.close()