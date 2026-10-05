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
        ('vectorizer', CountVectorizer()),
        ('tfidf_transformer', TfidfTransformer()),
        ('classifier', SVC(b5 = 5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    b6 = b4.fit(b2, b3)
    b7 = 'text_classification_model.sav'
    with open(b7, 'wb') as model_file:
        pickle.dump(b6, model_file)
    b8 = os.path.exists(b7)
    b9 = [
        "Success: Model trained and saved.",
        "Error: Model could not be saved.",
        f"Number of records: {len(b1)}"
    ]
    if b8:
        del b9[1]
    else:
        del b9[0]
    return b9
if b10 = = "__main__":
    b9 = fonk1()
    print(b9)