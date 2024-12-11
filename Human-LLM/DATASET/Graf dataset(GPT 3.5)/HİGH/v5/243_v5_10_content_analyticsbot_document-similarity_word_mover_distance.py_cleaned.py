from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import euclidean_distances
from gensim.models.word2vec import Word2Vec
from text_unidecode import unidecode
import os
import numpy as np
b1 = "Obama speaks to the media in Illinois"
b2 = "The President addresses the press in Chicago"
b3 = "data/embed.dat"
b4 = "data/embed.vocab"
b5 = "data/GoogleNews-vectors-negative300.bin.gz"
def fonk1(b9, b3, b4):
    if not os.path.exists(b3):
        print("Caching word b10 in memmapped format...")
        b9.init_sims(b6 = True)
        with np.memmap(b3, b7 = np.double, mode='w+', shape=b9.syn0norm.shape) as fp:
            fp[:] = b9.syn0norm[:]
        with open(b4, "w") as f:
            for _, word in sorted((voc.index, word) for word, voc in b9.vocab.items()):
                print(unidecode(word), b8 = f)
def fonk2(b3, b4):
    b9 = Word2Vec.load_word2vec_format(b5, b19=True)
    b10 = np.memmap(b3, b7=np.double, mode="r", shape=b9.syn0.shape)
    with open(b4) as f:
        b11 = map(str.strip, f.readlines())
    b12 = {word: idx for idx, word in enumerate(b11)}
    return b9, b10, b12
def fonk3(doc1, doc2, b10, b12):
    b13 = CountVectorizer(stop_words="english").fit([doc1, doc2])
    b14 = [b12[word] for word in b13.get_feature_names()]
    b15 = b10[b14]
    b16 = euclidean_distances(b15)
    b18, b17 = b13.transform([doc1, doc2]).toarray()
    b18 = b18.astype(np.double) / b18.sum()
    b17 = b17.astype(np.double) / b17.sum()
    b16 = b16.astype(np.double) / b16.max()
    return emd(b18, b17, b16)
fonk1(Word2Vec.load_word2vec_format(b5, b19 = True), b3, b4)
b9, b10, b12 = fonk2(b3, b4)
b20 = fonk3(b1, b2, b10, b12)
print("Similarity score between b1 and b2:", b20)