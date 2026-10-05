import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import numpy as np
def training():
    np.random.seed(100)
    Corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')
    my_data = Corpus['text']
    my_data1 = Corpus['label']
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    my_clf = text_clf.fit(my_data, my_data1)
    filename = 'Amz_5000_.sav'
    with open(filename, 'wb') as file:
        pickle.dump(my_clf, file)
    abs_exists = os.path.exists('Amz_5000_.sav')
    lis = ["Successful : Training model Saved", "Oh Snap! something's wrong", str(len(Corpus))]
    if abs_exists:
        del lis[1]
        return lis
    else:
        del lis[0]
        return lis
if __name__ == "__main__":
    result = training()
    print(result)