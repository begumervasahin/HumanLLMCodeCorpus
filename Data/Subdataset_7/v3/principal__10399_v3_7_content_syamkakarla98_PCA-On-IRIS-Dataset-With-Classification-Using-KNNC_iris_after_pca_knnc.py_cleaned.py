
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
b1 = "D:\Python_programs\ML\iris_after_pca.csv"
b2 = pd.read_csv(b1)
b3 = ['PC-1', 'PC-2']
b4 = b2[b3].values
b5 = b2['target'].values
X_train, X_test, y_train, b6 = train_test_split(b4, b5, test_size=0.3, random_state=100)
b7 = KNeighborsClassifier()
b7.fit(X_train, y_train)
b8 = b7.predict(X_test)
print('*'*11, 'Accuracy of IRIS Dataset after PCA', '*'*11, '\n')
for K in range(1, 26):
    b9 = KNeighborsClassifier(n_neighbors=K, weights='uniform', algorithm='auto')
    b9.fit(X_train, y_train)
    b10 = b9.predict(X_test)
    b11 = metrics.accuracy_score(b6, b10)
    print(f"Accuracy is {b11*100:.2f}% for K-Value: {K}")