import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.b23 import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
b1 = "models"
b2 = "data"
b3 = ["IE", "NS", "FT", "PJ"]
a1 = 2500
a2 = 40
b4 = False
b5 = False
for dimension in b3:
    x_train, b6 = [], []
    b21, b7 = [], []
    for data_type in ["train", "test"]:
        for b11 in [dimension[0], dimension[1]]:
            b8 = os.path.join(b2, f"{data_type}_{b11}.csv")
            with open(b8, "r") as file:
                b9 = csv.b9(file)
                for row in b9:
                    for post in row:
                        x_data, b10 = x_train, b6 if data_type == "train" else b21, b7
                        x_data.append(post)
                        b10.append(0 if b11 = = dimension[0] else 1)
    b12 = [
        "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
        "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
    ]
    b13 = stopwords.words("english")
    b14 = WordNetLemmatizer()
    b15 = Tokenizer(num_words=a1, filters="")
    b15.fit_on_texts(x_train + b21)
    def fonk1(data):
        b16 = []
        for post in data:
            b17 = post.lower()
            for b18 in b12:
                b18 = b18.lower()
                b17 = b17.replace(f" {b18}", "")
            b17 = " ".join([b14.lemmatize(word) for word in b17.split(" ") if word not in b13])
            b16.append(b17)
        b19 = b15.texts_to_sequences(b16)
        return sequence.pad_sequences(b19, b20 = a2)
    x_train, b21 = fonk1(x_train), fonk1(b21)
    b22 = pd.DataFrame(data={"text": x_train, "type": b6}).sample(frac=1).reset_index(drop=True)
    b23 = Pipeline([
        ("vectorizer", CountVectorizer(b13 = "english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if b4:
        b24 = KFold(n_splits=6)
        b25 = []
        b26 = np.zeros((2, 2))
        for train_indices, test_indices in b24:
            x_train_k, b27 = b22.iloc[train_indices]["text"].values, b22.iloc[train_indices]["type"].values
            x_test_k, b28 = b22.iloc[test_indices]["text"].values, b22.iloc[test_indices]["type"].values
            b23.fit(x_train_k, b27)
            b29 = b23.predict(x_test_k)
            b26 += confusion_matrix(b28, b29)
            b30 = accuracy_score(b28, b29)
            b25.append(b30)
        with open(os.path.join(b1, f"baseline_cross_validation_{dimension}.txt"), "w") as f:
            f.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            f.write(f"Total posts classified: {len(b22)}\n")
            f.write(f"Accuracy: {sum(b25) / len(b25)}\n")
            f.write("Confusion matrix: \n")
            f.write(np.array2string(b26, b31 = ", "))
    b23.fit(b22["text"].values, b22["type"].values)
    b32 = b23.predict(b21)
    b33 = confusion_matrix(b7, b32)
    b34 = accuracy_score(b7, b32)
    with open(os.path.join(b1, f"baseline_accuracy_{dimension}.txt"), "w") as f:
        f.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        f.write(f"Total posts classified: {len(b21)}\n")
        f.write(f"Accuracy: {b34}\n")
        f.write("Confusion matrix: \n")
        f.write(np.array2string(b33, b31 = ", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(b1, f'baseline_accuracy_{dimension}.txt')}")
    if b5:
        b35 = os.path.join(b1, f"NB_classifier_{dimension}.h5")
        b23.named_steps["classifier"].b36.save(b35)
        b23.named_steps["classifier"].b36 = None
        joblib.dump(b23, os.path.join(b1, f"baseline_pipeline_{dimension}.pkl"))
    del b23