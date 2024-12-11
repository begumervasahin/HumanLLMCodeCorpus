import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.b21 import Pipeline
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
for k in range(len(b3)):
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    with open(
        os.path.join(b2, "train_{}.csv".format(b3[k][0])), "r"
    ) as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b6.append(post)
                b7.append(0)
    with open(
        os.path.join(b2, "train_{}.csv".format(b3[k][1])), "r"
    ) as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b6.append(post)
                b7.append(1)
    with open(os.path.join(b2, "test_{}.csv".format(b3[k][0])), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b8.append(post)
                b9.append(0)
    with open(os.path.join(b2, "test_{}.csv".format(b3[k][1])), "r") as f:
        b10 = csv.b10(f)
        for row in b10:
            for post in row:
                b8.append(post)
                b9.append(1)
    b11 = [
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
    b12 = stopwords.words("english")
    b13 = WordNetLemmatizer()
    b14 = Tokenizer(num_words=a1, filters="")
    b14.fit_on_texts(b6 + b8)
    def fonk1(x):
        b15 = []
        for post in x:
            b16 = post.lower()
            for b17 in b11:
                b17 = b17.lower()
                b16 = b16.replace(" " + b17, "")
            b16 = " ".join(
                [
                    b13.fonk1(word)
                    for word in b16.split(" ")
                    if (word not in b12)
                ]
            )
            b15.append(b16)
        return np.array(b15)
    def fonk2(x):
        b15 = fonk1(x)
        b18 = b14.texts_to_sequences(b15)
        return sequence.pad_sequences(b18, b19 = a2)
    b6 = fonk1(b6)
    b8 = fonk1(b8)
    b20 = pd.DataFrame(data={"text": b6, "type": b7})
    b20 = b20.sample(frac=1).reset_index(drop=True)
    b21 = Pipeline(
        [
            ("vectorizer", CountVectorizer(b12 = "english")),
            ("transformer", TfidfTransformer()),
            ("classifier", MultinomialNB()),
        ]
    )
    if b4:
        b22 = KFold(n_splits=6)
        b23 = []
        b24 = np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in b22:
            b25 = b20.iloc[train_indices]["text"].values
            b26 = b20.iloc[train_indices]["type"].values
            b27 = b20.iloc[test_indices]["text"].values
            b28 = b20.iloc[test_indices]["type"].values
            b21.fit(b25, b26)
            b29 = b21.predict(b27)
            b24 += confusion_matrix(b28, b29)
            b30 = accuracy_score(b28, b29)
            b23.append(b30)
        with open(
            os.path.join(
                b1, "baseline_cross_validation_{}.txt".format(b3[k])
            ),
            "w",
        ) as f:
            f.write(
                "*** {}/{} TRAINING SET CROSS VALIDATION (POSTS) ***\n".format(
                    b3[k][0], b3[k][1]
                )
            )
            f.write("Total posts classified: {}\n".format(len(b20)))
            f.write("Accuracy: {}\n".format(sum(b23) / len(b23)))
            f.write("Confusion matrix: \n")
            f.write(np.array2string(b24, b31 = ", "))
    b21.fit(b20["text"].values, b20["type"].values)
    b32 = b21.predict(b8)
    b33 = confusion_matrix(b9, b32)
    b34 = accuracy_score(b9, b32)
    with open(
        os.path.join(b1, "baseline_accuracy_{}.txt".format(b3[k])), "w"
    ) as f:
        f.write(
            "*** {}/{} TEST SET CLASSIFICATION (POSTS) ***\n".format(
                b3[k][0], b3[k][1]
            )
        )
        f.write("Total posts classified: {}\n".format(len(b8)))
        f.write("Accuracy: {}\n".format(b34))
        f.write("Confusion matrix: \n")
        f.write(np.array2string(b33, b31 = ", "))
    print(
        f"Wrote training / test results for {b3[k]} here: {os.path.join(b1, 'baseline_accuracy_{}.txt'.format(b3[k]))}"
    )
    if b5:
        b21.named_steps["classifier"].b35.save(
            os.path.join(b1, "NB_classifier_{}.h5".format(b3[k]))
        )
        b21.named_steps["classifier"].b35 = None
        joblib.dump(
            b21,
            os.path.join(b1, "baseline_pipeline_{}.pkl".format(b3[k])),
        )
    del b21