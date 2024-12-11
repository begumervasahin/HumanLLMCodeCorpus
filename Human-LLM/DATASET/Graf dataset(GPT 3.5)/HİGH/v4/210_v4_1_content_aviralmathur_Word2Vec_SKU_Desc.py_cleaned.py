import pandas as pd
import os
import nltk.data
import logging
import numpy as np
import gensim
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(words, b11, a2):
    b1 = np.zeros((a2,), dtype="float32")
    a1 = 0.
    for word in words:
        if word in b11.wv.index2word:
            a1 += 1
            b1 = np.add(b1, b11[word])
    if a1 != 0:
        b1 = np.divide(b1, a1)
    return b1
def fonk2(skucollection, b11, a2):
    b2 = np.zeros((len(skucollection), a2), dtype="float32")
    for i, sku in enumerate(skucollection):
        if i % b3 = = 0:
            print(f"Processing SKU {i} of {len(skucollection)}")
        b2[i] = fonk1(sku, b11, a2)
    return b2
def fonk3(skucollection, column_name):
    b4 = []
    for sku in skucollection[column_name]:
        b4.append(KaggleWord2VecUtility.sku_to_wordlist(sku, b5 = False))
    return b4
if b6 = = '__main__':
    b7 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b7.csv'), header=0, delimiter=",", quoting=6)
    b8 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b8.csv'), header=0, delimiter=",", quoting=6)
    print(f"Read {len(b7)} labeled b7 SKUs, {len(b8)} labeled b8 SKUs")
    b9 = nltk.data.load('tokenizers/punkt/english.pickle')
    logging.basicConfig(b10 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    a2 = 300
    b11 = gensim.models.Word2Vec.load('300features_40minwords_10_SKU')
    print("Creating average feature vectors for training SKUs")
    b12 = fonk2(fonk3(b7, "product_title"), b11, a2)
    print("Creating average feature vectors for b8 SKUs")
    b13 = fonk2(fonk3(b8, "query"), b11, a2)
    print("Query ID, SKU ID, Cosine")
    try:
        for query, test_vector in enumerate(b13):
            for isku, train_vector in enumerate(b12):
                b14 = cosine_similarity(test_vector.reshape(1, -1), train_vector.reshape(1, -1))
                print(f"{query}, {isku}, {b14}")
    except Exception as e:
        print(f"An exception occurred: {e}")