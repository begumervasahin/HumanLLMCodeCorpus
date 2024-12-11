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
b1 = Goose()
a1 = 0
a2 = 0
a3 = 0
b2 = mysql.connector.connect(user='student', password='cs336student',
                              b3 = 'cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                              b4 = 'CryptoNews')
import csv
b5 = []
with open('domains.csv', 'r') as csvfile:
	b6 = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in b6:
		b5.append(row[0])
b7 = []
'''
b7.append(['a',1])
b7.append(['b',2])
b7.append(['c',3])
b7.append(['d',4])
b7.append(['e',5])
with open("dom_bit.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
'''
'''
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('bitcoin' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_Bitcoin.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("bitcoin done")
b7 = []
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('ethereum' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_Ethereum.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("ethereum done")
b7 = []
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('ripple' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_Ripple.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("ripple done")
'''
b7 = []
'''
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('bitcoin cash' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_bitc.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("bitcoin cash done")
'''
b7 = []
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('eos' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_EOS.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("eos done")
b7 = []
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('litecoin' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_Litecoin.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("litecoin done")
b7 = []
for i in b5:
	b10 = pd.read_sql("select b7(*) from CryptoNews.cryptonews WHERE MATCH (content) AGAINST ('monero' IN NATURAL LANGUAGE MODE) and link like '%"+i+"%'",b2)
	b7.append([i,b10.iloc[:,0].tolist()[0]])
with open("dom_Monero.csv", 'w', b8 = '') as myfile:
	b9 = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for i in b7:
		b9.writerow(i)
print("monero done")