from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import euclidean_distances
import os
from gensim.models.word2vec import Word2Vec
from text_unidecode import unidecode
document1 = "Obama speaks to the media in Illinois"
document2 = "The President addresses the press in Chicago"
embeddings_file = "data/embed.dat"
if not os.path.exists(embeddings_file):
    print("Caching word embeddings in memmapped format...")
    word2vec_model = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        binary=True)
    word2vec_model.init_sims(replace=True)
    with np.memmap(embeddings_file, dtype=np.double, mode='w+', shape=word2vec_model.syn0norm.shape) as fp:
        fp[:] = word2vec_model.syn0norm[:]
    with open("data/embed.vocab", "w") as f:
        for _, word in sorted((voc.index, word) for word, voc in word2vec_model.vocab.items()):
            print(unidecode(word), file=f)
word2vec_model = Word2Vec.load_word2vec_format(
    "data/GoogleNews-vectors-negative300.bin.gz",
    binary=True)
embeddings = np.memmap(embeddings_file, dtype=np.double, mode="r", shape=word2vec_model.syn0.shape)
with open("data/embed.vocab") as f:
    vocab_list = map(str.strip, f.readlines())
vocab_dict = {word: idx for idx, word in enumerate(vocab_list)}
def calculate_similarity(doc1, doc2):
    vectorizer = CountVectorizer(stop_words="english").fit([doc1, doc2])
    word_indices = [vocab_dict[word] for word in vectorizer.get_feature_names()]
    embeddings_subset = embeddings[word_indices]
    distances = euclidean_distances(embeddings_subset)
    doc1_vector, doc2_vector = vectorizer.transform([doc1, doc2]).toarray()
    doc1_vector = doc1_vector.astype(np.double)
    doc2_vector = doc2_vector.astype(np.double)
    doc1_vector /= doc1_vector.sum()
    doc2_vector /= doc2_vector.sum()
    distances = distances.astype(np.double)
    distances /= distances.max()
    return emd(doc1_vector, doc2_vector, distances)
similarity_score = calculate_similarity(document1, document2)
print("Similarity score between document1 and document2:", similarity_score)