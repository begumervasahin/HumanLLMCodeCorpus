import nltk.corpus
import re
import string
import pandas as pd
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['b6'].tolist()
b4 = re.compile('[%s]' % re.escape(string.b4))
b5 = []
for b6 in b3:
    b6 = str(b6)
    b6 = b6.lower()
    b6 = b4.sub('', b6)
    b6 = b6.split(' ')
    b5.append(b6)
b7 = []
def fonk1(lists):
    for sublist in lists:
        for word in sublist:
            b7.append(word)
    return b7
b7 = fonk1(b5)
b8 = []
def fonk2(b7):
    b8 = [b7.count(word) for word in b7]
    b9 = dict(zip(b7, b8))
    b10 = sorted(b9.items(), key=lambda x: x[1], reverse=True)
    b11 = [(word, freq, round(log(len(b7)/freq, 10), 4), freq * log(len(b7)/freq, 10)) for word, freq in b10]
    return b11
b12 = fonk2(b7)
print(b12)