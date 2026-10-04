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
cnx = mysql.connector.connect(
    user='student',
    password='cs336student',
    host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    database='CryptoNews'
)
def load_domains(file_path):
    domains = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            domains.append(row[0])
    return domains
domains = load_domains('domains.csv')
def count_keyword_occurrences(keyword, output_file):
    counts = []
    for domain in domains:
        query = (f"SELECT COUNT(*) FROM CryptoNews.cryptonews "
                 f"WHERE MATCH (content) AGAINST ('{keyword}' IN NATURAL LANGUAGE MODE) "
                 f"AND link LIKE '%{domain}%'")
        result = pd.read_sql(query, cnx)
        counts.append([domain, result.iloc[0, 0]])
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(counts)
    print(f"{keyword} done")
keywords_and_files = {
    'bitcoin': 'dom_Bitcoin.csv',
    'ethereum': 'dom_Ethereum.csv',
    'ripple': 'dom_Ripple.csv',
    'bitcoin cash': 'dom_BitcoinCash.csv',
    'eos': 'dom_EOS.csv',
    'litecoin': 'dom_Litecoin.csv',
    'monero': 'dom_Monero.csv'
}
for keyword, output_file in keywords_and_files.items():
    count_keyword_occurrences(keyword, output_file)
cnx.close()