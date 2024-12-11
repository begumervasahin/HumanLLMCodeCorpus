from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import euclidean_distances
import os
from gensim.models.word2vec import Word2Vec
from text_unidecode import unidecode
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
if not os.path.exists("data/embed.dat"):
    print("Caching word embeddings in memmapped format...")
    b3 = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b4 = True)
    b3.init_sims(b5 = True)
    b6 = np.memmap("data/embed.dat", dtype=np.double, mode='w+', shape=b3.syn0norm.shape)
    b6[:] = b3.syn0norm[:]
    with open("data/embed.vocab", "w") as f:
        for _, w in sorted((voc.index, word) for word, voc in b3.vocab.items()):
            print >>f, unidecode(w)
    del b6
b3 = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b4 = True)
b7 = np.memmap("data/embed.dat", dtype=np.double, mode="r", shape=b3.syn0.shape)
with open("data/embed.vocab") as f:
    b8 = map(str.strip, f.readlines())
b9 = {w: k for k, w in enumerate(b8)}
def fonk1(b1, b2):
    b10 = CountVectorizer(stop_words="english").fit([b1, b2])
    b11 = b7[[b9[w] for w in b10.get_feature_names()]]
    b12 = euclidean_distances(b11)
    b14, b13 = b10.transform([b1, b2])
    b14 = b14.toarray().ravel()
    b13 = b13.toarray().ravel()
    b14 = b14.astype(np.double)
    b13 = b13.astype(np.double)
    b14 /= b14.sum()
    b13 /= b13.sum()
    b12 = b12.astype(np.double)
    b12 /= b12.max()
    return emd(b14, b13, b12))