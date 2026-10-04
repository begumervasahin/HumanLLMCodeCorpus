import numpy as np
import pandas as pd
from b15 import Visualizer
from preprocessor import Preprocessor
from b12 import Classifier
from b16 import Regressor
from b18 import Clustering
from sklearn.datasets import load_iris
def fonk1():
    b1 = int(input('Enter 1 for Classification, 2 for Regression, or 3 for Clustering: '))
    b5, b2 = fonk2(b1)
    b3 = fonk3(b1)
    b4 = Preprocessor()
    if b1 = = 3:
        b2 = b4.drop_missing(b2)
    else:
        b5 = b4.drop_missing(b5)
    if b1 in [1, 2]:
        b2, b6 = fonk4(b5, b1)
    else:
        b6 = None
    X_train, b8, y_train, b7 = fonk5(b4, b2, b6, b1)
    X_train, b8 = b4.scaling(X_train, b8, scale_type='Standard Scaler')
    fonk6(b1, X_train, y_train, b8, b7, b3)
def fonk2(b1):
    if b1 = = 1:
        b5 = pd.read_csv('wisconsin_breast_cancer.csv')
        b2 = None
    elif b1 = = 2:
        b5 = pd.read_csv('diamonds.csv')
        b2 = None
    elif b1 = = 3:
        b9 = load_iris(return_X_y=False)
        b5 = None
        b2 = b9['data']
    return b5, b2
def fonk3(b1):
    if b1 = = 1:
        b10 = int(input('Enter 1 for KNN, 2 for Decision Tree, 3 for Naive Bayes, 4 for Random Forest, or 5 for Neural Network: '))
        b11 = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
    elif b1 = = 2:
        b10 = int(input('Enter 1 for Linear Regression, 2 for Polynomial Regression, 3 for Decision Tree, 4 for KNN Regression, 5 for Random Forest Regressor, or 6 for Neural Network: '))
        b11 = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
    else:
        return 'K-Means'
    return b11[b10 - 1]
def fonk4(b5, b1):
    b4 = Preprocessor()
    if b1 = = 1:
        b2, b6 = b4.dataframe_to_numpy(b5, 'breast cancer')
        b2, b6 = b4.encoding(b2, b6, 'breast cancer')
    elif b1 = = 2:
        b2, b6 = b4.dataframe_to_numpy(b5, 'diamonds')
        b2, b6 = b4.encoding(b2, b6, 'diamonds')
    return b2, b6
def fonk5(b4, b2, b6, b1):
    if b1 in [1, 2]:
        X_train, b8, y_train, b7 = b4.fonk5(b2, 0.19, b6)
    else:
        X_train, b8 = b4.fonk5(b2, test_ratio=0.3)
        y_train, b7 = None, None
    return X_train, b8, y_train, b7
def fonk6(b1, X_train, y_train, b8, b7, b3):
    if b1 = = 1:
        fonk7(X_train, y_train, b8, b7, b3)
    elif b1 = = 2:
        fonk8(X_train, y_train, b8, b7, b3)
    elif b1 = = 3:
        fonk9(X_train, b8, b3)
def fonk7(X_train, y_train, b8, b7, b3):
    b12 = Classifier(b3)
    b13 = b12.classify(X_train, y_train, b8, b7)
    b14 = b12.get_accuracy(b7, b13)
    b15 = Visualizer()
    b15.plot_classifier_regressor(b7, b13, 1)
    print(f'The accuracy is: {b14:.2f} %')
    print(b3)
def fonk8(X_train, y_train, b8, b7, b3):
    b16 = Regressor(b3)
    b13 = b16.predict(X_train, y_train, b8)
    b17 = b16.get_score(b7, b13)
    b15 = Visualizer()
    b15.plot_classifier_regressor(b7, b13, 2)
    print(f'The coefficient of determination is: {b17:.2f}')
    print(b3)
def fonk9(X_train, b8, b3):
    b18 = Clustering(b3)
    n_clusters, b19 = b18.tune_parameters(X_train)
    b20 = b18.cluster(X_train, b8, n_clusters)
    b15 = Visualizer()
    b15.plot_clustering(b8, b20)
    print(f"The b18 model's b19: {b19:.2f}")
    print(b3)
if b21 = = "__main__":
    fonk1()