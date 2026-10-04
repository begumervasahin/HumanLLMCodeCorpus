'''
This script uses the Iris dataset from UCI's Machine Learning Repository
to classify different types of iris flowers using a Gaussian Naive Bayes classifier.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
class_names = iris.target_names
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=0)
clf = GaussianNB()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)
score = accuracy_score(y_predict, y_test)
print(f"Accuracy Score: {score:.2f}")
def plot_iris(X, y, y_pred=None):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
    plt.title('True labels')
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    if y_pred is not None:
        plt.subplot(1, 2, 2)
        plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', edgecolor='k', s=50)
        plt.title('Predicted labels')
        plt.xlabel(iris.feature_names[0])
        plt.ylabel(iris.feature_names[1])
    plt.tight_layout()
    plt.show()
plot_iris(X_test, y_test, y_predict)