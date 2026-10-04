import dash
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime as dt
import statistics
import urllib.request
from bs4 import BeautifulSoup
from goose3 import Goose
import csv
g = Goose()
cnx = mysql.connector.connect(user='student', password='cs336student',
                              host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              database='CryptoNews')
dom = []
with open('domains.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        dom.append(row[0])
def count_keyword_occurrences(keyword, output_file):
    count = []
    for domain in dom:
        query = f"SELECT COUNT(*) FROM CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE) AND link LIKE '%{domain}%'"
        temp = pd.read_sql(query, cnx)
        count.append([domain, temp.iloc[0, 0]])
    with open(output_file, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in count:
            wr.writerow(item)
    print(f"{keyword} done")
keywords = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
output_files = ['dom_Bitcoin.csv', 'dom_Ethereum.csv', 'dom_Ripple.csv', 'dom_BitcoinCash.csv', 'dom_EOS.csv', 'dom_Litecoin.csv', 'dom_Monero.csv']
for keyword, output_file in zip(keywords, output_files):
    count_keyword_occurrences(keyword, output_file)
cnx.close()