import nltk.corpus
import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['title'].tolist()
print(type(b3))
print(len(b3))
b4 = re.compile('[%s]' % re.escape(string.punctuation))
b5 = []
for b6 in b3:
    b6 = str(b6).lower()
    b6 = b4.sub('', b6)
    b5.append(b6.split())
def fonk1(lists):
    return [word for sublist in lists for word in sublist]
b7 = fonk1(b5)
print(len(b7))
def fonk2(b7):
    b8 = {word: b7.count(word) for word in b7}
    b9 = sorted(b8.items(), key=lambda item: item[1], reverse=True)
    b10 = [
        (word, freq, round(log(len(b7) / freq, 10), 4), freq * log(len(b7) / freq, 10))
        for word, freq in b9
    ]
    return b10
b11 = fonk2(b7)
print(b11)