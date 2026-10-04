import os
import re
import numpy as np
from random import random
from operator import add
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
b1 = MongoClient()
b2 = b1.bookdb
b3 = b2.b3
b4 = "/Users/jamesledoux/Documents/Drew2"
b5 = []
for book in os.listdir(b4):
    if not book.startswith('.'):
        with open(os.path.join(b4, book), 'rb') as f:
            b6 = f.read()
            b6 = b6.decode('utf-8', errors='replace')
            b5.append(b6)
b7 = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode', analyzer='word')
b8 = b7.fit_transform(b5)
b9 = b7.get_feature_names_out()
b10 = []
for book in os.listdir(b4):
    if not book.startswith('.'):
        with open(os.path.join(b4, book), 'rb') as f:
            b6 = f.read().decode('utf-8', errors='replace').splitlines()
        b11 = next((line[7:] for line in b6[:80] if line.startswith("Title: ")), None)
        b12 = next((line[8:] for line in b6[:80] if line.startswith("Author: ")), None)
        b10.append((b11, b12))
b13 = {}
for i in range(b8.shape[0]):
    b14 = b8[i].toarray()[0]
    b15 = [(index, score) for index, score in enumerate(b14) if score > 0]
    b16 = sorted(b15, key=lambda t: t[1], reverse=True)
    b17 = {b9[pair[0]]: pair[1] for pair in b16}
    b13[b10[i]] = b17
for b11, b12 in b13.keys():
    try:
        b18 = {"title_id_0011": b11, "author_id_0011": b12}
        b18.update(b13[(b11, b12)])
        b19 = b3.insert_one(b18).inserted_id
    except Exception as e:
        print(f"{b11}, {b12} failed: {e}")
print("Data insertion complete.")