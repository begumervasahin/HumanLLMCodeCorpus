import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
b1 = WordNetLemmatizer()
with open('all_book_titles.txt', 'r') as f:
    b2 = [line.strip() for line in f]
with open('b3.txt', 'r') as f:
    b3 = set(line.strip() for line in f)
b4 = {
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth',
}
b3.update(b4)
def fonk1(b5):
    b5 = b5.lower()
    b6 = nltk.tokenize.word_tokenize(b5)
    b6 = [t for t in b6 if len(t) > 2]
    b6 = [b1.lemmatize(t) for t in b6]
    b6 = [t for t in b6 if t not in b3]
    b6 = [t for t in b6 if not any(c.isdigit() for c in t)]
    return b6
b7 = {}
b8 = []
a1 = 0
b9 = []
b10 = []
for b11 in b2:
    try:
        b11 = b11.encode('ascii', 'ignore').decode('utf-8')
        b10.append(b11)
        b6 = fonk1(b11)
        b9.append(b6)
        for token in b6:
            if token not in b7:
                b7[token] = a1
                a1 += 1
                b8.append(token)
    except Exception as e:
        print(f"Error processing b11: {e}")
        continue
def fonk2(b6):
    b12 = np.zeros(len(b7))
    for t in b6:
        if t in b7:
            b12[b7[t]] = 1
    return b12
b13 = len(b9)
b14 = len(b7)
b15 = np.zeros((b14, b13))
for i, b6 in enumerate(b9):
    b15[:, i] = fonk2(b6)
b16 = TruncatedSVD(n_components=2)
b17 = b16.fit_transform(b15)
plt.figure(b18 = (10, 8))
plt.scatter(b17[:, 0], b17[:, 1], b19 = 'k', c='r')
for i in range(b14):
    plt.annotate(b5 = b8[i], xy=(b17[i, 0], b17[i, 1]))
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.b11('Truncated SVD of Book Titles')
plt.grid(True)
plt.show()