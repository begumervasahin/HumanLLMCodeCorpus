
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def load_and_split_data():
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, y_test
def train_and_predict(X_train, X_test, y_train):
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    return y_predict
def calculate_accuracy(y_predict, y_test):
    score = accuracy_score(y_predict, y_test)
    print("Accuracy Score:", score)
def main():
    X_train, X_test, y_train, y_test = load_and_split_data()
    y_predict = train_and_predict(X_train, X_test, y_train)
    calculate_accuracy(y_predict, y_test)
if __name__ == "__main__":
    main()