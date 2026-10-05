from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn import metrics
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import csv
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score
def compute_and_print(X_train, Y_train, kf, pipeline):
    stats = []
    for i, (train_index, test_index) in enumerate(kf):
        X_train1, X_test = X_train[train_index], X_train[test_index]
        Y_train1, Y_test = Y_train[train_index], Y_train[test_index]
        probas_ = pipeline.fit(X_train1, Y_train1).predict(X_test)
        stats.append(accuracy_score(Y_test, probas_))
    return stats
df = pd.read_csv("grids.csv")
le = preprocessing.LabelEncoder()
le.fit(df["TripId"])
Y_train = le.transform(df["TripId"])
X_train1 = df['Grids']
X_train = np.array(X_train1)
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
svd = TruncatedSVD(n_components=300, random_state=42)
kf = KFold(len(X_train), n_folds=10)
clf1 = RandomForestClassifier(n_estimators=40, n_jobs=-1)
clf2 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
clf3 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
clf = VotingClassifier(estimators=[('rf1', clf1), ('rf2', clf2), ('knn', clf3)], voting='hard')
pipeline = Pipeline([
    ('vect', vectorizer),
    ('tfidf', transformer),
    ('svd', svd),
    ('clf', clf)
])
print(compute_and_print(X_train, Y_train, kf, pipeline))