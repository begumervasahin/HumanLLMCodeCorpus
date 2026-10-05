import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data
import logging
import numpy as np
import gensim
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.metrics.pairwise import cosine_similarity
def makeFeatureVec(words, model, num_features):
    featureVec = np.zeros((num_features,), dtype="float32")
    nwords = 0.
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            nwords = nwords + 1.
            featureVec = np.add(featureVec, model.wv[word])
    featureVec = np.divide(featureVec, nwords)
    return featureVec
def getAvgFeatureVecs(skucollection, model, num_features):
    reviewFeatureVecs = np.zeros((len(skucollection), num_features), dtype="float32")
    for i, sku in enumerate(skucollection):
        if i % 1000 == 0:
            print("sku %d of %d" % (i, len(skucollection)))
        reviewFeatureVecs[i] = makeFeatureVec(sku, model, num_features)
    return reviewFeatureVecs
def getCleanTrainReviews(skucollection):
    clean_skucollection = []
    for sku in skucollection["product_title"]:
        clean_skucollection.append(KaggleWord2VecUtility.sku_to_wordlist(sku, remove_stopwords=False))
    return clean_skucollection
def getCleanTestReviews(skucollection):
    clean_skucollection = []
    for sku in skucollection["query"]:
        clean_skucollection.append(KaggleWord2VecUtility.sku_to_wordlist(sku, remove_stopwords=False))
    return clean_skucollection
if __name__ == '__main__':
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'train.csv'), header=0, delimiter=",", quoting=6)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'test.csv'), header=0, delimiter=",", quoting=6)
    print("Read %d labeled train skucollection, %d labeled test skucollection" % (train["product_title"].size, test["query"].size))
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    num_features = 300
    model = gensim.models.Word2Vec.load('300features_40minwords_10_SKU')
    print("Creating average feature vecs for training skucollection")
    trainDataVecs = getAvgFeatureVecs(getCleanTrainReviews(train), model, num_features)
    print("Creating average feature vecs for test skucollection")
    testDataVecs = getAvgFeatureVecs(getCleanTestReviews(test), model, num_features)
    print("Query ID, SKU ID, Cosine")
    for query, i in enumerate(testDataVecs):
        for isku, j in enumerate(trainDataVecs):
            cos = 0.0
            try:
                cos = cosine_similarity(i.reshape(1, -1), j.reshape(1, -1))[0][0]
            except:
                pass
            print("%d, %d, %f" % (query, isku, cos))