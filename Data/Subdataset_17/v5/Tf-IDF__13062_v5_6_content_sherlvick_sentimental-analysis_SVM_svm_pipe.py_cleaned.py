import pandas as pd
import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def train_model():
    np.random.seed(100)
    corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')
    texts = corpus['text']
    labels = corpus['label']
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5))
    ])
    trained_clf = text_clf.fit(texts, labels)
    model_filename = 'Amz_5000_.sav'
    with open(model_filename, 'wb') as model_file:
        pickle.dump(trained_clf, model_file)
    is_model_saved = os.path.exists(model_filename)
    success_message = "Successful: Training model saved"
    error_message = "Oh Snap! Something's wrong"
    record_count_message = f"Number of records in the corpus: {len(corpus)}"
    if is_model_saved:
        return [success_message, record_count_message]
    else:
        return [error_message, record_count_message]
if __name__ == "__main__":
    result = train_model()
    print(result)