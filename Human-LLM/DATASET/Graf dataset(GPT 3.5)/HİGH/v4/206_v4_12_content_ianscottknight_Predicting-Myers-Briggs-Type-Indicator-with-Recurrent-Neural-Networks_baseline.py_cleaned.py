import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.b22 import Pipeline
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier, Perceptron
from sklearn.neighbors import KNeighborsClassifier
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
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    with open(os.path.join(b2, f"train_{dimension[0]}.csv"), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b6.append(post)
                b7.append(0)
    with open(os.path.join(b2, f"train_{dimension[1]}.csv"), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b6.append(post)
                b7.append(1)
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b8.append(post)
                b9.append(0)
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b8.append(post)
                b9.append(1)
    b11 = [
        "INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP",
        "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"
    ]
    b12 = stopwords.words("english")
    b13 = WordNetLemmatizer()
    b14 = Tokenizer(num_words=a1, filters="")
    b14.fit_on_texts(b6 + b8)
    def fonk1(data):
        b15 = []
        for post in data:
            b16 = post.lower()
            for b17 in b11:
                b17 = b17.lower()
                b16 = b16.replace(f" {b17}", "")
            b16 = " ".join([b13.fonk1(word) for word in b16.split(" ") if word not in b12])
            b15.append(b16)
        return np.array(b15)
    def fonk2(data):
        b18 = fonk1(data)
        b19 = b14.texts_to_sequences(b18)
        return sequence.pad_sequences(b19, b20 = a2)
    b6 = fonk1(b6)
    b8 = fonk1(b8)
    b21 = pd.DataFrame(data={"text": b6, "type": b7})
    b21 = b21.sample(frac=1).reset_index(drop=True)
    b22 = Pipeline([
        ("vectorizer", CountVectorizer(b12 = "english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if b4:
        b23 = KFold(n_splits=6)
        b24 = []
        b25 = np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in b23:
            b26 = b21.iloc[train_indices]["text"].values
            b27 = b21.iloc[train_indices]["type"].values
            b28 = b21.iloc[test_indices]["text"].values
            b29 = b21.iloc[test_indices]["type"].values
            b22.fit(b26, b27)
            b30 = b22.predict(b28)
            b25 += confusion_matrix(b29, b30)
            b31 = accuracy_score(b29, b30)
            b24.append(b31)
        with open(os.path.join(b1, f"baseline_cross_validation_{dimension}.txt"), "w") as f:
            f.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            f.write(f"Total posts classified: {len(b21)}\n")
            f.write(f"Accuracy: {sum(b24) / len(b24)}\n")
            f.write("Confusion matrix: \n")
            f.write(np.array2string(b25, b32 = ", "))
    b22.fit(b21["text"].values, b21["type"].values)
    b33 = b22.predict(b8)
    b34 = confusion_matrix(b9, b33)
    b35 = accuracy_score(b9, b33)
    with open(os.path.join(b1, f"baseline_accuracy_{dimension}.txt"), "w") as f:
        f.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        f.write(f"Total posts classified: {len(b8)}\n")
        f.write(f"Accuracy: {b35}\n")
        f.write("Confusion matrix: \n")
        f.write(np.array2string(b34, b32 = ", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(b1, f'baseline_accuracy_{dimension}.txt')}")
    if b5:
        b22.named_steps["classifier"].b36.save(os.path.join(b1, f"NB_classifier_{dimension}.h5"))
        b22.named_steps["classifier"].b36 = None
        joblib.dump(b22, os.path.join(b1, f"baseline_pipeline_{dimension}.pkl"))
    del b22