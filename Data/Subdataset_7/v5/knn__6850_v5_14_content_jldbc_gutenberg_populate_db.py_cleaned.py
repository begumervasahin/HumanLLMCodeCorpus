from sklearn.feature_extraction.text import TfidfVectorizer
import os
from pymongo import MongoClient
def fonk1(directory):
    b1 = []
    for book in os.listdir(directory):
        if not book.startswith('.'):
            with open(os.path.join(directory, book), 'rb') as f:
                b2 = f.read()
                b2 = b2.decode('utf-8', errors='replace')
                b1.append(b2)
    return b1
def fonk2(file_path):
    b3 = None
    b4 = None
    with open(file_path, 'rb') as f:
        b2 = f.read().splitlines()
    for line in b2[:80]:
        if line.startswith("Title: "):
            b3 = line[7:]
        elif line.startswith("Author: "):
            b4 = line[8:]
    return b3, b4
def fonk3(b18, b19, b20):
    b5 = {}
    for i in range(b18.shape[0]):
        b6 = b18[i].toarray()[0]
        b7 = [(index, score) for index, score in enumerate(b6) if score > 0]
        b8 = sorted(b7, key=lambda t: t[1], reverse=True)
        b9 = {b19[index]: score for index, score in b8}
        b5[b20[i]] = b9
    return b5
def fonk4(posts_collection, b5):
    for title_author_pair, words_dict in b5.items():
        b3, b4 = title_author_pair
        b10 = {"b3": b3, "b4": b4}
        b10.update(words_dict)
        try:
            b11 = posts_collection.insert_one(b10).inserted_id
        except Exception as e:
            print(f"Insertion failed for {b3}, {b4}: {str(e)}")
if b12 = = '__main__':
    b13 = MongoClient()
    b14 = b13.bookdb
    b15 = b14.b15
    b16 = "/Users/jamesledoux/Documents/Drew2"
    b1 = fonk1(b16)
    b17 = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode', analyzer='word')
    b18 = b17.fit_transform(b1)
    b19 = b17.get_feature_names()
    b20 = [fonk2(os.path.join(b16, book)) for book in os.listdir(b16) if not book.startswith('.')]
    b5 = fonk3(b18, b19, b20)
    fonk4(b15, b5)