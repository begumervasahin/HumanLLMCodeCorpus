import pandas as pd
import os
import nltk.data
import logging
import numpy as np
from gensim.models import Word2Vec
from KaggleWord2VecUtility import KaggleWord2VecUtility
def generate_feature_vector(words, model, num_features):
    feature_vector = np.zeros((num_features,), dtype="float32")
    word_count = 0
    for word in words:
        if word in model.wv:
            word_count += 1
            feature_vector += model[word]
    if word_count > 0:
        feature_vector /= word_count
    return feature_vector
def get_average_feature_vectors(sku_collection, model, num_features):
    feature_vectors = np.zeros((len(sku_collection), num_features), dtype="float32")
    counter = 0
    for sku in sku_collection:
        if counter % 1000 == 0:
            print(f"Processing SKU {counter} of {len(sku_collection)}")
        feature_vectors[counter] = generate_feature_vector(sku, model, num_features)
        counter += 1
    return feature_vectors
def clean_and_preprocess_skus(sku_collection):
    clean_sku_collection = []
    for sku in sku_collection["product_title"]:
        clean_sku_collection.append(KaggleWord2VecUtility.sku_to_wordlist(sku, remove_stopwords=True))
    return clean_sku_collection
if __name__ == '__main__':
    train_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'train.csv'),
                             header=0, delimiter=",", quoting=6)
    print(f"Read {train_data['product_title'].size} labeled train SKUs")
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = []
    print("Parsing sentences from the training set")
    for sku in train_data["product_title"]:
        sentences += KaggleWord2VecUtility.sku_to_sentences(sku, tokenizer)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    num_features = 300
    min_word_count = 40
    num_workers = 4
    context = 10
    downsampling = 1e-3
    print("Training Word2Vec model...")
    w2v_model = Word2Vec(sentences, workers=num_workers, size=num_features,
                          min_count=min_word_count, window=context, sample=downsampling, seed=1)
    w2v_model.init_sims(replace=True)
    model_name = "300features_40minwords_10_SKU"
    w2v_model.save(model_name)