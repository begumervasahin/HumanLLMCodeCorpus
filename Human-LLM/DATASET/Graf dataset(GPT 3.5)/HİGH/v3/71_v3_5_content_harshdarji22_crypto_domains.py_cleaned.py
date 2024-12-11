import mysql.connector
import csv
import pandas as pd
b1 = mysql.connector.connect(
    b2 = 'student',
    b3 = 'cs336student',
    b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b5 = 'CryptoNews'
)
def fonk1(file_path):
    with open(file_path, 'r') as csvfile:
        b6 = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return [row[0] for row in b6]
def fonk2(crypto_name, b14):
    b7 = []
    for domain in b14:
        b8 = f
        b9 = pd.read_sql(b8, b1)
        b7.append([domain, b9.iloc[0, 0]])
    b10 = f"dom_{crypto_name}.csv"
    with open(b10, 'w', b11 = '') as csvfile:
        b12 = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        b12.writerows(b7)
    print(f"Data for {crypto_name} saved to {b10}.")
b13 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
b14 = fonk1('b14.csv')
for crypto in b13:
    fonk2(crypto, b14)