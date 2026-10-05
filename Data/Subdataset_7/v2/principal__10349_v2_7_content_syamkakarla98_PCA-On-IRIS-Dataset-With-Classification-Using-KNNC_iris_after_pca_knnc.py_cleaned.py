
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
X_train, X_test, b6, b5 = train_test_split(b3, b4, test_size=0.3, random_state=100)
b6 = b6.ravel()
b5 = b5.ravel()
b7 = KNeighborsClassifier()
b7.fit(X_train, b6)
b8 = b7.predict(X_test)
print('*'*11, 'Accuracy of IRIS Dataset after PCA', '*'*11, '\n')
for K in range(25):
    b9 = K + 1
    b10 = KNeighborsClassifier(n_neighbors=b9, weights='uniform', algorithm='auto')
    b10.fit(X_train, b6)
    b11 = b10.predict(X_test)
    b12 = metrics.accuracy_score(b5, b11)
    print("Accuracy is {:.2f}% for K-Value: {}".format(b12 * 100, b9))