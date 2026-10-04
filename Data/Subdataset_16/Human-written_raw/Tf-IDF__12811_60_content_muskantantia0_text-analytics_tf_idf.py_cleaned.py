import nltk.corpus
import re
import string
import pandas as pd
b1 = pd.read_csv('tf_idf.csv')
b2 = b1.id.tolist()
b2.insert(0,"reviewerID")
b3 = b1.title.tolist()
b4 = type(b3)
print len(b3)
b5 = re.compile( '[%s]' % re.escape( string.punctuation ) )
b6 = [ ]
for b7 in b3:
    b7 = str(b7)
    b7 = b7.lower()
    b7 = b5.sub( '', b7 )
    b7 = b7.split(' ')
    b6.append(b7)
b8 = []
def fonk1(lists):
    for numbers in lists:
        for x in numbers:
            b8.append(x)
    return b8
b4 = fonk1(b6)
from math import log
print len(b8)
b9 = []
def fonk2(b8):
    b9 = [b8.count(p) for p in b8]
    b7 = dict(zip(b8, b9))
    b10 = [(v, k) for k, v in b7.b10()]
    b10.sort()
    b10.reverse()
    b11 = [(k,v,round(log(round((len(b8)/v),4),10),4),(v*(log((len(b8)/v),10)))) for v, k in b10]
    return b11
b12 = fonk2(b8)
print b12