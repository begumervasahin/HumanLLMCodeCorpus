import time
import os
import re
import numpy as np
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import mode
import tensorflow as tf
from tensorflow.python.framework import ops
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
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
        b7 = []
        for word in sent.split():
            if word in b5.vocab:
                b7.append(b5.wv[word])
        if b7:
            b7 = np.mean(b7, axis=0)
            b6.append(b7)
    return b6
def fonk2(b9, b8 = True):
    b9 = re.sub('<[^<]+?>', ' ', b9)
    b10 = re.sub('[^A-Za-z0-9]+', ' ', b9.lower())
    if b8:
        b10 = ' '.join([word for word in b10.split() if word not in b1])
    return b10
def fonk3(b21, b22, b23):
    b11 = TfidfVectorizer(min_df=0.001, max_df=0.98, ngram_range=(1, 4))
    b12 = SelectKBest(chi2, k=7000)
    b13 = b11.fit_transform(b21).toarray()
    b13 = b12.fit_transform(b13, b22)
    b14 = b11.transform(b23).toarray()
    b14 = b12.transform(b14)
    b15 = [fonk2(sent) for sent in b21]
    b16 = [fonk2(sent) for sent in b23]
    b17 = fonk1(b15)
    b17 = np.array(b17)
    b18 = fonk1(b16)
    b18 = np.array(b18)
    b13 = np.concatenate((b13, b17), axis=1)
    b14 = np.concatenate((b14, b18), axis=1)
    return b13, b14
def fonk4():
    b19 = 'train.dat'
    b20 = 'test_data.dat'
    b21 = []
    b22 = []
    b23 = []
    with open(b19, 'r') as f_train:
        for line in f_train:
            b24 = line.strip().split('\t')
            b25 = int(b24[0])
            b26 = b24[1]
            b26 = fonk2(b26, True)
            b21.append(b26)
            b22.append(b25)
    with open(b20, 'r') as f_test:
        for line in f_test:
            b24 = line.strip().split('\t')
            b26 = b24[0]
            b26 = fonk2(b26, True)
            b23.append(b26)
    b13, b14 = fonk3(b21, b22, b23)
    b22 = np.array(b22)
    return b22, b13, b14
def fonk5(b22, b21, b23):
    X_train, b40, Y_train, b27 = train_test_split(b21, b22, test_size=0.20, random_state=42)
    b28 = tf.placeholder("float", [None, b21.shape[1]])
    b29 = tf.placeholder("float", [None, b21.shape[1]])
    b30 = tf.nn.l2_normalize(b28, dim=0)
    b31 = tf.nn.l2_normalize(b29, dim=0)
    b32 = tf.matmul(b30, tf.transpose(b31))
    b33 = tf.argmax(b32, dimension=0)
    b34 = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.fonk7(b34)
        print("Training the b5")
        b35 = sess.fonk7(b32, feed_dict={b28: X_train, b29: b40})
        b35 = tf.transpose(b35)
        values, b36 = sess.fonk7(tf.nn.top_k(b35, a1))
        b37 = []
        for top in b36:
            b38 = []
            for neighbor in top:
                b38.append(Y_train[neighbor])
            b37.append(mode(b38)[0][0])
        b39 = np.sum(b37 == b27).astype(float) / len(b27)
        print("Accuracy: {:.2f}%".format(b39 * 100))
def fonk6(b22, b21, b23, b44):
    X_train, Y_train, b40 = b21, b22, b23
    b41 = [b23[i:i + 5000] for i in range(0, len(b23), 5000)]
    with open(b44, "w") as f_out:
        for batch in b41:
            b28 = tf.placeholder("float", [None, b21.shape[1]])
            b29 = tf.placeholder("float", [None, b21.shape[1]])
            b30 = tf.nn.l2_normalize(b28, dim=0)
            b31 = tf.nn.l2_normalize(b29, dim=0)
            b32 = tf.matmul(b30, tf.transpose(b31))
            b33 = tf.argmax(b32, dimension=0)
            b34 = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.fonk7(b34)
                print("Evaluating tensorflow KNN")
                b35 = sess.fonk7(b32, feed_dict={b28: X_train, b29: batch})
                b35 = tf.transpose(b35)
                values, b36 = sess.fonk7(tf.nn.top_k(b35, a1))
                b37 = []
                for top in b36:
                    b38 = []
                    for neighbor in top:
                        b38.append(Y_train[neighbor])
                    b37.append(mode(b38)[0][0])
                for b33 in b37:
                    if b33 > 0:
                        f_out.write('+1\n')
                    else:
                        f_out.write('-1\n')
                ops.reset_default_graph()
def fonk7(b43, b44):
    b22, b21, b23 = fonk4()
    if b43:
        fonk5(b22, b21, b23)
    else:
        fonk6(b22, b21, b23, b44)
if b42 = = "__main__":
    b43 = False
    b44 = "test.dat"
    fonk7(b43, b44)