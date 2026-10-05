import os
import numpy as np
import pandas as pd
import csv
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.models import load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
b1 = "models"
b2 = "data"
b3 = ["IE", "NS", "FT", "PJ"]
a1 = 500
a2 = 40
b4 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b4 = [type.lower() for type in b4]
b5 = WordNetLemmatizer()
b6 = set(stopwords.words("english"))
def fonk1(posts):
    b7 = []
    for user_posts in posts:
        for b8 in user_posts:
            b8 = b8.lower()
            for personality_type in b4:
                b8 = b8.replace(" " + personality_type, "")
            b9 = " ".join([b5.lemmatize(word) for word in b8.split() if word not in b6])
            b7.append(b9)
    return np.array(b7)
def fonk2(posts, b13):
    b10 = fonk1(posts)
    b11 = b13.texts_to_sequences(b10)
    return sequence.pad_sequences(b11, b12 = a2)
b13 = Tokenizer()
b14 = os.path.join(b1, "b13.pkl")
with open(b14, "rb") as tokenizer_file:
    b13 = pickle.load(tokenizer_file)
for dimension in b3:
    b15 = []
    b16 = []
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as file_a:
        b17 = csv.b17(file_a)
        for row in b17:
            b15.append(row)
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as file_b:
        b17 = csv.b17(file_b)
        for row in b17:
            b16.append(row)
    b18 = b15 + b16
    b19 = os.path.join(b1, f"rnn_model_{dimension}.h5")
    b20 = load_model(b19)
    b21 = fonk2(b18, b13)
    b22 = b20.predict_proba(b21)
    b23 = sorted(enumerate(b22), key=lambda x: x[1][0])
    b24 = b23[:a1]
    b25 = b23[-a1:]
    for i, extreme_indices in enumerate([b24, b25], b26 = 1):
        for prob, index in extreme_indices:
            b27 = os.path.join(b2, f"extreme_examples_{dimension[i-1]}.txt")
            with open(b27, "a") as file:
                b9 = fonk1([b18[index]])[0]
                file.write(b9 + "\n\n")