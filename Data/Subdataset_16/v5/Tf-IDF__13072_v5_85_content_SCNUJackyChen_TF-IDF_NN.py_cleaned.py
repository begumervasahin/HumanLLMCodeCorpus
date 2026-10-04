import TFIDF
import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
def fonk1(file_path: str):
    return gensim.models.KeyedVectors.load_word2vec_format(file_path, b1 = False)
def fonk2(b11):
    b2 = b11.key_to_index
    b3 = len(b2)
    b4 = np.ndarray(shape=(b3, 300))
    b5 = []
    for i, word in enumerate(b2):
        b5.append(word)
        b4[i] = b11[word]
    return b4, b5
def fonk3(b4):
    b6 = BallTree(b4)
    return pickle.dumps(b6)
def fonk4(b12):
    return pickle.loads(b12)
def fonk5(b6, b11, b5, target_word, dictionary, b7 = 100):
    if target_word in dictionary:
        return target_word
    b8 = b11[target_word].reshape(1, 300)
    dist, b9 = b6.query(b8, b7=b7)
    b10 = [b5[idx] for idx in b9[0]]
    for candidate in b10:
        if candidate in dictionary:
            return candidate
    return None
def fonk6():
    b11 = fonk1('embedding.txt')
    b4, b5 = fonk2(b11)
    b12 = fonk3(b4)
    b6 = fonk4(b12)
    b13 = fonk5(b6, b11, b5, 'fib', TFIDF.dictionary)
    print(b13)
if b14 = = '__main__':
    fonk6()