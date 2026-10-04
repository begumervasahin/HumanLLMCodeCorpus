import numpy as np
import pandas as pd
from b13 import Visualizer
from preprocessor import Preprocessor
from sklearn.datasets import load_iris
b1 = int(input('Enter 1 for Classification, 2 for Regression, or 3 for Clustering: '))
if b1 = = 1:
    b2 = pd.read_csv('wisconsin_breast_cancer.csv')
elif b1 = = 2:
    b2 = pd.read_csv('diamonds.csv')
elif b1 = = 3:
    b3 = load_iris()
    b4 = b3['data']
    b5 = load_iris()
if b1 = = 1:
    b6 = int(input('Enter 1 for KNN, 2 for Decision Tree, 3 for Naive Bayes, 4 for Random Forest, or 5 for Neural Network: '))
    b7 = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
    b8 = b7[b6 - 1]
elif b1 = = 2:
    b6 = int(input('Enter 1 for Linear Regression, 2 for Polynomial Regression, 3 for Decision Tree, 4 for KNN Regression, 5 for Random Forest Regressor, or 6 for Neural Network: '))
    b7 = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
    b8 = b7[b6 - 1]
else:
    b8 = 'K-Means'
b9 = Preprocessor()
if b1 = = 3:
    b4 = b9.drop_missing(b4)
else:
    b2 = b9.drop_missing(b2)
if b1 = = 1:
    b4, b10 = b9.dataframe_to_numpy(b2, 'breast cancer')
    b4, b10 = b9.encoding(b4, b10, 'breast cancer')
elif b1 = = 2:
    b4, b10 = b9.dataframe_to_numpy(b2, 'diamonds')
    b4, b10 = b9.encoding(b4, b10, 'diamonds')
if b1 in [1, 2]:
    X_train, b12, y_train, b11 = b9.split_data(b4, 0.19, b10)
else:
    X_train, b12 = b9.split_data(b4, test_ratio=0.3)
X_train, b12 = b9.scaling(X_train, b12, scale_type='Standard Scaler')
b13 = Visualizer()
if b1 = = 1:
    from b14 import Classifier
    b14 = Classifier(b8)
    b15 = b14.classify(X_train, y_train, b12, b11)
    b16 = b14.get_accuracy(b11, b15)
    b13.plot_classifier_regressor(b11, b15, b1)
    print(f'The accuracy is: {b16} %')
    print(b8)
elif b1 = = 2:
    from b17 import Regressor
    b17 = Regressor(b8)
    b15 = b17.predict(X_train, y_train, b12)
    b18 = b17.get_score(b11, b15)
    b13.plot_classifier_regressor(b11, b15, b1)
    print(f'The coefficient of determination is: {b18}')
    print(b8)
elif b1 = = 3:
    from b19 import Clustering
    b19 = Clustering(b8)
    n_clusters, b20 = b19.tune_parameters(X_train)
    b21 = b19.cluster(X_train, b12, n_clusters)
    b13.plot_clustering(b12, b21)
    print(f"The b19 model's b20: {b20}")
    print(b8)