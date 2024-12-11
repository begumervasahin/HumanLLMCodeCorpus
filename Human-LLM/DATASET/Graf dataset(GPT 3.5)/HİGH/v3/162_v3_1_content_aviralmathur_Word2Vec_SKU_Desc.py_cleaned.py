import pandas as pd
import os
import nltk.data
import logging
import numpy as np
import gensim
from sklearn.metrics.pairwise import cosine_similarity
from KaggleWord2VecUtility import KaggleWord2VecUtility
def fonk1(words, b12, a2):
    b1 = np.zeros((a2,), dtype="float32")
    a1 = 0
    b2 = set(b12.wv.index2word)
    for word in words:
        if word in b2:
            a1 += 1
            b1 += b12.wv[word]
    return b1 / max(a1, 1)
def fonk2(skucollection, b12, a2):
    b3 = np.zeros((len(skucollection), a2), dtype="float32")
    for i, sku in enumerate(skucollection):
        if i % b4 = = 0:
            print(f"Processing SKU {i+1} of {len(skucollection)}")
        b3[i] = fonk1(sku, b12, a2)
    return b3
def fonk3(skucollection, column_name):
    b5 = []
    for sku in skucollection[column_name]:
        b5.append(KaggleWord2VecUtility.sku_to_wordlist(sku, b6 = False))
    return b5
if b7 = = '__main__':
    b8 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b8.csv'), header=0, delimiter=",", quoting=6)
    b9 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b9.csv'), header=0, delimiter=",", quoting=6)
    print(f"Read {len(b8)} labeled b8 SKUs, {len(b9)} labeled b9 SKUs")
    b10 = nltk.data.load('tokenizers/punkt/english.pickle')
    logging.basicConfig(b11 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    a2 = 300
    b12 = gensim.models.Word2Vec.load('300features_40minwords_10_SKU')
    print("Creating average feature vectors for training SKUs")
    b13 = fonk2(fonk3(b8, "product_title"), b12, a2)
    print("Creating average feature vectors for b9 SKUs")
    b14 = fonk2(fonk3(b9, "query"), b12, a2)
    print("Query ID, SKU ID, Cosine")
    for query, test_vector in enumerate(b14):
        for isku, train_vector in enumerate(b13):
            try:
                b15 = cosine_similarity(test_vector.reshape(1, -1), train_vector.reshape(1, -1))[0][0]
                print(f"{query}, {isku}, {b15}")
            except Exception as e:
                print(f"Error processing query {query} and SKU {isku}: {e}")