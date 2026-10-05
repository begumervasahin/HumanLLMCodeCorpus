import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.b20 import Pipeline
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
def fonk1(posts, mbti_types, b14, b15):
    b6 = []
    for post in posts:
        b7 = post.lower()
        for b8 in mbti_types:
            b8 = b8.lower()
            b7 = b7.replace(" " + b8, "")
        b7 = " ".join([b15.fonk1(word) for word in b7.split(" ") if (word not in b14)])
        b6.append(b7)
    return np.array(b6)
def fonk2(posts, b16, max_post_length):
    b9 = b16.texts_to_sequences(posts)
    return sequence.pad_sequences(b9, b10 = max_post_length)
for dimension in b3:
    b17, y_train, b18, b11 = [], [], [], []
    with open(os.path.join(b2, f"train_{dimension[0]}.csv"), "r") as file:
        b12 = csv.b12(file)
        for row in b12:
            for post in row:
                b17.append(post)
                y_train.append(0)
    with open(os.path.join(b2, f"train_{dimension[1]}.csv"), "r") as file:
        b12 = csv.b12(file)
        for row in b12:
            for post in row:
                b17.append(post)
                y_train.append(1)
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as file:
        b12 = csv.b12(file)
        for row in b12:
            for post in row:
                b18.append(post)
                b11.append(0)
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as file:
        b12 = csv.b12(file)
        for row in b12:
            for post in row:
                b18.append(post)
                b11.append(1)
    b13 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
    b14 = stopwords.words("english")
    b15 = WordNetLemmatizer()
    b16 = Tokenizer(num_words=a1, filters="")
    b16.fit_on_texts(b17 + b18)
    b17 = fonk1(b17, b13, b14, b15)
    b18 = fonk1(b18, b13, b14, b15)
    b19 = pd.DataFrame(data={"text": b17, "type": y_train})
    b19 = b19.sample(frac=1).reset_index(drop=True)
    b20 = Pipeline([
        ("vectorizer", CountVectorizer(b14 = "english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if b4:
        b21 = KFold(n_splits=6)
        scores, b22 = [], np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in b21:
            x_train_k, b23 = b19.iloc[train_indices]["text"].values, b19.iloc[train_indices]["type"].values
            x_test_k, b24 = b19.iloc[test_indices]["text"].values, b19.iloc[test_indices]["type"].values
            b20.fit(x_train_k, b23)
            b25 = b20.predict(x_test_k)
            b22 += confusion_matrix(b24, b25)
            b26 = accuracy_score(b24, b25)
            scores.append(b26)
        with open(os.path.join(b1, f"baseline_cross_validation_{dimension}.txt"), "w") as file:
            file.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            file.write(f"Total posts classified: {len(b19)}\n")
            file.write(f"Accuracy: {sum(scores) / len(scores)}\n")
            file.write("Confusion matrix: \n")
            file.write(np.array2string(b22, b27 = ", "))
    b20.fit(b19["text"].values, b19["type"].values)
    b28 = b20.predict(b18)
    b29 = confusion_matrix(b11, b28)
    b30 = accuracy_score(b11, b28)
    with open(os.path.join(b1, f"baseline_accuracy_{dimension}.txt"), "w") as file:
        file.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        file.write(f"Total posts classified: {len(b18)}\n")
        file.write(f"Accuracy: {b30}\n")
        file.write("Confusion matrix: \n")
        file.write(np.array2string(b29, b27 = ", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(b1, f'baseline_accuracy_{dimension}.txt')}")
    if b5:
        b20.named_steps["classifier"].b31.save(os.path.join(b1, f"NB_classifier_{dimension}.h5"))
        b20.named_steps["classifier"].b31 = None
        joblib.dump(b20, os.path.join(b1, f"baseline_pipeline_{dimension}.pkl"))
    del b20