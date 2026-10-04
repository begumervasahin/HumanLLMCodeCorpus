import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
import TFIDF
b1 = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
b2 = b1.key_to_index
b3 = b1.vector_size
b4 = len(b2)
b5 = np.zeros((b4, b3))
b6 = list(b2.keys())
for i, word in enumerate(b6):
    b5[i] = b1[word]
b7 = BallTree(b5)
b8 = pickle.dumps(b7)
def fonk1(word: str) -> str:
    if word in TFIDF.dictionary:
        return word
    b9 = pickle.loads(b8)
    b10 = b1[word].reshape(1, -1)
    distances, b11 = b9.query(b10, k=100)
    b12 = [b6[idx] for idx in b11[0]]
    for candidate in b12:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if b13 = = '__main__':
    b14 = fonk1('fib')
    print(f"Rewritten word: {b14}")