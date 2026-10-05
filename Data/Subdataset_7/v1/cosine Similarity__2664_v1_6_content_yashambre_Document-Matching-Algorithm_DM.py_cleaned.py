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
    if b2 in b25:
        return b25[b2]
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
    b7 = len(b23)
    b8 = {}
    for wor, a1 in b6.items():
        a1 = 0
        for para, t in b24.items():
            if wor in b24[para].keys():
                a1 += 1
        b8[wor] = math.log(b7 / a1, 10) if a1 > 0 else 0
    b9 = {lett: b6[lett] * b8[lett] for lett in b5}
    b10 = sum(b9[lett] ** 2 for lett in b9)
    b11 = {lett: b9[lett] / math.sqrt(b10) for lett in b9}
    return b11
def fonk3(b29):
    b9 = fonk2(b29)
    b12 = {}
    for para in b27.keys():
        b13 = sum(b9[key] * b27[para].get(key, 0) for key in b9)
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
a2 = 1
for k in b18:
    if not k.isspace():
        b19["para " + str(a2)] = k
        a2 += 1
b20 = []
b2 = RegexpTokenizer(r'[a-zA-Z]+')
for k in b18:
    if not k.isspace():
        b21 = b2.tokenize(k.lower())
        b20.append(b21)
b22 = [[b2 for b2 in wor if b2 not in b3] for wor in b20]
b23 = [[PorterStemmer().stem(key) for key in s] for s in b22]
b24 = {"para " + str(a2): {wor: lett.count(wor) for wor in lett} for a2, lett in enumerate(b23, start=1)}
b7 = len(b23)
b25 = {}
for tfDict in b24.values():
    for b2 in tfDict:
        b26 = sum(1 for value in b24.values() if b2 in value)
        if b2 not in b25:
            b25[b2] = math.log(b7 / b26, 10)
b27 = {"para " + str(a2): {lor: b24[lett][lor] * b25[lor] for lor in b24[lett]} for a2, (lett, tf) in enumerate(b24.items(), start=1)}
for document in b27:
    b28 = sum(weight ** 2 for weight in b27[document].values())
    b27[document] = {b2: weight / math.sqrt(b28) for b2, weight in b27[document].items()}
b29 = "What are the benefits of renewable energy?"
result, b30 = fonk3(b29)
print("Most similar paragraph:")
print(result)
print("Similarity score:", b30)