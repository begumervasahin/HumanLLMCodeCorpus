
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = pd.read_csv("D:\Python_programs\ML\iris_after_pca.csv")
b2 = ['PC-1', 'PC-2']
b3 = b1[b2].values
b4 = b1['target'].values
X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.3, random_state=100)
b6 = KNeighborsClassifier()
b6.fit(X_train, y_train)
b7 = b6.predict(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset after PCA', '*' * 11, '\n')
for K in range(25):
    b8 = K + 1
    b9 = KNeighborsClassifier(n_neighbors=b8, weights='uniform', algorithm='auto')
    b9.fit(X_train, y_train)
    b10 = b9.predict(X_test)
    b11 = metrics.accuracy_score(b5, b10) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(b11, b8))