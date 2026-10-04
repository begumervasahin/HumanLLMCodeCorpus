import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.b16 import Pipeline
from sklearn.model_selection import GridSearchCV, KFold
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score
def fonk1(b17, b16, b8, b7):
    b1 = []
    for train_index, test_index in b17.split(b8):
        X_train1, b2 = b8[train_index], b8[test_index]
        Y_train1, b3 = b7[train_index], b7[test_index]
        b4 = b16.fit(X_train1, Y_train1).predict(b2)
        b1.append(accuracy_score(b3, b4))
    return b1
b5 = pd.read_csv("grids.csv")
b6 = preprocessing.LabelEncoder()
b6.fit(b5["TripId"])
b7 = b6.transform(b5["TripId"])
b8 = np.array(b5['Grids'])
b9 = CountVectorizer()
b10 = TfidfTransformer()
b11 = TruncatedSVD(n_components=300, random_state=42)
b12 = RandomForestClassifier(n_estimators=40, n_jobs=-1)
b13 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
b14 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
b15 = VotingClassifier(estimators=[('rf1', b12), ('rf2', b13), ('knn', b14)], voting='hard')
b16 = Pipeline([
    ('vect', b9),
    ('tfidf', b10),
    ('b11', b11),
    ('b15', b15)
])
b17 = KFold(n_splits=10)
b1 = fonk1(b17, b16, b8, b7)
print(b1)