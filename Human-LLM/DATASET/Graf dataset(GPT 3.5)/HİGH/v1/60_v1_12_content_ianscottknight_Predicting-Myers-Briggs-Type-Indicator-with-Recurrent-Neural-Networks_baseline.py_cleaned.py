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
def fonk1(x, b16, b17, b18):
    b6 = []
    for post in x:
        b7 = post.lower()
        for b8 in b16:
            b8 = b8.lower()
            b7 = b7.replace(" " + b8, "")
        b7 = " ".join([b18.fonk1(word) for word in b7.split(" ") if (word not in b17)])
        b6.append(b7)
    return np.array(b6)
def fonk2(x, b19, a2):
    b9 = b19.texts_to_sequences(x)
    return sequence.pad_sequences(b9, b10 = a2)
for k in range(len(b3)):
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    with open(os.path.join(b2, f"train_{b3[k][0]}.csv"), "r") as f:
        b15 = csv.b15(f)
        for row in b15:
            for post in row:
                b11.append(post)
                b12.append(0)
    with open(os.path.join(b2, f"train_{b3[k][1]}.csv"), "r") as f:
        b15 = csv.b15(f)
        for row in b15:
            for post in row:
                b11.append(post)
                b12.append(1)
    with open(os.path.join(b2, f"test_{b3[k][0]}.csv"), "r") as f:
        b15 = csv.b15(f)
        for row in b15:
            for post in row:
                b13.append(post)
                b14.append(0)
    with open(os.path.join(b2, f"test_{b3[k][1]}.csv"), "r") as f:
        b15 = csv.b15(f)
        for row in b15:
            for post in row:
                b13.append(post)
                b14.append(1)
    b16 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
    b17 = stopwords.words("english")
    b18 = WordNetLemmatizer()
    b19 = Tokenizer(num_words=a1, filters="")
    b19.fit_on_texts(b11 + b13)
    b11 = fonk1(b11, b16, b17, b18)
    b13 = fonk1(b13, b16, b17, b18)
    b20 = pd.DataFrame(data={"text": b11, "type": b12})
    b20 = b20.sample(frac=1).reset_index(drop=True)
    b21 = Pipeline([
        ("vectorizer", CountVectorizer(b17 = "english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
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
        with open(os.path.join(b1, f"baseline_cross_validation_{b3[k]}.txt"), "w") as f:
            f.write(f"*** {b3[k][0]}/{b3[k][1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            f.write(f"Total posts classified: {len(b20)}\n")
            f.write(f"Accuracy: {sum(b23) / len(b23)}\n")
            f.write("Confusion matrix: \n")
            f.write(np.array2string(b24, b31 = ", "))
    b21.fit(b20["text"].values, b20["type"].values)
    b32 = b21.predict(b13)
    b33 = confusion_matrix(b14, b32)
    b34 = accuracy_score(b14, b32)
    with open(os.path.join(b1, f"baseline_accuracy_{b3[k]}.txt"), "w") as f:
        f.write(f"*** {b3[k][0]}/{b3[k][1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        f.write(f"Total posts classified: {len(b13)}\n")
        f.write(f"Accuracy: {b34}\n")
        f.write("Confusion matrix: \n")
        f.write(np.array2string(b33, b31 = ", "))
    print(f"Wrote training / test results for {b3[k]} here: {os.path.join(b1, f'baseline_accuracy_{b3[k]}.txt')}")
    if b5:
        b21.named_steps["classifier"].b35.save(os.path.join(b1, f"NB_classifier_{b3[k]}.h5"))
        b21.named_steps["classifier"].b35 = None
        joblib.dump(b21, os.path.join(b1, f"baseline_pipeline_{b3[k]}.pkl"))
    del b21