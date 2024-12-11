import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def fonk1(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)
def fonk2(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)
def fonk3(features, labels, b1 = 0.1, random_state=42):
    return train_test_split(features, labels, b1 = b1, random_state=random_state)
def fonk4(features_train, features_test, **kwargs):
    b2 = TfidfVectorizer(**kwargs)
    return b2.fit_transform(features_train), b2.transform(features_test)
def fonk5(features_train, features_test, labels_train, b3 = 10):
    b4 = SelectPercentile(f_classif, b3=b3)
    b4.fit(features_train, labels_train)
    return b4.transform(features_train).toarray(), b4.transform(features_test).toarray()
def fonk6(b5 = "../tools/b7.pkl", authors_file="../tools/email_authors.pkl"):
    b6 = fonk1(authors_file)
    b7 = fonk1(b5)
    features_train, features_test, labels_train, b8 = fonk3(b7, b6)
    features_train_transformed, b9 = fonk4(features_train, features_test,
                                                                           b10 = True, max_df=0.5,
                                                                           b11 = 'english')
    features_train_transformed, b9 = fonk5(features_train_transformed,
                                                                             b9,
                                                                             labels_train)
    print("Number of Chris training emails:", sum(labels_train))
    print("Number of Sara training emails:", len(labels_train) - sum(labels_train))
    return features_train_transformed, b9, labels_train, b8
