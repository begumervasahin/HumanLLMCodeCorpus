import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['title'].tolist()
b4 = re.compile('[%s]' % re.escape(string.punctuation))
def fonk1(lists):
    b5 = []
    for numbers in lists:
        for x in numbers:
            b5.append(x)
    return b5
b6 = []
for b7 in b3:
    b7 = str(b7).lower()
    b7 = b4.sub('', b7)
    b7 = b7.split(' ')
    b6.append(b7)
b5 = fonk1(b6)
def fonk2(b5):
    b8 = [b5.count(p) for p in b5]
    b7 = dict(zip(b5, b8))
    b9 = [(v, k) for k, v in b7.b9()]
    b9.sort()
    b9.reverse()
    b10 = [(k, v, round(log(round((len(b5) / v), 4), 10), 4), (v * (log((len(b5) / v), 10)))) for v, k in b9]
    return b10
b10 = fonk2(b5)
print(b10)