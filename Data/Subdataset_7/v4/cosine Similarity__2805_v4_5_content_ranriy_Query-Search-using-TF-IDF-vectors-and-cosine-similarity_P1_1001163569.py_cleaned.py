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
for filename in os.listdir(b1):
    with open(os.path.join(b1, filename), "r", b9 = 'UTF-8') as file:
        b8.append(filename)
        b10 = file.read().lower()
        b11 = b2.tokenize(b10)
        b12 = [word for word in b11 if word not in b3]
        b13 = [b4.stem(word) for word in b12]
        b14 = nltk.FreqDist(b13)
        b15 = {term: 1 + math.log(freq, 10) for term, freq in b14.items()}
        b6.append(b15)
        for term in b14.keys():
            b5[term] = b5.get(term, 0) + 1
        a2 += 1
for term, freq in b5.items():
    b7[term] = math.log(a1 / freq, 10)
b16 = []
b17 = []
for log_freqs in b6:
    b18 = {term: freq * b7[term] for term, freq in log_freqs.items()}
    b16.append(b18)
    b19 = sum(weight ** 2 for weight in b18.values()) ** 0.5
    b17.append(b19)
b20 = []
for b18 in b16:
    b21 = {term: weight / b19 for term, weight in b18.items()}
    b20.append(b21)
b22 = {}
for doc_index, b18 in enumerate(b20):
    for term, weight in b18.items():
        b22.setdefault(term, []).extend([doc_index, weight])
def fonk1(term):
    try:
        b23 = {doc_index: weight for doc_index, weight in zip(b22[term][::2], b22[term][1::2])}
        b24 = sorted(b23, key=b23.get, reverse=True)
        return b24[:10]
    except KeyError:
        return []
def fonk2(b25):
    b25 = b25.lower()
    b11 = b2.tokenize(b25)
    b26 = [b4.stem(word) for word in b11 if word not in b3]
    b27 = nltk.FreqDist(b26)
    b28 = {term: 1 + math.log(freq, 10) for term, freq in b27.items()}
    b29 = sum(freq ** 2 for freq in b28.values()) ** 0.5
    b30 = {term: freq / b29 for term, freq in b28.items()}
    b31 = [fonk1(term) for term in b28.keys()]
    b32 = set(b31[0])
    for token in b31:
        b32.intersection_update(token)
    if not b32:
        return 'None', 0
    b33 = []
    for doc_index in b32:
        b34 = sum(b30[term] * b20[doc_index].get(term, 0) for term in b28.keys())
        b33.append(b34)
    b35 = max(b33)
    b36 = b33.a2(b35)
    b37 = b32.pop()
    return b8[b37], b35
def fonk3():
    while True:
        b25 = input("Enter your query (or 'exit' to quit): ")
        if b25.lower() == 'exit':
            break
        else:
            b38 = fonk2(b25)
            print(f"Document: {b38[0]}, Score: {b38[1]}")
if b39 = = "__main__":
    fonk3()