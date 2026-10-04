import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
import TFIDF
model = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
vocab = model.wv.vocab
embedding_dim = model.vector_size
X = np.ndarray(shape=(len(vocab), embedding_dim))
words = list(vocab.keys())
for i, word in enumerate(words):
    X[i] = model[word]
tree = BallTree(X)
serialized_tree = pickle.dumps(tree)
def word_rewrite(word: str) -> str:
    if word in TFIDF.dictionary:
        return word
    tree_copy = pickle.loads(serialized_tree)
    q_embedding = model[word].reshape(1, -1)
    dist, ind = tree_copy.query(q_embedding, k=100)
    candidates = [words[idx] for idx in ind[0]]
    for candidate in candidates:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if __name__ == '__main__':
    rewritten_word = word_rewrite('fib')
    print(rewritten_word)