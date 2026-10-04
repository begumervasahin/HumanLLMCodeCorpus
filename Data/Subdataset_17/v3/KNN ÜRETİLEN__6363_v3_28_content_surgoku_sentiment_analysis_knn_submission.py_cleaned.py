import time
import os
import re
import numpy as np
import gensim
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import mode
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.python.framework import ops
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
stop_words = stopwords.words('english')
porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
K = 250
def get_word_embeddings(data, model_path='GoogleNews-vectors-negative300.bin'):
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    out_sent_vectors = []
    for sent in data:
        sent_vec = [model.wv[word] for word in sent.split() if word in model.vocab]
        sent_vec = np.mean(sent_vec, axis=0) if sent_vec else np.zeros(300)
        out_sent_vectors.append(sent_vec)
    return out_sent_vectors
def clean_data(input_str, remove_stop=True):
    input_str = re.sub('<[^<]+?>', ' ', input_str)
    out = re.sub('[^A-Za-z0-9]+', ' ', input_str.lower())
    if remove_stop:
        out = ' '.join([word for word in out.split() if word not in stop_words])
    return out
def extract_features(train_x, train_y, test_x):
    vectorizer = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    selector = SelectKBest(chi2, k=7000)
    train_x_fit = vectorizer.fit_transform(train_x).toarray()
    train_x_fit = selector.fit_transform(train_x_fit, train_y)
    test_x_fit = vectorizer.transform(test_x).toarray()
    test_x_fit = selector.transform(test_x_fit)
    train_x_fit_embedding = get_word_embeddings(train_x)
    test_x_fit_embedding = get_word_embeddings(test_x)
    train_x_fit = np.concatenate((train_x_fit, train_x_fit_embedding), axis=1)
    test_x_fit = np.concatenate((test_x_fit, test_x_fit_embedding), axis=1)
    return train_x_fit, test_x_fit
def process_data(train_file='train.dat', test_file='test_data.dat'):
    with open(train_file) as f_train, open(test_file) as f_test:
        train_x, train_y, test_x = [], [], []
        for line in f_train:
            y, x = line.strip().split('\t')
            train_x.append(clean_data(x))
            train_y.append(int(y))
        for line in f_test:
            x = line.strip()
            test_x.append(clean_data(x))
    train_x_fit, test_x_fit = extract_features(train_x, train_y, test_x)
    train_y = np.array(train_y)
    print(train_x_fit.shape, test_x_fit.shape, train_x_fit.dtype, test_x_fit.dtype)
    return train_y, train_x_fit, test_x_fit
def test_model_locally(train_y, train_x, test_x):
    X_train, X_test, Y_train, Y_test = train_test_split(train_x, train_y, test_size=0.20, random_state=42)
    x_keys = tf.placeholder("float", [None, train_x.shape[1]])
    x_queries = tf.placeholder("float", [None, train_x.shape[1]])
    normalized_keys = tf.nn.l2_normalize(x_keys, axis=1)
    normalized_query = tf.nn.l2_normalize(x_queries, axis=1)
    query_result = tf.matmul(normalized_query, tf.transpose(normalized_keys))
    pred = tf.argmax(query_result, axis=1)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        print("Training the model")
        preds = sess.run(query_result, feed_dict={x_keys: X_train, x_queries: X_test})
        preds = tf.transpose(preds)
        values, indices = sess.run(tf.nn.top_k(preds, K))
        y_preds = []
        for top in indices:
            sample_label = [Y_train[neighbor] for neighbor in top]
            y_preds.append(mode(sample_label)[0][0])
        accuracy = accuracy_score(Y_test, y_preds)
        print(f"Accuracy: {accuracy * 100:.2f}%")
def generate_predictions(train_y, train_x, test_x, prediction_output_file_name):
    X_train, Y_train, X_test = train_x, train_y, test_x
    batches_x_test = [test_x[i:i + 5000] for i in range(0, len(test_x), 5000)]
    with open(prediction_output_file_name, "w") as f_out:
        for batch in batches_x_test:
            x_keys = tf.placeholder("float", [None, train_x.shape[1]])
            x_queries = tf.placeholder("float", [None, train_x.shape[1]])
            normalized_keys = tf.nn.l2_normalize(x_keys, axis=1)
            normalized_query = tf.nn.l2_normalize(x_queries, axis=1)
            query_result = tf.matmul(normalized_query, tf.transpose(normalized_keys))
            pred = tf.argmax(query_result, axis=1)
            init = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.run(init)
                print("Evaluating TensorFlow k-NN")
                preds = sess.run(query_result, feed_dict={x_keys: X_train, x_queries: batch})
                preds = tf.transpose(preds)
                values, indices = sess.run(tf.nn.top_k(preds, K))
                y_preds = []
                for top in indices:
                    sample_label = [Y_train[neighbor] for neighbor in top]
                    y_preds.append(mode(sample_label)[0][0])
                for pred in y_preds:
                    f_out.write(f'+1\n' if pred > 0 else '-1\n')
            ops.reset_default_graph()
def run(evaluate_model_locally, prediction_output_file_name):
    train_y, train_x, test_x = process_data()
    if evaluate_model_locally:
        test_model_locally(train_y, train_x, test_x)
    else:
        generate_predictions(train_y, train_x, test_x, prediction_output_file_name)
if __name__ == "__main__":
    evaluate_model_locally = False
    prediction_output_file_name = "test.dat"
    run(evaluate_model_locally, prediction_output_file_name)