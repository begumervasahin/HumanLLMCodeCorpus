import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.b18 import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
def fonk1(b9, b8, b13, b18):
    b1 = []
    for fold, (train_index, test_index) in enumerate(b13):
        X_train_fold, b2 = b9[train_index], b9[test_index]
        Y_train_fold, b3 = b8[train_index], b8[test_index]
        b4 = b18.fit(X_train_fold, Y_train_fold).predict(b2)
        b5 = accuracy_score(b3, b4)
        b1.append(b5)
    return b1
def fonk2():
    b6 = pd.read_csv("grids.csv")
    b7 = LabelEncoder()
    b7.fit(b6["TripId"])
    b8 = b7.transform(b6["TripId"])
    b9 = np.array(b6['Grids'])
    b10 = CountVectorizer()
    b11 = TfidfTransformer()
    b12 = TruncatedSVD(n_components=300, random_state=42)
    b13 = KFold(n_splits=10)
    b14 = RandomForestClassifier(n_estimators=40, n_jobs=-1)
    b15 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
    b16 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
    b17 = VotingClassifier(estimators=[('rf1', b14), ('rf2', b15), ('knn', b16)], voting='hard')
    b18 = Pipeline([
        ('vect', b10),
        ('tfidf', b11),
        ('b12', b12),
        ('clf', b17)
    ])
    b1 = fonk1(b9, b8, b13.split(b9), b18)
    print("Accuracy for each fold:", b1)
if b19 = = "__main__":
    fonk2()