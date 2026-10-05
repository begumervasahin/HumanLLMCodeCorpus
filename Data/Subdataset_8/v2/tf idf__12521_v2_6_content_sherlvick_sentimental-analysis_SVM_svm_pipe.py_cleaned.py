import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import numpy as np
def train_and_save_model():
    np.random.seed(100)
    dataset = pd.read_csv("Test.csv", encoding='utf-8-sig')
    texts = dataset['text']
    labels = dataset['label']
    text_clf = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf_transformer', TfidfTransformer()),
        ('classifier', SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    trained_model = text_clf.fit(texts, labels)
    model_filename = 'text_classification_model.sav'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(trained_model, model_file)
    model_file_exists = os.path.exists(model_filename)
    training_result = ["Success: Model trained and saved.", "Error: Model could not be saved.", f"Number of records: {len(dataset)}"]
    if model_file_exists:
        del training_result[1]
    else:
        del training_result[0]
    return training_result
if __name__ == "__main__":
    training_result = train_and_save_model()
    print(training_result)