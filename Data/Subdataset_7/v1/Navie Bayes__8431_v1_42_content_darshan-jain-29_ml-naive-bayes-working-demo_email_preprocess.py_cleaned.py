import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(b1 = "../tools/b3.pkl", authors_file="../tools/email_authors.pkl"):
    with open(authors_file, "rb") as f:
        b2 = pickle.load(f)
    with open(b1, "rb") as f:
        b3 = pickle.load(f)
    features_train, features_test, labels_train, b4 = train_test_split(b3, b2, test_size=0.1, random_state=42)
    b5 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b6 = b5.fit_transform(features_train)
    b7 = b5.transform(features_test)
    b8 = SelectPercentile(f_classif, percentile=10)
    b8.fit(b6, labels_train)
    b6 = b8.transform(b6).toarray()
    b7 = b8.transform(b7).toarray()
    print("no. of Chris training emails:", sum(labels_train))
    print("no. of Sara training emails:", len(labels_train) - sum(labels_train))
    return b6, b7, labels_train, b4
