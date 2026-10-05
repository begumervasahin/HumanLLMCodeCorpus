
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import decomposition
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = pd.read_csv("D:\Python_programs\ML\iris_after_pca.csv")
b2 = ['PC-1', 'PC-2']
b3 = b1.loc[:, b2].values
b4 = b1.loc[:, ['target']].values
X_train, X_test, b7, b5 = train_test_split(
    b3, b4, b6 = 0.3, random_state=100)
b7 = b7.ravel()
b5 = b5.ravel()
b8 = KNeighborsClassifier()
b8.fit(X_train, b7)
b9 = b8.predict(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset after PCA', '*' * 11, '\n')
for K in range(25):
    b10 = K + 1
    b11 = KNeighborsClassifier(n_neighbors=b10, weights='uniform', algorithm='auto')
    b11.fit(X_train, b7)
    b12 = b11.predict(X_test)
    b13 = metrics.accuracy_score(b5, b12) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(b13, b10))