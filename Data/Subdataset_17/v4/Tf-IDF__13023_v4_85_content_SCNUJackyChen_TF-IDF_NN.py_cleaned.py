import TFIDF
import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
model = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
vocab = model.key_to_index
length = len(vocab)
X = np.ndarray(shape=(length, 300))
words = []
for i, key in enumerate(vocab):
    words.append(key)
    X[i] = model[key]
tree = BallTree(X)
tree_serialized = pickle.dumps(tree)
def word_rewrite(word: str):
    if word in TFIDF.dictionary:
        return word
    tree_copy = pickle.loads(tree_serialized)
    q_embedding = model[word].reshape(1, 300)
    dist, ind = tree_copy.query(q_embedding, k=100)
    candidates = [words[idx] for idx in ind[0]]
    for candidate in candidates:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if __name__ == '__main__':
    rewritten_word = word_rewrite('fib')
    print(rewritten_word)