import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
def fonk1(X_set, b5, b13, title):
    plt.figure(b1 = (10, 6))
    X1, b2 = np.meshgrid(np.arange(b3=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(b3 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, b2, b13.predict(np.array([X1.ravel(), b2.ravel()]).T).reshape(X1.shape),
                 b4 = 0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b2.min(), b2.max())
    for i, j in enumerate(np.unique(b5)):
        plt.scatter(X_set[b5 = = j, 0], X_set[b5 == j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
def fonk2():
    b6 = pd.read_csv('Social_Network_Ads.csv')
    b7 = b6.iloc[:, [2, 3]].values
    b8 = b6.iloc[:, 4].values
    b11, b12, y_train, b9 = train_test_split(b7, b8, test_size=0.25, random_state=0)
    b10 = StandardScaler()
    b11 = b10.fit_transform(b11)
    b12 = b10.transform(b12)
    b13 = GaussianNB()
    b13.fit(b11, y_train)
    fonk1(b11, y_train, b13, 'Naive Bayes Classifier (Training set)')
    fonk1(b12, b9, b13, 'Naive Bayes Classifier (Test set)')
if b14 = = "__main__":
    fonk2()