import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import numpy as np
def fonk1():
    np.random.seed(100)
    b1 = pd.read_csv("Test.csv", encoding='utf-8-sig')
    b2 = b1['text']
    b3 = b1['label']
    b4 = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SVC(b5 = 5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    b6 = b4.fit(b2, b3)
    b7 = 'Amz_5000_.sav'
    with open(b7, 'wb') as file:
        pickle.dump(b6, file)
    b8 = os.path.exists('Amz_5000_.sav')
    b9 = ["Successful : Training model Saved", "Oh Snap! something's wrong", str(len(b1))]
    if b8:
        del b9[1]
        return b9
    else:
        del b9[0]
        return b9
if b10 = = "__main__":
    b11 = fonk1()
    print(b11)