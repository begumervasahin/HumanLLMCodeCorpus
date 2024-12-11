import nltk,math
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from math import log10,sqrt
from collections import Counter
b1 = PorterStemmer()
b2 = RegexpTokenizer(r'[a-zA-Z]+')
import os
b3 = './presidential_debates'
b4 = {}
b5 = Counter()
b6 = {}
b7 = Counter()
b8 = {}
b9 = []
for filename in os.listdir(b3):
    b10 = open(os.path.join(b3, filename), "r", encoding='UTF-8')
    b11 = b10.read()
    b10.close()
    b11 = b11.lower()
    b12 = b2.tokenize(b11)
    b13 = stopwords.words('english')
    b12 = [b1.stem(b22) for b22 in b12 if b22 not in b13]
    b14 = Counter(b12)
    b5+=Counter(list(set(b12)))
    b6[filename]=b14.copy()
    b14.clear()
def fonk1(filename, b22):
    b15 = fonk2(b22)
    return (1+log10(b6[filename][b22]))*b15
def fonk2(b22):
    if b5[b22]==0:
        return -1
    return log10(len(b6)/b5[b22])
for filename in b6:
    b4[filename]=Counter()
    a1 = 0
    for b22 in b6[filename]:
        b16 = fonk1(filename, b22)
        b4[filename][b22]=b16
        a1 += b16**2
    b7[filename]=math.sqrt(a1)
for filename in b4:
    for b22 in b4[filename]:
        b4[filename][b22]= b4[filename][b22] / b7[filename]
        if b22 not in b8:
            b8[b22]=Counter()
        b8[b22][filename]=b4[filename][b22]
def fonk3(filename,b22):
    return b4[filename][b22]
def fonk4(b17):
    b17 = b17.lower()
    b18 = {}
    a2 = 0
    a3 = 0
    b19 = {}
    b20 = {}
    b21 = Counter()
    for b22 in b17.split():
        b22 = b1.stem(b22)
        if b22 not in b8:
            continue
        if fonk2(b22)==0:
            b19[b22], b23 = zip(*b8[b22].most_common())
        else:
            b19[b22],b23 = zip(*b8[b22].most_common(10))
        b20[b22]=b23[9]
        if a3 = =1:
            b24 = set(b19[b22]) & b24
        else:
            b24 = set(b19[b22])
            a3 = 1
        b18[b22]=1+log10(b17.count(b22))
        a2+=b18[b22]**2
    a2 = sqrt(a2)
    for b11 in b4:
        a4 = 0
        for b22 in b18:
            if b11 in b19[b22]:
                a4 = a4 + (b18[b22] / a2) * b8[b22][b11]
            else:
                a4 = a4 + (b18[b22] / a2) * b20[b22]
        b21[b11]=a4
    b25 = b21.most_common(1)
    ans,b26 = zip(*b25)
    try:
        if ans[0] in b24:
            return ans[0],b26[0]
        else:
            return "fetch more",0
    except UnboundLocalError:
        return "None",0
print("(%s, %.12f)" % fonk4("health insurance wall street"))
print("(%s, %.12f)" % fonk4("security conference ambassador"))
print("(%s, %.12f)" % fonk4("particular constitutional amendment"))
print("(%s, %.12f)" % fonk4("terror attack"))
print("(%s, %.12f)" % fonk4("vector entropy"))