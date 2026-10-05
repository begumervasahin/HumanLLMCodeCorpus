import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
def load_data(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)
def save_data(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)
def split_data(features, labels, test_size=0.1, random_state=42):
    return train_test_split(features, labels, test_size=test_size, random_state=random_state)
def vectorize_data(features_train, features_test, **kwargs):
    vectorizer = TfidfVectorizer(**kwargs)
    return vectorizer.fit_transform(features_train), vectorizer.transform(features_test)
def select_features(features_train, features_test, labels_train, percentile=10):
    selector = SelectPercentile(f_classif, percentile=percentile)
    selector.fit(features_train, labels_train)
    return selector.transform(features_train).toarray(), selector.transform(features_test).toarray()
def preprocess(words_file="../tools/word_data.pkl", authors_file="../tools/email_authors.pkl"):
    authors = load_data(authors_file)
    word_data = load_data(words_file)
    features_train, features_test, labels_train, labels_test = split_data(word_data, authors)
    features_train_transformed, features_test_transformed = vectorize_data(features_train, features_test,
                                                                           sublinear_tf=True, max_df=0.5,
                                                                           stop_words='english')
    features_train_transformed, features_test_transformed = select_features(features_train_transformed,
                                                                             features_test_transformed,
                                                                             labels_train)
    print("Number of Chris training emails:", sum(labels_train))
    print("Number of Sara training emails:", len(labels_train) - sum(labels_train))
    return features_train_transformed, features_test_transformed, labels_train, labels_test
