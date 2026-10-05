import os
import numpy as np
import pandas as pd
import csv
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.b18 import Pipeline
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
def fonk1(posts, mbti_types, b12, b13):
    b6 = [b13.fonk1(word) for word in post.lower().split(" ") if word not in b12]
    return " ".join(b6)
def fonk2(posts, b14, max_post_length):
    b7 = b14.texts_to_sequences(posts)
    return sequence.pad_sequences(b7, b8 = max_post_length)
for dimension in b3:
    b15, y_train, b16, b9 = [], [], [], []
    with open(os.path.join(b2, f"train_{dimension[0]}.csv"), "r") as file:
        b10 = csv.b10(file)
        for row in b10:
            b15.extend(row)
            y_train.extend([0] * len(row))
    with open(os.path.join(b2, f"train_{dimension[1]}.csv"), "r") as file:
        b10 = csv.b10(file)
        for row in b10:
            b15.extend(row)
            y_train.extend([1] * len(row))
    with open(os.path.join(b2, f"test_{dimension[0]}.csv"), "r") as file:
        b10 = csv.b10(file)
        for row in b10:
            b16.extend(row)
            b9.extend([0] * len(row))
    with open(os.path.join(b2, f"test_{dimension[1]}.csv"), "r") as file:
        b10 = csv.b10(file)
        for row in b10:
            b16.extend(row)
            b9.extend([1] * len(row))
    b11 = ["INFJ", "ENTP", "INTP", "INTJ", "ENTJ", "ENFJ", "INFP", "ENFP", "ISFP", "ISTP", "ISFJ", "ISTJ", "ESTP", "ESFP", "ESTJ", "ESFJ"]
    b12 = stopwords.words("english")
    b13 = WordNetLemmatizer()
    b14 = Tokenizer(num_words=a1, filters="")
    b14.fit_on_texts(b15 + b16)
    b15 = [fonk1(post, b11, b12, b13) for post in b15]
    b16 = [fonk1(post, b11, b12, b13) for post in b16]
    b17 = pd.DataFrame(data={"text": b15, "type": y_train})
    b17 = b17.sample(frac=1).reset_index(drop=True)
    b18 = Pipeline([
        ("vectorizer", CountVectorizer(b12 = "english")),
        ("transformer", TfidfTransformer()),
        ("classifier", MultinomialNB()),
    ])
    if b4:
        b19 = KFold(n_splits=6)
        scores, b20 = [], np.array([[0, 0], [0, 0]])
        for train_indices, test_indices in b19:
            x_train_k, b21 = b17.iloc[train_indices]["text"].values, b17.iloc[train_indices]["type"].values
            x_test_k, b22 = b17.iloc[test_indices]["text"].values, b17.iloc[test_indices]["type"].values
            b18.fit(x_train_k, b21)
            b23 = b18.predict(x_test_k)
            b20 += confusion_matrix(b22, b23)
            b24 = accuracy_score(b22, b23)
            scores.append(b24)
        with open(os.path.join(b1, f"baseline_cross_validation_{dimension}.txt"), "w") as file:
            file.write(f"*** {dimension[0]}/{dimension[1]} TRAINING SET CROSS VALIDATION (POSTS) ***\n")
            file.write(f"Total posts classified: {len(b17)}\n")
            file.write(f"Accuracy: {sum(scores) / len(scores)}\n")
            file.write("Confusion matrix: \n")
            file.write(np.array2string(b20, b25 = ", "))
    b18.fit(b17["text"].values, b17["type"].values)
    b26 = b18.predict(b16)
    b27 = confusion_matrix(b9, b26)
    b28 = accuracy_score(b9, b26)
    with open(os.path.join(b1, f"baseline_accuracy_{dimension}.txt"), "w") as file:
        file.write(f"*** {dimension[0]}/{dimension[1]} TEST SET CLASSIFICATION (POSTS) ***\n")
        file.write(f"Total posts classified: {len(b16)}\n")
        file.write(f"Accuracy: {b28}\n")
        file.write("Confusion matrix: \n")
        file.write(np.array2string(b27, b25 = ", "))
    print(f"Wrote training/test results for {dimension} here: {os.path.join(b1, f'baseline_accuracy_{dimension}.txt')}")
    if b5:
        b18.named_steps["classifier"].b29.save(os.path.join(b1, f"NB_classifier_{dimension}.h5"))
        b18.named_steps["classifier"].b29 = None
        joblib.dump(b18, os.path.join(b1, f"baseline_pipeline_{dimension}.pkl"))
    del b18