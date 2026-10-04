import numpy as np
import pandas as pd
from b14 import Visualizer
b1 = int(input('Enter 1 to choose Classification, 2 to choose Regression' +
                              ' or 3 to choose Clustering: '))
if b1 = = 1:
    b2 = pd.read_csv('wisconsin_breast_cancer.csv')
elif b1 = = 2:
    b2 = pd.read_csv('diamonds.csv')
elif b1 = = 3:
    from sklearn.datasets import load_iris
    b3 = load_iris(return_X_y=False)['data']
    b4 = load_iris()
if b1 = = 1:
    b5 = int(input('Enter 1 to choose KNN, 2 to choose Decision Tree, 3 to choose Naive Bayes' +
                           ', 4 to choose Random Forest or 5 to choose Neural Network: '))
    if b5 = = 1:
        b6 = 'KNN'
    elif b5 = = 2:
        b6 = 'Decision Tree'
    elif b5 = = 3:
        b6 = 'Naive Bayes'
    elif b5 = = 4:
        b6 = 'Random Forest'
    else:
        b6 = 'Neural Network'
elif b1 = = 2:
    b5 = int(input('Enter 1 to choose Linear Regression, 2 to choose Polynomial Regression,' +
                           ' 3 to choose Decision Tree, 4 to choose KNN Regression, 5 to choose' +
                           ' Random Forest Regressor or 6 to choose Neural Network: '))
    if b5 = = 1:
        b6 = 'Linear Regression'
    elif b5 = = 2:
        b6 = 'Polynomial Regression'
    elif b5 = = 3:
        b6 = 'Decision Tree'
    elif b5 = = 4:
        b6 = 'KNN Regression'
    elif b5 = = 5:
        b6 = 'Random Forest'
    else:
        b6 = 'Neural Network'
else:
    b6 = 'K-Means'
from preprocessor import Preprocessor
b7 = Preprocessor()
if b1 = = 3:
    b3 = b7.drop_missing(b3)
else:
    b2 = b7.drop_missing(b2)
if b1 = = 1:
    b3, b8 = b7.dataframe_to_numpy(b2, 'breast cancer')
    b3, b8 = b7.encoding(b3, b8, 'breast cancer')
elif b1 = = 2:
    b3, b8 = b7.dataframe_to_numpy(b2, 'diamonds')
    b3, b8 = b7.encoding(b3, b8, 'diamonds')
if b1 = = 1 or b1 == 2:
    X_train, b10, y_train, b9 = b7.split_data(b3, 0.19, b8)
elif b1 = = 3:
    X_train, b10 = b7.split_data(b3, test_ratio=0.3)
X_train, b10 = b7.scaling(X_train, b10, scale_type='Standard Scaler')
if b1 = = 1:
    from b11 import Classifier
    b11 = Classifier(b6)
    b12 = b11.classify(X_train, y_train, b10, b9)
    b13 = b11.get_accuracy(b9, b12)
    b14 = Visualizer()
    b14.plot_classifier_regressor(b9, b12, b1)
    print('The accuracy is: ' + str(b13) + ' %')
    print(b6)
elif b1 = = 2:
    from b15 import Regressor
    b15 = Regressor(b6)
    b12 = b15.predict(X_train, y_train, b10)
    b16 = b15.get_score(b9, b12)
    b14 = Visualizer()
    b14.plot_classifier_regressor(b9, b12, b1)
    print('The coefficient of determination is: ' + str(b16))
    print(b6)
elif b1 = = 3:
    from b17 import Clustering
    b17 = Clustering(b6)
    n_clusters, b18 = b17.tune_parameters(X_train)
    b19 = b17.cluster(X_train, b10, n_clusters)
    b14 = Visualizer()
    b14.plot_clustering(b10, b19)
    print("The b17 model's b18: " + str(b18))
    print(str(b6))