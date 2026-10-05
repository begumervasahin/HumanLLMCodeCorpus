
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = pd.read_csv("D:\Python_programs\ML\iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1[b2].values
b4 = b1['target'].values
X_train, X_test, b6, b5 = train_test_split(b3, b4, test_size=0.3, random_state=100)
b6 = b6.ravel()
b5 = b5.ravel()
b7 = KNeighborsClassifier()
b7.fit(X_train, b6)
b8 = b7.predict(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset Before PCA', '*' * 11, '\n')
for k_value in range(1, 26):
    b9 = KNeighborsClassifier(n_neighbors=k_value, weights='uniform', algorithm='auto')
    b9.fit(X_train, b6)
    b8 = b9.predict(X_test)
    b10 = metrics.accuracy_score(b5, b8) * 100
    print(f"Accuracy is {b10:.2f}% for K-Value: {k_value}")