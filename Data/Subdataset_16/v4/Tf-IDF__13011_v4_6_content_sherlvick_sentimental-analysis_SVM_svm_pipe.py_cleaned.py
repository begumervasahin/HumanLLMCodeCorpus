import pandas as pd
import pickle
import os
import numpy as np
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
    pickle.dump(b6, open(b7, 'wb'))
    b8 = os.path.exists(b7)
    b9 = [
        "Successful: Training model saved",
        "Oh Snap! Something's wrong",
        f"Number of records in the b1: {len(b1)}"
    ]
    if b8:
        return [b9[0], b9[2]]
    else:
        return [b9[1], b9[2]]
b10 = fonk1()
print(b10)