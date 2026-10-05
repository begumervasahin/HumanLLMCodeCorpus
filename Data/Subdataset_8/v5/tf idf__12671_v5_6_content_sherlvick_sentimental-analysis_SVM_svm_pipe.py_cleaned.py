import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def train_and_save_model():
    np.random.seed(100)
    corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')
    texts = corpus['text']
    labels = corpus['label']
    text_classifier = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    trained_classifier = text_classifier.fit(texts, labels)
    model_filename = 'Amz_5000_.sav'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(trained_classifier, model_file)
    model_exists = os.path.exists(model_filename)
    success_message = "Successful: Training model saved."
    error_message = "Error: Something went wrong while saving the model."
    corpus_length = f"Number of data points: {len(corpus)}"
    if model_exists:
        return [success_message, corpus_length]
    else:
        return [error_message, corpus_length]
train_and_save_model()