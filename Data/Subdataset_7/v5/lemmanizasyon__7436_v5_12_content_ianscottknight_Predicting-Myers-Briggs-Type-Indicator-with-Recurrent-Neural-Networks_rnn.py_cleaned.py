import os
import numpy as np
import pandas as pd
import csv
from keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Embedding
from keras.optimizers import Adam
from keras.preprocessing import sequence
import tensorflow as tf
b1 = "models"
b2 = "b9"
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
def fonk1(dimension, data_type):
    b9 = []
    b10 = []
    for trait in dimension:
        b11 = os.path.join(b2, "{}_{}.csv".format(data_type, trait))
        with open(b11, "r") as file:
            b12 = csv.b12(file)
            for row in b12:
                for post in row:
                    b9.append(post)
                    b10.append(0 if trait[0] == dimension[k][0] else 1)
    return b9, b10
def fonk2(text, b41, b42, b43, b44):
    b13 = []
    for post in text:
        b14 = post.lower()
        for b15 in b41:
            b15 = b15.lower()
            b14 = b14.replace(" " + b15, "")
        b14 = " ".join([b43.lemmatize(b50) for b50 in b14.split(" ") if b50 not in b42])
        b13.append(b14)
    return np.array(b13), b44.texts_to_sequences(b13)
def fonk3(b44, b48, top_words, embedding_vector_length):
    b16 = np.zeros((top_words, embedding_vector_length))
    for b50, i in b44.word_index.items():
        if i < top_words:
            b17 = b48.get(b50)
            if b17 is not None:
                b16[i] = b17
    return b16
def fonk4(top_words, embedding_vector_length, max_post_length, b16, dropout_rate):
    b18 = Sequential()
    b18.add(Embedding(top_words, embedding_vector_length, b19 = max_post_length, weights=[b16], mask_zero=True, trainable=True))
    b18.add(LSTM(embedding_vector_length, b20 = dropout_rate, recurrent_dropout=dropout_rate, b21="sigmoid", kernel_initializer="zeros"))
    b18.add(Dense(1, b21 = "sigmoid"))
    b22 = Adam(lr=a5, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
    b18.compile(b23 = "binary_crossentropy", b22=b22, metrics=["accuracy"])
    return b18
def fonk5(b18, b25, b26, x_test, b40, preprocess_fn, b34, batch_size, sample_size, cross_validation):
    if sample_size is not None:
        b24 = random.sample(range(len(b25)), sample_size)
        b25 = [b25[i] for i in b24]
        b26 = [b26[i] for i in b24]
    b27 = preprocess_fn(b25)
    b28 = preprocess_fn(x_test)
    if cross_validation:
        b29 = KFold(n_splits=6)
        b30 = []
        b31 = np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in b29.split(b25):
            x_train_k, b32 = b25[train_indices], b26[train_indices]
            x_test_k, b33 = b25[test_indices], b26[test_indices]
            b18.fit(b27(x_train_k), b32, b34 = b34, batch_size=batch_size)
            b35 = b18.predict_classes(b28(x_test_k))
            b31 += confusion_matrix(b33, b35)
            b36 = accuracy_score(b33, b35)
            b30.append(b36)
        return np.array(b30), b31
    else:
        b18.fit(b27(b25), b26, b34 = b34, batch_size=batch_size)
        b37 = b18.predict_classes(b28(x_test))
        b38 = confusion_matrix(b40, b37)
        b39 = accuracy_score(b40, b37)
        return b39, b38
def fonk6():
    for dimension in b4:
        b25, b26 = fonk1(b4, "train")
        x_test, b40 = fonk1(b4, "test")
        b41 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
        b42 = stopwords.words("english")
        b43 = WordNetLemmatizer()
        b44 = Tokenizer(num_words=a2, filters="")
        b44.fit_on_texts(b25 + x_test)
        x_train_lemmatized, b45 = fonk2(b25, b41, b42, b43, b44)
        x_test_lemmatized, b46 = fonk2(x_test, b41, b42, b43, b44)
        b47 = pd.DataFrame(b9={"x": x_train_lemmatized, "y": b26})
        b47 = b47.sample(frac=1).reset_index(drop=True)
        b48 = dict()
        with open(b3) as f:
            for line in f:
                b49 = line.split()
                b50 = b49[0]
                b48[b50] = np.asarray(b49[1:], b51 = "float32")
        print("Loaded {} b50 vectors.".format(len(b48)))
        b16 = fonk3(b44, b48, a2, a4)
        with tf.device("/gpu:0"):
            b18 = fonk4(a2, a4, a3, b16, a6)
            if b5:
                b55, b38 = fonk5(b18, x_train_lemmatized, b26, x_test_lemmatized, b40,
                                                       lambda x: sequence.pad_sequences(b44.texts_to_sequences(x), b52 = a3),
                                                       a7, a1, None, b5)
                with open(os.path.join(b2, "rnn_cross_validation_{}.txt".format(dimension)), "w") as f:
                    f.write("*** {}/{} TRAINING SET CROSS VALIDATION (POSTS) ***\n".format(dimension[0], dimension[1]))
                    f.write("Total posts classified: {}\n".format(len(b25)))
                    f.write("Accuracy: {}\n".format(b55.mean()))
                    f.write("Confusion matrix: \n")
                    f.write(np.array2string(b38, b53 = ", "))
            else:
                b39, b38 = fonk5(b18, x_train_lemmatized, b26, x_test_lemmatized, b40,
                                                      lambda x: sequence.pad_sequences(b44.texts_to_sequences(x), b52 = a3),
                                                      a7, a1, b6, b5)
                with open(os.path.join(b1, "rnn_accuracy_{}.txt".format(dimension)), "w") as f:
                    f.write("*** {}/{} TEST SET CLASSIFICATION (POSTS) ***\n".format(dimension[0], dimension[1]))
                    f.write("Total posts classified: {}\n".format(len(x_test)))
                    f.write("Accuracy: {}\n".format(b39))
                    f.write("Confusion matrix: \n")
                    f.write(np.array2string(b38, b53 = ", "))
                print("\nWrote training / test results for {} here: {}\n".format(dimension, os.path.join(b1, 'rnn_accuracy_{}.txt'.format(dimension))))
                if b7:
                    a8 = 500
                    b54 = b18.predict_proba(sequence.pad_sequences(b44.texts_to_sequences(x_test_lemmatized), b52=a3))
                    b55 = []
                    b56 = []
                    for i, prob in enumerate(b54, 0):
                        b55.append(prob[0])
                        b56.append(i)
                    b57 = sorted(zip(b55, b56))
                    b58 = b57[:a8]
                    b59 = b57[-a8:]
                    with open(os.path.join(b2, "extreme_examples_{}.txt".format(dimension[0])), "w") as f:
                        for prob, i in b58:
                            f.write(x_test_lemmatized[i] + "\n")
                            f.write("\n")
                    with open(os.path.join(b2, "extreme_examples_{}.txt".format(dimension[1])), "w") as f:
                        for prob, i in b59:
                            f.write(x_test_lemmatized[i] + "\n")
                            f.write("\n")
                b18.save(os.path.join(b1, "rnn_model_{}.h5".format(dimension)))
                with open(os.path.join(b1, "rnn_tokenizer_{}.pkl".format(dimension)), "wb") as f:
                    pickle.dump(b44, f, b60 = pickle.HIGHEST_PROTOCOL)
if b61 = = "__main__":
    fonk6()