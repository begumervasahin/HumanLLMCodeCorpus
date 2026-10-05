import os
import numpy as np
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import euclidean_distances
from pyemd import emd
from text_unidecode import unidecode
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
b3 = "data/embed.dat"
b4 = "data/embed.vocab"
if not os.path.exists(b3):
    print("Caching word b15 in memmapped format...")
    b5 = KeyedVectors.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b6 = True)
    b5.init_sims(b7 = True)
    with np.memmap(b3, b8 = np.double, mode='w+', shape=b5.vectors_norm.shape) as fp:
        fp[:] = b5.vectors_norm[:]
    with open(b4, "w") as f:
        for word in sorted(b5.vocab.keys()):
            print(unidecode(word), b9 = f)
b5 = KeyedVectors.load_word2vec_format(
    "data/GoogleNews-vectors-negative300.bin.gz",
    b6 = True)
b10 = np.memmap(b3, b8=np.double, mode="r", shape=b5.vectors.shape)
with open(b4) as f:
    b11 = [line.strip() for line in f.readlines()]
b12 = {word: idx for idx, word in enumerate(b11)}
def fonk1(b1, b2):
    b13 = CountVectorizer(stop_words="english").fit([b1, b2])
    b14 = [b12[word] for word in b13.get_feature_names()]
    b15 = b10[b14]
    b16 = euclidean_distances(b15)
    b18, b17 = b13.transform([b1, b2]).toarray()
    b18 = b18.astype(np.double)
    b17 = b17.astype(np.double)
    b18 /= b18.sum()
    b17 /= b17.sum()
    b16 = b16.astype(np.double)
    b16 /= b16.max()
    return emd(b18, b17, b16)
b19 = fonk1(b1, b2)
print("Similarity score between b1 and b2:", b19)