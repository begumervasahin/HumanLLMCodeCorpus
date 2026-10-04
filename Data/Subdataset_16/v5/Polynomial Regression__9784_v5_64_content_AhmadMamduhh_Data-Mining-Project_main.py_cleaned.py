import numpy as np
import pandas as pd
from b11 import Visualizer
from preprocessor import Preprocessor
from sklearn.datasets import load_iris
def fonk1():
    return int(input('Enter 1 for Classification, 2 for Regression, or 3 for Clustering: '))
def fonk2(b1):
    if b1 = = 1:
        return pd.read_csv('wisconsin_breast_cancer.csv')
    elif b1 = = 2:
        return pd.read_csv('diamonds.csv')
    elif b1 = = 3:
        b2 = load_iris()
        return b2['data'], b2
def fonk3(b1):
    if b1 = = 1:
        b3 = int(input('Enter 1 for KNN, 2 for Decision Tree, 3 for Naive Bayes, 4 for Random Forest, or 5 for Neural Network: '))
        b4 = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
        return b4[b3 - 1]
    elif b1 = = 2:
        b3 = int(input('Enter 1 for Linear Regression, 2 for Polynomial Regression, 3 for Decision Tree, 4 for KNN Regression, 5 for Random Forest Regressor, or 6 for Neural Network: '))
        b4 = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
        return b4[b3 - 1]
    else:
        return 'K-Means'
def fonk4(b1, b5, b20):
    if b1 = = 3:
        return b20.drop_missing(b5), None
    else:
        b5 = b20.drop_missing(b5)
        b6 = 'breast cancer' if b1 == 1 else 'diamonds'
        X, b7 = b20.dataframe_to_numpy(b5, b6)
        X, b7 = b20.encoding(X, b7, b6)
        return X, b7
def fonk5(b1, b20, X, b7 = None):
    if b1 in [1, 2]:
        X_train, b9, b10, b8 = b20.split_data(X, 0.19, b7)
        X_train, b9 = b20.scaling(X_train, b9, scale_type='Standard Scaler')
        return X_train, b9, b10, b8
    else:
        X_train, b9 = b20.split_data(X, test_ratio=0.3)
        X_train, b9 = b20.scaling(X_train, b9, scale_type='Standard Scaler')
        return X_train, b9
def fonk6(b1, b22, X_train, b9, b10 = None, b8=None):
    b11 = Visualizer()
    if b1 = = 1:
        from b12 import Classifier
        b12 = Classifier(b22)
        b13 = b12.classify(X_train, b10, b9, b8)
        b14 = b12.get_accuracy(b8, b13)
        b11.plot_classifier_regressor(b8, b13, b1)
        print(f'The b14 is: {b14} %')
        print(b22)
    elif b1 = = 2:
        from b15 import Regressor
        b15 = Regressor(b22)
        b13 = b15.predict(X_train, b10, b9)
        b16 = b15.get_score(b8, b13)
        b11.plot_classifier_regressor(b8, b13, b1)
        print(f'The coefficient of determination is: {b16}')
        print(b22)
    elif b1 = = 3:
        from b17 import Clustering
        b17 = Clustering(b22)
        n_clusters, b18 = b17.tune_parameters(X_train)
        b19 = b17.cluster(X_train, b9, n_clusters)
        b11.plot_clustering(b9, b19)
        print(f"The b17 model's b18: {b18}")
        print(b22)
def fonk7():
    b1 = fonk1()
    b20 = Preprocessor()
    if b1 = = 3:
        X, b21 = fonk2(b1)
        b5 = X
    else:
        b5 = fonk2(b1)
    b22 = fonk3(b1)
    if b1 = = 3:
        X, b23 = fonk4(b1, b5, b20)
        X_train, b9 = fonk5(b1, b20, X)
        fonk6(b1, b22, X_train, b9)
    else:
        X, b7 = fonk4(b1, b5, b20)
        X_train, b9, b10, b8 = fonk5(b1, b20, X, b7)
        fonk6(b1, b22, X_train, b9, b10, b8)
if b24 = = "__main__":
    fonk7()