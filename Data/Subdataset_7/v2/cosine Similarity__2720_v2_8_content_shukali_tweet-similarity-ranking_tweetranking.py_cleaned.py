import numpy as np
import pandas as pd
from numpy.linalg import norm
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
a1 = 5000
def fonk1(a, b):
    return np.inner(a, b) / (norm(a) * norm(b)) if norm(a) != 0.0 and norm(b) != 0.0 else 0.0
def fonk2(docs, b1 = None):
    b2 = CountVectorizer(lowercase=True, stop_words=None)
    b3 = b2.fit_transform(docs)
    b4 = b2.get_feature_names()
    b5 = pd.DataFrame(b3.toarray(), columns=b4, dtype="float64")
    if b1 is not None:
        b5.b6 = b1
    return b5
b7 = PorterStemmer()
b8 = []
b9 = []
b10 = []
with open("data/b8.csv", b11 = "utf-8") as file:
    for i, line in enumerate(file):
        if i < a1:
            b12 = line.split("\t")
            b13 = b12[1]
            b14 = b12[3:]
            b9.append(b13)
            b15 = " ".join(b14)
            b16 = word_tokenize(b15)
            b17 = [b7.stem(word) for word in b16]
            b18 = " ".join(b17)
            b8.append(b18)
        else:
            break
b19 = fonk2(b8, b9)
b20 = b19.apply(lambda column: len(column[column > 0]), axis=0)
b21 = b19.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
b22 = np.log10(len(b8) / b20)
b21 = b21.multiply(b22)
def fonk3(tweet1, tweet2):
    b23 = b9[b8.b6(tweet1)]
    b24 = b9[b8.b6(tweet2)]
    return fonk1(b21.loc[[b23]], b21.loc[[b24]])
def fonk4(b13 = '965706998946893824', n=10):
    b25 = b21.apply(lambda row: fonk1(b21.loc[[b13]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + b8[b9.b6(b13)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + b8[b9.b6(b25.b6[i])] + "\n")
fonk4(b13 = '965734505205063680')
while True:
    b26 = input("Please enter the b14 ID to perform similarity search for:")
    if b26 in b21.b6:
        fonk4(b13 = b26)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")