import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
import csv
def compute_accuracy(pipeline, X, y):
    accuracies = []
    kf = KFold(n_splits=10)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        y_pred = pipeline.fit(X_train, y_train).predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))
    return accuracies
df = pd.read_csv("grids.csv")
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["TripId"])
X = df['Grids'].values
vectorizer = CountVectorizer()
tfidf_transformer = TfidfTransformer()
svd = TruncatedSVD(n_components=300, random_state=42)
classifiers = {
    "KNN": KNeighborsClassifier(n_neighbors=7, n_jobs=-1),
    "RandomForest": RandomForestClassifier(n_estimators=50, n_jobs=-1),
    "LogisticRegression": LogisticRegression()
}
results = {}
for name, clf in classifiers.items():
    pipeline = Pipeline([
        ('vect', vectorizer),
        ('tfidf', tfidf_transformer),
        ('svd', svd),
        ('clf', clf)
    ])
    results[name] = compute_accuracy(pipeline, X, y)
with open('EvaluationsMetricAccuracy.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    fieldnames = ['Fold'] + list(classifiers.keys())
    csv_writer.writerow(fieldnames)
    for i in range(10):
        row = [f'Fold{i+1}'] + [results[clf][i] for clf in classifiers.keys()]
        csv_writer.writerow(row)