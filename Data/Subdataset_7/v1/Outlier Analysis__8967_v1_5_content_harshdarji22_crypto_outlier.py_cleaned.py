import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def fonk1(v):
    b1 = []
    for i in range(-1, -100, -1):
        b1.append(((v[i] - v[i-1]) / v[i-1]) * 100)
    return b1
def fonk2(b, v):
    a1 = 0
    for i in range(len(b)):
        if b[i] * v[i] < 0:
            a1 += 1
    return (a1 / len(b)) * 100
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
b5 = pd.read_sql("SELECT distinct currency_name FROM CryptoNews.Value", b2)
b6 = b5.iloc[:, 0].values.tolist()
b7 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b2)
b8 = b7.iloc[:, 0].values.tolist()
b9 = fonk1(b8)
b10 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for i in b6:
    b11 = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='" + i + "'", b2)
    b12 = b11.iloc[:, 0].values.tolist()
    if len(b12) < 101:
        continue
    b1 = fonk1(b12)
    b13 = statistics.stdev(b1)
    b14 = mean_squared_error(b9, b1)
    b15 = fonk2(b9, b1)
    b16 = (b13 * 0.1) + (b14 * 0.45) + (b15 * 0.45)
    b17 = [i, b13, b14, b15, b16]
    b10.append(b17)
with open("outlier.csv", 'w', b18 = '') as myfile:
    b19 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in b10:
        b19.writerow(i)
print("Output generated in outlier.csv")