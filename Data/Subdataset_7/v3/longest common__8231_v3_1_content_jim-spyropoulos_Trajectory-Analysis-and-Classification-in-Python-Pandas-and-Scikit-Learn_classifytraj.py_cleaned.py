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
def fonk1(b9, b8, b22, pipeline):
    b1 = []
    for fold, (train_index, test_index) in enumerate(b22):
        X_train_fold, b2 = b9[train_index], b9[test_index]
        Y_train_fold, b3 = b8[train_index], b8[test_index]
        b4 = pipeline.fit(X_train_fold, Y_train_fold).predict(b2)
        b5 = accuracy_score(b3, b4)
        b1.append(b5)
    return b1
def fonk2(file_path):
    b6 = pd.read_csv(file_path)
    b7 = preprocessing.LabelEncoder()
    b7.fit(b6["TripId"])
    b8 = b7.transform(b6["TripId"])
    b9 = np.array(b6['Grids'])
    return b9, b8
def fonk3():
    b10 = CountVectorizer()
    b11 = TfidfTransformer()
    b12 = TruncatedSVD(n_components=300, random_state=42)
    b13 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
    b14 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
    b15 = LogisticRegression()
    b16 = Pipeline([('vect', b10), ('tfidf', b11), ('b12', b12), ('clf', b13)])
    b17 = Pipeline([('vect', b10), ('tfidf', b11), ('b12', b12), ('clf', b14)])
    b18 = Pipeline([('vect', b10), ('tfidf', b11), ('b12', b12), ('clf', b15)])
    return b16, b17, b18
def fonk4(file_path, b23, b24, b25):
    with open(file_path, 'w', b19 = '') as csv_out:
        b20 = csv.writer(csv_out)
        b20.writerow(['Fold', 'KNN', 'RandomForests', 'LogisticRegression'])
        for i in range(10):
            b20.writerow(['Fold' + str(i + 1), b23[i], b24[i], b25[i]])
if b21 = = "__main__":
    b9, b8 = fonk2("grids.csv")
    b22 = KFold(n_splits=10)
    b16, b17, b18 = fonk3()
    b23 = fonk1(b9, b8, b22.split(b9), b16)
    b24 = fonk1(b9, b8, b22.split(b9), b17)
    b25 = fonk1(b9, b8, b22.split(b9), b18)
    fonk4('EvaluationsMetricAccuracy.csv', b23, b24, b25)