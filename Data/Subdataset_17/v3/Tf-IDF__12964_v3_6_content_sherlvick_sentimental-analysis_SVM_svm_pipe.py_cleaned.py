import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def load_dataset(path):
    return pd.read_csv(path, encoding='utf-8-sig')
def create_pipeline():
    return Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
def save_model(model, filename):
    with open(filename, 'wb') as model_file:
        pickle.dump(model, model_file)
    return os.path.exists(filename)
def prepare_result_message(model_saved, corpus_length):
    messages = [
        "Successful: Training model saved",
        "Oh Snap! Something's wrong",
        f"Number of samples: {corpus_length}"
    ]
    return [messages[0], messages[2]] if model_saved else [messages[1], messages[2]]
def train_model():
    np.random.seed(100)
    dataset_path = "Test.csv"
    corpus = load_dataset(dataset_path)
    texts = corpus['text']
    labels = corpus['label']
    pipeline = create_pipeline()
    model = pipeline.fit(texts, labels)
    model_filename = 'Amz_5000_.sav'
    model_saved = save_model(model, model_filename)
    return prepare_result_message(model_saved, len(corpus))
if __name__ == "__main__":
    result = train_model()
    print(result)