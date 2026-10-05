
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df = pd.read_csv("D:\Python_programs\ML\iris.csv")
feature_columns = ['sepal length', 'sepal width', 'petal length', 'petal width']
X = df[feature_columns].values
y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
y_train = y_train.ravel()
y_test = y_test.ravel()
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
y_pred = knn_model.predict(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset Before PCA', '*' * 11, '\n')
for k_value in range(1, 26):
    knn_classifier = KNeighborsClassifier(n_neighbors=k_value, weights='uniform', algorithm='auto')
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print(f"Accuracy is {accuracy:.2f}% for K-Value: {k_value}")