import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['b7'].tolist()
b4 = re.compile('[%s]' % re.escape(string.punctuation))
def fonk1(nested_lists):
    b5 = []
    for sublist in nested_lists:
        for item in sublist:
            b5.append(item)
    return b5
b6 = []
for b7 in b3:
    b7 = str(b7).lower()
    b7 = b4.sub('', b7)
    b8 = b7.split(' ')
    b6.append(b8)
b9 = fonk1(b6)
def fonk2(words):
    b10 = [words.count(word) for word in words]
    b11 = dict(zip(words, b10))
    b12 = [(freq, word) for word, freq in b11.items()]
    b12.sort(b13 = True)
    b14 = [(word, freq, round(log(round((len(words) / freq), 4), 10), 4), freq * log(len(words) / freq, 10)) for freq, word in b12]
    return b14
b15 = fonk2(b9)
print(b15)