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
b1 = stopwords.words('english')
b2 = PorterStemmer()
b3 = LancasterStemmer()
b4 = WordNetLemmatizer()
a1 = 250
def fonk1(data, b5 = 'GoogleNews-vectors-negative300.bin'):
    b6 = gensim.models.KeyedVectors.load_word2vec_format(b5, binary=True)
    b7 = []
    for sent in data:
        b8 = [b6.wv[word] for word in sent.split() if word in b6.vocab]
        b8 = np.mean(b8, axis=0) if b8 else np.zeros(300)
        b7.append(b8)
    return b7
def fonk2(b10, b9 = True):
    b10 = re.sub('<[^<]+?>', ' ', b10)
    b11 = re.sub('[^A-Za-z0-9]+', ' ', b10.lower())
    if b9:
        b11 = ' '.join([word for word in b11.split() if word not in b1])
    return b11
def fonk3(train_x, b21, b19):
    b12 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    b13 = SelectKBest(chi2, k=7000)
    b14 = b12.fit_transform(train_x).toarray()
    b14 = b13.fit_transform(b14, b21)
    b15 = b12.transform(b19).toarray()
    b15 = b13.transform(b15)
    b16 = fonk1(train_x)
    b17 = fonk1(b19)
    b14 = np.concatenate((b14, b16), axis=1)
    b15 = np.concatenate((b15, b17), axis=1)
    return b14, b15
def fonk4(b18 = 'train.dat', test_file='test_data.dat'):
    with open(b18) as f_train, open(test_file) as f_test:
        train_x, b21, b19 = [], [], []
        for line in f_train:
            y, b20 = line.strip().split('\t')
            train_x.append(fonk2(b20))
            b21.append(int(y))
        for line in f_test:
            b20 = line.strip()
            b19.append(fonk2(b20))
    b14, b15 = fonk3(train_x, b21, b19)
    b21 = np.array(b21)
    print(b14.shape, b15.shape, b14.dtype, b15.dtype)
    return b21, b14, b15
def fonk5(b21, train_x, b19):
    X_train, b35, Y_train, b22 = train_test_split(train_x, b21, test_size=0.20, random_state=42)
    b23 = tf.placeholder("float", [None, train_x.shape[1]])
    b24 = tf.placeholder("float", [None, train_x.shape[1]])
    b25 = tf.nn.l2_normalize(b23, axis=1)
    b26 = tf.nn.l2_normalize(b24, axis=1)
    b27 = tf.matmul(b26, tf.transpose(b25))
    b28 = tf.argmax(b27, axis=1)
    b29 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b29)
        print("Training the b6")
        b30 = sess.fonk7(b27, feed_dict={b23: X_train, b24: b35})
        b30 = tf.transpose(b30)
        values, b31 = sess.fonk7(tf.nn.top_k(b30, a1))
        b32 = []
        for top in b31:
            b33 = [Y_train[neighbor] for neighbor in top]
            b32.append(mode(b33)[0][0])
        b34 = accuracy_score(b22, b32)
        print(f"Accuracy: {b34 * 100:.2f}%")
def fonk6(b21, train_x, b19, b39):
    X_train, Y_train, b35 = train_x, b21, b19
    b36 = [b19[i:i + 5000] for i in range(0, len(b19), 5000)]
    with open(b39, "w") as f_out:
        for batch in b36:
            b23 = tf.placeholder("float", [None, train_x.shape[1]])
            b24 = tf.placeholder("float", [None, train_x.shape[1]])
            b25 = tf.nn.l2_normalize(b23, axis=1)
            b26 = tf.nn.l2_normalize(b24, axis=1)
            b27 = tf.matmul(b26, tf.transpose(b25))
            b28 = tf.argmax(b27, axis=1)
            b29 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b29)
                print("Evaluating TensorFlow k-NN")
                b30 = sess.fonk7(b27, feed_dict={b23: X_train, b24: batch})
                b30 = tf.transpose(b30)
                values, b31 = sess.fonk7(tf.nn.top_k(b30, a1))
                b32 = []
                for top in b31:
                    b33 = [Y_train[neighbor] for neighbor in top]
                    b32.append(mode(b33)[0][0])
                for b28 in b32:
                    f_out.write(f'+1\n' if b28 > 0 else '-1\n')
            ops.reset_default_graph()
def fonk7(b38, b39):
    b21, train_x, b19 = fonk4()
    if b38:
        fonk5(b21, train_x, b19)
    else:
        fonk6(b21, train_x, b19, b39)
if b37 = = "__main__":
    b38 = False
    b39 = "test.dat"
    fonk7(b38, b39)