import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(b1 = "../tools/b3.pkl", authors_file="../tools/email_authors.pkl"):
    with open(authors_file, "rb") as af:
        b2 = pickle.load(af)
    with open(b1, "rb") as wf:
        b3 = pickle.load(wf)
    features_train, features_test, labels_train, b4 = train_test_split(
        b3, b2, b5 = 0.1, random_state=42
    )
    b6 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b7 = b6.fit_transform(features_train)
    b8 = b6.transform(features_test)
    b9 = SelectPercentile(f_classif, percentile=10)
    b9.fit(b7, labels_train)
    b7 = b9.transform(b7).toarray()
    b8 = b9.transform(b8).toarray()
    print("Number of Chris training emails:", sum(labels_train))
    print("Number of Sara training emails:", len(labels_train) - sum(labels_train))
    return b7, b8, labels_train, b4
features_train, features_test, labels_train, b4 = fonk1()