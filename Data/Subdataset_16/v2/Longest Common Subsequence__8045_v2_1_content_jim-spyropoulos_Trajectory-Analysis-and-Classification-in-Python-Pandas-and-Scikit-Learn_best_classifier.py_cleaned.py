import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.b17 import Pipeline
from sklearn.metrics import accuracy_score
def fonk1(b8, b7, b17, b12):
    b1 = []
    for train_index, test_index in b12.split(b8):
        X_train1, b2 = b8[train_index], b8[test_index]
        Y_train1, b3 = b7[train_index], b7[test_index]
        b4 = b17.fit(X_train1, Y_train1).predict(b2)
        b1.append(accuracy_score(b3, b4))
    return b1
b5 = pd.read_csv("grids.csv")
b6 = preprocessing.LabelEncoder()
b6.fit(b5["TripId"])
b7 = b6.transform(b5["TripId"])
b8 = b5['Grids'].values
b9 = CountVectorizer()
b10 = TfidfTransformer()
b11 = TruncatedSVD(n_components=300, random_state=42)
b12 = KFold(n_splits=10, shuffle=True, random_state=42)
b13 = RandomForestClassifier(n_estimators=40, n_jobs=-1)
b14 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b15 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b16 = VotingClassifier(estimators=[('rf1', b13), ('rf2', b14), ('knn', b15)], voting='hard')
b17 = Pipeline([
    ('vect', b9),
    ('tfidf', b10),
    ('b11', b11),
    ('b16', b16)
])
b1 = fonk1(b8, b7, b17, b12)
print(b1)