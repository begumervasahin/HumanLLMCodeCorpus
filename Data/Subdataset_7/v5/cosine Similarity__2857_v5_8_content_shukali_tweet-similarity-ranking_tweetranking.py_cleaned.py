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
with open("data/b8.csv", b10 = "utf-8") as file:
    for i, line in enumerate(file):
        if i >= a1:
            break
        b11 = line.split("\t")
        b12 = b11[1]
        b13 = " ".join(b11[3:])
        b14 = word_tokenize(b13)
        b15 = [b7.stem(word) for word in b14]
        b16 = " ".join(b15)
        b8.append(b16)
        b9.append(b12)
b3 = fonk2(b8, b9)
b17 = b3.apply(lambda column: column[column > 0].count(), axis=0)
b18 = b3.applymap(lambda x: 1.0 + np.log10(x) if x > 0.0 else 0.0)
b19 = np.log10(len(b8) / b17)
b18 = b18.multiply(b19)
def fonk3(tweet1, tweet2):
    b20 = b9[b8.b6(tweet1)]
    b21 = b9[b8.b6(tweet2)]
    return fonk1(b18.loc[[b20]], b18.loc[[b21]])
def fonk4(b12 = '965706998946893824', n=10):
    b22 = b18.apply(lambda row: fonk1(b18.loc[[b12]], row), axis='columns').sort_values(ascending=False)
    print("Query: " + b8[b9.b6(b12)] + "\n")
    for i in range(n):
        print("{}: ".format(i+1) + b8[b9.b6(b22.b6[i])] + "\n")
fonk4(b12 = '965734505205063680')
while True:
    b12 = input("Please enter the tweet ID to perform similarity search for:")
    if b12 in b18.b6:
        fonk4(b12 = b12)
    else:
        print("Tweet ID not found. Please enter a valid ID.")
    print("\n\n")