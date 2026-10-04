import TFIDF
import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
b1 = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
b2 = b1.key_to_index
b3 = len(b2)
b4 = np.ndarray(shape=(b3, 300))
b5 = []
for i, key in enumerate(b2):
    b5.append(key)
    b4[i] = b1[key]
b6 = BallTree(b4)
b7 = pickle.dumps(b6)
def fonk1(word: str):
    if word in TFIDF.dictionary:
        return word
    b8 = pickle.loads(b7)
    b9 = b1[word].reshape(1, 300)
    dist, b10 = b8.query(b9, k=100)
    b11 = [b5[idx] for idx in b10[0]]
    for candidate in b11:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if b12 = = '__main__':
    b13 = fonk1('fib')
    print(b13)