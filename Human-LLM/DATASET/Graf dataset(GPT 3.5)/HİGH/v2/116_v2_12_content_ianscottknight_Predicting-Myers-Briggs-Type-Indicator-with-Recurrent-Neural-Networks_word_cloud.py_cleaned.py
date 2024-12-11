import os
import numpy as np
import pandas as pd
import csv
import pickle
import tensorflow as tf
from nltk import word_tokenize
from keras.preprocessing.text import Tokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from keras.preprocessing import sequence
b1 = "models"
b2 = "data"
b3 = ["IE", "NS", "FT", "PJ"]
a1 = 128
a2 = 40
b4 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b4 = [x.lower() for x in b4]
b5 = WordNetLemmatizer()
b6 = set(stopwords.words("english"))
def fonk1(posts):
    b7 = []
    for post in posts:
        b8 = post.lower()
        for type_ in b4:
            b8 = b8.replace(" " + type_, "")
        b8 = " ".join(
            [b5.lemmatize(word) for word in b8.split(" ") if word not in b6]
        )
        b7.append(b8)
    return b7
def fonk2(b16, texts):
    b9 = b16.texts_to_sequences(texts)
    return sequence.pad_sequences(b9, b10 = a2)
def fonk3(dimension):
    b11 = []
    b12 = []
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            b11.append(row)
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as f:
        b13 = csv.b13(f)
        for row in b13:
            b12.append(row)
    b14 = b11 + b12
    b15 = load_model(os.path.join(b1, f"rnn_model_{dimension}.h5"))
    with open(os.path.join(b1, f"rnn_tokenizer_{dimension}.pkl"), "rb") as f:
        b16 = pickle.load(f)
    b17 = fonk1(b14)
    b18 = fonk2(b16, b17)
    b19 = b15.predict(b18)
    b20 = np.argsort(b19.flatten())
    a3 = 500
    b21 = b20[:a3]
    b22 = b20[-a3:]
    with open(os.path.join(b2, f"extreme_examples_{dimension[0]}.txt"), "w") as f:
        for i in b21:
            f.write(b17[i] + "\n\n")
    with open(os.path.join(b2, f"extreme_examples_{dimension[1]}.txt"), "w") as f:
        for i in b22:
            f.write(b17[i] + "\n\n")
if b23 = = "__main__":
    for dimension in b3:
        fonk3(dimension)