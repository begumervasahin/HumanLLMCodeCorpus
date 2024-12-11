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
        b6.append(row)
b9 = [
    "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
    "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
]
b9 = [personality.lower() for personality in b9]
b10 = WordNetLemmatizer()
b11 = stopwords.words("english")
def fonk1(text):
    b12 = []
    for post in text:
        b13 = post.lower()
        for personality_type in b9:
            b13 = b13.replace(" " + personality_type, "")
        b13 = " ".join([b10.lemmatize(word) for word in b13.split(" ") if word not in b11])
        b12.append(b13)
    return np.array(b12)
for dimension in b4:
    b14 = load_model(os.path.join(b1, f"rnn_model_{dimension}.h5"))
    with open(os.path.join(b1, f"rnn_tokenizer_{dimension}.pkl"), "rb") as file:
        b15 = pickle.load(file)
    def fonk2(text):
        b16 = fonk1(text)
        b17 = b15.texts_to_sequences(b16)
        return sequence.pad_sequences(b17, b18 = a3)
    b19 = b14.predict(fonk2(b6))
    b20 = float(sum(b19) / len(b19))
    print(f"{dimension}:")
    print(b20)
    if b20 >= 0.5:
        b5 += dimension[1]
    else:
        b5 += dimension[0]
print("")
print("Final prediction:", b5)