'''
This script uses the Iris dataset from UCI's Machine Learning Repository
to classify different types of b1 flowers using a Gaussian Naive Bayes classifier.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def fonk1():
    b1 = datasets.load_iris()
    b2 = pd.DataFrame(b1.data, columns=b1.b11)
    b2['target'] = b1.target
    return b2
def fonk2(X_train, y_train, X_test, b10):
    b3 = GaussianNB()
    b3.fit(X_train, y_train)
    b4 = b3.predict(X_test)
    b5 = accuracy_score(b10, b4)
    return b5, b4
def fonk3(b8, b9, b4 = None, b11=None):
    plt.figure(b6 = (12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(b8[:, 0], b8[:, 1], b7 = b9, cmap='viridis', edgecolor='k', s=50)
    plt.title('True Labels')
    plt.xlabel(b11[0])
    plt.ylabel(b11[1])
    if b4 is not None:
        plt.subplot(1, 2, 2)
        plt.scatter(b8[:, 0], b8[:, 1], b7 = b4, cmap='viridis', edgecolor='k', s=50)
        plt.title('Predicted Labels')
        plt.xlabel(b11[0])
        plt.ylabel(b11[1])
    plt.tight_layout()
    plt.show()
def fonk4():
    b2 = fonk1()
    b8 = b2.drop(columns=['target']).values
    b9 = b2['target'].values
    X_train, X_test, y_train, b10 = train_test_split(b8, b9, test_size=0.25, random_state=0)
    b5, b4 = fonk2(X_train, y_train, X_test, b10)
    print(f"Accuracy Score: {b5:.2f}")
    fonk3(X_test, b10, b4, b11 = b2.columns[:2])
if b12 = = "__main__":
    fonk4()