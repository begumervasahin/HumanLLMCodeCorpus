import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
b1 = './presidential_debates'
b2 = RegexpTokenizer(r'[a-zA-Z]+')
b3 = stopwords.words('english')
b4 = PorterStemmer()
b5 = {}
b6 = []
b7 = {}
b8 = {}
a1 = 30
b9 = []
a2 = 0
b10 = []
for filename in os.listdir(b1):
    b11 = open(os.path.join(b1, filename), "r", encoding='UTF-8')
    b10.append(filename)
    b12 = b11.read()
    b11.close()
    b12 = b12.lower()
    b13 = b2.tokenize(b12)
    b14 = [word for word in b13 if word not in b3]
    b15 = []
    for a5 in b14:
        b16 = b4.stem(a5)
        b15.append(b16)
    b17 = {}
    for a5 in b15:
        if a5 in b17:
            b17[a5] = b17[a5]+1
        elif a5 not in b17:
            b17[a5] = 1
    b18 = {}
    for keys, value in b17.items():
        b18[keys] = 1+math.log(value,10)
    b6.append(b27(b18))
    for terms in b17.keys():
        if terms not in b5:
            b5[terms] =1
        else :
            b5[terms] = b5[terms]+1
    for keys,value in b5.items():
        b7[keys]= math.log(a1/value,10)
    a2 = a2 +1
b19 = []
a3 = 0
while(a3<a2):
    b20 = {}
    for keys,value in b6[a3].items():
        b20[keys] = value * b7[keys]
    b19.append(b27(b20))
    a3 = a3+1
b21 = []
a3 = 0
while(a3<a2):
    b22 = sum(a5**2 for a5 in b19[a3].values())
    b21.append(b22**0.5)
    a3 = a3 + 1
b23 = []
a3 = 0
while(a3<a2):
    b24 = {}
    for keys,value in b19[a3].items():
            b24[keys] = value/b21[a3]
    b23.append(b27(b24))
    a3 = a3 +1
def fonk1(token):
    if token in b7.keys():
        return b7[token]
    else:
        return -1
def fonk2(filemae,token):
    b25 = b10.a2(filemae)
    b26 = fonk1(token)
    b27 = b6[b25]
    if token in b27.keys():
        b28 = b27[token]
        b20 = (b28*b26)/b21[b25]
        return b20
    else:
        return 0
b29 = {}
a4 = 0
b30 = {}
while(a4 <a2):
    for key,value in b23[a4].items():
        b29.setdefault(key, []).append(a4)
        b29.setdefault(key, []).append(value)
    a4 = a4 +1
def fonk3(term):
    b31 = []
    try:
        b22 = b29[term]
        b32 = { x : y for x, y in zip(b29[term][::2], b29[term][1::2]) }
        b31 = sorted(b32, key=b32.get, reverse=True)
        return(b31[:10])
    except:
        return(b31)
def fonk4(b34):
    b33 = ()
    b34 = b34.lower()
    b13 = b2.tokenize(b34)
    b35 = [word for word in b13 if word not in b3]
    b36 = []
    for a5 in b35:
        b16 = b4.stem(a5)
        b36.append(b16)
    b37 = {}
    for a5 in b36:
        if a5 in b37:
            b37[a5] = b37[a5]+1
        elif a5 not in b37:
            b37[a5] = 1
    b38 = {}
    for keys, value in b37.items():
        b38[keys] = 1+math.log(value,10)
    b39 = (sum(a5**2 for a5 in b38.values()))**0.5
    b40 = {}
    for keys,value in b38.items():
        b40[keys] = value/b39
    b41 = []
    for keys,values in b38.items():
        b42 = fonk3(keys)
        b41.append(b42)
    b12 = b41[0]
    for a5 in b41:
        b12 = intersection = [x for x in a5 if x in set(b12)]
    if(not intersection):
        return('None',0)
    else:
        b43 = []
        a5 = 0
        while(a5<len(intersection)):
            a6 = 0
            for keys,values in b38.items():
                b44 = intersection[a5]
                a6 = a6 + (b40[keys] * b23[b44][keys])
            b43.append(a6)
            a5 = a5+1
        a6 = max(b43)
        b45 = intersection[b43.a2(a6)]
        b33 = (b10[b45],a6)
        b46 = []
        for q in b41:
            b47 = list(set(q)-set(intersection))
            b46.append(b47)
        return(b33)