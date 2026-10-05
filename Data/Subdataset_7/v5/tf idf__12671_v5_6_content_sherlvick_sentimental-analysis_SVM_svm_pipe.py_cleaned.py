import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
def fonk1():
    np.random.seed(100)
    b1 = pd.read_csv("Test.csv", encoding='utf-8-sig')
    b2 = b1['text']
    b3 = b1['label']
    b4 = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(b5 = 5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    b6 = b4.fit(b2, b3)
    b7 = 'Amz_5000_.sav'
    with open(b7, 'wb') as model_file:
        pickle.dump(b6, model_file)
    b8 = os.path.exists(b7)
    b9 = "Successful: Training model saved."
    b10 = "Error: Something went wrong while saving the model."
    b11 = f"Number of data points: {len(b1)}"
    if b8:
        return [b9, b11]
    else:
        return [b10, b11]
fonk1()