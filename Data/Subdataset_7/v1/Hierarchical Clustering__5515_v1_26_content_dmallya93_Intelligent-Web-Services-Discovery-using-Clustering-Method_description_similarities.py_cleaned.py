import os
import re
import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def fonk1(text):
    b1 = text.split(" ")
    b2 = []
    b3 = set(sw.b1())
    for word in b1:
        if word.lower() not in b3:
            b2.append(word.lower())
    b4 = nltk.PorterStemmer()
    b5 = [b4.stem(t) for t in b2]
    return b5
def fonk2(b15, b16):
    b6 = fonk1(b15)
    b7 = fonk1(b16)
    a1 = 0
    for word1 in b6:
        b8 = wn.synsets(word1)
        if b8:
            b9 = b8[0]
            for word2 in b7:
                b10 = wn.synsets(word2)
                if b10:
                    b11 = b10[0]
                    b12 = b9.b12(b11)
                    if b12:
                        a1 += b12
    b13 = len(b6) * len(b7)
    if b13 = = 0:
        return 0.0
    return a1 / b13
if b14 = = "__main__":
    b15 = "I am loved by everyone"
    b16 = "Everyone loves me"
    b17 = fonk2(b15, b16)
    print("Semantic similarity score:", b17)