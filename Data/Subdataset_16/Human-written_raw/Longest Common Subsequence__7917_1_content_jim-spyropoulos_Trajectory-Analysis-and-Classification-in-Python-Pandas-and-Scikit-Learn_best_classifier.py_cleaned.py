from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.b18 import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn import metrics
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
def fonk1():
	b1 = []
	for i, (train_index, test_index) in enumerate(b13):
		b8, b2 = b9[train_index], b9[test_index]
		Y_train1, b3 = b7[train_index], b7[test_index]
		b4 = b18.fit(b8,Y_train1).predict(b2)
		b1.append(accuracy_score(b3, b4))
	return b1
'''			preprocessing:
apart from CountVectorizer and TfidfTransformer TruncatedSVD of 300 elements and random state 42'''
b5 = pd.read_csv("grids.csv")
b6 = preprocessing.LabelEncoder()
b6.fit(b5["TripId"])
b7 = b6.transform(b5["TripId"])
b8 = b5['Grids']
b9 = np.array(b8)
b10 = CountVectorizer()
b11 = TfidfTransformer()
b12 = TruncatedSVD(n_components=300, random_state=42)
b13 = KFold(len(b9), n_folds=10)
'''1 best version of KNN
2 simple RandomForestClassifier
3 Best RandomForestClassifier'''
b14 = RandomForestClassifier(n_estimators=40,n_jobs=-1)
b15 = RandomForestClassifier(n_estimators=50,n_jobs=-1)
b16 = KNeighborsClassifier(n_neighbors=7,n_jobs=-1)
b17 = VotingClassifier(estimators=[('rf1',b14),('rf2',b15),('knn',b16)], voting='hard')
b18 = Pipeline([
    ('vect', b10),
    ('tfidf', b11),
    ('b12',b12),
    ('b17', b17)
])
print fonk1()