import pandas as pd
import os
import nltk.data
import logging
import numpy as np
from gensim.models import Word2Vec
from KaggleWord2VecUtility import KaggleWord2VecUtility
def make_feature_vec(words, model, num_features):
    feature_vec = np.zeros((num_features,), dtype="float32")
    n_words = 0.
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    feature_vec = np.divide(feature_vec, n_words)
    return feature_vec
def get_avg_feature_vecs(sku_collection, model, num_features):
    review_feature_vecs = np.zeros((len(sku_collection), num_features), dtype="float32")
    for i, sku in enumerate(sku_collection):
        if i % 1000 == 0:
            print(f"Processing SKU {i} of {len(sku_collection)}")
        review_feature_vecs[i] = make_feature_vec(sku, model, num_features)
    return review_feature_vecs
def get_clean_skus(sku_collection):
    clean_sku_collection = []
    for sku in sku_collection["product_title"]:
        clean_sku_collection.append(KaggleWord2VecUtility.sku_to_wordlist(sku, remove_stopwords=True))
    return clean_sku_collection
if __name__ == '__main__':
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'train.csv'), header=0, delimiter=",", quoting=6)
    print(f"Read {train['product_title'].size} labeled train SKUs")
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = []
    print("Parsing sentences from training set")
    for sku in train["product_title"]:
        sentences += KaggleWord2VecUtility.sku_to_sentences(sku, tokenizer)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    num_features = 300
    min_word_count = 40
    num_workers = 4
    context = 10
    downsampling = 1e-3
    print("Training Word2Vec model...")
    model = Word2Vec(sentences, workers=num_workers, size=num_features, min_count=min_word_count, window=context, sample=downsampling, seed=1)
    model.init_sims(replace=True)
    model_name = "300features_40minwords_10_SKU"
    model.save(model_name)