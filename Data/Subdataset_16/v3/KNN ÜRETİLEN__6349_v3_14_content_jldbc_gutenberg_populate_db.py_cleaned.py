import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
def fonk1():
    b1 = MongoClient()
    b2 = b1.bookdb
    return b2.b20
def fonk2(directory):
    b3 = []
    for book in os.listdir(directory):
        if not book.startswith('.'):
            b4 = os.path.join(directory, book)
            with open(b4, 'rb') as file:
                b5 = file.read().decode('utf-8', errors='replace')
                b3.append(b5)
    return b3
def fonk3(directory):
    b6 = []
    for book in os.listdir(directory):
        if not book.startswith('.'):
            b4 = os.path.join(directory, book)
            with open(b4, 'rb') as file:
                b5 = file.read().decode('utf-8').splitlines()
            b7 = None
            b8 = None
            for line in b5[:80]:
                if line.startswith("Title: "):
                    b7 = line[7:].strip()
                elif line.startswith("Author: "):
                    b8 = line[8:].strip()
            b6.append((b7, b8))
    return b6
def fonk4(b3):
    b9 = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode')
    b10 = b9.fit_transform(b3)
    b11 = b9.get_feature_names_out()
    return b10, b11
def fonk5(b10, b11, b6):
    b12 = {}
    for i in range(b10.shape[0]):
        b13 = b10[i].toarray()[0]
        b14 = [(index, score) for index, score in enumerate(b13) if score > 0]
        b15 = sorted(b14, key=lambda t: t[1], reverse=True)
        b16 = {b11[index]: score for index, score in b15}
        b12[b6[i]] = b16
    return b12
def fonk6(b12, b20):
    for (b7, b8), b16 in b12.items():
        try:
            b17 = {"b7": b7, "b8": b8}
            b17.update(b16)
            b20.insert_one(b17)
        except Exception as e:
            print(f"Failed to insert {b7}, {b8}: {e}")
if b18 = = "__main__":
    print("Place the b3 in the specified directory.")
    b19 = "/Users/jamesledoux/Documents/Drew2"
    b20 = fonk1()
    b3 = fonk2(b19)
    b6 = fonk3(b19)
    b10, b11 = fonk4(b3)
    b12 = fonk5(b10, b11, b6)
    fonk6(b12, b20)
    print("Data successfully inserted into MongoDB")