import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
def fonk1(token, b24):
    if any(char.isupper() for char in token):
        return -1.0
    if token in b24:
        return b24[token]
    else:
        return -1.0
def fonk2(b27, b15, b20, b24):
    b1 = RegexpTokenizer(r'[a-zA-Z]+')
    b2 = b1.tokenize(b27.lower())
    b3 = [token for token in b2 if token not in b15]
    b4 = [b20.stem(token) for token in b3]
    b5 = Counter(b4)
    b6 = {}
    for token, freq in b5.items():
        b7 = fonk1(token, b24)
        if b7 != -1.0:
            b8 = 1 + math.log(freq, 10)
            b6[token] = b8 * b7
    b9 = sum(b6[token] ** 2 for token in b6)
    b10 = {token: value / math.sqrt(b9) for token, value in b6.items()}
    return b10
def fonk3(b27, b25, b19):
    b6 = fonk2(b27, b15, b20, b24)
    b11 = {}
    for b21, weights in b25.items():
        b12 = sum(b6[token] * weights.get(token, 0) for token in b6)
        b11[b21] = b12
    b13 = max(b11.values())
    b14 = max(b11, key=b11.get)
    if b13 = = 0:
        return "NO MATCH\n", b13
    else:
        return b19[b14], b13
nltk.download('stopwords')
b15 = set(stopwords.words('english'))
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
        b3 = [token for token in b2 if token not in b15]
        b4 = [b20.stem(token) for token in b3]
        b21 = f"para {len(b19) + 1}"
        b19[b21] = b4
b22 = {b21: Counter(b2) for b21, b2 in b19.items()}
b23 = len(b19)
b24 = {token: math.log(b23 / sum(1 for b2 in b19.values() if token in b2), 10) for b2 in set(token for b2 in b19.values() for token in b2)}
b25 = {b21: {token: b22[b21][token] * b24[token] for token in b22[b21]} for b21 in b19}
for b21 in b25:
    b26 = math.sqrt(sum(weight ** 2 for weight in b25[b21].values()))
    b25[b21] = {token: weight / b26 for token, weight in b25[b21].items()}
b27 = "What are the benefits of renewable energy?"
result, b28 = fonk3(b27, b25, b19)
print("Most similar paragraph:")
print(result)
print("Similarity score:", b28)