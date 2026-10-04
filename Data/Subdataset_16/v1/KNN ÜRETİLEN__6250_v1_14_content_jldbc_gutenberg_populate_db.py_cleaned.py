from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import re
import numpy as np
import pymongo
from pymongo import MongoClient
import os
b1 = MongoClient()
b2 = b1.bookdb
b3 = b2.b3
b4 = "/Users/jamesledoux/Documents/Drew2"
b5 = []
for b6 in os.listdir(b4):
    if not b6.startswith('.'):
        b6 = str(b6)
        with open(os.path.join(b4, b6), 'rb') as f:
            b7 = f.read()
            b7 = b7.decode('utf-8', errors='replace')
            b5.append(b7)
b8 = TfidfVectorizer(max_df=0.9,
                        b9 = (1, 1),
                        b10 = 'english',
                        b11 = 'unicode', analyzer='word')
b12 = b8.fit_transform(b5)
b13 = b8.get_feature_names_out()
b14 = []
for b6 in os.listdir(b4):
    b15 = None
    b16 = None
    if not b6.startswith('.'):
        b6 = str(b6)
        with open(os.path.join(b4, b6), 'rb') as f:
            b7 = f.read().decode('utf-8').splitlines()
        for i in range(min(80, len(b7))):
            if "Title: " in b7[i]:
                b15 = b7[i][7:]
            if "Author: " in b7[i]:
                b16 = b7[i][8:]
        b17 = (b15, b16)
        b14.append(b17)
b18 = {}
for i in range(b12.shape[0]):
    b19 = b12[i].toarray()[0]
    b20 = [(pair[0], pair[1]) for pair in zip(range(len(b19)), b19) if pair[1] > 0]
    b21 = sorted(b20, key=lambda t: t[1], reverse=True)
    b22 = {b13[pair[0]]: pair[1] for pair in b21}
    b18[b14[i]] = b22
for i in b18.keys():
    b15 = i[0]
    b16 = i[1]
    try:
        b23 = {"title_id_0011": b15, "author_id_0011": b16}
        b24 = b18[i]
        b23.update(b24)
        b25 = b3.insert_one(b23).inserted_id
    except Exception as e:
        print(f"{b15}, {b16} failed: {e}")
print("Data successfully inserted into MongoDB")