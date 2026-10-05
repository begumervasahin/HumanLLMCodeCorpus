import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = pd.read_csv("D:/Python_programs/ML/iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1[b2].values
b4 = b1['target'].values
X_train, X_test, y_train, b5 = train_test_split(b3, b4, test_size=0.3, random_state=100)
b6 = StandardScaler()
b7 = b6.fit_transform(X_train)
b8 = b6.transform(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset Before PCA', '*' * 11, '\n')
for K in range(25):
    b9 = K + 1
    b10 = KNeighborsClassifier(n_neighbors=b9, weights='uniform', algorithm='auto')
    b10.fit(b7, y_train)
    b11 = b10.predict(b8)
    b12 = metrics.accuracy_score(b5, b11) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(b12, b9))