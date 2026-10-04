import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(b11, authors_file):
    with open(authors_file, "rb") as af:
        b1 = pickle.load(af)
    with open(b11, "rb") as wf:
        b2 = pickle.load(wf)
    return b2, b1
def fonk2(b2, b1, b3 = 0.1, random_state=42):
    return train_test_split(b2, b1, b3 = b3, random_state=random_state)
def fonk3(features_train, features_test):
    b4 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b5 = b4.fit_transform(features_train)
    b6 = b4.transform(features_test)
    return b5, b6
def fonk4(b5, labels_train, b6, b7 = 10):
    b8 = SelectPercentile(f_classif, b7=b7)
    b8.fit(b5, labels_train)
    b5 = b8.transform(b5).toarray()
    b6 = b8.transform(b6).toarray()
    return b5, b6
def fonk5(labels_train):
    b9 = sum(labels_train)
    b10 = len(labels_train) - b9
    print("Number of Chris training emails:", b9)
    print("Number of Sara training emails:", b10)
def fonk6(b11 = "../tools/b2.pkl", authors_file="../tools/email_authors.pkl"):
    b2, b1 = fonk1(b11, authors_file)
    features_train, features_test, labels_train, b12 = fonk2(b2, b1)
    b5, b6 = fonk3(features_train, features_test)
    b5, b6 = fonk4(b5, labels_train, b6)
    fonk5(labels_train)
    return b5, b6, labels_train, b12
features_train, features_test, labels_train, b12 = fonk6()