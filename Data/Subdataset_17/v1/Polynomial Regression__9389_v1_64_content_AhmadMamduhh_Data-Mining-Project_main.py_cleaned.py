import numpy as np
import pandas as pd
from visualizer import Visualizer
from preprocessor import Preprocessor
from classifier import Classifier
from regressor import Regressor
from clustering import Clustering
from sklearn.datasets import load_iris
def main():
    method_identifier = int(input('Enter 1 to choose Classification, 2 to choose Regression or 3 to choose Clustering: '))
    if method_identifier == 1:
        dataset = pd.read_csv('wisconsin_breast_cancer.csv')
    elif method_identifier == 2:
        dataset = pd.read_csv('diamonds.csv')
    elif method_identifier == 3:
        iris_data = load_iris(return_X_y=False)
        X = iris_data['data']
        iris = load_iris()
    if method_identifier == 1:
        identifier = int(input('Enter 1 to choose KNN, 2 to choose Decision Tree, 3 to choose Naive Bayes, 4 to choose Random Forest or 5 to choose Neural Network: '))
        algorithm_name = choose_algorithm(identifier, method_identifier)
    elif method_identifier == 2:
        identifier = int(input('Enter 1 to choose Linear Regression, 2 to choose Polynomial Regression, 3 to choose Decision Tree, 4 to choose KNN Regression, 5 to choose Random Forest Regressor or 6 to choose Neural Network: '))
        algorithm_name = choose_algorithm(identifier, method_identifier)
    else:
        algorithm_name = 'K-Means'
    preprocess = Preprocessor()
    if method_identifier == 3:
        X = preprocess.drop_missing(X)
    else:
        dataset = preprocess.drop_missing(dataset)
    if method_identifier == 1:
        X, y = preprocess.dataframe_to_numpy(dataset, 'breast cancer')
        X, y = preprocess.encoding(X, y, 'breast cancer')
    elif method_identifier == 2:
        X, y = preprocess.dataframe_to_numpy(dataset, 'diamonds')
        X, y = preprocess.encoding(X, y, 'diamonds')
    if method_identifier == 1 or method_identifier == 2:
        X_train, X_test, y_train, y_test = preprocess.split_data(X, 0.19, y)
    elif method_identifier == 3:
        X_train, X_test = preprocess.split_data(X, test_ratio=0.3)
    X_train, X_test = preprocess.scaling(X_train, X_test, scale_type='Standard Scaler')
    if method_identifier == 1:
        classifier_workflow(X_train, y_train, X_test, y_test, algorithm_name)
    elif method_identifier == 2:
        regressor_workflow(X_train, y_train, X_test, y_test, algorithm_name)
    elif method_identifier == 3:
        clustering_workflow(X_train, X_test, algorithm_name)
def choose_algorithm(identifier, method_identifier):
    if method_identifier == 1:
        algorithms = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
    elif method_identifier == 2:
        algorithms = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
    return algorithms[identifier - 1]
def classifier_workflow(X_train, y_train, X_test, y_test, algorithm_name):
    classifier = Classifier(algorithm_name)
    y_predicted = classifier.classify(X_train, y_train, X_test, y_test)
    classifier_accuracy = classifier.get_accuracy(y_test, y_predicted)
    visualizer = Visualizer()
    visualizer.plot_classifier_regressor(y_test, y_predicted, 1)
    print(f'The accuracy is: {classifier_accuracy} %')
    print(algorithm_name)
def regressor_workflow(X_train, y_train, X_test, y_test, algorithm_name):
    regressor = Regressor(algorithm_name)
    y_predicted = regressor.predict(X_train, y_train, X_test)
    regressor_score = regressor.get_score(y_test, y_predicted)
    visualizer = Visualizer()
    visualizer.plot_classifier_regressor(y_test, y_predicted, 2)
    print(f'The coefficient of determination is: {regressor_score}')
    print(algorithm_name)
def clustering_workflow(X_train, X_test, algorithm_name):
    clustering = Clustering(algorithm_name)
    n_clusters, inertia = clustering.tune_parameters(X_train)
    clusters = clustering.cluster(X_train, X_test, n_clusters)
    visualizer = Visualizer()
    visualizer.plot_clustering(X_test, clusters)
    print(f"The clustering model's inertia: {inertia}")
    print(algorithm_name)
if __name__ == "__main__":
    main()