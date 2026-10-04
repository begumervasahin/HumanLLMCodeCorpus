import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
import TFIDF
b1 = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
b2 = b1.wv.b2
b3 = b1.vector_size
b4 = np.ndarray(shape=(len(b2), b3))
b5 = list(b2.keys())
for i, word in enumerate(b5):
    b4[i] = b1[word]
b6 = BallTree(b4)
b7 = pickle.dumps(b6)
def fonk1(word: str) -> str:
    if word in TFIDF.dictionary:
        return word
    b8 = pickle.loads(b7)
    b9 = b1[word].reshape(1, -1)
    dist, b10 = b8.query(b9, k=100)
    b11 = [b5[idx] for idx in b10[0]]
    for candidate in b11:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if b12 = = '__main__':
    b13 = fonk1('fib')
    print(b13)