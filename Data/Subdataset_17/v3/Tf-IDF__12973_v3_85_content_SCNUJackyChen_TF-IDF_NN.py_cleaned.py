import gensim
import numpy as np
import pickle
from sklearn.neighbors import BallTree
import TFIDF
model = gensim.models.KeyedVectors.load_word2vec_format('embedding.txt', binary=False)
vocab = model.key_to_index
embedding_dim = model.vector_size
vocab_size = len(vocab)
embeddings_matrix = np.zeros((vocab_size, embedding_dim))
words = list(vocab.keys())
for i, word in enumerate(words):
    embeddings_matrix[i] = model[word]
ball_tree = BallTree(embeddings_matrix)
serialized_tree = pickle.dumps(ball_tree)
def word_rewrite(word: str) -> str:
    if word in TFIDF.dictionary:
        return word
    tree_copy = pickle.loads(serialized_tree)
    query_embedding = model[word].reshape(1, -1)
    distances, indices = tree_copy.query(query_embedding, k=100)
    candidate_words = [words[idx] for idx in indices[0]]
    for candidate in candidate_words:
        if candidate in TFIDF.dictionary:
            return candidate
    return None
if __name__ == '__main__':
    rewritten_word = word_rewrite('fib')
    print(f"Rewritten word: {rewritten_word}")