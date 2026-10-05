import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
def load_and_split_data():
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, y_test
def train_and_predict(X_train, X_test, y_train):
    naive_bayes_classifier = GaussianNB()
    naive_bayes_classifier.fit(X_train, y_train)
    predictions = naive_bayes_classifier.predict(X_test)
    return predictions
def evaluate_accuracy(y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    return accuracy
def main():
    X_train, X_test, y_train, y_test = load_and_split_data()
    predictions = train_and_predict(X_train, X_test, y_train)
    accuracy = evaluate_accuracy(y_test, predictions)
    print("Accuracy Score:", accuracy)
if __name__ == "__main__":
    main()