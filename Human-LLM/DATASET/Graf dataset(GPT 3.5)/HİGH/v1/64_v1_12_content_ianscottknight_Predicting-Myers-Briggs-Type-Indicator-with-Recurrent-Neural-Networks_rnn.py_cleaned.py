import os
import numpy as np
import pandas as pd
import csv
import random
import pickle
import collections
import tensorflow as tf
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
from keras.optimizers import Adam
b1 = "models"
b2 = "data"
b3 = os.path.join(b2, "glove.6B.50d.txt")
b4 = ["IE", "NS", "FT", "PJ"]
a1 = 128
a2 = 2500
a3 = 40
a4 = 50
a5 = 0.01
a6 = 0.1
a7 = 1
b5 = False
b6 = True
b7 = True
b8 = True
def fonk1(dimension):
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    with open(os.path.join(b2, f"train_{dimension[0]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b9.append(post)
                b10.append(0)
    with open(os.path.join(b2, f"train_{dimension[1]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b9.append(post)
                b10.append(1)
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b11.append(post)
                b12.append(0)
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b11.append(post)
                b12.append(1)
    return b9, b10, b11, b12
def fonk2(x, b25, b26, b27):
    b14 = []
    for post in x:
        b15 = post.lower()
        for b16 in b25:
            b16 = b16.lower()
            b15 = b15.replace(" " + b16, "")
        b15 = " ".join([b27.fonk2(b32) for b32 in b15.split(" ") if b32 not in b26])
        b14.append(b15)
    return np.array(b14)
def fonk3(x, b28, a2, a3):
    b17 = b28.texts_to_sequences(x)
    return sequence.pad_sequences(b17, b18 = a3)
def fonk4(a2, a4, a3, a6, a5):
    b19 = Sequential()
    b19.add(Embedding(a2, a4, b20 = a3, mask_zero=True, trainable=True))
    b19.add(LSTM(a4, b21 = a6, recurrent_dropout=a6, b22="sigmoid", kernel_initializer="zeros"))
    b19.add(Dense(1, b22 = "sigmoid"))
    b23 = Adam(lr=a5, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    b19.compile(b24 = "binary_crossentropy", b23=b23, metrics=["accuracy"])
    return b19
def fonk5():
    for k in range(len(b4)):
        b9, b10, b11, b12 = fonk1(b4[k])
        b25 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
        b26 = stopwords.words("english")
        b27 = WordNetLemmatizer()
        b28 = Tokenizer(num_words=a2, filters="")
        b28.fit_on_texts(b9 + b11)
        b9 = fonk2(b9, b25, b26, b27)
        b11 = fonk2(b11, b25, b26, b27)
        b29 = pd.DataFrame(data={"x": b9, "y": b10})
        b29 = b29.sample(frac=1).reset_index(drop=True)
        if b6:
            b29 = b29.head(10000)
        b30 = dict()
        with open(b3) as f:
            for line in f:
                b31 = line.split()
                b32 = b31[0]
                b30[b32] = np.asarray(b31[1:], b33 = "float32")
        print(f"Loaded {len(b30)} b32 vectors.")
        b34 = np.zeros((a2, a4))
        for b32, i in b28.word_index.items():
            if i < a2:
                b35 = b30.get(b32)
                if b35 is not None:
                    b34[i] = b35
        with tf.device("/gpu:0"):
            b19 = fonk4(a2, a4, a3, a6, a5)
            print(b19.summary())
            if b5:
                b36 = KFold(n_splits=6)
                b37 = []
                b38 = np.array([[0, 0], [0, 0]])
                for train_indices, test_indices in b36:
                    b39 = b29.iloc[train_indices]["x"].b31
                    b40 = b29.iloc[train_indices]["y"].b31
                    b41 = b29.iloc[test_indices]["x"].b31
                    b42 = b29.iloc[test_indices]["y"].b31
                    b19.fit(fonk3(b39, b28, a2, a3), b40, b43 = a7, batch_size=a1)
                    b44 = b19.predict_classes(fonk3(b41, b28, a2, a3))
                    b38 += confusion_matrix(b42, b44)
                    b45 = accuracy_score(b42, b44)
                    b37.append(b45)
                with open(os.path.join(b2, f"rnn_cross_validation_{b4[k]}.txt"), "w") as f:
                    f.write(f"*** {b4[k][0]}/{b4[k][1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
                    f.write(f"Total posts classified: {len(b9)}\n")
                    f.write(f"Accuracy: {sum(b37) / len(b37)}\n")
                    f.write("Confusion matrix: \n")
                    f.write(np.array2string(b38, b46 = ", "))
            b19.fit(fonk3(b29["x"].b31, b28, a2, a3), b29["y"].b31, b43 = a7, batch_size=a1)
            b47 = b19.predict_classes(fonk3(b11, b28, a2, a3))
            b48 = confusion_matrix(b12, b47)
            b49 = accuracy_score(b12, b47)
            with open(os.path.join(b1, f"rnn_accuracy_{b4[k]}.txt"), "w") as f:
                f.write(f"*** {b4[k][0]}/{b4[k][1]} TEST SET CLASSIFICATION (POSTS) ***\n")
                f.write(f"Total posts classified: {len(b11)}\n")
                f.write(f"Accuracy: {b49}\n")
                f.write("Confusion matrix: \n")
                f.write(np.array2string(b48, b46 = ", "))
            print(f"\nWrote training / test results for {b4[k]} here: {os.path.join(b1, 'rnn_accuracy_{b4[k]}.txt')}\n")
            if b7:
                a8 = 500
                b50 = b19.predict_proba(fonk3(b11, b28, a2, a3))
                b51 = []
                b52 = []
                for i, prob in enumerate(b50, 0):
                    b51.append(prob[0])
                    b52.append(i)
                b53 = sorted(zip(b51, b52))
                b54 = b53[:a8]
                b55 = b53[-a8:]
                with open(os.path.join(b2, f"extreme_examples_{b4[k][0]}.txt"), "w") as f:
                    for prob, i in b54:
                        f.write(b11[i] + "\n")
                        f.write("\n")
                with open(os.path.join(b2, f"extreme_examples_{b4[k][1]}.txt"), "w") as f:
                    for prob, i in b55:
                        f.write(b11[i] + "\n")
                        f.write("\n")
            b19.save(os.path.join(b1, f"rnn_model_{b4[k]}.h5"))
            with open(os.path.join(b1, f"rnn_tokenizer_{b4[k]}.pkl"), "wb") as f:
                pickle.dump(b28, f, b56 = pickle.HIGHEST_PROTOCOL)
if b57 = = "__main__":
    fonk5()