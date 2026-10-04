import TFIDF
import gensim
from pprint import pprint
import numpy as np
import pickle
from sklearn.neighbors import BallTree, KDTree
model = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
vocab = model.wv.vocab
length = len(vocab)
X = np.ndarray(shape=(length, 300))
words = []
for key, i in zip(vocab.keys(), range(length)):
    words.append(key)
    X[i] = model[str(key)]
tree = BallTree(X)
s = pickle.dumps(tree)
def word_rewrite(word: str):
    if word in TFIDF.dictionary:
        return word
    tree_copy = pickle.loads(s)
    q_embedding = model[word].reshape(1, 300)
    dist, ind = tree_copy.query(q_embedding, k=100)
    index = ind.tolist()[0]
    candidates = [words[x] for x in index]
    for candidate in candidates:
        if candidate not in TFIDF.dictionary:
            continue
        else:
            return candidate
if __name__ == '__main__':
    a = word_rewrite('fib')
    print(a)