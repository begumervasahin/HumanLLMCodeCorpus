import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.b17 import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import csv
def fonk1(b17, b9, b8):
    b1 = []
    b2 = KFold(n_splits=10)
    for train_index, test_index in b2.split(b9):
        X_train, b3 = b9[train_index], b9[test_index]
        y_train, b4 = b8[train_index], b8[test_index]
        b5 = b17.fit(X_train, y_train).predict(b3)
        b1.append(accuracy_score(b4, b5))
    return b1
b6 = pd.read_csv("grids.csv")
b7 = LabelEncoder()
b8 = b7.fit_transform(b6["TripId"])
b9 = b6['Grids'].values
b10 = CountVectorizer()
b11 = TfidfTransformer()
b12 = TruncatedSVD(n_components=300, random_state=42)
b13 = {
    "KNN": KNeighborsClassifier(b14 = 7, n_jobs=-1),
    "RandomForest": RandomForestClassifier(b15 = 50, n_jobs=-1),
    "LogisticRegression": LogisticRegression()
}
b16 = {}
for name, clf in b13.items():
    b17 = Pipeline([
        ('vect', b10),
        ('tfidf', b11),
        ('b12', b12),
        ('clf', clf)
    ])
    b16[name] = fonk1(b17, b9, b8)
with open('EvaluationsMetricAccuracy.csv', 'w', b18 = '') as csv_out:
    b19 = csv.writer(csv_out)
    b20 = ['Fold'] + list(b13.keys())
    b19.writerow(b20)
    for i in range(10):
        b21 = [f'Fold{i+1}'] + [b16[clf][i] for clf in b13.keys()]
        b19.writerow(b21)