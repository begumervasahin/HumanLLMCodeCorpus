import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.b5 import Pipeline
from sklearn import svm
def fonk1():
    np.random.seed(100)
    b1 = "Test.csv"
    b2 = pd.read_csv(b1, encoding='utf-8-sig')
    b3 = b2['text']
    b4 = b2['label']
    b5 = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('classifier', svm.SVC(b6 = 5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    b7 = b5.fit(b3, b4)
    b8 = 'Amz_5000_.sav'
    with open(b8, 'wb') as model_file:
        pickle.dump(b7, model_file)
    b9 = os.path.exists(b8)
    b10 = ["Successful: Training b7 saved", "Oh Snap! Something's wrong", f"Number of samples: {len(b2)}"]
    if b9:
        del b10[1]
    else:
        del b10[0]
    return b10
if b11 = = "__main__":
    b12 = fonk1()
    print(b12)