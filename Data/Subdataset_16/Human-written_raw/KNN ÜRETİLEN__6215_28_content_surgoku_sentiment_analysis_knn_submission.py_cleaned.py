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
b1 = stopwords.words('english')
b2 = PorterStemmer()
b3 = LancasterStemmer()
b4 = WordNetLemmatizer()
a1 = 250
def fonk1(data):
    b5 = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    b6 = []
    for sent in data:
        b7 = []
        for word in sent.split():
            if word in b5.vocab:
                b7.append(b5.wv[word])
        b7 = np.array(b7)
        b7 = np.mean(b7, axis=0)
        b6.append(b7)
    return b6
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b10 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    return b10
def fonk3(b23, b24, b22):
    b11 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1,4))
    b12 = SelectKBest(chi2, k = 7000)
    b13 = b11.fit_transform(b23).toarray()
    b13 = b12.fit_transform(b13, b24)
    b14 = b11.transform(b22).toarray()
    b14 = b12.transform(b14)
    b15 = []
    for sent in b23:
        b16 = ' '.join([i for i in sent.split() if i not in b1])
        b15.append(b16)
    b17 = []
    for sent in b22:
        b16 = ' '.join([i for i in sent.split() if i not in b1])
        b17.append(b16)
    b18 = fonk1(b15)
    b18 = np.array(b18)
    b19 = fonk1(b17)
    b19 = np.array(b19)
    b13 = np.concatenate((b13, b18), axis=1)
    b14 = np.concatenate((b14, b19), axis=1)
    return (b13, b14)
def fonk4():
    b20 = open('train.dat')
    b21 = open('test_data.dat')
    b22 = []
    b23 = []
    b24 = []
    for line in b20:
        b25 = line.strip().split('\t')
        b26 = int(b25[0])
        b27 = b25[1]
        b27 = fonk2(b27, True)
        b23.append(b27)
        b24.append(b26)
    for line in b21:
        b25 = line.strip().split('\t')
        b27 = b25[0]
        b27 = fonk2(b27, True)
        b22.append(b27)
    b13, b14 = fonk3(b23, b24, b22)
    b24 = np.array(b24)
    print b13.shape, b14.shape, b13.dtype, b14.dtype
    return (b24, b13, b14)
def fonk5(b24, b23, b22):
	X_train, b41, Y_train, b28 = train_test_split(b23, b24, test_size=0.20, random_state=42)
	b29 = tf.placeholder("float", [None, b23.shape[1]])
	b30 = tf.placeholder("float", [None, b23.shape[1]])
	b31 = tf.nn.l2_normalize(b29, dim=0)
	b32 = tf.nn.l2_normalize(b30, dim=0)
	b33 = tf.matmul(b31, tf.transpose(b32))
	b34 = tf.arg_max(b33, dimension=0)
	b35 = tf.global_variables_initializer()
	with tf.Session() as sess:
	    sess.fonk7(b35)
	    print("Training the b5")
	    b36 = sess.fonk7(b33, feed_dict={b29: X_train, b30: b41})
	    b36 = tf.transpose(b36)
	    values, b37 = sess.fonk7(tf.nn.top_k(b36, a1))
	    b38 = []
	    for top in b37:
	    	b39 = []
	    	for neighbor in top:
	    		b39.append(Y_train[neighbor])
	    	b38.append(mode(b39)[0][0])
	    b40 = np.sum(b38 == b28).astype(float) / len(b28)
	    print("Accuracy: " + str(b40 * 100) + '%')
def fonk6(b24, b23, b22, b47):
	X_train, Y_train, b41 = b23, b24, b22
	b42 = [b22[:5000], b22[5000:10000], b22[10000:15000], b22[15000:20000], b22[20000:25000]]
	b43 = open(b47, "w")
	for batch in b42[:3]:
		b29 = tf.placeholder("float", [None, b23.shape[1]])
		b30 = tf.placeholder("float", [None, b23.shape[1]])
		b31 = tf.nn.l2_normalize(b29, dim=0)
		b32 = tf.nn.l2_normalize(b30, dim=0)
		b33 = tf.matmul(b31, tf.transpose(b32))
		b34 = tf.arg_max(b33, dimension=0)
		b35 = tf.global_variables_initializer()
		with tf.Session() as sess:
		    sess.fonk7(b35)
		    b44 = time.time()
		    print("Evaluating tensorflow KNN")
		    b36 = sess.fonk7( b33 , feed_dict={b29: X_train, b30: batch})
		    b36 = tf.transpose(b36)
		    values, b37 = sess.fonk7(tf.nn.top_k(b36, a1))
		    b38 = []
		    for top in b37:
		    	b39 = []
		    	for neighbor in top:
		    		b39.append(Y_train[neighbor])
		    	b38.append(mode(b39)[0][0])
		    for b34 in b38:
		    	if b34 >0 :
		    		b43.write('+1\n')
		    	else:
		    		b43.write('-1\n')
		ops.reset_default_graph()
	for batch in b42[3:]:
		b29 = tf.placeholder("float", [None, b23.shape[1]])
		b30 = tf.placeholder("float", [None, b23.shape[1]])
		b31 = tf.nn.l2_normalize(b29, dim=0)
		b32 = tf.nn.l2_normalize(b30, dim=0)
		b33 = tf.matmul(b31, tf.transpose(b32))
		b34 = tf.arg_max(b33, dimension=0)
		b35 = tf.global_variables_initializer()
		with tf.Session() as sess:
		    sess.fonk7(b35)
		    b44 = time.time()
		    print("Evaluating tensorflow KNN")
		    b36 = sess.fonk7( b33 , feed_dict={b29: X_train, b30: batch})
		    b36 = tf.transpose(b36)
		    values, b37 = sess.fonk7(tf.nn.top_k(b36, a1))
		    b38 = []
		    for top in b37:
		    	b39 = []
		    	for neighbor in top:
		    		b39.append(Y_train[neighbor])
		    	b38.append(mode(b39)[0][0])
		    for b34 in b38:
		    	if b34 >0 :
		    		b43.write('+1\n')
		    	else:
		    		b43.write('-1\n')
		ops.reset_default_graph()
def fonk7(b46, b47):
	b24, b23, b22 = fonk4()
	if b46:
		fonk5(b24, b23, b22)
	else:
		fonk6(b24, b23, b22, b47)
if b45 = = "__main__":
	b46 = False
	b47 = "test.dat"
	fonk7(b46, b47)