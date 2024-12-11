import os
import csv
import pickle
import numpy as np
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from keras.preprocessing import sequence, text
from keras.models import load_model
b1 = "models"
b2 = "data"
b3 = os.path.join(b2, "trumptweets.csv")
b4 = ["IE", "NS", "FT", "PJ"]
a1 = 128
a2 = 2500
a3 = 40
a4 = 20
def fonk1(b10, b14, b13, b15, b18):
    b5 = []
    for b6 in b10:
        b6 = b6.lower()
        for t in b13:
            b6 = b6.replace(" " + t, "")
        b7 = " ".join([
            b14.lemmatize(word)
            for word in b6.split(" ")
            if word not in b15
        ])
        b5.append(b7)
    b8 = b18.texts_to_sequences(b5)
    return sequence.pad_sequences(b8, b9 = a3)
b10 = []
with open(b3, "r", b11 = "ISO-8859-1") as file:
    b12 = csv.b12(file)
    for row in b12:
        b10.append(row[0])
b13 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b13 = [t.lower() for t in b13]
b14 = WordNetLemmatizer()
b15 = stopwords.words("english")
b16 = ""
for dim in b4:
    b17 = load_model(os.path.join(b1, f"rnn_model_{dim}.h5"))
    with open(os.path.join(b1, f"rnn_tokenizer_{dim}.pkl"), "rb") as file:
        b18 = pickle.load(file)
    b19 = fonk1(b10, b14, b13, b15, b18)
    b20 = b17.predict(b19)
    b21 = float(sum(b20) / len(b20))
    print(f"Dimension: {dim}")
    print(f"Average Prediction: {b21}")
    b16 += dim[1] if b21 >= 0.5 else dim[0]
print("")
print("Final prediction:", b16)