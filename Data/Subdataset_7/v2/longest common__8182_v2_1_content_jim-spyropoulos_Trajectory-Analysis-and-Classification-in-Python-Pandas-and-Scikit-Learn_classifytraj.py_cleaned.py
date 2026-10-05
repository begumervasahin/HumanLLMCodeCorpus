import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def fonk1(b9, b8, b13, pipeline):
    b1 = []
    for fold, (train_index, test_index) in enumerate(b13):
        X_train_fold, b2 = b9[train_index], b9[test_index]
        Y_train_fold, b3 = b8[train_index], b8[test_index]
        b4 = pipeline.fit(X_train_fold, Y_train_fold).predict(b2)
        b5 = accuracy_score(b3, b4)
        b1.append(b5)
    return b1
b6 = pd.read_csv("grids.csv")
b7 = preprocessing.LabelEncoder()
b7.fit(b6["TripId"])
b8 = b7.transform(b6["TripId"])
b9 = np.array(b6['Grids'])
b10 = CountVectorizer()
b11 = TfidfTransformer()
b12 = TruncatedSVD(n_components=300, random_state=42)
b13 = KFold(n_splits=10)
b14 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b15 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b16 = LogisticRegression()
b17 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('clf', b14)
])
b18 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('clf', b15)
])
b19 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('clf', b16)
])
b20 = fonk1(b9, b8, b13.split(b9), b17)
b21 = fonk1(b9, b8, b13.split(b9), b18)
b22 = fonk1(b9, b8, b13.split(b9), b19)
with open('EvaluationsMetricAccuracy.csv', 'w', b23 = '') as csv_out:
    b24 = csv.writer(csv_out)
    b24.writerow(['Fold', 'KNN', 'RandomForests', 'LogisticRegression'])
    for i in range(10):
        b24.writerow(['Fold' + str(i + 1), b20[i], b21[i], b22[i]])