import os
import numpy as np
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import euclidean_distances
from pyemd import emd
from text_unidecode import unidecode
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
if not os.path.exists("data/embed.dat"):
    print("Caching word b13 in memmapped format...")
    b3 = KeyedVectors.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b4 = True)
    b3.init_sims(b5 = True)
    with np.memmap("data/embed.dat", b6 = np.double, mode='w+', shape=b3.vectors_norm.shape) as fp:
        fp[:] = b3.vectors_norm[:]
    with open("data/embed.vocab", "w") as f:
        for word in sorted(b3.vocab.keys()):
            print(unidecode(word), b7 = f)
b3 = KeyedVectors.load_word2vec_format(
    "data/GoogleNews-vectors-negative300.bin.gz",
    b4 = True)
b8 = np.memmap("data/embed.dat", b6=np.double, mode="r", shape=b3.vectors.shape)
with open("data/embed.vocab") as f:
    b9 = [line.strip() for line in f.readlines()]
b10 = {word: idx for idx, word in enumerate(b9)}
def fonk1(b1, b2):
    b11 = CountVectorizer(stop_words="english").fit([b1, b2])
    b12 = [b10[word] for word in b11.get_feature_names()]
    b13 = b8[b12]
    b14 = euclidean_distances(b13)
    b16, b15 = b11.transform([b1, b2]).toarray()
    b16 = b16.astype(np.double)
    b15 = b15.astype(np.double)
    b16 /= b16.sum()
    b15 /= b15.sum()
    b14 = b14.astype(np.double)
    b14 /= b14.max()
    return emd(b16, b15, b14)
b17 = fonk1(b1, b2)
print("Similarity score between b1 and b2:", b17)