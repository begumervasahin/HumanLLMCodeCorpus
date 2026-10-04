import time
import os
import re
import numpy as np
import operator
import math
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
b1 = stopwords.words('english')
b2 = PorterStemmer()
b3 = LancasterStemmer()
b4 = WordNetLemmatizer()
a1 = 250
def fonk1(data):
    b5 = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    b6 = []
    for sent in data:
        b7 = []
        for word in sent.split():
            if word in b5.vocab:
                b7.append(b5.wv[word])
        b7 = np.array(b7)
        b7 = np.mean(b7, axis=0) if len(b7) > 0 else np.zeros(300)
        b6.append(b7)
    return b6
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b10 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    if b8:
        b10 = ' '.join([word for word in b10.split() if word not in b1])
    return b10
def fonk3(train_x, b17, b37):
    b11 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1,4))
    b12 = SelectKBest(chi2, k=7000)
    b13 = b11.fit_transform(train_x).toarray()
    b13 = b12.fit_transform(b13, b17)
    b14 = b11.transform(b37).toarray()
    b14 = b12.transform(b14)
    b15 = fonk1(train_x)
    b15 = np.array(b15)
    b16 = fonk1(b37)
    b16 = np.array(b16)
    b13 = np.concatenate((b13, b15), axis=1)
    b14 = np.concatenate((b14, b16), axis=1)
    return (b13, b14)
def fonk4():
    with open('train.dat') as f_train, open('test_data.dat') as f_test:
        b37, train_x, b17 = [], [], []
        for line in f_train:
            b18 = line.strip().split('\t')
            b19 = int(b18[0])
            b20 = fonk2(b18[1], True)
            train_x.append(b20)
            b17.append(b19)
        for line in f_test:
            b18 = line.strip().split('\t')
            b20 = fonk2(b18[0], True)
            b37.append(b20)
    b13, b14 = fonk3(train_x, b17, b37)
    b17 = np.array(b17)
    print(b13.shape, b14.shape, b13.dtype, b14.dtype)
    return (b17, b13, b14)
def fonk5(b17, train_x, b37):
    X_train, b34, Y_train, b21 = train_test_split(train_x, b17, test_size=0.20, random_state=42)
    b22 = tf.placeholder("float", [None, train_x.shape[1]])
    b23 = tf.placeholder("float", [None, train_x.shape[1]])
    b24 = tf.nn.l2_normalize(b22, axis=1)
    b25 = tf.nn.l2_normalize(b23, axis=1)
    b26 = tf.matmul(b25, tf.transpose(b24))
    b27 = tf.argmax(b26, axis=1)
    b28 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b28)
        print("Training the b5")
        b29 = sess.fonk7(b26, feed_dict={b22: X_train, b23: b34})
        b29 = tf.transpose(b29)
        values, b30 = sess.fonk7(tf.nn.top_k(b29, a1))
        b31 = []
        for top in b30:
            b32 = [Y_train[neighbor] for neighbor in top]
            b31.append(mode(b32)[0][0])
        b33 = np.sum(b31 == b21).astype(float) / len(b21)
        print("Accuracy: " + str(b33 * 100) + '%')
def fonk6(b17, train_x, b37, b40):
    X_train, Y_train, b34 = train_x, b17, b37
    b35 = [b37[:5000], b37[5000:10000], b37[10000:15000], b37[15000:20000], b37[20000:25000]]
    with open(b40, "w") as f_out:
        for batch in b35[:3]:
            b22 = tf.placeholder("float", [None, train_x.shape[1]])
            b23 = tf.placeholder("float", [None, train_x.shape[1]])
            b24 = tf.nn.l2_normalize(b22, axis=1)
            b25 = tf.nn.l2_normalize(b23, axis=1)
            b26 = tf.matmul(b25, tf.transpose(b24))
            b27 = tf.argmax(b26, axis=1)
            b28 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b28)
                b36 = time.time()
                print("Evaluating tensorflow KNN")
                b29 = sess.fonk7(b26, feed_dict={b22: X_train, b23: batch})
                b29 = tf.transpose(b29)
                values, b30 = sess.fonk7(tf.nn.top_k(b29, a1))
                b31 = []
                for top in b30:
                    b32 = [Y_train[neighbor] for neighbor in top]
                    b31.append(mode(b32)[0][0])
                for b27 in b31:
                    f_out.write('+1\n' if b27 > 0 else '-1\n')
            ops.reset_default_graph()
        for batch in b35[3:]:
            b22 = tf.placeholder("float", [None, train_x.shape[1]])
            b23 = tf.placeholder("float", [None, train_x.shape[1]])
            b24 = tf.nn.l2_normalize(b22, axis=1)
            b25 = tf.nn.l2_normalize(b23, axis=1)
            b26 = tf.matmul(b25, tf.transpose(b24))
            b27 = tf.argmax(b26, axis=1)
            b28 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b28)
                b36 = time.time()
                print("Evaluating tensorflow KNN")
                b29 = sess.fonk7(b26, feed_dict={b22: X_train, b23: batch})
                b29 = tf.transpose(b29)
                values, b30 = sess.fonk7(tf.nn.top_k(b29, a1))
                b31 = []
                for top in b30:
                    b32 = [Y_train[neighbor] for neighbor in top]
                    b31.append(mode(b32)[0][0])
                for b27 in b31:
                    f_out.write('+1\n' if b27 > 0 else '-1\n')
            ops.reset_default_graph()
def fonk7(b39, b40):
    b17, train_x, b37 = fonk4()
    if b39:
        fonk5(b17, train_x, b37)
    else:
        fonk6(b17, train_x, b37, b40)
if b38 = = "__main__":
    b39 = False
    b40 = "test.dat"
    fonk7(b39, b40)