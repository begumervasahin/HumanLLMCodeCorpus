import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = pd.read_csv("D:/Python_programs/ML/iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1.loc[:, b2].values
b4 = b1.loc[:, 'target'].values
b8, b9, y_train, b5 = train_test_split(
    b3, b4, b6 = 0.3, random_state=100)
b7 = StandardScaler()
b8 = b7.fit_transform(b8)
b9 = b7.transform(b9)
print('*'*11, 'Accuracy of IRIS Dataset Before PCA', '*'*11, '\n')
for K in range(25):
    b10 = K + 1
    b11 = KNeighborsClassifier(n_neighbors=b10, weights='uniform', algorithm='auto')
    b11.fit(b8, y_train)
    b12 = b11.predict(b9)
    b13 = metrics.accuracy_score(b5, b12) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(b13, b10))