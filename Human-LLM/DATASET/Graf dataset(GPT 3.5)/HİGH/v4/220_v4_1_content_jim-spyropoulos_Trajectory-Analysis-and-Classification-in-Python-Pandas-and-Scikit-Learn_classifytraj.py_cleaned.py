import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
def fonk1(b8, b7, b12, pipeline):
    b1 = []
    for train_index, test_index in b12.split(b8):
        X_train_fold, b2 = b8[train_index], b8[test_index]
        Y_train_fold, b3 = b7[train_index], b7[test_index]
        b4 = pipeline.fit(X_train_fold, Y_train_fold).predict(b2)
        b1.append(accuracy_score(b3, b4))
    return b1
b5 = pd.read_csv("grids.csv")
b6 = LabelEncoder()
b6.fit(b5["TripId"])
b7 = b6.transform(b5["TripId"])
b8 = np.array(b5['Grids'])
b9 = CountVectorizer()
b10 = TfidfTransformer()
b11 = TruncatedSVD(n_components=300, random_state=42)
b12 = KFold(n_splits=10)
b13 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b14 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b15 = LogisticRegression()
b16 = Pipeline([
    ('vect', b9),
    ('tfidf', b10),
    ('b11', b11),
    ('clf', b13)
])
b17 = Pipeline([
    ('vect', b9),
    ('tfidf', b10),
    ('b11', b11),
    ('clf', b14)
])
b18 = Pipeline([
    ('vect', b9),
    ('tfidf', b10),
    ('b11', b11),
    ('clf', b15)
])
b19 = fonk1(b8, b7, b12, b16)
b20 = fonk1(b8, b7, b12, b17)
b21 = fonk1(b8, b7, b12, b18)
with open('EvaluationsMetricAccuracy.csv', 'w', b22 = '') as csv_out:
    b23 = csv.writer(csv_out)
    b23.writerow(['Accuracy', 'KNN', 'RandomForests', 'LogisticRegression'])
    for i in range(10):
        b23.writerow(['Fold' + str(i + 1), b19[i], b20[i], b21[i]])