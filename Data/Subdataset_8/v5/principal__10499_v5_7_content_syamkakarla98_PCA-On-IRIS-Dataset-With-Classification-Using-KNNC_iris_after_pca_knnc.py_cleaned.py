
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df = pd.read_csv("D:\Python_programs\ML\iris_after_pca.csv")
features = ['PC-1', 'PC-2']
X = df[features].values
Y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
model = KNeighborsClassifier()
model.fit(X_train, y_train)
Yhat = model.predict(X_test)
print('*' * 11, 'Accuracy of IRIS Dataset after PCA', '*' * 11, '\n')
for K in range(25):
    K_value = K + 1
    neigh = KNeighborsClassifier(n_neighbors=K_value, weights='uniform', algorithm='auto')
    neigh.fit(X_train, y_train)
    y_pred = neigh.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print("Accuracy is {:.2f}% for K-Value: {}".format(accuracy, K_value))