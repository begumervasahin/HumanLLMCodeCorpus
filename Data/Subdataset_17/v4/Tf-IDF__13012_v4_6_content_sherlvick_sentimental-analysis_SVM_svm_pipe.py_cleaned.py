import pandas as pd
import pickle
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def training():
    np.random.seed(100)
    corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')
    texts = corpus['text']
    labels = corpus['label']
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    trained_clf = text_clf.fit(texts, labels)
    model_filename = 'Amz_5000_.sav'
    pickle.dump(trained_clf, open(model_filename, 'wb'))
    is_model_saved = os.path.exists(model_filename)
    messages = [
        "Successful: Training model saved",
        "Oh Snap! Something's wrong",
        f"Number of records in the corpus: {len(corpus)}"
    ]
    if is_model_saved:
        return [messages[0], messages[2]]
    else:
        return [messages[1], messages[2]]
result = training()
print(result)