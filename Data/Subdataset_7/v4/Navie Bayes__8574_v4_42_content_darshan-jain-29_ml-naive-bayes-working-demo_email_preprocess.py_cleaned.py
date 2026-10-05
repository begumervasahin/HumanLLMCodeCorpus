import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(b1 = "../tools/b3.pkl", authors_file="../tools/email_authors.pkl"):
    with open(authors_file, "rb") as authors_file_handler:
        b2 = pickle.load(authors_file_handler)
    with open(b1, "rb") as words_file_handler:
        b3 = pickle.load(words_file_handler)
    features_train, features_test, labels_train, b4 = train_test_split(b3, b2,
                                                                                 b5 = 0.1,
                                                                                 b6 = 42)
    b7 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b8 = b7.fit_transform(features_train)
    b9 = b7.transform(features_test)
    b10 = SelectPercentile(f_classif, percentile=10)
    b10.fit(b8, labels_train)
    b8 = b10.transform(b8).toarray()
    b9 = b10.transform(b9).toarray()
    print("No. of Chris training emails:", np.sum(labels_train))
    print("No. of Sara training emails:", len(labels_train) - np.sum(labels_train))
    return b8, b9, labels_train, b4