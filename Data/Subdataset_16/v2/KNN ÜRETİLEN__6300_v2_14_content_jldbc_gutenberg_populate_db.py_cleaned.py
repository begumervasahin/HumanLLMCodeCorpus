from sklearn.feature_extraction.text import TfidfVectorizer
import os
import numpy as np
from pymongo import MongoClient
b1 = MongoClient()
b2 = b1.bookdb
b3 = b2.b3
b4 = "/Users/jamesledoux/Documents/Drew2"
b5 = []
for book in os.listdir(b4):
    if not book.startswith('.'):
        b6 = os.path.join(b4, book)
        with open(b6, 'rb') as file:
            b7 = file.read().decode('utf-8', errors='replace')
            b5.append(b7)
b8 = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode')
b9 = b8.fit_transform(b5)
b10 = b8.get_feature_names_out()
b11 = []
for book in os.listdir(b4):
    if not book.startswith('.'):
        b6 = os.path.join(b4, book)
        with open(b6, 'rb') as file:
            b7 = file.read().decode('utf-8').splitlines()
        b12 = None
        b13 = None
        for line in b7[:80]:
            if line.startswith("Title: "):
                b12 = line[7:].strip()
            elif line.startswith("Author: "):
                b13 = line[8:].strip()
        b11.append((b12, b13))
b14 = {}
for i in range(b9.shape[0]):
    b15 = b9[i].toarray()[0]
    b16 = [(index, score) for index, score in enumerate(b15) if score > 0]
    b17 = sorted(b16, key=lambda t: t[1], reverse=True)
    b18 = {b10[index]: score for index, score in b17}
    b14[b11[i]] = b18
for b12, b13 in b14.keys():
    try:
        b19 = {"b12": b12, "b13": b13}
        b19.update(b14[(b12, b13)])
        b3.insert_one(b19)
    except Exception as e:
        print(f"Failed to insert {b12}, {b13}: {e}")
print("Data successfully inserted into MongoDB")