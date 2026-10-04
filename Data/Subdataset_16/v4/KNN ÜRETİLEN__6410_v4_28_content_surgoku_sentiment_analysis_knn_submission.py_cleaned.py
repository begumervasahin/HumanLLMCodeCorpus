import time
import os
import re
import numpy as np
import gensim
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
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
        b7 = [b5[word] for word in sent.split() if word in b5]
        b7 = np.mean(b7, axis=0) if b7 else np.zeros(300)
        b6.append(b7)
    return np.array(b6)
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b9 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    return b9
def fonk3(b22, b23, b24):
    b10 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    b11 = SelectKBest(chi2, k=7000)
    b12 = b10.fit_transform(b22).toarray()
    b12 = b11.fit_transform(b12, b23)
    b13 = b10.transform(b24).toarray()
    b13 = b11.transform(b13)
    b14 = [' '.join([word for word in sent.split() if word not in b1]) for sent in b22]
    b15 = [' '.join([word for word in sent.split() if word not in b1]) for sent in b24]
    b16 = fonk1(b14)
    b17 = fonk1(b15)
    b18 = np.concatenate((b12, b16), axis=1)
    b19 = np.concatenate((b13, b17), axis=1)
    return b18, b19
def fonk4():
    with open('train.dat') as f_train:
        b20 = [line.strip().split('\t') for line in f_train]
    with open('b21.dat') as f_test:
        b21 = [line.strip() for line in f_test]
    b22 = [fonk2(sample[1], True) for sample in b20]
    b23 = [int(sample[0]) for sample in b20]
    b24 = [fonk2(sample, True) for sample in b21]
    train_x_fit, b25 = fonk3(b22, b23, b24)
    print(train_x_fit.shape, b25.shape, train_x_fit.dtype, b25.dtype)
    return np.array(b23), train_x_fit, b25
def fonk5(b23, b22, b24):
    X_train, X_test, Y_train, b26 = train_test_split(b22, b23, test_size=0.20, random_state=42)
    b27 = tf.placeholder(tf.float32, [None, b22.shape[1]])
    b28 = tf.placeholder(tf.float32, [None, b22.shape[1]])
    b29 = tf.nn.l2_normalize(b27, axis=1)
    b30 = tf.nn.l2_normalize(b28, axis=1)
    b31 = tf.matmul(b30, tf.transpose(b29))
    b32 = tf.argmax(b31, axis=1)
    b33 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b33)
        print("Training the b5")
        b34 = sess.fonk7(b31, feed_dict={b27: X_train, b28: X_test})
        b34 = tf.transpose(b34)
        values, b35 = sess.fonk7(tf.nn.top_k(b34, a1))
        b36 = []
        for top in b35:
            b37 = [Y_train[neighbor] for neighbor in top]
            b36.append(mode(b37)[0][0])
        b38 = np.mean(b36 == b26)
        print(f"Accuracy: {b38 * 100:.2f}%")
def fonk6(b23, b22, b24, b42):
    b39 = [b24[i:i+5000] for i in range(0, len(b24), 5000)]
    with open(b42, "w") as f_out:
        for batch in b39:
            b27 = tf.placeholder(tf.float32, [None, b22.shape[1]])
            b28 = tf.placeholder(tf.float32, [None, b22.shape[1]])
            b29 = tf.nn.l2_normalize(b27, axis=1)
            b30 = tf.nn.l2_normalize(b28, axis=1)
            b31 = tf.matmul(b30, tf.transpose(b29))
            b32 = tf.argmax(b31, axis=1)
            b33 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b33)
                print("Evaluating tensorflow KNN")
                b34 = sess.fonk7(b31, feed_dict={b27: b22, b28: batch})
                b34 = tf.transpose(b34)
                values, b35 = sess.fonk7(tf.nn.top_k(b34, a1))
                b36 = []
                for top in b35:
                    b37 = [b23[neighbor] for neighbor in top]
                    b36.append(mode(b37)[0][0])
                for b32 in b36:
                    f_out.write('+1\n' if b32 > 0 else '-1\n')
            ops.reset_default_graph()
def fonk7(b41, b42):
    b23, b22, b24 = fonk4()
    if b41:
        fonk5(b23, b22, b24)
    else:
        fonk6(b23, b22, b24, b42)
if b40 = = "__main__":
    b41 = False
    b42 = "test.dat"
    fonk7(b41, b42)