import numpy as np
import pandas as pd
from visualizer import Visualizer
from preprocessor import Preprocessor
from sklearn.datasets import load_iris
def select_method():
    return int(input('Enter 1 for Classification, 2 for Regression, or 3 for Clustering: '))
def load_dataset(method_identifier):
    if method_identifier == 1:
        return pd.read_csv('wisconsin_breast_cancer.csv')
    elif method_identifier == 2:
        return pd.read_csv('diamonds.csv')
    elif method_identifier == 3:
        iris_data = load_iris()
        return iris_data['data'], iris_data
def select_algorithm(method_identifier):
    if method_identifier == 1:
        identifier = int(input('Enter 1 for KNN, 2 for Decision Tree, 3 for Naive Bayes, 4 for Random Forest, or 5 for Neural Network: '))
        algorithms = ['KNN', 'Decision Tree', 'Naive Bayes', 'Random Forest', 'Neural Network']
        return algorithms[identifier - 1]
    elif method_identifier == 2:
        identifier = int(input('Enter 1 for Linear Regression, 2 for Polynomial Regression, 3 for Decision Tree, 4 for KNN Regression, 5 for Random Forest Regressor, or 6 for Neural Network: '))
        algorithms = ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'KNN Regression', 'Random Forest', 'Neural Network']
        return algorithms[identifier - 1]
    else:
        return 'K-Means'
def preprocess_data(method_identifier, dataset, preprocess):
    if method_identifier == 3:
        return preprocess.drop_missing(dataset), None
    else:
        dataset = preprocess.drop_missing(dataset)
        target = 'breast cancer' if method_identifier == 1 else 'diamonds'
        X, y = preprocess.dataframe_to_numpy(dataset, target)
        X, y = preprocess.encoding(X, y, target)
        return X, y
def split_and_scale_data(method_identifier, preprocess, X, y=None):
    if method_identifier in [1, 2]:
        X_train, X_test, y_train, y_test = preprocess.split_data(X, 0.19, y)
        X_train, X_test = preprocess.scaling(X_train, X_test, scale_type='Standard Scaler')
        return X_train, X_test, y_train, y_test
    else:
        X_train, X_test = preprocess.split_data(X, test_ratio=0.3)
        X_train, X_test = preprocess.scaling(X_train, X_test, scale_type='Standard Scaler')
        return X_train, X_test
def train_and_evaluate(method_identifier, algorithm_name, X_train, X_test, y_train=None, y_test=None):
    visualizer = Visualizer()
    if method_identifier == 1:
        from classifier import Classifier
        classifier = Classifier(algorithm_name)
        y_predicted = classifier.classify(X_train, y_train, X_test, y_test)
        accuracy = classifier.get_accuracy(y_test, y_predicted)
        visualizer.plot_classifier_regressor(y_test, y_predicted, method_identifier)
        print(f'The accuracy is: {accuracy} %')
        print(algorithm_name)
    elif method_identifier == 2:
        from regressor import Regressor
        regressor = Regressor(algorithm_name)
        y_predicted = regressor.predict(X_train, y_train, X_test)
        score = regressor.get_score(y_test, y_predicted)
        visualizer.plot_classifier_regressor(y_test, y_predicted, method_identifier)
        print(f'The coefficient of determination is: {score}')
        print(algorithm_name)
    elif method_identifier == 3:
        from clustering import Clustering
        clustering = Clustering(algorithm_name)
        n_clusters, inertia = clustering.tune_parameters(X_train)
        clusters = clustering.cluster(X_train, X_test, n_clusters)
        visualizer.plot_clustering(X_test, clusters)
        print(f"The clustering model's inertia: {inertia}")
        print(algorithm_name)
def main():
    method_identifier = select_method()
    preprocess = Preprocessor()
    if method_identifier == 3:
        X, iris = load_dataset(method_identifier)
        dataset = X
    else:
        dataset = load_dataset(method_identifier)
    algorithm_name = select_algorithm(method_identifier)
    if method_identifier == 3:
        X, _ = preprocess_data(method_identifier, dataset, preprocess)
        X_train, X_test = split_and_scale_data(method_identifier, preprocess, X)
        train_and_evaluate(method_identifier, algorithm_name, X_train, X_test)
    else:
        X, y = preprocess_data(method_identifier, dataset, preprocess)
        X_train, X_test, y_train, y_test = split_and_scale_data(method_identifier, preprocess, X, y)
        train_and_evaluate(method_identifier, algorithm_name, X_train, X_test, y_train, y_test)
if __name__ == "__main__":
    main()