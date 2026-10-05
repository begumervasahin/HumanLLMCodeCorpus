import os
import numpy as np
import pandas as pd
import csv
import random
import pickle
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Embedding, LSTM, Dense
from keras.optimizers import Adam
from keras.preprocessing import sequence, text
from keras.wrappers.scikit_learn import KerasClassifier
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
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
    b26, y_train, b27, b9 = [], [], [], []
    def fonk2(file_path, label):
        with open(file_path, "r") as f:
            b10 = csv.b10(f)
            for row in b10:
                for post in row:
                    b26.append(post)
                    y_train.append(label)
    fonk2(os.path.join(b2, f"train_{dimension[0]}.csv"), 0)
    fonk2(os.path.join(b2, f"train_{dimension[1]}.csv"), 1)
    fonk2(os.path.join(b2, f"test_{dimension[0]}.csv"), 0)
    fonk2(os.path.join(b2, f"test_{dimension[1]}.csv"), 1)
    return b26, y_train, b27, b9
def fonk3(x, b22, b23, b24):
    b11 = []
    for post in x:
        b12 = post.lower()
        for b13 in b22:
            b13 = b13.lower()
            b12 = b12.replace(" " + b13, "")
        b12 = " ".join([b24.fonk3(b31) for b31 in b12.split(" ") if b31 not in b23])
        b11.append(b12)
    return np.array(b11)
def fonk4(x, b25, a2, a3):
    b14 = b25.texts_to_sequences(x)
    return sequence.pad_sequences(b14, b15 = a3)
def fonk5(a2, a4, a3, a6, a5):
    b16 = Sequential()
    b16.add(Embedding(a2, a4, b17 = a3, mask_zero=True, trainable=True))
    b16.add(LSTM(a4, b18 = a6, recurrent_dropout=a6, b19="sigmoid", kernel_initializer="zeros"))
    b16.add(Dense(1, b19 = "sigmoid"))
    b20 = Adam(lr=a5, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    b16.compile(b21 = "binary_crossentropy", b20=b20, metrics=["accuracy"])
    return b16
def fonk6():
    for k in range(len(b4)):
        b26, y_train, b27, b9 = fonk1(b4[k])
        b22 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
        b23 = stopwords.words("english")
        b24 = WordNetLemmatizer()
        b25 = text.Tokenizer(num_words=a2, filters="")
        b25.fit_on_texts(b26 + b27)
        b26 = fonk3(b26, b22, b23, b24)
        b27 = fonk3(b27, b22, b23, b24)
        b28 = pd.DataFrame(data={"x": b26, "y": y_train})
        b28 = b28.sample(frac=1).reset_index(drop=True)
        if b6:
            b28 = b28.head(10000)
        b29 = dict()
        with open(b3) as f:
            for line in f:
                b30 = line.split()
                b31 = b30[0]
                b29[b31] = np.asarray(b30[1:], b32 = "float32")
        print(f"Loaded {len(b29)} b31 vectors.")
        b33 = np.zeros((a2, a4))
        for b31, i in b25.word_index.items():
            if i < a2:
                b34 = b29.get(b31)
                if b34 is not None:
                    b33[i] = b34
        with tf.device("/gpu:0"):
            b16 = fonk5(a2, a4, a3, a6, a5)
            print(b16.summary())
            if b5:
                b35 = KFold(n_splits=6)
                b36 = []
                b37 = np.array([[0, 0], [0, 0]])
                for train_indices, test_indices in b35:
                    b38 = b28.iloc[train_indices]["x"].b30
                    b39 = b28.iloc[train_indices]["y"].b30
                    b40 = b28.iloc[test_indices]["x"].b30
                    b41 = b28.iloc[test_indices]["y"].b30
                    b16.fit(fonk4(b38, b25, a2, a3), b39, b42 = a7, batch_size=a1)
                    b43 = b16.predict_classes(fonk4(b40, b25, a2, a3))
                    b37 += confusion_matrix(b41, b43)
                    b44 = accuracy_score(b41, b43)
                    b36.append(b44)
                with open(os.path.join(b2, f"rnn_cross_validation_{b4[k]}.txt"), "w") as f:
                    f.write(f"*** {b4[k][0]}/{b4[k][1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
                    f.write(f"Total posts classified: {len(b26)}\n")
                    f.write(f"Accuracy: {sum(b36) / len(b36)}\n")
                    f.write("Confusion matrix: \n")
                    f.write(np.array2string(b37, b45 = ", "))
            b16.fit(fonk4(b28["x"].b30, b25, a2, a3), b28["y"].b30, b42 = a7, batch_size=a1)
            b46 = b16.predict_classes(fonk4(b27, b25, a2, a3))
            b47 = confusion_matrix(b9, b46)
            b48 = accuracy_score(b9, b46)
            with open(os.path.join(b1, f"rnn_accuracy_{b4[k]}.txt"), "w") as f:
                f.write(f"*** {b4[k][0]}/{b4[k][1]} TEST SET CLASSIFICATION (POSTS) ***\n")
                f.write(f"Total posts classified: {len(b27)}\n")
                f.write(f"Accuracy: {b48}\n")
                f.write("Confusion matrix: \n")
                f.write(np.array2string(b47, b45 = ", "))
            print(f"\nWrote training / test results for {b4[k]} here: {os.path.join(b1, 'rnn_accuracy_{b4[k]}.txt')}\n")
            if b7:
                a8 = 500
                b49 = b16.predict_proba(fonk4(b27, b25, a2, a3))
                b50 = []
                b51 = []
                for i, prob in enumerate(b49, 0):
                    b50.append(prob[0])
                    b51.append(i)
                b52 = sorted(zip(b50, b51))
                b53 = b52[:a8]
                b54 = b52[-a8:]
                with open(os.path.join(b2, f"extreme_examples_{b4[k][0]}.txt"), "w") as f:
                    for prob, i in b53:
                        f.write(b27[i] + "\n")
                        f.write("\n")
                with open(os.path.join(b2, f"extreme_examples_{b4[k][1]}.txt"), "w") as f:
                    for prob, i in b54:
                        f.write(b27[i] + "\n")
                        f.write("\n")
            b16.save(os.path.join(b1, f"rnn_model_{b4[k]}.h5"))
            with open(os.path.join(b1, f"rnn_tokenizer_{b4[k]}.pkl"), "wb") as f:
                pickle.dump(b25, f, b55 = pickle.HIGHEST_PROTOCOL)
if b56 = = "__main__":
    fonk6()