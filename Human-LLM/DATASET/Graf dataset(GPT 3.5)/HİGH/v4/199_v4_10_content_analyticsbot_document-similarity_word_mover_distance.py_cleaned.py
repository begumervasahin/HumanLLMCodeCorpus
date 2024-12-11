from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import euclidean_distances
import os
from gensim.models.word2vec import Word2Vec
from text_unidecode import unidecode
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
b3 = "data/embed.dat"
if not os.path.exists(b3):
    print("Caching word b9 in memmapped format...")
    b4 = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        b5 = True)
    b4.init_sims(b6 = True)
    with np.memmap(b3, b7 = np.double, mode='w+', shape=b4.syn0norm.shape) as fp:
        fp[:] = b4.syn0norm[:]
    with open("data/embed.vocab", "w") as f:
        for _, word in sorted((voc.index, word) for word, voc in b4.vocab.items()):
            print(unidecode(word), b8 = f)
b4 = Word2Vec.load_word2vec_format(
    "data/GoogleNews-vectors-negative300.bin.gz",
    b5 = True)
b9 = np.memmap(b3, b7=np.double, mode="r", shape=b4.syn0.shape)
with open("data/embed.vocab") as f:
    b10 = map(str.strip, f.readlines())
b11 = {word: idx for idx, word in enumerate(b10)}
def fonk1(doc1, doc2):
    b12 = CountVectorizer(stop_words="english").fit([doc1, doc2])
    b13 = [b11[word] for word in b12.get_feature_names()]
    b14 = b9[b13]
    b15 = euclidean_distances(b14)
    b17, b16 = b12.transform([doc1, doc2]).toarray()
    b17 = b17.astype(np.double)
    b16 = b16.astype(np.double)
    b17 /= b17.sum()
    b16 /= b16.sum()
    b15 = b15.astype(np.double)
    b15 /= b15.max()
    return emd(b17, b16, b15)
b18 = fonk1(b1, b2)
print("Similarity score between b1 and b2:", b18)