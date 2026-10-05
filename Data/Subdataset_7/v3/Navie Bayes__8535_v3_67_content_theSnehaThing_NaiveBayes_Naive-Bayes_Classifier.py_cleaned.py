import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1.iloc[:, [2, 3]].values
    b3 = b1.iloc[:, 4].values
    return b2, b3
def fonk2(b2, b3, b4 = 0.25, random_state=0):
    return train_test_split(b2, b3, b4 = b4, random_state=random_state)
def fonk3(X_train, X_test):
    b5 = StandardScaler()
    b6 = b5.fit_transform(X_train)
    b7 = b5.transform(X_test)
    return b6, b7
def fonk4(X_train, y_train):
    b8 = GaussianNB()
    b8.fit(X_train, y_train)
    return b8
def fonk5(b8, X_test, b16):
    b9 = b8.predict(X_test)
    b10 = confusion_matrix(b16, b9)
    return b10
def fonk6(X_set, b14, b8, title):
    X1, b11 = np.meshgrid(np.arange(b12=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(b12 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, b11, b8.predict(np.array([X1.ravel(), b11.ravel()]).T).reshape(X1.shape),
                 b13 = 0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b11.min(), b11.max())
    for i, j in enumerate(np.unique(b14)):
        plt.scatter(X_set[b14 = = j, 0], X_set[b14 == j, 1],
                    b15 = ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
def fonk7():
    b2, b3 = fonk1('Social_Network_Ads.csv')
    X_train, X_test, y_train, b16 = fonk2(b2, b3)
    b6, b7 = fonk3(X_train, X_test)
    b8 = fonk4(b6, y_train)
    b10 = fonk5(b8, b7, b16)
    fonk6(b6, y_train, b8, 'Naive Bayes Classifier (Training set)')
    fonk6(b7, b16, b8, 'Naive Bayes Classifier (Test set)')
if b17 = = "__main__":
    fonk7()