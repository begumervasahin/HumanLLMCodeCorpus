
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
dataset_path = "D:\Python_programs\ML\iris_after_pca.csv"
df = pd.read_csv(dataset_path)
features = ['PC-1', 'PC-2']
X = df[features].values
Y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
y_pred_test = knn_model.predict(X_test)
print('*'*11, 'Accuracy of IRIS Dataset after PCA', '*'*11, '\n')
for K in range(1, 26):
    knn_classifier = KNeighborsClassifier(n_neighbors=K, weights='uniform', algorithm='auto')
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy is {accuracy*100:.2f}% for K-Value: {K}")