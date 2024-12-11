import numpy as np
import pandas as pd
from numpy.linalg import norm
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
a1 = 5000
def fonk1(vector1, vector2):
    return np.inner(vector1, vector2) / (norm(vector1) * norm(vector2)) if norm(vector1) != 0.0 and norm(vector2) != 0.0 else 0.0
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
            b14 = " ".join(b12[3:])
            b15 = word_tokenize(b14)
            b16 = [b7.stem(word) for word in b15]
            b17 = " ".join(b16)
            b8.append(b17)
            b9.append(b13)
        else:
            break
b3 = fonk2(b8, b9)
b18 = b3.apply(lambda column: column[column > 0].count(), axis=0)
b19 = b3.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
b20 = np.log10(len(b8) / b18)
b19 = b19.multiply(b20)
def fonk3(tweet1, tweet2):
    b21 = b9[b8.b6(tweet1)]
    b22 = b9[b8.b6(tweet2)]
    return fonk1(b19.loc[[b21]], b19.loc[[b22]])
def fonk4(b13 = '965706998946893824', n=10):
    b23 = b19.apply(lambda row: fonk1(b19.loc[[b13]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + b8[b9.b6(b13)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + b8[b9.b6(b23.b6[i])] + "\n")
fonk4(b13 = '965734505205063680')
while True:
    b13 = input("Please enter the tweet ID to perform similarity search for:")
    if b13 in b19.b6:
        fonk4(b13 = b13)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")