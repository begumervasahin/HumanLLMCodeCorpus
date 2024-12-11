import nltk
import math
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from math import log10, sqrt
from collections import Counter
nltk.download('stopwords')
b1 = PorterStemmer()
b2 = RegexpTokenizer(r'[a-zA-Z]+')
b3 = './presidential_debates'
b4 = {}
b5 = Counter()
b6 = {}
b7 = Counter()
b8 = {}
def fonk1(filename, b21):
    b9 = fonk2(b21)
    return (1 + log10(b6[filename][b21])) * b9
def fonk2(b21):
    if b5[b21] == 0:
        return -1
    return log10(len(b6) / b5[b21])
for filename in os.listdir(b3):
    with open(os.path.join(b3, filename), "r", b10 = 'UTF-8') as file:
        b11 = file.read().lower()
        b12 = b2.tokenize(b11)
        b13 = set(stopwords.words('english'))
        b12 = [b1.stem(b21) for b21 in b12 if b21 not in b13]
        b14 = Counter(b12)
        b5 += Counter(list(set(b12)))
        b6[filename] = b14.copy()
        b14.clear()
for filename in b6:
    b4[filename] = Counter()
    a1 = 0
    for b21 in b6[filename]:
        b15 = fonk1(filename, b21)
        b4[filename][b21] = b15
        a1 += b15 ** 2
    b7[filename] = math.sqrt(a1)
for filename in b4:
    for b21 in b4[filename]:
        b4[filename][b21] = b4[filename][b21] / b7[filename]
        if b21 not in b8:
            b8[b21] = Counter()
        b8[b21][filename] = b4[filename][b21]
def fonk3(filename, b21):
    return b4[filename][b21]
def fonk4(b16):
    b16 = b16.lower()
    b17 = {}
    a2 = 0
    a3 = 0
    b18 = {}
    b19 = {}
    b20 = Counter()
    for b21 in b16.split():
        b21 = b1.stem(b21)
        if b21 not in b8:
            continue
        if fonk2(b21) == 0:
            b18[b21], b22 = zip(*b8[b21].most_common())
        else:
            b18[b21], b22 = zip(*b8[b21].most_common(10))
        b19[b21] = b22[9]
        if a3 = = 1:
            b23 = set(b18[b21]) & b23
        else:
            b23 = set(b18[b21])
            a3 = 1
        b17[b21] = 1 + log10(b16.count(b21))
        a2 += b17[b21] ** 2
    a2 = sqrt(a2)
    for b11 in b4:
        a4 = 0
        for b21 in b17:
            if b11 in b18[b21]:
                a4 += (b17[b21] / a2) * b8[b21][b11]
            else:
                a4 += (b17[b21] / a2) * b19[b21]
        b20[b11] = a4
    b24 = b20.most_common(1)
    ans, b25 = zip(*b24)
    try:
        if ans[0] in b23:
            return ans[0], b25[0]
        else:
            return "fetch more", 0
    except UnboundLocalError:
        return "None", 0
print("(%s, %.12f)" % fonk4("health insurance wall street"))
print("(%s, %.12f)" % fonk4("security conference ambassador"))
print("(%s, %.12f)" % fonk4("particular constitutional amendment"))
print("(%s, %.12f)" % fonk4("terror attack"))
print("(%s, %.12f)" % fonk4("vector entropy"))