import numpy as np
import pandas as pd
from b16 import Visualizer
from preprocessor import Preprocessor
from b13 import Classifier
from b17 import Regressor
from b19 import Clustering
from sklearn.datasets import load_iris
def fonk1():
    b1 = int(input('Enter 1 to choose Classification, 2 to choose Regression or 3 to choose Clustering: '))
    if b1 = = 1:
        b2 = pd.read_csv('wisconsin_breast_cancer.csv')
    elif b1 = = 2:
        b2 = pd.read_csv('diamonds.csv')
    elif b1 = = 3:
        b3 = load_iris(return_X_y=False)
        b4 = b3['data']
        b5 = load_iris()
    if b1 = = 1:
        b6 = int(input('Enter 1 to choose KNN, 2 to choose Decision Tree, 3 to choose Naive Bayes, 4 to choose Random Forest or 5 to choose Neural Network: '))
        b7 = fonk2(b6, b1)
    elif b1 = = 2:
        b6 = int(input('Enter 1 to choose Linear Regression, 2 to choose Polynomial Regression, 3 to choose Decision Tree, 4 to choose KNN Regression, 5 to choose Random Forest Regressor or 6 to choose Neural Network: '))
        b7 = fonk2(b6, b1)
    else:
        b7 = 'K-Means'
    b8 = Preprocessor()
    if b1 = = 3:
        b4 = b8.drop_missing(b4)
    else:
        b2 = b8.drop_missing(b2)
    if b1 = = 1:
        b4, b9 = b8.dataframe_to_numpy(b2, 'breast cancer')
        b4, b9 = b8.encoding(b4, b9, 'breast cancer')
    elif b1 = = 2:
        b4, b9 = b8.dataframe_to_numpy(b2, 'diamonds')
        b4, b9 = b8.encoding(b4, b9, 'diamonds')
    if b1 = = 1 or b1 == 2:
        X_train, b11, y_train, b10 = b8.split_data(b4, 0.19, b9)
    elif b1 = = 3:
        X_train, b11 = b8.split_data(b4, test_ratio=0.3)
    X_train, b11 = b8.scaling(X_train, b11, scale_type='Standard Scaler')
    if b1 = = 1:
        fonk3(X_train, y_train, b11, b10, b7)
    elif b1 = = 2:
        fonk4(X_train, y_train, b11, b10, b7)
    elif b1 = = 3:
        fonk5(X_train, b11, b7)
def fonk2(b6, b1):
    if b1 = = 1:
        b12 = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
    elif b1 = = 2:
        b12 = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
    return b12[b6 - 1]
def fonk3(X_train, y_train, b11, b10, b7):
    b13 = Classifier(b7)
    b14 = b13.classify(X_train, y_train, b11, b10)
    b15 = b13.get_accuracy(b10, b14)
    b16 = Visualizer()
    b16.plot_classifier_regressor(b10, b14, 1)
    print(f'The accuracy is: {b15} %')
    print(b7)
def fonk4(X_train, y_train, b11, b10, b7):
    b17 = Regressor(b7)
    b14 = b17.predict(X_train, y_train, b11)
    b18 = b17.get_score(b10, b14)
    b16 = Visualizer()
    b16.plot_classifier_regressor(b10, b14, 2)
    print(f'The coefficient of determination is: {b18}')
    print(b7)
def fonk5(X_train, b11, b7):
    b19 = Clustering(b7)
    n_clusters, b20 = b19.tune_parameters(X_train)
    b21 = b19.cluster(X_train, b11, n_clusters)
    b16 = Visualizer()
    b16.plot_clustering(b11, b21)
    print(f"The b19 model's b20: {b20}")
    print(b7)
if b22 = = "__main__":
    fonk1()