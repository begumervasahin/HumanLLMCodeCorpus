from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.b18 import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
def fonk1():
	b1 = []
	for i, (train_index, test_index) in enumerate(b16):
		b11, b2 = b12[train_index], b12[test_index]
		Y_train1, b3 = b10[train_index], b10[test_index]
		b4 = b18.fit(b11,Y_train1).predict(b2)
		b1.append(accuracy_score(b3, b4))
	return b1
b1 = []
b5 = []
b6 = []
b7 = []
b8 = pd.read_csv("grids.csv")
b9 = preprocessing.LabelEncoder()
b9.fit(b8["TripId"])
b10 = b9.transform(b8["TripId"])
b11 = b8['Grids']
b12 = np.array(b11)
b13 = CountVectorizer()
b14 = TfidfTransformer()
b15 = TruncatedSVD(n_components=300, random_state=42)
b16 = KFold(len(b12), n_folds=10)
b17 = KNeighborsClassifier(n_neighbors=7,n_jobs=-1)
b18 = Pipeline([
    ('vect', b13),
    ('tfidf', b14),
    ('b15',b15),
    ('b17', b17)
])
b5 = fonk1()
b17 = RandomForestClassifier(n_estimators=50,n_jobs=-1)
b18 = Pipeline([
    ('vect', b13),
    ('tfidf', b14),
    ('b15',b15),
    ('b17', b17)
])
b6 = fonk1()
b17 = LogisticRegression()
b18 = Pipeline([
    ('vect', b13),
    ('tfidf', b14),
    ('b15',b15),
    ('b17', b17)
])
b7 = fonk1()
b19 = open('EvaluationsMetricAccuracy', 'wb')
b20 = csv.writer(b19)
for i in range(1,11):
	b1.append('Fold'+str(i) )
b21 = ['Accuracy','KNN','RandomForests','LogisticRegression']
b22 = zip(b1, b5, b6,b7)
b20.writerow(b21)
b20.writerows(b22)
b19.close()