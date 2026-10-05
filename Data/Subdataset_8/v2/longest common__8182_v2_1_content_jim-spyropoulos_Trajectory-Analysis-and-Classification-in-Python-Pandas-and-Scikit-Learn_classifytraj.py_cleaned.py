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
def compute_accuracy(X_train, Y_train, kf, pipeline):
    accuracies = []
    for fold, (train_index, test_index) in enumerate(kf):
        X_train_fold, X_test_fold = X_train[train_index], X_train[test_index]
        Y_train_fold, Y_test_fold = Y_train[train_index], Y_train[test_index]
        predicted_labels = pipeline.fit(X_train_fold, Y_train_fold).predict(X_test_fold)
        accuracy = accuracy_score(Y_test_fold, predicted_labels)
        accuracies.append(accuracy)
    return accuracies
data = pd.read_csv("grids.csv")
le = preprocessing.LabelEncoder()
le.fit(data["TripId"])
Y_train = le.transform(data["TripId"])
X_train = np.array(data['Grids'])
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
svd = TruncatedSVD(n_components=300, random_state=42)
kf = KFold(n_splits=10)
knn_classifier = KNeighborsClassifier(n_neighbors=7, n_jobs=-1)
random_forest_classifier = RandomForestClassifier(n_estimators=50, n_jobs=-1)
logistic_regression_classifier = LogisticRegression()
knn_pipeline = Pipeline([
    ('vect', vectorizer),
    ('tfidf', transformer),
    ('svd', svd),
    ('clf', knn_classifier)
])
random_forest_pipeline = Pipeline([
    ('vect', vectorizer),
    ('tfidf', transformer),
    ('svd', svd),
    ('clf', random_forest_classifier)
])
logistic_regression_pipeline = Pipeline([
    ('vect', vectorizer),
    ('tfidf', transformer),
    ('svd', svd),
    ('clf', logistic_regression_classifier)
])
knn_accuracies = compute_accuracy(X_train, Y_train, kf.split(X_train), knn_pipeline)
random_forest_accuracies = compute_accuracy(X_train, Y_train, kf.split(X_train), random_forest_pipeline)
logistic_regression_accuracies = compute_accuracy(X_train, Y_train, kf.split(X_train), logistic_regression_pipeline)
with open('EvaluationsMetricAccuracy.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(['Fold', 'KNN', 'RandomForests', 'LogisticRegression'])
    for i in range(10):
        csv_writer.writerow(['Fold' + str(i + 1), knn_accuracies[i], random_forest_accuracies[i], logistic_regression_accuracies[i]])