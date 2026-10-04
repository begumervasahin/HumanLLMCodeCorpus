import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
b1 = WordNetLemmatizer()
with open('all_book_titles.txt', 'r') as f:
    b2 = [line.rstrip() for line in f]
with open('b3.txt', 'r') as f:
    b3 = set(w.rstrip() for w in f)
b4 = {
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth',
}
b3 = b3.union(b4)
def fonk1(b5):
    b5 = b5.lower()
    b6 = nltk.tokenize.word_tokenize(b5)
    b6 = [t for t in b6 if len(t) > 2]
    b6 = [b1.lemmatize(t) for t in b6]
    b6 = [t for t in b6 if t not in b3]
    b6 = [t for t in b6 if not any(c.isdigit() for c in t)]
    return b6
b7 = {}
a1 = 0
b8 = []
b9 = []
b10 = []
for b11 in b2:
    try:
        b11 = b11.encode('ascii', 'ignore').decode('utf-8')
        b9.append(b11)
        b6 = fonk1(b11)
        b8.append(b6)
        for token in b6:
            if token not in b7:
                b7[token] = a1
                a1 += 1
                b10.append(token)
    except Exception as e:
        print(f"Error processing b11: {b11} - {e}")
def fonk2(b6):
    b12 = np.zeros(len(b7))
    for t in b6:
        if t in b7:
            b13 = b7[t]
            b12[b13] = 1
    return b12
b14 = len(b8)
b15 = len(b7)
b16 = np.zeros((b15, b14))
for b13, b6 in enumerate(b8):
    b16[:, b13] = fonk2(b6)
b17 = TruncatedSVD(n_components=2)
b18 = b17.fit_transform(b16)
plt.figure(b19 = (10, 8))
plt.scatter(b18[:, 0], b18[:, 1])
for b13 in range(b15):
    plt.annotate(b5 = b10[b13], xy=(b18[b13, 0], b18[b13, 1]))
plt.b11('Truncated SVD of Book Titles')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.grid(True)
plt.show()