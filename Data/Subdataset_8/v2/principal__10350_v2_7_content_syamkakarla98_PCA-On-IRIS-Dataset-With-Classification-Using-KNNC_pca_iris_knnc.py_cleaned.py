import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df = pd.read_csv("D:/Python_programs/ML/iris.csv")
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
X = df[features].values
y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset Before PCA', '*' * 11, '\n')
for K in range(25):
    K_value = K + 1
    knn_classifier = KNeighborsClassifier(n_neighbors=K_value, weights='uniform', algorithm='auto')
    knn_classifier.fit(X_train_scaled, y_train)
    y_pred = knn_classifier.predict(X_test_scaled)
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(accuracy, K_value))