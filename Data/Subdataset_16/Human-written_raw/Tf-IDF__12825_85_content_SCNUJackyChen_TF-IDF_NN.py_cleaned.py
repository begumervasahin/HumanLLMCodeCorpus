import TFIDF
import gensim
from pprint import pprint
import numpy as np
import pickle
from sklearn.neighbors import BallTree, KDTree
b1 = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
b2 = b1.wv.b2
b3 = len(b2)
b4 = np.ndarray(shape=(b3, 300))
b5 = []
for key, i in zip(b2.keys(), range(b3)):
    b5.append(key)
    b4[i] = b1[str(key)]
b6 = BallTree(b4)
b7 = pickle.dumps(b6)
def fonk1(word: str):
    if word in TFIDF.dictionary:
        return word
    b8 = pickle.loads(b7)
    b9 = b1[word].reshape(1, 300)
    dist, b10 = b8.query(b9, k=100)
    b11 = b10.tolist()[0]
    b12 = [b5[x] for x in b11]
    for candidate in b12:
        if candidate not in TFIDF.dictionary:
            continue
        else:
            return candidate
if b13 = = '__main__':
    b14 = fonk1('fib')
    print(b14)