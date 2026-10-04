import time
import os
import re
import numpy as np
import operator
import math
import gensim
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
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
def get_word_embeddings(data):
    model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    out_sent_vectors = []
    for sent in data:
        sent_vec = []
        for word in sent.split():
            if word in model.vocab:
                sent_vec.append(model.wv[word])
        sent_vec = np.array(sent_vec)
        sent_vec =  np.mean(sent_vec, axis=0)
        out_sent_vectors.append(sent_vec)
    return out_sent_vectors
def clean_data(input_str, remove_stop = True):
    input_str = re.sub('<[^<]+?>', ' ', input_str)
    out = re.sub('[^A-Za-z0-9]+', ' ', input_str.lower())
    return out
def extract_features(train_x, train_y, test_x):
    vectroizer = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1,4))
    selector = SelectKBest(chi2, k = 7000)
    train_x_fit = vectroizer.fit_transform(train_x).toarray()
    train_x_fit = selector.fit_transform(train_x_fit, train_y)
    test_x_fit = vectroizer.transform(test_x).toarray()
    test_x_fit = selector.transform(test_x_fit)
    train_x_withot_stop = []
    for sent in train_x:
        clean_sent = ' '.join([i for i in sent.split() if i not in stop_words])
        train_x_withot_stop.append(clean_sent)
    test_x_withot_stop = []
    for sent in test_x:
        clean_sent = ' '.join([i for i in sent.split() if i not in stop_words])
        test_x_withot_stop.append(clean_sent)
    train_x_fit_embedding = get_word_embeddings(train_x_withot_stop)
    train_x_fit_embedding = np.array(train_x_fit_embedding)
    test_x_fit_embedding = get_word_embeddings(test_x_withot_stop)
    test_x_fit_embedding = np.array(test_x_fit_embedding)
    train_x_fit = np.concatenate((train_x_fit, train_x_fit_embedding), axis=1)
    test_x_fit = np.concatenate((test_x_fit, test_x_fit_embedding), axis=1)
    return (train_x_fit, test_x_fit)
def process_data():
    f_train = open('train.dat')
    f_test = open('test_data.dat')
    test_x = []
    train_x = []
    train_y = []
    for line in f_train:
        sample = line.strip().split('\t')
        y = int(sample[0])
        x = sample[1]
        x = clean_data(x, True)
        train_x.append(x)
        train_y.append(y)
    for line in f_test:
        sample = line.strip().split('\t')
        x = sample[0]
        x = clean_data(x, True)
        test_x.append(x)
    train_x_fit, test_x_fit = extract_features(train_x, train_y, test_x)
    train_y = np.array(train_y)
    print train_x_fit.shape, test_x_fit.shape, train_x_fit.dtype, test_x_fit.dtype
    return (train_y, train_x_fit, test_x_fit)
def test_model_locally(train_y, train_x, test_x):
	X_train, X_test, Y_train, Y_test = train_test_split(train_x, train_y, test_size=0.20, random_state=42)
	x_keys = tf.placeholder("float", [None, train_x.shape[1]])
	x_queries = tf.placeholder("float", [None, train_x.shape[1]])
	normalized_keys = tf.nn.l2_normalize(x_keys, dim=0)
	normalized_query = tf.nn.l2_normalize(x_queries, dim=0)
	query_result = tf.matmul(normalized_keys, tf.transpose(normalized_query))
	pred = tf.arg_max(query_result, dimension=0)
	init = tf.global_variables_initializer()
	with tf.Session() as sess:
	    sess.run(init)
	    print("Training the model")
	    preds = sess.run(query_result, feed_dict={x_keys: X_train, x_queries: X_test})
	    preds = tf.transpose(preds)
	    values, indices = sess.run(tf.nn.top_k(preds, K))
	    y_preds = []
	    for top in indices:
	    	sample_label = []
	    	for neighbor in top:
	    		sample_label.append(Y_train[neighbor])
	    	y_preds.append(mode(sample_label)[0][0])
	    accuracy = np.sum(y_preds == Y_test).astype(float) / len(Y_test)
	    print("Accuracy: " + str(accuracy * 100) + '%')
def generate_predictions(train_y, train_x, test_x, prediction_output_file_name):
	X_train, Y_train, X_test = train_x, train_y, test_x
	batches_x_test = [test_x[:5000], test_x[5000:10000], test_x[10000:15000], test_x[15000:20000], test_x[20000:25000]]
	f_out = open(prediction_output_file_name, "w")
	for batch in batches_x_test[:3]:
		x_keys = tf.placeholder("float", [None, train_x.shape[1]])
		x_queries = tf.placeholder("float", [None, train_x.shape[1]])
		normalized_keys = tf.nn.l2_normalize(x_keys, dim=0)
		normalized_query = tf.nn.l2_normalize(x_queries, dim=0)
		query_result = tf.matmul(normalized_keys, tf.transpose(normalized_query))
		pred = tf.arg_max(query_result, dimension=0)
		init = tf.global_variables_initializer()
		with tf.Session() as sess:
		    sess.run(init)
		    start = time.time()
		    print("Evaluating tensorflow KNN")
		    preds = sess.run( query_result , feed_dict={x_keys: X_train, x_queries: batch})
		    preds = tf.transpose(preds)
		    values, indices = sess.run(tf.nn.top_k(preds, K))
		    y_preds = []
		    for top in indices:
		    	sample_label = []
		    	for neighbor in top:
		    		sample_label.append(Y_train[neighbor])
		    	y_preds.append(mode(sample_label)[0][0])
		    for pred in y_preds:
		    	if pred >0 :
		    		f_out.write('+1\n')
		    	else:
		    		f_out.write('-1\n')
		ops.reset_default_graph()
	for batch in batches_x_test[3:]:
		x_keys = tf.placeholder("float", [None, train_x.shape[1]])
		x_queries = tf.placeholder("float", [None, train_x.shape[1]])
		normalized_keys = tf.nn.l2_normalize(x_keys, dim=0)
		normalized_query = tf.nn.l2_normalize(x_queries, dim=0)
		query_result = tf.matmul(normalized_keys, tf.transpose(normalized_query))
		pred = tf.arg_max(query_result, dimension=0)
		init = tf.global_variables_initializer()
		with tf.Session() as sess:
		    sess.run(init)
		    start = time.time()
		    print("Evaluating tensorflow KNN")
		    preds = sess.run( query_result , feed_dict={x_keys: X_train, x_queries: batch})
		    preds = tf.transpose(preds)
		    values, indices = sess.run(tf.nn.top_k(preds, K))
		    y_preds = []
		    for top in indices:
		    	sample_label = []
		    	for neighbor in top:
		    		sample_label.append(Y_train[neighbor])
		    	y_preds.append(mode(sample_label)[0][0])
		    for pred in y_preds:
		    	if pred >0 :
		    		f_out.write('+1\n')
		    	else:
		    		f_out.write('-1\n')
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