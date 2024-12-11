import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
def fonk1(b2):
    if any(x.isupper() for x in b2):
        return -1.0000
    if b2 in b24:
        return b24[b2]
    else:
        return -1.0000
def fonk2(qstring):
    b1 = []
    b2 = RegexpTokenizer(r'[a-zA-Z]+')
    b1 = b2.tokenize(qstring.lower())
    b3 = set(stopwords.words('english'))
    b4 = [wor for wor in b1 if wor not in b3]
    b5 = [Qstemmer.stem(s) for s in b4]
    b6 = {wor: 1 + math.log(b5.count(wor), 10) for wor in b5}
    b7 = len(b22)
    b8 = {}
    for wor, a1 in b6.items():
        a1 = 0
        for para, t in b23.items():
            if wor in b23[para].keys():
                a1 += 1
        b8[wor] = math.log(b7 / a1, 10) if a1 > 0 else 0
    b9 = {lett: b6[lett] * b8[lett] for lett in b5}
    b10 = sum(b9[lett] ** 2 for lett in b9)
    b11 = {lett: b9[lett] / math.sqrt(b10) for lett in b9}
    return b11
def fonk3(b27):
    b9 = fonk2(b27)
    b12 = {}
    for para in b25.keys():
        b13 = sum(b9[key] * b25[para].get(key, 0) for key in b9)
        b12[para] = b13
    b14 = max(b12.values())
    b15 = max(b12, key=b12.get)
    if b14 = = 0:
        return "NO MATCH\n", b14
    else:
        return b19[b15], b14
b3 = set(stopwords.words('english'))
b16 = './debate.txt'
b17 = open(b16, "r", encoding='UTF-8')
b18 = b17.readlines()
b17.close()
b19 = {}
b2 = RegexpTokenizer(r'[a-zA-Z]+')
for k in b18:
    if not k.isspace():
        b20 = b2.tokenize(k.lower())
        b21 = [b2 for b2 in b20 if b2 not in b3]
        b22 = [PorterStemmer().stem(key) for key in b21]
        b19["para " + str(len(b19) + 1)] = b22
b23 = {para: Counter(data) for para, data in b19.items()}
b7 = len(b19)
b24 = {b2: math.log(b7 / sum(1 for data in b19.values() if b2 in data), 10) for b2 in set(b2 for data in b19.values() for b2 in data)}
b25 = {para: {b2: b23[para][b2] * b24[b2] for b2 in b23[para]} for para in b19}
for para in b25:
    b26 = math.sqrt(sum(weight ** 2 for weight in b25[para].values()))
    b25[para] = {b2: weight / b26 for b2, weight in b25[para].items()}
b27 = "What are the benefits of renewable energy?"
result, b28 = fonk3(b27)
print("Most similar paragraph:")
print(result)
print("Similarity score:", b28)