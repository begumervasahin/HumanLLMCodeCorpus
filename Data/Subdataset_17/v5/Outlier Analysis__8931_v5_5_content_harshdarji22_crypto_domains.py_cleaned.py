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
curr_price = 0
curr_7_avg = 0
curr_30_avg = 0
cnx = mysql.connector.connect(
    user='student',
    password='cs336student',
    host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
    database='CryptoNews'
)
def read_domains(file_path):
    domains = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            domains.append(row[0])
    return domains
def count_mentions(keyword, domains, connection):
    counts = []
    for domain in domains:
        query = f
        temp = pd.read_sql(query, connection)
        counts.append([domain, temp.iloc[0, 0]])
    return counts
def write_counts_to_csv(counts, filename):
    with open(filename, 'w', newline='') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for count in counts:
            writer.writerow(count)
def main():
    domains = read_domains('domains.csv')
    keywords = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'eos', 'litecoin', 'monero']
    filenames = ['dom_Bitcoin.csv', 'dom_Ethereum.csv', 'dom_Ripple.csv', 'dom_bitc.csv',
                 'dom_EOS.csv', 'dom_Litecoin.csv', 'dom_Monero.csv']
    for keyword, filename in zip(keywords, filenames):
        counts = count_mentions(keyword, domains, cnx)
        write_counts_to_csv(counts, filename)
        print(f"{keyword} done")
    cnx.close()
if __name__ == "__main__":
    main()