import os
import math
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
def fonk1(token):
    if any(char.isupper() for char in token):
        return -1.0000
    if token in b23:
        return b23[token]
    else:
        return -1.0000
def fonk2(b25):
    b1 = RegexpTokenizer(r'[a-zA-Z]+')
    b2 = b1.tokenize(b25.lower())
    b3 = set(stopwords.words('english'))
    b4 = [token for token in b2 if token not in b3]
    b5 = [b20.stem(token) for token in b4]
    b6 = Counter(b5)
    b7 = {}
    for token, freq in b6.items():
        b8 = fonk1(token)
        if b8 != -1.0:
            b9 = 1 + math.log(freq, 10)
            b7[token] = b9 * b8
    b10 = math.sqrt(sum(value ** 2 for value in b7.values()))
    b11 = {token: value / b10 for token, value in b7.items()}
    return b11
def fonk3(b25):
    b7 = fonk2(b25)
    b12 = {}
    for b21, weights in b24.items():
        b13 = sum(b7[token] * weights.get(token, 0) for token in b7)
        b12[b21] = b13
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
b1 = RegexpTokenizer(r'[a-zA-Z]+')
b20 = PorterStemmer()
for line in b18:
    if not line.isspace():
        b2 = b1.tokenize(line.lower())
        b4 = [token for token in b2 if token not in b3]
        b5 = [b20.stem(token) for token in b4]
        b21 = f"para {len(b19) + 1}"
        b19[b21] = b5
b22 = {b21: Counter(b2) for b21, b2 in b19.items()}
b23 = {token: math.log(len(b19) / sum(1 for b2 in b19.values() if token in b2), 10) for b2 in set(token for b2 in b19.values() for token in b2)}
b24 = {b21: {token: b22[b21][token] * b23[token] for token in b22[b21]} for b21 in b19}
for b21 in b24:
    b10 = math.sqrt(sum(weight ** 2 for weight in b24[b21].values()))
    b24[b21] = {token: weight / b10 for token, weight in b24[b21].items()}
b25 = "What are the benefits of renewable energy?"
result, b26 = fonk3(b25)
print("Most similar paragraph:")
print(result)
print("Similarity score:", b26)