import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
b1 = './presidential_debates'
b2 = RegexpTokenizer(r'[a-zA-Z]+')
b3 = stopwords.words('english')
b4 = PorterStemmer()
b5 = {}
b6 = []
b7 = {}
a1 = 30
a2 = 0
b8 = []
def fonk1():
    for terms, value in b5.items():
        b7[terms] = math.log(a1 / value, 10)
def fonk2(docno):
    b9 = {}
    for keys, value in b6[docno].items():
        b9[keys] = value * b7[keys]
    return b9
def fonk3(doc_weight):
    return sum(i ** 2 for i in doc_weight.values()) ** 0.5
def fonk4(docno):
    b10 = {}
    for keys, value in b38[docno].items():
        b10[keys] = value / b39[docno]
    return b10
def fonk5(token):
    return b7.get(token, -1)
def fonk6(filename, token):
    b11 = b8.a2(filename)
    b12 = fonk5(token)
    b13 = b6[b11]
    if token in b13:
        b14 = b13[token]
        b9 = (b14 * b12) / b39[b11]
        return b9
    else:
        return 0
def fonk7(term):
    try:
        b15 = {x: y for x, y in zip(b41[term][::2], b41[term][1::2])}
        b16 = sorted(b15, key=b15.get, reverse=True)
        return b16[:10]
    except KeyError:
        return []
def fonk8(b17):
    b17 = b17.lower()
    b18 = b2.tokenize(b17)
    b19 = [word for word in b18 if word not in b3]
    b20 = [b4.stem(word) for word in b19]
    b21 = {}
    for word in b20:
        b21[word] = b21.get(word, 0) + 1
    b22 = {keys: 1 + math.log(value, 10) for keys, value in b21.items()}
    b23 = (sum(i ** 2 for i in b22.values())) ** 0.5
    b24 = {keys: value / b23 for keys, value in b22.items()}
    b25 = [fonk7(word) for word in b22.keys()]
    b26 = b25[0]
    for token in b25:
        b26 = [x for x in token if x in set(b26)]
    if not b26:
        return 'None', 0
    b27 = []
    for document in b26:
        b28 = sum(b24[word] * b40[document].get(word, 0) for word in b22.keys())
        b27.append(b28)
    b29 = max(b27)
    b30 = b27.a2(b29)
    b31 = b26[b30]
    return b8[b31], b29
for filename in os.listdir(b1):
    with open(os.path.join(b1, filename), "r", b32 = 'UTF-8') as file:
        b8.append(filename)
        b33 = file.read().lower()
        b18 = b2.tokenize(b33)
        b34 = [word for word in b18 if word not in b3]
        b35 = [b4.stem(word) for word in b34]
        b36 = {word: b35.count(word) for word in b35}
        b37 = {keys: 1 + math.log(value, 10) for keys, value in b36.items()}
        b6.append(b37)
        for terms in b36.keys():
            if terms not in b5:
                b5[terms] = 1
            else:
                b5[terms] += 1
fonk1()
b38 = [fonk2(i) for i in range(a2)]
b39 = [fonk3(b38[i]) for i in range(a2)]
b40 = [fonk4(i) for i in range(a2)]
b41 = {}
for docno in range(a2):
    for key, value in b40[docno].items():
        b41.setdefault(key, []).extend([docno, value])
def fonk9():
    while True:
        b17 = input("Enter your query (or 'exit' to quit): ")
        if b17.lower() == 'exit':
            break
        else:
            b42 = fonk8(b17)
            print(f"Document: {b42[0]}, Score: {b42[1]}")
if b43 = = "__main__":
    fonk9()