import pandas as pd
import numpy as np
import csv
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.b17 import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
def fonk1(b17, b8, b7, b12):
    b1 = []
    for train_index, test_index in b12.split(b8):
        X_train1, b2 = b8[train_index], b8[test_index]
        Y_train1, b3 = b7[train_index], b7[test_index]
        b4 = b17.fit(X_train1, Y_train1).predict(b2)
        b1.append(accuracy_score(b3, b4))
    return b1
b5 = pd.read_csv("grids.csv")
b6 = LabelEncoder()
b7 = b6.fit_transform(b5["TripId"])
b8 = b5['Grids'].values
b9 = CountVectorizer()
b10 = TfidfTransformer()
b11 = TruncatedSVD(n_components=300, random_state=42)
b12 = KFold(n_splits=10, shuffle=True, random_state=42)
b13 = {
    'KNN': KNeighborsClassifier(b14 = 7, n_jobs=-1),
    'RandomForest': RandomForestClassifier(b15 = 50, n_jobs=-1),
    'LogisticRegression': LogisticRegression()
}
b16 = {}
for name, clf in b13.items():
    b17 = Pipeline([
        ('vect', b9),
        ('tfidf', b10),
        ('b11', b11),
        ('clf', clf)
    ])
    b16[name] = fonk1(b17, b8, b7, b12)
b18 = ['Fold'] + list(b13.keys())
b19 = list(zip(['Fold'+str(i) for i in range(1, 11)], *b16.values()))
with open('EvaluationsMetricAccuracy.csv', 'w', b20 = '') as csv_out:
    b21 = csv.writer(csv_out)
    b21.writerow(b18)
    b21.writerows(b19)
print("Evaluation metrics saved to EvaluationsMetricAccuracy.csv")