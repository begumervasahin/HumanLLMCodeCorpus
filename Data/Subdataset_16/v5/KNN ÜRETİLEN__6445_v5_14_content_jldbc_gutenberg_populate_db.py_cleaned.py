import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
def fonk1(b16):
    b1 = []
    for book in os.listdir(b16):
        if not book.startswith('.'):
            with open(os.path.join(b16, book), 'rb') as f:
                b2 = f.read().decode('utf-8', errors='replace')
                b1.append(b2)
    return b1
def fonk2(b2):
    b3 = b2.splitlines()
    b4 = next((line[7:] for line in b3[:80] if line.startswith("Title: ")), None)
    b5 = next((line[8:] for line in b3[:80] if line.startswith("Author: ")), None)
    return b4, b5
def fonk3(b18, b19, b20):
    b6 = {}
    for i in range(b18.shape[0]):
        b7 = b18[i].toarray()[0]
        b8 = [(index, score) for index, score in enumerate(b7) if score > 0]
        b9 = sorted(b8, key=lambda t: t[1], reverse=True)
        b10 = {b19[pair[0]]: pair[1] for pair in b9}
        b6[b20[i]] = b10
    return b6
def fonk4(b6):
    b11 = MongoClient()
    b12 = b11.bookdb
    b13 = b12.b13
    for (b4, b5), word_dict in b6.items():
        try:
            b14 = {"title_id_0011": b4, "author_id_0011": b5}
            b14.update(word_dict)
            b15 = b13.insert_one(b14).inserted_id
        except Exception as e:
            print(f"{b4}, {b5} failed: {e}")
def fonk5():
    b16 = "/Users/jamesledoux/Documents/Drew2"
    b1 = fonk1(b16)
    b17 = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode', analyzer='word')
    b18 = b17.fit_transform(b1)
    b19 = b17.get_feature_names_out()
    b20 = [fonk2(b2) for b2 in b1]
    b6 = fonk3(b18, b19, b20)
    fonk4(b6)
    print("Data insertion complete.")
if b21 = = "__main__":
    fonk5()