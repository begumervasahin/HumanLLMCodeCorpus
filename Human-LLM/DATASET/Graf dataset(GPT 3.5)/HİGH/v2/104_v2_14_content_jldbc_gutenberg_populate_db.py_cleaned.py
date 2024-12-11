from sklearn.feature_extraction.text import TfidfVectorizer
import os
from pymongo import MongoClient
b1 = MongoClient()
b2 = b1.bookdb
b3 = b2.b3
def fonk1(directory):
    b4 = []
    for book_file in os.listdir(directory):
        if not book_file.startswith('.'):
            with open(os.path.join(directory, book_file), 'rb') as f:
                b5 = f.read().decode('utf-8', errors='replace')
                b4.append(b5)
    return b4
def fonk2(b5):
    b7, b6 = None, None
    for line in b5.splitlines():
        if line.startswith("Title: "):
            b7 = line[7:].strip()
        elif line.startswith("Author: "):
            b6 = line[8:].strip()
        if b7 and b6:
            break
    return b7, b6
def fonk3(b22, b23, b24):
    b8 = {}
    for i in range(b22.shape[0]):
        b9 = b22[i].toarray()[0]
        b10 = [(index, score) for index, score in enumerate(b9) if score > 0]
        b11 = sorted(b10, key=lambda t: t[1], reverse=True)
        b12 = {}
        for index, score in b11:
            b13 = b23[index]
            b12[b13] = score
        b7, b6 = b24[i]
        b8[(b7, b6)] = b12
    return b8
def fonk4(b8):
    for info, b12 in b8.items():
        b7, b6 = info
        try:
            b14 = {"b7": b7, "b6": b6}
            b14.update(b12)
            b15 = b3.insert_one(b14).inserted_id
        except Exception as e:
            print(f"Failed to insert: {b7}, {b6}. Error: {e}")
def fonk5():
    b16 = "/path/to/b4"
    b4 = fonk1(b16)
    b17 = TfidfVectorizer(max_df=0.9,
                            b18 = (1, 1),
                            b19 = 'english',
                            b20 = 'unicode',
                            b21 = 'word')
    b22 = b17.fit_transform(b4)
    b23 = b17.get_feature_names()
    b24 = [fonk2(b5) for b5 in b4]
    b8 = fonk3(b22, b23, b24)
    fonk4(b8)
if b25 = = '__main__':
    fonk5()