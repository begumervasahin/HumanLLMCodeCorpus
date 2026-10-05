import os
import numpy as np
import pandas as pd
import csv
import random
import pickle
import collections
import tensorflow as tf
from nltk import word_tokenize
from keras.preprocessing.text import Tokenizer
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Bidirectional
from keras.layers import GRU
from keras.layers import SimpleRNN
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.preprocessing import text
from keras.models import load_model
b1 = "models"
b2 = "data"
b3 = ["IE", "NS", "FT", "PJ"]
a1 = 128
a2 = 2500
a3 = 40
a4 = 50
b4 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b4 = [x.lower() for x in b4]
b5 = WordNetLemmatizer()
b6 = stopwords.words("english")
def fonk1(x):
    b7 = []
    for user in x:
        for post in user:
            b8 = post.lower()
            for type_ in b4:
                b8 = b8.replace(" " + type_, "")
            b8 = " ".join(
                [
                    b5.fonk1(word)
                    for word in b8.split(" ")
                    if (word not in b6)
                ]
            )
            b7.append(b8)
    return np.array(b7)
for k in range(len(b3)):
    b9 = []
    b10 = []
    with open(os.path.join(b2, "test_{}.csv".format(b3[k][0])), "r") as f:
        b11 = csv.b11(f)
        for row in b11:
            b9.append(row)
    with open(os.path.join(b2, "test_{}.csv".format(b3[k][1])), "r") as f:
        b11 = csv.b11(f)
        for row in b11:
            b10.append(row)
    b12 = b9 + b10
    b13 = load_model(os.path.join(b1, "rnn_model_{}.h5".format(b3[k])))
    b14 = None
    with open(
        os.path.join(b1, "rnn_tokenizer_{}.pkl".format(b3[k])), "rb"
    ) as f:
        b14 = pickle.load(f)
    def fonk2(x):
        b7 = fonk1(x)
        b15 = b14.texts_to_sequences(b7)
        return sequence.pad_sequences(b15, b16 = a3)
    a5 = 500
    b17 = b13.predict_proba(fonk2(b12))
    b18 = []
    b19 = []
    for i, prob in enumerate(b17, 0):
        b18.append(prob[0])
        b19.append(i)
    b20 = sorted(zip(b18, b19))
    b21 = b20[:a5]
    b22 = b20[-a5:]
    b7 = fonk1(b12)
    with open(
        os.path.join(b2, "extreme_examples_{}.txt".format(b3[k][0])), "w"
    ) as f:
        for prob, i in b21:
            f.write(b7[i] + "\n")
            f.write("\n")
    with open(
        os.path.join(b2, "extreme_examples_{}.txt".format(b3[k][1])), "w"
    ) as f:
        for prob, i in b22:
            f.write(b7[i] + "\n")
            f.write("\n")