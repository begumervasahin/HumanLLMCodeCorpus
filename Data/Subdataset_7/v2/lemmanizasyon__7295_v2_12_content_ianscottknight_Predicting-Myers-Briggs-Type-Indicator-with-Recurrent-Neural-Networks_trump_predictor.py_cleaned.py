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
b5 = ""
b6 = []
with open(b3, "r", b7 = "ISO-8859-1") as file:
    b8 = csv.b8(file)
    for row in b8:
        b6.append(row[0])
b9 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b9 = [t.lower() for t in b9]
b10 = WordNetLemmatizer()
b11 = stopwords.words("english")
def fonk1(b6):
    b12 = []
    for b13 in b6:
        b13 = b13.lower()
        for t in b9:
            b13 = b13.replace(" " + t, "")
        b13 = " ".join([
            b10.lemmatize(word)
            for word in b13.split(" ")
            if word not in b11
        ])
        b12.append(b13)
    return np.array(b12)
for dim in b4:
    b14 = load_model(os.path.join(b1, f"rnn_model_{dim}.h5"))
    with open(os.path.join(b1, f"rnn_tokenizer_{dim}.pkl"), "rb") as file:
        b15 = pickle.load(file)
    def fonk2(b6):
        b12 = fonk1(b6)
        b16 = b15.texts_to_sequences(b12)
        return sequence.pad_sequences(b16, b17 = a3)
    b18 = b14.predict(fonk2(b6))
    b19 = float(sum(b18) / len(b18))
    print(f"Dimension: {dim}")
    print(f"Average Prediction: {b19}")
    if b19 >= 0.5:
        b5 += dim[1]
    else:
        b5 += dim[0]
print("")
print("Final prediction:", b5)