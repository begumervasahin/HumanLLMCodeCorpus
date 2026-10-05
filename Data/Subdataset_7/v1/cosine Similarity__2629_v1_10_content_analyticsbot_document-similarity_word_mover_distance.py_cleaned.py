from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import euclidean_distances
import os
from gensim.models import KeyedVectors
from text_unidecode import unidecode
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
if not os.path.exists("data/embed.dat"):
    print("Caching word embeddings in memmapped format...")
    b3 = KeyedVectors.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b4 = True)
    b3.init_sims(b5 = True)
    b6 = np.memmap("data/embed.dat", dtype=np.double, mode='w+', shape=b3.vectors_norm.shape)
    b6[:] = b3.vectors_norm[:]
    with open("data/embed.vocab", "w") as f:
        for word in sorted(b3.vocab.keys()):
            print(unidecode(word), b7 = f)
    del b6
b3 = KeyedVectors.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b4 = True)
b8 = np.memmap("data/embed.dat", dtype=np.double, mode="r", shape=b3.vectors.shape)
with open("data/embed.vocab") as f:
    b9 = [line.strip() for line in f.readlines()]
b10 = {w: k for k, w in enumerate(b9)}
def fonk1(b1, b2):
    b11 = CountVectorizer(stop_words="english").fit([b1, b2])
    b12 = b8[[b10[w] for w in b11.get_feature_names()]]
    b13 = euclidean_distances(b12)
    b15, b14 = b11.transform([b1, b2])
    b15 = b15.toarray().ravel().astype(np.double)
    b14 = b14.toarray().ravel().astype(np.double)
    b15 /= b15.sum()
    b14 /= b14.sum()
    b13 = b13.astype(np.double)
    b13 /= b13.max()
    return emd(b15, b14, b13)
b16 = fonk1(b1, b2)
print("Similarity score between b1 and b2:", b16)