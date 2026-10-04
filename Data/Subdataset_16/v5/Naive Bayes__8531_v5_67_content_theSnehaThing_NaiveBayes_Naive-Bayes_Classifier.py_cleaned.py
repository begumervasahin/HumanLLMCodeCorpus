import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
b1 = pd.read_csv('Social_Network_Ads.csv')
b2 = b1.iloc[:, [2, 3]].values
b3 = b1.iloc[:, 4].values
b6, b7, y_train, b4 = train_test_split(b2, b3, test_size=0.25, random_state=0)
b5 = StandardScaler()
b6 = b5.fit_transform(b6)
b7 = b5.transform(b7)
b8 = GaussianNB()
b8.fit(b6, y_train)
b9 = b8.predict(b7)
b10 = confusion_matrix(b4, b9)
print("Confusion Matrix:\n", b10)
def fonk1(X_set, b14, b8, b16):
    X1, b11 = np.meshgrid(
        np.arange(b12 = X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
        np.arange(b12 = X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01)
    )
    plt.contourf(
        X1, b11, b8.predict(np.array([X1.ravel(), b11.ravel()]).T).reshape(X1.shape),
        b13 = 0.075, cmap=ListedColormap(('red', 'green'))
    )
    plt.xlim(X1.min(), X1.max())
    plt.ylim(b11.min(), b11.max())
    for i, j in enumerate(np.unique(b14)):
        plt.scatter(X_set[b14 = = j, 0], X_set[b14 == j, 1],
                    b15 = ListedColormap(('red', 'green'))(i), label=j)
    plt.b16(b16)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
fonk1(b6, y_train, b8, b16 = 'Naive Bayes Classifier on Training Set')
fonk1(b7, b4, b8, b16 = 'Naive Bayes Classifier on Test Set')