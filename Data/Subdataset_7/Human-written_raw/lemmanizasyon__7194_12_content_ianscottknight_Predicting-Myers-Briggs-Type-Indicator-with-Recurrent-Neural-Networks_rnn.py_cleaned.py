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
for k in range(len(b4)):
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    with open(
        os.path.join(b2, "train_{}.csv".format(b4[k][0])), "r"
    ) as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b9.append(post)
                b10.append(0)
    with open(
        os.path.join(b2, "train_{}.csv".format(b4[k][1])), "r"
    ) as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b9.append(post)
                b10.append(1)
    with open(os.path.join(b2, "test_{}.csv".format(b4[k][0])), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b11.append(post)
                b12.append(0)
    with open(os.path.join(b2, "test_{}.csv".format(b4[k][1])), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            for post in row:
                b11.append(post)
                b12.append(1)
    b14 = [
        "INFJ",
        "ENTP",
        "INTP",
        "INTJ",
        "ENTJ",
        "ENFJ",
        "INFP",
        "ENFP",
        "ISFP",
        "ISTP",
        "ISFJ",
        "ISTJ",
        "ESTP",
        "ESFP",
        "ESTJ",
        "ESFJ",
    ]
    b15 = stopwords.words("english")
    b16 = WordNetLemmatizer()
    b17 = Tokenizer(num_words=a2, filters="")
    b17.fit_on_texts(b9 + b11)
    def fonk1(x):
        b18 = []
        for post in x:
            b19 = post.lower()
            for b20 in b14:
                b20 = b20.lower()
                b19 = b19.replace(" " + b20, "")
            b19 = " ".join(
                [
                    b16.fonk1(b26)
                    for b26 in b19.split(" ")
                    if (b26 not in b15)
                ]
            )
            b18.append(b19)
        return np.array(b18)
    def fonk2(x):
        b18 = fonk1(x)
        b21 = b17.texts_to_sequences(b18)
        return sequence.pad_sequences(b21, b22 = a3)
    b9 = fonk1(b9)
    b11 = fonk1(b11)
    b23 = pd.DataFrame(data={"x": b9, "y": b10})
    b23 = b23.sample(frac=1).reset_index(drop=True)
    if b6:
        b23 = b23.head(10000)
    b24 = dict()
    with open(b3) as f:
        for line in f:
            b25 = line.split()
            b26 = b25[0]
            b24[b26] = np.asarray(b25[1:], b27 = "float32")
    print("Loaded {} b26 vectors.".format(len(b24)))
    b28 = np.zeros((a2, a4))
    for b26, i in b17.word_index.items():
        if i < a2:
            b29 = b24.get(b26)
            if b29 is not None:
                b28[i] = b29
    with tf.device("/gpu:0"):
        b30 = Sequential()
        b30.add(
            Embedding(
                a2,
                a4,
                b31 = a3,
                b32 = [b28],
                b33 = True,
                b34 = True,
            )
        )
        b30.add(
            LSTM(
                a4,
                b35 = a6,
                b36 = a6,
                b37 = "sigmoid",
                b38 = "zeros",
            )
        )
        b30.add(Dense(1, b37 = "sigmoid"))
        b39 = Adam(lr=a5, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
        b30.compile(
            b40 = "binary_crossentropy", b39=b39, metrics=["accuracy"]
        )
        print(b30.summary())
        if b5:
            b41 = KFold(n_splits=6)
            b42 = []
            b43 = np.array([[0, 0], [0, 0]])
            for train_indices, test_indices in b41:
                b44 = b23.iloc[train_indices]["x"].b25
                b45 = b23.iloc[train_indices]["y"].b25
                b46 = b23.iloc[test_indices]["x"].b25
                b47 = b23.iloc[test_indices]["y"].b25
                b30.fit(
                    fonk2(b44),
                    b45,
                    b48 = a7,
                    b49 = a1,
                )
                b50 = b30.predict_classes(fonk2(b46))
                b43 += confusion_matrix(b47, b50)
                b51 = accuracy_score(b47, b50)
                b42.append(b51)
            with open(
                os.path.join(
                    b2, "rnn_cross_validation_{}.txt".format(b4[k])
                ),
                "w",
            ) as f:
                f.write(
                    "*** {}/{} TRAINING SET CROSS VALIDATION (POSTS) ***\n".format(
                        b4[k][0], b4[k][1]
                    )
                )
                f.write("Total posts classified: {}\n".format(len(b9)))
                f.write("Accuracy: {}\n".format(sum(b42) / len(b42)))
                f.write("Confusion matrix: \n")
                f.write(np.array2string(b43, b52 = ", "))
        b30.fit(
            fonk2(b23["x"].b25),
            b23["y"].b25,
            b48 = a7,
            b49 = a1,
        )
        b53 = b30.predict_classes(fonk2(b11))
        b54 = confusion_matrix(b12, b53)
        b55 = accuracy_score(b12, b53)
        with open(
            os.path.join(b1, "rnn_accuracy_{}.txt".format(b4[k])), "w"
        ) as f:
            f.write(
                "*** {}/{} TEST SET CLASSIFICATION (POSTS) ***\n".format(
                    b4[k][0], b4[k][1]
                )
            )
            f.write("Total posts classified: {}\n".format(len(b11)))
            f.write("Accuracy: {}\n".format(b55))
            f.write("Confusion matrix: \n")
            f.write(np.array2string(b54, b52 = ", "))
        print(
            f"\nWrote training / test results for {b4[k]} here: {os.path.join(b1, 'rnn_accuracy_{}.txt'.format(b4[k]))}\n"
        )
        if b7:
            a8 = 500
            b56 = b30.predict_proba(fonk2(b11))
            b57 = []
            b58 = []
            for i, prob in enumerate(b56, 0):
                b57.append(prob[0])
                b58.append(i)
            b59 = sorted(zip(b57, b58))
            b60 = b59[:a8]
            b61 = b59[-a8:]
            with open(
                os.path.join(
                    b2, "extreme_examples_{}.txt".format(b4[k][0])
                ),
                "w",
            ) as f:
                for prob, i in b60:
                    f.write(b11[i] + "\n")
                    f.write("\n")
            with open(
                os.path.join(
                    b2, "extreme_examples_{}.txt".format(b4[k][1])
                ),
                "w",
            ) as f:
                for prob, i in b61:
                    f.write(b11[i] + "\n")
                    f.write("\n")
        b30.save(os.path.join(b1, "rnn_model_{}.h5".format(b4[k])))
        with open(
            os.path.join(b1, "rnn_tokenizer_{}.pkl".format(b4[k])), "wb"
        ) as f:
            pickle.dump(b17, f, b62 = pickle.HIGHEST_PROTOCOL)