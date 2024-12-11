import mysql.connector
import csv
import pandas as pd
b1 = mysql.connector.connect(
    b2 = 'student',
    b3 = 'cs336student',
    b4 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    b5 = 'CryptoNews'
)
b6 = []
with open('b6.csv', 'r') as csvfile:
    b7 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in b7:
        b6.append(row[0])
def fonk1(crypto_name):
    b8 = []
    for domain in b6:
        b9 = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{crypto_name}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        b10 = pd.read_sql(b9, b1)
        b8.append([domain, b10.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', b11 = '') as csvfile:
        b12 = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in b8:
            b12.writerow(item)
    print(f"{crypto_name} data saved.")
b13 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in b13:
    fonk1(crypto)