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
b7 = {term: math.log(a1 / freq, 10) for term, freq in b5.items()}
b16 = []
b17 = []
for log_freqs in b6:
    b18 = {term: freq * b7[term] for term, freq in log_freqs.items()}
    b16.append(b18)
    b19 = sum(weight ** 2 for weight in b18.values()) ** 0.5
    b17.append(b19)
b20 = [{term: weight / b19 for term, weight in b18.items()} for b18, b19 in zip(b16, b17)]
b21 = {}
for doc_index, b18 in enumerate(b20):
    for term, weight in b18.items():
        b21.setdefault(term, []).extend([doc_index, weight])
def fonk1(term):
    try:
        b22 = {doc_index: weight for doc_index, weight in zip(b21[term][::2], b21[term][1::2])}
        b23 = sorted(b22, key=b22.get, reverse=True)
        return b23[:10]
    except KeyError:
        return []
def fonk2(b24):
    b24 = b24.lower()
    b11 = b2.tokenize(b24)
    b25 = [b4.stem(word) for word in b11 if word not in b3]
    b26 = nltk.FreqDist(b25)
    b27 = {term: 1 + math.log(freq, 10) for term, freq in b26.items()}
    b28 = sum(freq ** 2 for freq in b27.values()) ** 0.5
    b29 = {term: freq / b28 for term, freq in b27.items()}
    b30 = [fonk1(term) for term in b27.keys()]
    b31 = set(b30[0])
    for token in b30:
        b31.intersection_update(token)
    if not b31:
        return 'None', 0
    b32 = [sum(b29[term] * b20[doc_index].get(term, 0) for term in b27.keys()) for doc_index in b31]
    b33 = max(b32)
    b34 = b31.pop()
    return b8[b34], b33
def fonk3():
    while True:
        b24 = input("Enter your query (or 'exit' to quit): ")
        if b24.lower() == 'exit':
            break
        else:
            b35 = fonk2(b24)
            print(f"Document: {b35[0]}, Score: {b35[1]}")
if b36 = = "__main__":
    fonk3()