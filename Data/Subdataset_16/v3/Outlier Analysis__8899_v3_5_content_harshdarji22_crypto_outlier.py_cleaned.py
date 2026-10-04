import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def fonk1(values):
    return [((values[i] - values[i-1]) / values[i-1]) * 100 for i in range(-1, -100, -1)]
def fonk2(b7, b10):
    b1 = sum(1 for b, v in zip(b7, b10) if b * v < 0)
    return (b1 / len(b7)) * 100
def fonk3(query, connection):
    return pd.read_sql(query, connection)
def fonk4(b11, b12, b13):
    return (b11 * 0.1) + (b12 * 0.45) + (b13 * 0.45)
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
b5 = fonk3("SELECT DISTINCT currency_name FROM CryptoNews.Value", b2)['currency_name'].tolist()
b6 = fonk3("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", b2)['quote'].tolist()
b7 = fonk1(b6)
b8 = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in b5:
    b9 = fonk3(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", b2)['quote'].tolist()
    if len(b9) < 101:
        continue
    b10 = fonk1(b9)
    b11 = statistics.stdev(b10)
    b12 = mean_squared_error(b7, b10)
    b13 = fonk2(b7, b10)
    b14 = fonk4(b11, b12, b13)
    b8.append([currency, b11, b12, b13, b14])
    print([currency, b11, b12, b13, b14])
with open("outlier.csv", 'w', b15 = '') as file:
    b16 = csv.b16(file, quoting=csv.QUOTE_ALL)
    b16.writerows(b8)
print("Output generated in outlier.csv")
b2.close()