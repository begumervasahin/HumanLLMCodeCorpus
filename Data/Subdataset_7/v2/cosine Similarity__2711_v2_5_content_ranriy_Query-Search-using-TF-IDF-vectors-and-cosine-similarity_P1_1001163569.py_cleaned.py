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
b3 = set(stopwords.words('english'))
b4 = PorterStemmer()
b5 = {}
b6 = []
b7 = {}
a1 = 30
a2 = 0
b8 = []
def fonk1():
    for term, frequency in b5.items():
        b7[term] = math.log(a1 / frequency, 10)
def fonk2(b11):
    b9 = {}
    for term, frequency in b6[b11].items():
        b9[term] = frequency * b7[term]
    return b9
def fonk3(b13):
    return sum(b9 ** 2 for b9 in b13.values()) ** 0.5
def fonk4(b11):
    b10 = {}
    for term, b9 in b37[b11].items():
        b10[term] = b9 / b38[b11]
    return b10
def fonk5(token):
    return b7.get(token, -1)
def fonk6(filename, token):
    b11 = b8.index(filename)
    b12 = fonk5(token)
    b13 = b6[b11]
    if token in b13:
        b14 = b13[token]
        b9 = (b14 * b12) / b38[b11]
        return b9
    else:
        return 0
def fonk7(term):
    try:
        b15 = {b11: b9 for b11, b9 in zip(b40[term][::2], b40[term][1::2])}
        b16 = sorted(b15, key=b15.get, reverse=True)
        return b16[:10]
    except KeyError:
        return []
def fonk8(b17):
    b17 = b17.lower()
    b18 = b2.tokenize(b17)
    b19 = [word for word in b18 if word not in b3]
    b20 = [b4.stem(term) for term in b19]
    b21 = {term: 1 + math.log(frequency, 10) for term, frequency in nltk.FreqDist(b20).items()}
    b22 = (sum(log_frequency ** 2 for log_frequency in b21.values())) ** 0.5
    b23 = {term: frequency / b22 for term, frequency in b21.items()}
    b24 = [fonk7(term) for term in b21.keys()]
    b25 = b24[0]
    for token in b24:
        b25 = [b11 for b11 in token if b11 in set(b25)]
    if not b25:
        return 'None', 0
    b26 = []
    for b11 in b25:
        b27 = sum(b23[term] * b39[b11].get(term, 0) for term in b21.keys())
        b26.append(b27)
    b28 = max(b26)
    b29 = b26.index(b28)
    b30 = b25[b29]
    return b8[b30], b28
for filename in os.listdir(b1):
    with open(os.path.join(b1, filename), "r", b31 = 'UTF-8') as file:
        b8.append(filename)
        b32 = file.read().lower()
        b18 = b2.tokenize(b32)
        b33 = [word for word in b18 if word not in b3]
        b34 = [b4.stem(word) for word in b33]
        b35 = nltk.FreqDist(b34)
        b36 = {term: 1 + math.log(frequency, 10) for term, frequency in b35.items()}
        b6.append(b36)
        for term in b35.keys():
            if term not in b5:
                b5[term] = 1
            else:
                b5[term] += 1
fonk1()
b37 = [fonk2(i) for i in range(a2)]
b38 = [fonk3(weights) for weights in b37]
b39 = [fonk4(i) for i in range(a2)]
b40 = {}
for b11 in range(a2):
    for term, b9 in b39[b11].items():
        b40.setdefault(term, []).extend([b11, b9])
def fonk9():
    while True:
        b17 = input("Enter your query (or 'exit' to quit): ")
        if b17.lower() == 'exit':
            break
        else:
            b41 = fonk8(b17)
            print(f"Document: {b41[0]}, Score: {b41[1]}")
if b42 = = "__main__":
    fonk9()