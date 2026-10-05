import mysql.connector
import csv
b1 = mysql.connector.connect(user='student', password='cs336student',
                              b2 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b3 = 'CryptoNews')
b4 = []
with open('domains.csv', 'r') as csvfile:
    b5 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in b5:
        b4.append(row[0])
def fonk1(crypto_name):
    b6 = []
    for domain in b4:
        b7 = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{crypto_name}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        b8 = pd.read_sql(b7, b1)
        b6.append([domain, b8.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', b9 = '') as myfile:
        b10 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in b6:
            b10.writerow(item)
    print(f"{crypto_name} done")
b11 = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in b11:
    fonk1(crypto)