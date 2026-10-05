import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import decomposition
from sklearn import datasets
b1 = pd.read_csv("D:\Python_programs\ML\iris.csv")
from sklearn.preprocessing import StandardScaler
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1.loc[:, b2].values
b4 = b1.loc[:,['target']].values
from sklearn.model_selection import train_test_split
X_train, X_test, b7, b5 = train_test_split(
 b3, b4, b6 = 0.3, random_state = 100)
b7 = b7.ravel()
b5 = b5.ravel()
from sklearn.neighbors import KNeighborsClassifier
b8 = KNeighborsClassifier()
b8.fit(X_train, b7)
b9 = b8.predict(X_test)
from sklearn import metrics
print('*'*11,'Accuracy of IRIS Dataset Before PCA','*'*11,'\n')
for K in range(25):
 b10 = K+1
 b11 = KNeighborsClassifier(n_neighbors = b10, weights='uniform', algorithm='auto')
 b11.fit(X_train, b7)
 b12 = b11.predict(X_test)
 print ("Accuracy is ", metrics.accuracy_score(b5,b12)*100,"% for K-Value:",b10)