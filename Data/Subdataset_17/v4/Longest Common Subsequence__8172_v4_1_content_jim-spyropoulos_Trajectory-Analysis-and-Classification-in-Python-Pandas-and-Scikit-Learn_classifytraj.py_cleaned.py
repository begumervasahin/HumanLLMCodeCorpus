import pandas as pd
import numpy as np
import csv
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
def compute_and_print(pipeline, X_train, Y_train, kf):
    stats = []
    for train_index, test_index in kf.split(X_train):
        X_train1, X_test = X_train[train_index], X_train[test_index]
        Y_train1, Y_test = Y_train[train_index], Y_train[test_index]
        probas_ = pipeline.fit(X_train1, Y_train1).predict(X_test)
        stats.append(accuracy_score(Y_test, probas_))
    return stats
df = pd.read_csv("grids.csv")
le = LabelEncoder()
Y_train = le.fit_transform(df["TripId"])
X_train = df['Grids'].values
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
svd = TruncatedSVD(n_components=300, random_state=42)
kf = KFold(n_splits=10, shuffle=True, random_state=42)
classifiers = {
    'KNN': KNeighborsClassifier(n_neighbors=7, n_jobs=-1),
    'RandomForest': RandomForestClassifier(n_estimators=50, n_jobs=-1),
    'LogisticRegression': LogisticRegression()
}
stats_dict = {}
for name, clf in classifiers.items():
    pipeline = Pipeline([
        ('vect', vectorizer),
        ('tfidf', transformer),
        ('svd', svd),
        ('clf', clf)
    ])
    stats_dict[name] = compute_and_print(pipeline, X_train, Y_train, kf)
fieldnames = ['Fold'] + list(classifiers.keys())
rows = list(zip(['Fold'+str(i) for i in range(1, 11)], *stats_dict.values()))
with open('EvaluationsMetricAccuracy.csv', 'w', newline='') as csv_out:
    clwriter = csv.writer(csv_out)
    clwriter.writerow(fieldnames)
    clwriter.writerows(rows)
print("Evaluation metrics saved to EvaluationsMetricAccuracy.csv")