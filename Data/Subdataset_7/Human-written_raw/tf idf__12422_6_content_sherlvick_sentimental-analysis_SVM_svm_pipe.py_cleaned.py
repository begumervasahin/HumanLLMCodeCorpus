import pandas as pd
import sys
import pickle
import os
import pathlib
from numpy import loadtxt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
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
    b8 = os.path.exists('Amz_5000_.sav')
    b9 = ["Successful : Training model Saved", "Oh Snap! something's wrong", str(len(b1))]
    if b8 is True:
        del b9[1]
        return b9
    if b8 is False:
        del b9[0]
        return b9