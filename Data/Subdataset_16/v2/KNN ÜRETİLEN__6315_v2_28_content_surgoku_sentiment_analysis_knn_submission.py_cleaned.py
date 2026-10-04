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
def fonk1(data):
    b5 = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    b6 = []
    for sent in data:
        b7 = [b5.wv[word] for word in sent.split() if word in b5.vocab]
        b7 = np.mean(b7, axis=0) if b7 else np.zeros(300)
        b6.append(b7)
    return b6
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b10 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    if b8:
        b10 = ' '.join([word for word in b10.split() if word not in b1])
    return b10
def fonk3(train_x, b19, b17):
    b11 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    b12 = SelectKBest(chi2, k=7000)
    b13 = b11.fit_transform(train_x).toarray()
    b13 = b12.fit_transform(b13, b19)
    b14 = b11.transform(b17).toarray()
    b14 = b12.transform(b14)
    b15 = fonk1(train_x)
    b16 = fonk1(b17)
    b13 = np.concatenate((b13, b15), axis=1)
    b14 = np.concatenate((b14, b16), axis=1)
    return b13, b14
def fonk4():
    with open('train.dat') as f_train, open('test_data.dat') as f_test:
        train_x, b19, b17 = [], [], []
        for line in f_train:
            y, b18 = line.strip().split('\t')
            train_x.append(fonk2(b18))
            b19.append(int(y))
        for line in f_test:
            b18 = line.strip()
            b17.append(fonk2(b18))
    b13, b14 = fonk3(train_x, b19, b17)
    b19 = np.array(b19)
    print(b13.shape, b14.shape, b13.dtype, b14.dtype)
    return b19, b13, b14
def fonk5(b19, train_x, b17):
    X_train, b33, Y_train, b20 = train_test_split(train_x, b19, test_size=0.20, random_state=42)
    b21 = tf.placeholder("float", [None, train_x.shape[1]])
    b22 = tf.placeholder("float", [None, train_x.shape[1]])
    b23 = tf.nn.l2_normalize(b21, axis=1)
    b24 = tf.nn.l2_normalize(b22, axis=1)
    b25 = tf.matmul(b24, tf.transpose(b23))
    b26 = tf.argmax(b25, axis=1)
    b27 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b27)
        print("Training the b5")
        b28 = sess.fonk7(b25, feed_dict={b21: X_train, b22: b33})
        b28 = tf.transpose(b28)
        values, b29 = sess.fonk7(tf.nn.top_k(b28, a1))
        b30 = []
        for top in b29:
            b31 = [Y_train[neighbor] for neighbor in top]
            b30.append(mode(b31)[0][0])
        b32 = accuracy_score(b20, b30)
        print(f"Accuracy: {b32 * 100:.2f}%")
def fonk6(b19, train_x, b17, b37):
    X_train, Y_train, b33 = train_x, b19, b17
    b34 = [b17[i:i + 5000] for i in range(0, len(b17), 5000)]
    with open(b37, "w") as f_out:
        for batch in b34:
            b21 = tf.placeholder("float", [None, train_x.shape[1]])
            b22 = tf.placeholder("float", [None, train_x.shape[1]])
            b23 = tf.nn.l2_normalize(b21, axis=1)
            b24 = tf.nn.l2_normalize(b22, axis=1)
            b25 = tf.matmul(b24, tf.transpose(b23))
            b26 = tf.argmax(b25, axis=1)
            b27 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b27)
                print("Evaluating TensorFlow k-NN")
                b28 = sess.fonk7(b25, feed_dict={b21: X_train, b22: batch})
                b28 = tf.transpose(b28)
                values, b29 = sess.fonk7(tf.nn.top_k(b28, a1))
                b30 = []
                for top in b29:
                    b31 = [Y_train[neighbor] for neighbor in top]
                    b30.append(mode(b31)[0][0])
                for b26 in b30:
                    f_out.write(f'+1\n' if b26 > 0 else '-1\n')
            ops.reset_default_graph()
def fonk7(b36, b37):
    b19, train_x, b17 = fonk4()
    if b36:
        fonk5(b19, train_x, b17)
    else:
        fonk6(b19, train_x, b17, b37)
if b35 = = "__main__":
    b36 = False
    b37 = "test.dat"
    fonk7(b36, b37)