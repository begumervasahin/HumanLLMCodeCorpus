import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data
import logging
import numpy as np
import gensim
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(words, b12, a2):
    b1 = np.zeros((a2,), dtype="float32")
    a1 = 0.
    b2 = set(b12.wv.index2word)
    for word in words:
        if word in b2:
            a1 = a1 + 1.
            b1 = np.add(b1, b12.wv[word])
    b1 = np.divide(b1, a1)
    return b1
def fonk2(skucollection, b12, a2):
    b3 = np.zeros((len(skucollection), a2), dtype="float32")
    for i, sku in enumerate(skucollection):
        if i % b4 = = 0:
            print("sku %d of %d" % (i, len(skucollection)))
        b3[i] = fonk1(sku, b12, a2)
    return b3
def fonk3(skucollection):
    b5 = []
    for sku in skucollection["product_title"]:
        b5.append(KaggleWord2VecUtility.sku_to_wordlist(sku, b6 = False))
    return b5
def fonk4(skucollection):
    b5 = []
    for sku in skucollection["query"]:
        b5.append(KaggleWord2VecUtility.sku_to_wordlist(sku, b6 = False))
    return b5
if b7 = = '__main__':
    b8 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b8.csv'), header=0, delimiter=",", quoting=6)
    b9 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b9.csv'), header=0, delimiter=",", quoting=6)
    print("Read %d labeled b8 skucollection, %d labeled b9 skucollection" % (b8["product_title"].size, b9["query"].size))
    b10 = nltk.data.load('tokenizers/punkt/english.pickle')
    logging.basicConfig(b11 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    a2 = 300
    b12 = gensim.models.Word2Vec.load('300features_40minwords_10_SKU')
    print("Creating average feature vecs for training skucollection")
    b13 = fonk2(fonk3(b8), b12, a2)
    print("Creating average feature vecs for b9 skucollection")
    b14 = fonk2(fonk4(b9), b12, a2)
    print("Query ID, SKU ID, Cosine")
    for query, i in enumerate(b14):
        for isku, j in enumerate(b13):
            a3 = 0.0
            try:
                a3 = cosine_similarity(i.reshape(1, -1), j.reshape(1, -1))[0][0]
            except:
                pass
            print("%d, %d, %f" % (query, isku, a3))