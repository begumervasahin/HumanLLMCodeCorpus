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
b1 = datasets.load_iris()
b2 = b1.target_names
b3 = pd.DataFrame(b1.data, columns=b1.feature_names)
b3['target'] = b1.target
X_train, X_test, y_train, b4 = train_test_split(b1.data, b1.target, test_size=0.25, random_state=0)
b5 = GaussianNB()
b5.fit(X_train, y_train)
b6 = b5.predict(X_test)
b7 = accuracy_score(b6, b4)
print(f"Accuracy Score: {b7:.2f}")
def fonk1(X, y, b8 = None):
    plt.figure(b9 = (12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], b10 = y, cmap='viridis', edgecolor='k', s=50)
    plt.title('True labels')
    plt.xlabel(b1.feature_names[0])
    plt.ylabel(b1.feature_names[1])
    if b8 is not None:
        plt.subplot(1, 2, 2)
        plt.scatter(X[:, 0], X[:, 1], b10 = b8, cmap='viridis', edgecolor='k', s=50)
        plt.title('Predicted labels')
        plt.xlabel(b1.feature_names[0])
        plt.ylabel(b1.feature_names[1])
    plt.tight_layout()
    plt.show()
fonk1(X_test, b4, b6)