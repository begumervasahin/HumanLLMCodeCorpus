import time
import os
import re
import numpy as np
import operator
import math
import gensim
import pickle
import nltk
import tensorflow as tf
from tensorflow.python.framework import ops
from sklearn.feature_extraction.b20 import TfidfVectorizer
from sklearn.feature_extraction.b20 import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
nltk.download('stopwords')
nltk.download('wordnet')
b1 = stopwords.words('english')
b2 = PorterStemmer()
b3 = LancasterStemmer()
b4 = WordNetLemmatizer()
a1 = 250
def fonk1(data):
    b5 = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    b6 = []
    for sent in data:
        b7 = [b5.wv[word] for word in sent.split() if word in b5.vocab]
        if b7:
            b7 = np.mean(b7, axis=0)
            b6.append(b7)
    return b6
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b10 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    return b10
def fonk3(train_x, b21, b19):
    b11 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    b12 = SelectKBest(chi2, k=7000)
    b13 = b11.fit_transform(train_x).toarray()
    b13 = b12.fit_transform(b13, b21)
    b14 = b11.transform(b19).toarray()
    b14 = b12.transform(b14)
    b15 = [' '.join([i for i in sent.split() if i not in b1]) for sent in train_x]
    b16 = [' '.join([i for i in sent.split() if i not in b1]) for sent in b19]
    b17 = fonk1(b15)
    b17 = np.array(b17)
    b18 = fonk1(b16)
    b18 = np.array(b18)
    b13 = np.concatenate((b13, b17), axis=1)
    b14 = np.concatenate((b14, b18), axis=1)
    return b13, b14
def fonk4():
    with open('train.dat') as f_train, open('test_data.dat') as f_test:
        train_x, b21, b19 = [], [], []
        for line in f_train:
            label, b20 = line.strip().split('\t')
            train_x.append(fonk2(b20, True))
            b21.append(int(label))
        for line in f_test:
            b20 = line.strip().split('\t')[0]
            b19.append(fonk2(b20, True))
    b21 = np.array(b21)
    b13, b14 = fonk3(train_x, b21, b19)
    print(b13.shape, b14.shape, b13.dtype, b14.dtype)
    return b21, b13, b14
def fonk5(b21, train_x, b19):
    X_train, b34, Y_train, b22 = train_test_split(train_x, b21, test_size=0.20, random_state=42)
    b23 = tf.placeholder("float", [None, train_x.shape[1]])
    b24 = tf.placeholder("float", [None, train_x.shape[1]])
    b25 = tf.nn.l2_normalize(b23, dim=0)
    b26 = tf.nn.l2_normalize(b24, dim=0)
    b27 = tf.matmul(b25, tf.transpose(b26))
    b28 = tf.argmax(b27, dimension=0)
    b29 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b29)
        print("Training the b5")
        b30 = sess.fonk7(b27, feed_dict={b23: X_train, b24: b34})
        b30 = tf.transpose(b30)
        values, b31 = sess.fonk7(tf.nn.top_k(b30, a1))
        b32 = [mode([Y_train[neighbor] for neighbor in top])[0][0] for top in b31]
        b33 = np.sum(b32 == b22).astype(float) / len(b22)
        print("Accuracy: {:.2f}%".format(b33 * 100))
def fonk6(b21, train_x, b19, b38):
    X_train, Y_train, b34 = train_x, b21, b19
    b35 = [b19[i:i+5000] for i in range(0, len(b19), 5000)]
    with open(b38, "w") as f_out:
        for batch in b35:
            b23 = tf.placeholder("float", [None, train_x.shape[1]])
            b24 = tf.placeholder("float", [None, train_x.shape[1]])
            b25 = tf.nn.l2_normalize(b23, dim=0)
            b26 = tf.nn.l2_normalize(b24, dim=0)
            b27 = tf.matmul(b25, tf.transpose(b26))
            b28 = tf.argmax(b27, dimension=0)
            b29 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b29)
                print("Evaluating TensorFlow KNN")
                b30 = sess.fonk7(b27, feed_dict={b23: X_train, b24: batch})
                b30 = tf.transpose(b30)
                values, b31 = sess.fonk7(tf.nn.top_k(b30, a1))
                b32 = [mode([Y_train[neighbor] for neighbor in top])[0][0] for top in b31]
                for b28 in b32:
                    f_out.write('+1\n' if b28 > 0 else '-1\n')
            ops.reset_default_graph()
def fonk7(b37, b38):
    b21, train_x, b19 = fonk4()
    if b37:
        fonk5(b21, train_x, b19)
    else:
        fonk6(b21, train_x, b19, b38)
if b36 = = "__main__":
    b37 = False
    b38 = "test.dat"
    fonk7(b37, b38)