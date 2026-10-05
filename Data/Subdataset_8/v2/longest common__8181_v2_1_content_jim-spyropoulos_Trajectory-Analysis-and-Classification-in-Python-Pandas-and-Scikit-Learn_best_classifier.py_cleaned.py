import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
def compute_and_print(X_train, Y_train, kf, pipeline):
    accuracies = []
    for fold, (train_index, test_index) in enumerate(kf):
        X_train_fold, X_test_fold = X_train[train_index], X_train[test_index]
        Y_train_fold, Y_test_fold = Y_train[train_index], Y_train[test_index]
        predictions = pipeline.fit(X_train_fold, Y_train_fold).predict(X_test_fold)
        accuracy = accuracy_score(Y_test_fold, predictions)
        accuracies.append(accuracy)
    return accuracies
df = pd.read_csv("grids.csv")
label_encoder = LabelEncoder()
label_encoder.fit(df["TripId"])
Y_train = label_encoder.transform(df["TripId"])
X_train = np.array(df['Grids'])
vectorizer = CountVectorizer()
tfidf_transformer = TfidfTransformer()
svd = TruncatedSVD(n_components=300, random_state=42)
kf = KFold(n_splits=10)
clf1 = RandomForestClassifier(n_estimators=40, n_jobs=-1)
clf2 = RandomForestClassifier(n_estimators=50, n_jobs=-1)
clf3 = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
voting_classifier = VotingClassifier(estimators=[('rf1', clf1), ('rf2', clf2), ('knn', clf3)], voting='hard')
pipeline = Pipeline([
    ('vect', vectorizer),
    ('tfidf', tfidf_transformer),
    ('svd', svd),
    ('clf', voting_classifier)
])
accuracies = compute_and_print(X_train, Y_train, kf.split(X_train), pipeline)
print(accuracies)