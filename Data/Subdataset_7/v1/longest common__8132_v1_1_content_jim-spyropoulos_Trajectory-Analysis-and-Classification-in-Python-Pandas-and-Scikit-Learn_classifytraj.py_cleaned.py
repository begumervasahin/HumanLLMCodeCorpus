from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.b15 import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
def fonk1(b9, b7, b13, b15):
    b1 = []
    for i, (train_index, test_index) in enumerate(b13):
        b8, b2 = b9[train_index], b9[test_index]
        Y_train1, b3 = b7[train_index], b7[test_index]
        b4 = b15.fit(b8, Y_train1).predict(b2)
        b1.append(accuracy_score(b3, b4))
    return b1
b5 = pd.read_csv("grids.csv")
b6 = preprocessing.LabelEncoder()
b6.fit(b5["TripId"])
b7 = b6.transform(b5["TripId"])
b8 = b5['Grids']
b9 = np.array(b8)
b10 = CountVectorizer()
b11 = TfidfTransformer()
b12 = TruncatedSVD(n_components=300, random_state=42)
b13 = KFold(n_splits=10)
b14 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b15 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('b14', b14)
])
b16 = fonk1(b9, b7, b13.split(b9), b15)
b14 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b15 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('b14', b14)
])
b17 = fonk1(b9, b7, b13.split(b9), b15)
b14 = LogisticRegression()
b15 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12', b12),
    ('b14', b14)
])
b18 = fonk1(b9, b7, b13.split(b9), b15)
with open('EvaluationsMetricAccuracy.csv', 'w', b19 = '') as csv_out:
    b20 = csv.writer(csv_out)
    b21 = ['Accuracy', 'KNN', 'RandomForests', 'LogisticRegression']
    b20.writerow(b21)
    for i in range(10):
        b22 = ['Fold' + str(i + 1), b16[i], b17[i], b18[i]]
        b20.writerow(b22)