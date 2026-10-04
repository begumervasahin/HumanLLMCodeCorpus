import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import csv
def fonk1(pipeline, b10, b8):
    b1 = []
    b2 = KFold(n_splits=10)
    for train_index, test_index in b2.split(b10):
        b9, b3 = b10[train_index], b10[test_index]
        Y_train1, b4 = b8[train_index], b8[test_index]
        b5 = pipeline.fit(b9, Y_train1).predict(b3)
        b1.append(accuracy_score(b4, b5))
    return b1
b6 = pd.read_csv("grids.csv")
b7 = LabelEncoder()
b7.fit(b6["TripId"])
b8 = b7.transform(b6["TripId"])
b9 = b6['Grids']
b10 = np.array(b9)
b11 = CountVectorizer()
b12 = TfidfTransformer()
b13 = TruncatedSVD(n_components=300, random_state=42)
b14 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b15 = Pipeline([
    ('vect', b11),
    ('tfidf', b12),
    ('b13', b13),
    ('clf', b14)
])
b16 = fonk1(b15, b10, b8)
b17 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b18 = Pipeline([
    ('vect', b11),
    ('tfidf', b12),
    ('b13', b13),
    ('clf', b17)
])
b19 = fonk1(b18, b10, b8)
b20 = LogisticRegression()
b21 = Pipeline([
    ('vect', b11),
    ('tfidf', b12),
    ('b13', b13),
    ('clf', b20)
])
b22 = fonk1(b21, b10, b8)
with open('EvaluationsMetricAccuracy.csv', 'w', b23 = '') as csv_out:
    b24 = csv.writer(csv_out)
    b25 = ['Fold', 'KNN', 'RandomForests', 'LogisticRegression']
    b24.writerow(b25)
    for i in range(10):
        b24.writerow([f'Fold{i+1}', b16[i], b19[i], b22[i]])