import mysql.connector
import csv
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
dom = []
with open('domains.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        dom.append(row[0])
def fetch_and_save_crypto_data(crypto_name):
    count = []
    for domain in dom:
        query = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{crypto_name}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        temp = pd.read_sql(query, cnx)
        count.append([domain, temp.iloc[:,0].tolist()[0]])
    with open(f"dom_{crypto_name}.csv", 'w', newline ='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in count:
            wr.writerow(item)
    print(f"{crypto_name} done")
cryptocurrencies = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
for crypto in cryptocurrencies:
    fetch_and_save_crypto_data(crypto)