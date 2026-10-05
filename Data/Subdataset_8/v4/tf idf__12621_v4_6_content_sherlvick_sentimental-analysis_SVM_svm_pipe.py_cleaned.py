
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def training():
    np.random.seed(100)
    Corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')
    my_data = Corpus['text']
    my_data1 = Corpus['label']
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    my_clf = text_clf.fit(my_data, my_data1)
    filename = 'Amz_5000_.sav'
    pickle.dump(my_clf, open(filename, 'wb'))
    model_exists = os.path.exists('Amz_5000_.sav')
    messages = ["Successful : Training model Saved", "Oh Snap! something's wrong", str(len(Corpus))]
    if model_exists:
        del messages[1]
        return messages
    else:
        del messages[0]
        return messages
training()